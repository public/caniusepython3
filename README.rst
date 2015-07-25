Can I Use PyPy?
================

This script takes in a set of dependencies and then figures out which
of them are holding you up from porting to PyPy.

Command-line/Web Usage
----------------------

You can specify your dependencies in multiple ways::

    caniusepypy -r requirements.txt test-requirement.txt
    caniusepypy -m PKG-INFO
    caniusepypy -p numpy scipy ipython
    # If your project's setup.py uses setuptools
    # (note that setup_requires can't be checked) ...
    python setup.py caniusepypy

The output of the script will tell you how many (implicit) dependencies you need
to transition to PyPy in order to allow you to make the same transition. It
will also list what projects have no dependencies blocking their
transition so you can ask them to start a port to PyPy.


Integrating With Your Tests
---------------------------

If you want to check for PyPy availability as part of your tests, you can
use ``caniusepypy.check()``:

.. code-block:: python

    def check(requirements_paths=[], metadata=[], projects=[]):
        """Return True if all of the specified dependencies have been ported to PyPy.

        The requirements_paths argument takes a sequence of file paths to
        requirements files. The 'metadata' argument takes a sequence of strings
        representing metadata. The 'projects' argument takes a sequence of project
        names.

        Any project that is not listed on PyPI will be considered ported.
        """

You can then integrate it into your tests like so:

.. code-block:: python

  import unittest
  import caniusepypy

  class DependenciesOnPython3(unittest.TestCase):
    def test_dependencies(self):
      # Will begin to fail when dependencies are no longer blocking you
      # from using PyPy.
      self.assertFalse(caniusepypy.check(projects=['ipython']))

For the change log, how to tell if a project has been ported, as well as help on
how to port a project, please see the
`project website <https://github.com/brettcannon/caniusepypy>`__.
