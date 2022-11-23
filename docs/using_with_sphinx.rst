Using with Sphinx
=================

This PeakRDL extension can be used to include the SystemRDL description in
Sphinx documentation. For now, there is no direct support for reStructuredText
(will be added in future versions), but you can use ``m2r2`` Sphinx extension
to import Markdown files. You can find a complete guide how to install and
enable ``m2r2`` extension on the `project's website`_.

Example
-------

As an example, we can use the following SystemRDL source:

.. literalinclude:: minimal_example.rdl
  :language: systemrdl

The generated Markdown file can be included with the following Sphinx
statement:

.. code-block:: rst

    .. mdinclude:: minimal_example.md

It generates the following output:

.. mdinclude:: minimal_example.md


.. _project's website: https://blog.crossnox.dev/m2r2/
