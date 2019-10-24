======
findme
======

|PyPI| |Pythons| |CI| |Codecov|

.. |PyPI| image:: https://img.shields.io/pypi/v/findme.svg
  :alt: PyPI version
  :target: https://pypi.org/project/findme/

.. |Pythons| image:: https://img.shields.io/pypi/pyversions/findme.svg
  :alt: Supported Python versions
  :target: https://pypi.org/project/findme/

.. |CI| image:: https://travis-ci.com/Julian/findme.svg?branch=master
  :alt: Build status
  :target: https://travis-ci.com/Julian/findme

.. |Codecov| image:: https://codecov.io/gh/Julian/findme/branch/master/graph/badge.svg
  :alt: Codecov Code coverage
  :target: https://codecov.io/gh/Julian/findme


Usage
-----

``findme`` does a simple thing (entirely via Hypothesis):

.. code-block::

    $ findme integers x 'x > 1000'
    1001
