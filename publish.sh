#!/bin/sh

rm -rf dist/
rm -rf build/
python3 setup.py clean sdist bdist_wheel &&
python3 -m twine upload dist/*
