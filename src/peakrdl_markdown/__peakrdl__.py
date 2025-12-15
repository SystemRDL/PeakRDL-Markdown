"""PeakRDL Markdown plug-in."""

__authors__ = ["Marek Pikuła <marek at serenitycode.dev>"]

from typing import TYPE_CHECKING

from peakrdl.plugins.exporter import ExporterSubcommandPlugin  # type: ignore

from .exporter import MarkdownExporter

if TYPE_CHECKING:
    import argparse
    from typing import Union

    from systemrdl.node import AddrmapNode, RootNode  # type: ignore


class Exporter(ExporterSubcommandPlugin):  # pylint: disable=too-few-public-methods
    """PeakRDL Markdown exporter plug-in."""

    short_desc = "Generate Markdown documentation"
    long_desc = "Export the register model to Markdown"

    def add_exporter_arguments(self, arg_group: "argparse._ActionsContainer"):  # type: ignore
        """Add PeakRDL exporter arguments."""
        arg_group.add_argument(
            "--depth",
            dest="depth",
            default=0,
            type=int,
            help="Depth of generation (0 means all)",
        )
        arg_group.add_argument(
            "--heading_level",
            dest="heading_level",
            default=2,
            type=int,
            help="Starting heading level for top-level node.",
        )
        arg_group.add_argument(
            "--style",
            dest="style",
            choices=["flat", "hierarchy"],
            default="flat",
            help="Generation style: 'flat' or 'hierarchy'."
        )

    def do_export(
        self, top_node: "Union[AddrmapNode, RootNode]", options: "argparse.Namespace"
    ):
        """Perform the export of SystemRDL node to Markdown.

        Arguments:
            top_node -- top node to export.
            options -- argparse options from the `peakrdl` tool.
        """
        MarkdownExporter().export(
            top_node,
            options.output,
            input_files=options.input_files,
            rename=options.inst_name,
            depth=options.depth,
            heading_level=options.heading_level,
            style=options.style,
        )