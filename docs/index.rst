Introduction
============

This package implements a Markdown exporter for the PeakRDL toolchain.


Installing
----------

Install from `PyPi`_ using pip:

.. code-block:: bash

    python3 -m pip install peakrdl-markdown

.. _PyPi: https://pypi.org/project/peakrdl-markdown

Quick Start
-----------

Exporting to Python interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The module integrates with PeakRDL CLI interface:

.. code-block:: bash

    peakrdl markdown input_file.rdl -o output_file.md

Python compatibility
--------------------

The library supports Python 3.8 and newer. For development, using Python 3.12
or later (the version shipped with current Ubuntu LTS) is recommended, as
several developer-focused dependencies and tools require a newer Python and
improve the development experience.

To install the library with Poetry for version smaller than 3.12 use:

.. code-block:: bash

    poetry install --only main,test

For newer versions the ``--only main,test`` can be omitted.

Links
-----

- `Source repository <https://github.com/SystemRDL/PeakRDL-Markdown>`_
- `Release Notes <https://github.com/SystemRDL/PeakRDL-Markdown/releases>`_
- `Issue tracker <https://github.com/SystemRDL/PeakRDL-Markdown/issues>`_
- `PyPi <https://pypi.org/project/peakrdl-markdown>`_



.. toctree::
    :hidden:

    self
    using_with_sphinx
    CHANGELOG
