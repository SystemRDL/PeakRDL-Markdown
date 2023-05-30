[![Documentation Status](https://readthedocs.org/projects/peakrdl-markdown/badge/?version=latest)](http://peakrdl-markdown.readthedocs.io)
[![build](https://github.com/SystemRDL/PeakRDL-Markdown/workflows/build/badge.svg)](https://github.com/SystemRDL/PeakRDL-Markdown/actions?query=workflow%3Abuild+branch%3Amain)
[![Coverage Status](https://coveralls.io/repos/github/SystemRDL/PeakRDL-Markdown/badge.svg?branch=main)](https://coveralls.io/github/SystemRDL/PeakRDL-Markdown?branch=main)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/peakrdl-markdown.svg)](https://pypi.org/project/peakrdl-markdown)

# PeakRDL-Markdown

This package implements Markdown exporter for the PeakRDL toolchain.

- **Export:** Convert compiled SystemRDL input into Markdown description.

For the command line tool, see the [PeakRDL
project](https://peakrdl.readthedocs.io).

## Usage

PeakRDL project provides a standard CLI interface. It can be installed directly
via pip:

    $ pip install peakrdl-markdown

Then this package can be used with the following command:

    $ peakrdl markdown input_file.rdl -o output_file.md

## Documentation

See the [PeakRDL-Markdown
Documentation](http://peakrdl-markdown.readthedocs.io) for more details.
