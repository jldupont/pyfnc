#!/bin/sh

echo "Tagging & submitting to Pypi, version:" $1
GIT=`which git`

$GIT tag -a $1 -m "version $1"
$GIT push --tags

echo "Submitting egg to Pypi"
python setup.py sdist --formats=zip,gztar upload

