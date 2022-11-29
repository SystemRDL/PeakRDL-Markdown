Introduction
============

This package implements a Markdown exporter for the PeakRDL toolchain.


Installing
----------

Install from `PyPi`_ using pip:

.. code-block:: bash

    python3 -m pip install peakrdl-markdown

.. _PyPi: https://pypi.org/project/peakrdl-markdown

If you want to use official PeakRDL CLI you can install with ``cli`` extra:

.. code-block:: bash

    python3 -m pip install peakrdl-markdown[cli]

Quick Start
-----------

Exporting to Python interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The module integrates with PeakRDL CLI interface (via optional extra ``cli``):

.. code-block:: bash

    peakrdl markdown input_file.rdl -o output_file.md


Links
-----

- `Source repository <https://github.com/MarekPikula/PeakRDL-Markdown>`_
- `Release Notes <https://github.com/MarekPikula/PeakRDL-Markdown/releases>`_
- `Issue tracker <https://github.com/MarekPikula/PeakRDL-Markdown/issues>`_
- `PyPi <https://pypi.org/project/peakrdl-markdown>`_



.. toctree::
    :hidden:

    self
    using_with_sphinx
    CHANGELOG
