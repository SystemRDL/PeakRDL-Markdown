"""PeakRDL Markdown plug-in."""

__authors__ = ["Marek Pikuła <marek.pikula at embevity.com>"]

from typing import TYPE_CHECKING

from .exporter import MarkdownExporter

if TYPE_CHECKING:
    import argparse
    from typing import Union

    from systemrdl.node import AddrmapNode, RootNode  # type: ignore


class Exporter:  # pylint: disable=too-few-public-methods
    """PeakRDL Markdown exporter plug-in."""

    short_desc = "Export the register model to Markdown"

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
        )
