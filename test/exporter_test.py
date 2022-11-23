"""Exporter tests."""

__authors__ = ["Marek Pikuła <marek.pikula at embevity.com>"]

import difflib

from systemrdl import RDLCompiler  # type: ignore

from peakrdl_markdown.exporter import MarkdownExporter


def test_exporter_basic():
    """Basic exporter test comparing with a reference file."""
    in_path = "example/accelera_generic_example.rdl"
    ref_out_path = "example/accelera_generic_example.md"
    out_path = "output/accelera_generic_example.md"

    # Generate the file.
    rdlc = RDLCompiler()
    rdlc.compile_file(in_path)
    MarkdownExporter().export(
        rdlc.elaborate(),  # type: ignore
        out_path,
        input_files=[in_path],
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
