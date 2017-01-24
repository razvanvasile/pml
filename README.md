# PML

[![Build Status](https://travis-ci.org/simkimsia/UtilityBehaviors.png)](https://travis-ci.org/simkimsia/UtilityBehaviors) [![Coverage Status](https://coveralls.io/repos/github/willrogers/pml/badge.svg?branch=master)](https://coveralls.io/github/willrogers/pml?branch=master) [![Health](https://landscape.io/github/willrogers/pml/master/landscape.svg?style=flat)](https://landscape.io/github/willrogers/pml/)

Python Middlelayer is a Python library intended to make it easy to work with particle accelerators.

## Testing

It is simplest to work with a virtualenv.  Then:

* `pip install -r requirements/local.txt`
* `export PYTHONPATH=.`
* `py.test test`

To see a coverage report:

* `py.test --cov=pml test`
