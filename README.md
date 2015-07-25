# Can I Use PyPy?

[![Build Status](https://travis-ci.org/public/caniusepypy.svg?branch=master)](https://travis-ci.org/brettcannon/caniusepypy)

This is a minor variation on [caniusepython3](https://github.com/brettcannon/caniusepython3) which checks for PyPy compatibility instead of Python 3.

# How do you tell if a project has been ported to PyPy?

On [PyPI](https://pypi.python.org/) each project can specify various
[trove classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers)
(typically in a project's `setup.py` through a [`classifier`](https://docs.python.org/3/distutils/setupscript.html#additional-meta-data)
argument to `setup()`).
There are various classifiers related to what version of Python a project can
run on. E.g.:

    Programming Language :: Python :: 3
    Programming Language :: Python :: Implementation :: PyPy

As long as a trove classifier for some version of PyPy is specified then the
project is considered to support PyPy.

## What if I know of a project that should be added to the overrides file?

If a project has PyPy support in a release on PyPI but they have not added the
proper trove classifier, then either submit a
[pull request](https://github.com/public/caniusepypy/pulls) or file an
[issue](https://github.com/public/pypy/issues) with the name of the
project and a link to some proof that a release available on PyPI has indeed been
ported (e.g. PyPI page stating the support, tox.ini file showing tests being run
against Python 3, etc.). Projects that have PyPy support in their version control
system but not yet available on PyPI will **not** be considered for inclusion in the
overrides file.


# How can I get a project ported to PyPy?

Typically projects which have not switched to Python 3 yet are waiting for:

* A dependency to be ported to PyPy
* Someone to volunteer to put in the time and effort to do the port

Since `caniusepypy` will tell you what dependencies are blocking a project
that you depend on from being ported, you can try to port a project farther
down your dependency graph to help a more direct dependency make the transition.

Which brings up the second point: volunteering to do a port. Most projects
happily accept help, they just have not done the port yet because they have
not had the time ("volunteering" can also take the form of paying someone to do
the port on your behalf). Some projects are simply waiting for people to ask for it,
so even speaking up politely and requesting a port can get the process started.

# Change Log

## 1.0.0

Based on caniusepython3 90fe11eda597c44750255fa76577e5d374b05579.
