"""PeakRDL Markdown exporter."""

__authors__ = ["Marek Pikuła <marek.pikula at embevity.com>"]

from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

from markdownTable import markdownTable  # type:ignore
from systemrdl.messages import MessageHandler  # type: ignore
from systemrdl.node import (  # type: ignore
    AddressableNode,
    AddrmapNode,
    FieldNode,
    Node,
    RegfileNode,
    RegNode,
    RootNode,
)


class MarkdownExporter:  # pylint: disable=too-few-public-methods
    """PeakRDL Markdown exporter main class."""

    @dataclass
    class GenStageOutput:
        """Generation stage output."""

        node: Node
        """Node on which generation has been performed."""

        table_row: "OrderedDict[str, Union[str, int]]"
        """Row for the parent table."""

        generated: str
        """Markdown generated during this stage."""

    @staticmethod
    def _heading(depth: int, title: str):
        """Generate Markdown heading of a given depth with newline envelope.

        Arguments:
            depth -- heading depth (number of hashes)
            title -- heading title

        Returns:
            Formatted Markdown heading.
        """
        return "\n" + "#" * depth + f" {title}\n\n"

    @staticmethod
    def _addrnode_info(node: AddressableNode):
        """Generate AddressableNode basic information dictionary."""
        ret: "OrderedDict[str, str]" = OrderedDict()

        ret["Absolute Address"] = f"0x{node.absolute_address:X}"
        ret["Base Offset"] = f"0x{node.raw_address_offset:X}"
        ret["Size"] = f"0x{node.size:X}"

        if node.is_array:
            ret["Array Dimensions"] = str(node.array_dimensions)
            ret["Array Stride"] = f"0x{node.array_stride:X}"
            ret["Total Size"] = f"0x{node.total_size:X}"

        return ret

    def _addrnode_info_md(self, node: AddressableNode) -> str:
        """Generate AddressableNode basic information as a Markdown list."""
        return "- " + "\n- ".join(
            f"{key}: {value}" for key, value in self._addrnode_info(node).items()
        )

    @staticmethod
    def _node_name_sanitized(node: Node) -> str:
        """Get the Node name as HTML without newlines.

        Needed for proper inclusion in tables.
        """
        name = node.get_html_name()
        if name is None:
            name = "—"
        else:
            name = name.replace("\n", "")
        return name

    def _addrnode_header(self, node: AddressableNode, heading_level: int) -> str:
        """Get the AddressableNode header.

        Arguments:
            node -- node to generate the header for.
            heading_level -- Markdown heading level.
        """
        ret = self._heading(heading_level, node.inst_name)
        ret += self._addrnode_info_md(node) + "\n\n"
        desc = node.get_html_desc()
        if desc is not None:
            ret += desc + "\n\n"
        return ret

    def _addrnode_table_row(
        self, node: AddressableNode
    ) -> "OrderedDict[str, Union[str, int]]":
        """Generate AddressableNode table row.

        The "Offset" is an integer so that it can be formatted in the parent
        node.
        """
        offset = node.address_offset
        identifier = node.inst_name
        if node.is_array:
            assert node.array_dimensions is not None
            identifier += "".join(f"[{dim}]" for dim in node.array_dimensions)
        name = self._node_name_sanitized(node)

        table_row: "OrderedDict[str, Union[str, int]]" = OrderedDict()
        table_row["Offset"] = offset
        table_row["Identifier"] = identifier
        table_row["Name"] = name

        return table_row

    def export(
        self,
        node: Union[AddrmapNode, RootNode],
        output_path: str,
        input_files: Optional[List[str]] = None,
        rename: Optional[str] = None,
    ):
        """Export the `node` to generated Python interface file.

        Arguments:
            node -- node to export.
            input_files -- list of input files.
            output_path -- path to the exported file.
            rename -- name to rename the top-level to.
        """
        # Get the top node.
        top = node.top if isinstance(node, RootNode) else node
        top_name = rename if rename is not None else node.inst_name

        generated_from = top_name
        if input_files is not None:
            generated_from = "  " + ("\n" + "  ").join(f for f in input_files)

        # Ensure proper format of the output path and that the directory exists.
        if not output_path.endswith(".md"):
            raise ValueError("The output file is not Markdown file.")
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        # Generate the file.
        with open(output_path, "w", encoding="UTF-8") as output:
            output.write(
                (
                    "<!---\n"
                    "Markdown description for SystemRDL register map.\n\n"
                    f"Don't override. Generated from: {generated_from}\n"
                    "-->\n"
                )
                + self._add_addrmap_regfile(top, node.env.msg).generated
            )

    def _add_addrmap_regfile(
        self,
        node: Union[AddrmapNode, RegfileNode],
        msg: MessageHandler,
    ) -> GenStageOutput:
        """Generate addrmap or regfile.

        Arguments:
            node -- RegfileNode or AddrmapNode.
            msg -- message handler from top-level.

        Keyword Arguments:
            is_top -- if the current not is the top node. If True the
                specification is embedded as class member.

        Returns:
            Generated addrmap output.
        """
        members: List[MarkdownExporter.GenStageOutput] = []
        member_gen: str = ""
        for child in node.children(unroll=True, skip_not_present=False):
            if isinstance(child, (AddrmapNode, RegfileNode)):
                output = self._add_addrmap_regfile(child, msg)
                member_gen += output.generated
                members.append(output)
            elif isinstance(child, RegNode):
                output = self._add_reg(child, msg)
                member_gen += output.generated
                members.append(output)
            else:
                msg.warning(
                    f"Unsupported type of node ({child.__class__.__name__}) "
                    f"for {'/'.join(child.get_path_segments())}."
                )

        gen: str = self._addrnode_header(node, 2)

        # Find the maximum width of the offset hex int and format the offset
        # for all members.
        base_addr_digits = max(
            map(lambda m: len(f'{m.table_row["Offset"]:X}'), members)
        )
        for member in members:
            member.table_row[
                "Offset"
            ] = f'0x{member.table_row["Offset"]:0{base_addr_digits}X}'

        gen += (
            markdownTable([*map(lambda m: m.table_row, members)])
            .setParams(row_sep="markdown", quote=False)
            .getMarkdown()
        )

        gen += "\n"

        return MarkdownExporter.GenStageOutput(
            node, self._addrnode_table_row(node), gen + member_gen
        )

    def _add_reg(self, node: RegNode, msg: MessageHandler) -> GenStageOutput:
        """Generate register.

        Arguments:
            node -- RegNode.
            msg -- message handler from top-level.

        Returns:
            Generated register output.
        """
        field_gen: str = ""
        members: List[MarkdownExporter.GenStageOutput] = []
        for field in node.fields(skip_not_present=True):
            output = self._add_field(field, msg)
            field_gen += output.generated
            members.append(output)

        gen: str = self._addrnode_header(node, 3)
        gen += (
            markdownTable([*map(lambda m: m.table_row, members)])
            .setParams(row_sep="markdown", quote=False)
            .getMarkdown()
        )
        gen += "\n"

        return MarkdownExporter.GenStageOutput(
            node, self._addrnode_table_row(node), gen + field_gen
        )

    def _add_field(
        self,
        node: FieldNode,
        msg: MessageHandler,  # pylint: disable=unused-argument
    ) -> GenStageOutput:
        """Generate field.

        Arguments:
            node -- FieldNode.
            msg -- message handler from top-level.

        Returns:
            Generated field output.
        """
        if node.msb == node.lsb:
            bits = str(node.msb)
        else:
            bits = f"{node.msb}:{node.lsb}"

        identifier = node.inst_name

        access = node.get_property("sw").name
        if node.get_property("onread") is not None:
            access += ", " + node.get_property("onread").name
        if node.get_property("onwrite") is not None:
            access += ", " + node.get_property("onwrite").name

        reset_value: str = node.get_property("reset", default="—")
        if isinstance(reset_value, int):
            reset = f"0x{reset_value:X}"
        else:
            reset = str(reset_value)

        name = self._node_name_sanitized(node)

        table_row: "OrderedDict[str, Union[str, int]]" = OrderedDict()
        table_row["Bits"] = bits
        table_row["Identifier"] = identifier
        table_row["Access"] = access
        table_row["Reset"] = reset
        table_row["Name"] = name

        gen = ""
        desc = node.get_html_desc()
        if desc is not None:
            gen = self._heading(4, node.inst_name) + desc + "\n"

        return MarkdownExporter.GenStageOutput(node, table_row, gen)
