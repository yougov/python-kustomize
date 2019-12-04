python-kustomize
================

Build your Kubernetes manifests for Kustomize in Python!

.. image:: https://img.shields.io/pypi/v/kustomize.svg
   :target: https://pypi.org/project/kustomize

.. image:: https://img.shields.io/pypi/pyversions/kustomize.svg

.. image:: https://img.shields.io/travis/yougov/python-kustomize/master.svg
   :target: https://travis-ci.org/yougov/python-kustomize

.. .. image:: https://img.shields.io/appveyor/ci/yougov/python-kustomize/master.svg
..    :target: https://ci.appveyor.com/project/yougov/python-kustomize/branch/master

.. .. image:: https://readthedocs.org/projects/kustomize/badge/?version=latest
..    :target: https://kustomize.readthedocs.io/en/latest/?badge=latest

* PyPI: https://pypi.org/project/kustomize/
* Repository: https://github.com/yougov/python-kustomize
* Documentation: https://python-kustomize.readthedocs.io/en/latest/

Overview
--------

The reason for this project to exist is to make it easier to create dynamic
manifests to be exported for usage in Kubernetes' "Kustomize" tool. And, by
using Python and supporting the "dataclasses" language feature, it also helps
reducing boilerplate by encouraging code reuse.

Kustomize, by itself, is already a very powerful tool, and it's possible to
deal with different apps and environments by using the "overlays" approach; but
it's not dynamic enough if you need to define manifests parameters through
environment variables, for example. So this project aims to cover that gap.

A complement for Kustomize
--------------------------

This project is by no means a replacement for Kustomize, but rather a
complement. The idea is to generate kustomization files from Python files, and
then use ``kubectl apply -k`` or ``kustomize build`` to transform them into
final manifests for Kubernetes (even applying them to the cluster).

In other words, the idea is to "compile" Python files into Kustomize files, then
just use Kustomize for the rest of the deployment.

Installing
----------

The only mandatory dependency to this project is ``PyYAML``. Besides this, you
can have ``attr`` installed if you want to use their classes, and, if you're
running on Python 3.6, you can install ``dataclasses`` to use them - although
this project is tested on Python 3.7 and 3.8 only, it probably runs fine on 3.6.

This package will be available as ``kustomize``; you may install it with pip,
for example::

    $ pip install kustomize

This will also install ``PyYAML`` if it's not already installed.

Alternatively, you can use any other package manager capable of installing
packages from PyPI.

Usage
-----

The summary is:

1. You write a source directory with Python files representing the Kustomize
   files (see directories at ``python-kustomize/tests/fixtures/``);
2. You run::

   $ pykustomize <source-dir> <dest-dir>

   where ``<dest-dir>`` will be
   the directory where Kustomize YAML files will be put at;
3. Then you can apply the generated Kustomize files into your cluster::

   $ kubectl apply -f <dest-dir>

   and done!
