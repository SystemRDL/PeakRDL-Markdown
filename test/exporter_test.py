"""Exporter tests."""

__authors__ = ["Marek Pikuła <marek at serenitycode.dev>"]

import difflib
from typing import Optional

from systemrdl import RDLCompiler  # type: ignore

from peakrdl_markdown.exporter import MarkdownExporter


def basic_export_diff(
    in_path: str,
    ref_out_path: str,
    out_path: str,
    rename: Optional[str] = None,
    depth: int = 0,
):
    """Test exporter by comparing with a reference file.

    Arguments:
        in_path -- input SystemRDL path.
        ref_out_path -- reference generated file path.
        out_path -- test generated file path.

    Keyword Arguments:
        rename -- rename the generated top-level (default: {None})
    """
    # Generate the file.
    rdlc = RDLCompiler()
    rdlc.compile_file(in_path)
    MarkdownExporter().export(
        rdlc.elaborate(),  # type: ignore
        out_path,
        input_files=[in_path],
        rename=rename,
        depth=depth,
    )

    # Check if the generated file matches reference file.
    with open(out_path, encoding="UTF-8") as out_file, open(
        ref_out_path, encoding="UTF-8"
    ) as ref_out_file:
        result = "\n".join(
            difflib.unified_diff(
                out_file.readlines(),
                ref_out_file.readlines(),
                out_path,
                ref_out_path,
            )
        )
    print(result)
    assert len(result) == 0, "Generated file doesn't match reference file."


def test_exporter_basic_accelera():
    """Test Accelera generic example."""
    basic_export_diff(
        "example/accelera_generic_example.rdl",
        "example/accelera_generic_example.md",
        "output/accelera_generic_example.md",
        "some_register_map",
    )


def test_exporter_basic_accelera_depth_1():
    """Test Accelera generic example with depth=1."""
    basic_export_diff(
        "example/accelera_generic_example.rdl",
        "example/accelera_generic_example_depth_1.md",
        "output/accelera_generic_example_depth_1.md",
        "some_register_map",
        depth=1,
    )


def test_exporter_basic_minimal():
    """Test minimal example."""
    basic_export_diff(
        "example/minimal_example.rdl",
        "example/minimal_example.md",
        "output/minimal_example.md",
        "some_register_map",
    )
