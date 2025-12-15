"""PeakRDL Markdown exporter."""

__authors__ = [
    "Marek Pikuła <marek at serenitycode.dev>",
    "Maciej Dudek <mdudek at antmicro.com>",
]

from collections import OrderedDict
from dataclasses import dataclass
from functools import reduce
from operator import mul
from pathlib import Path
from typing import List, Optional, Union, Literal

from py_markdown_table.markdown_table import markdown_table  # type:ignore
from systemrdl.messages import MessageHandler  # type: ignore
from systemrdl.node import (  # type: ignore
    AddressableNode,
    AddrmapNode,
    FieldNode,
    MemNode,
    Node,
    RegfileNode,
    RegNode,
    RootNode,
)

class MarkdownExporter:  # pylint: disable=too-few-public-methods
    """PeakRDL Markdown exporter main class."""

    def __init__(self):
        """Initialize the exporter."""
        self.style = "flat"

    @dataclass
    class GenStageOutput:
        """Generation stage output."""
        node: Node
        table_row: "OrderedDict[str, Union[str, int]]"
        generated: str

    @staticmethod
    def _heading(depth: int, title: str):
        """Generate Markdown heading.

        Arguments:
            depth -- Heading depth (number of hashes).
            title -- Heading title text.

        Returns:
            Formatted Markdown heading string.
        """
        # Safety check: Markdown only supports up to level 6
        safe_depth = min(depth, 6)
        if safe_depth < 1: safe_depth = 1 # Prevent 0 or negative

        return "\n" + "#" * safe_depth + f" {title}\n\n"

    @staticmethod
    def _addrnode_info(node: AddressableNode):
        """Generate AddressableNode basic information dictionary.

        Arguments:
            node -- The addressable node (Addrmap, Regfile, Mem) to extract info from.

        Returns:
            OrderedDict containing address, offset, size, etc.
        """
        ret: "OrderedDict[str, str]" = OrderedDict()

        set_index = False
        if node.is_array and node.current_idx is None:
            node.current_idx = [0]
            set_index = True
        ret["Absolute Address"] = f"0x{node.absolute_address:X}"
        ret["Base Offset"] = f"0x{node.raw_address_offset:X}"
        if node.is_array and node.array_dimensions is not None and set_index:
            ret["Size"] = f"0x{node.size * reduce(mul, node.array_dimensions, 1):X}"
        else:
            ret["Size"] = f"0x{node.size:X}"

        if node.is_array:
            ret["Array Dimensions"] = str(node.array_dimensions)
            ret["Array Stride"] = f"0x{node.array_stride:X}"
            ret["Total Size"] = f"0x{node.total_size:X}"

        return ret

    def _addrnode_info_md(self, node: AddressableNode) -> str:
        """Generate AddressableNode basic information as a Markdown list.

        Arguments:
            node -- The addressable node to format.

        Returns:
            String containing the markdown list of properties.
        """
        return "- " + "\n- ".join(
            f"{key}: {value}" for key, value in self._addrnode_info(node).items()
        )

    @staticmethod
    def _node_name_sanitized(node: Node) -> str:
        """Get the Node name as HTML without newlines.

        Arguments:
            node -- The node to get the name from.

        Returns:
            Sanitized name string suitable for table inclusion.
        """
        name = node.get_html_name()
        if name is None:
            name = "—"
        else:
            name = name.replace("\n", "")
        return name

    def _addrnode_header(
        self, node: AddressableNode, msg: MessageHandler, heading_level: int
    ) -> str:
        """Get the AddressableNode header.

        Arguments:
            node -- Node to generate the header for.
            msg -- Message handler from top-level for warnings.
            heading_level -- The Markdown heading depth level to use.

        Returns:
            String containing the header, info list, and description.
        """
        if isinstance(node, AddrmapNode):
            node_type_name = "address map"
        elif isinstance(node, RegfileNode):
            node_type_name = "register file"
        elif isinstance(node, MemNode):
            node_type_name = "memory"
        elif isinstance(node, RegNode):
            node_type_name = "register"
        else:
            node_type_name = "addressable node"
            msg.warning(f"Unsupported type of node ({node.__class__.__name__}).")

        ret = self._heading(heading_level, f"{node.inst_name} {node_type_name}")
        ret += self._addrnode_info_md(node) + "\n\n"
        desc = node.get_html_desc()
        if desc is not None:
            ret += desc + "\n\n"
        return ret

    def _addrnode_table_row(
        self, node: AddressableNode
    ) -> "OrderedDict[str, Union[str, int]]":
        """Generate AddressableNode table row.

        Arguments:
            node -- The node to generate a summary row for.

        Returns:
            OrderedDict representing the table row (Offset, Identifier, Name).
        """
        offset = node.address_offset
        identifier = node.inst_name
        if node.is_array:
            assert node.current_idx is not None
            identifier += "".join(f"[{idx}]" for idx in node.current_idx)
        name = self._node_name_sanitized(node)

        table_row: "OrderedDict[str, Union[str, int]]" = OrderedDict()
        table_row["Offset"] = offset
        table_row["Identifier"] = identifier
        table_row["Name"] = name

        return table_row

    def export(  # pylint: disable=too-many-arguments
        self,
        node: Union[AddrmapNode, RootNode],
        output_path: str,
        input_files: Optional[List[str]] = None,
        rename: Optional[str] = None,
        depth: int = 0,
        heading_level: int = 2,
        style: Literal["flat", "hierarchy"] = "flat",
    ):
        """Export the `node` to generated Markdown file.

        Arguments:
            node -- Node to export (Root or Addrmap).
            output_path -- Path to the exported .md file.
            input_files -- List of input RDL files used for annotation.
            rename -- Optional name to rename the top-level to.
            depth -- Depth of generation (0 means all).
            heading_level -- Starting heading level for top-level node.
            style -- Generation style: 'flat' or 'hierarchy'.
        """
        self.style = style

        top = node.top if isinstance(node, RootNode) else node
        top_name = rename if rename is not None else node.inst_name

        generated_from = top_name
        if input_files is not None:
            generated_from += "\n  - " + "\n  - ".join(f for f in input_files)

        if not output_path.endswith(".md"):
            raise ValueError("The output file is not Markdown file.")
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        gen = self._add_addrmap_regfile_mem(top, node.env.msg, depth - 1, heading_level).generated

        with open(output_path, "w", encoding="UTF-8") as output:
            output.write(
                "<!---\n"
                "Markdown description for SystemRDL register map.\n\n"
                f"Don't override. Generated from: {generated_from}\n"
                "-->\n"
            )
            output.write(gen)

    def _add_addrmap_regfile_mem(
        self,
        node: Union[AddrmapNode, RegfileNode, MemNode],
        msg: MessageHandler,
        depth: int,
        heading_level: int,
    ) -> GenStageOutput:
        """Generate addrmap, regfile or memory.

        Arguments:
            node -- The container node (Addrmap, Regfile, Mem).
            msg -- Message handler for warnings.
            depth -- Depth of generation left.

        Returns:
            GenStageOutput object containing generated markdown.
        """
        next_header_level = 2 if self.style == "flat" else heading_level + 1
    
        members: List[MarkdownExporter.GenStageOutput] = []
        member_gen: str = ""
        # Don't unroll register arrays when they are inside memories.
        # Memories can contain hundreds of entires.
        not_memory = not isinstance(node, MemNode)
        for child in node.children(unroll=not_memory, skip_not_present=True):
            if isinstance(child, (AddrmapNode, RegfileNode, MemNode)):
                output = self._add_addrmap_regfile_mem(child, msg, depth - 1, next_header_level)
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
        gen: str = self._addrnode_header(node, msg, heading_level)

        if len(members) == 0:
            gen += "No supported members.\n"
        else:
            base_addr_digits = max(
                map(lambda m: len(f'{m.table_row["Offset"]:X}'), members), default=4
            )
            for member in members:
                member.table_row["Offset"] = (
                    f'0x{member.table_row["Offset"]:0{base_addr_digits}X}'
                )

            gen += (
                markdown_table([*map(lambda m: m.table_row, members)])
                .set_params(row_sep="markdown", quote=False)
                .get_markdown()
            )

        gen += "\n"

        return MarkdownExporter.GenStageOutput(
            node,
            self._addrnode_table_row(node),
            gen + (member_gen if depth != 0 else ""),
        )

    def _add_reg(self, node: RegNode, msg: MessageHandler) -> GenStageOutput:
        """Generate register markdown.

        Arguments:
            node -- The register node.
            msg -- Message handler.

        Returns:
            GenStageOutput object containing generated markdown for the register.
        """
        field_gen: str = ""
        members: List[MarkdownExporter.GenStageOutput] = []
        for field in node.fields(skip_not_present=True):
            output = self._add_field(field, msg)
            field_gen += output.generated
            members.append(output)

        if self.style == "flat":
            gen = self._addrnode_header(node, msg, 3) # Hardcoded level 3
            if members:
                gen += (
                    markdown_table([*map(lambda m: m.table_row, members)])
                    .set_params(row_sep="markdown", quote=False)
                    .get_markdown()
                )
            gen += "\n"
            content = gen + field_gen
        else:
            gen = f"\n- **{node.inst_name}** (Offset: 0x{node.address_offset:X})\n"

            desc = node.get_html_desc()
            if desc:
                indented_desc = "\n".join("  " + line for line in desc.splitlines())
                gen += "\n" + indented_desc + "\n"

            if members:
                table_md = (
                    markdown_table([*map(lambda m: m.table_row, members)])
                    .set_params(row_sep="markdown", quote=False)
                    .get_markdown()
                )
                indented_table = "\n".join("  " + line for line in table_md.splitlines())
                gen += "\n" + indented_table + "\n"

            if field_gen:
                gen += field_gen
            content = gen

        return MarkdownExporter.GenStageOutput(
            node, self._addrnode_table_row(node), content
        )

    def _add_field(
        self,
        node: FieldNode,
        msg: MessageHandler,  # pylint: disable=unused-argument
    ) -> GenStageOutput:
        """Generate field markdown.

        Arguments:
            node -- The field node.
            msg -- Message handler.

        Returns:
            GenStageOutput object containing generated markdown for the field.
        """
        if node.msb == node.lsb:
            bits = str(node.msb)
        else:
            bits = f"{node.msb}:{node.lsb}"

        identifier = node.inst_name
        access = node.get_property("sw").name
        onread = node.get_property("onread")
        if onread is not None: access += ", " + onread.name
        onwrite = node.get_property("onwrite")
        if onwrite is not None: access += ", " + onwrite.name

        reset_value = node.get_property("reset", default="—")
        reset = f"0x{reset_value:X}" if isinstance(reset_value, int) else str(reset_value)
        name = self._node_name_sanitized(node)

        table_row: "OrderedDict[str, Union[str, int]]" = OrderedDict()
        table_row["Bits"] = bits
        table_row["Identifier"] = identifier
        table_row["Access"] = access
        table_row["Reset"] = reset
        table_row["Name"] = name

        if self.style == "flat":
            gen = ""
            desc = node.get_html_desc()
            if desc is not None:
                gen = self._heading(4, f"{node.inst_name} field") + desc + "\n" # Hardcoded level 4
        else:
            gen = f"\n  - **{node.inst_name}** [{bits}]\n"
            desc = node.get_html_desc()
            if desc:
                indented_desc = "\n".join("    " + line for line in desc.splitlines())
                gen += "\n" + indented_desc + "\n"

        return MarkdownExporter.GenStageOutput(node, table_row, gen)