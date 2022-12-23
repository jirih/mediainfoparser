#!/bin/bash
rm dist/mediainfoparser-0.1.?-py3-none-any.whl
python setup.py sdist bdist_wheel
pip install -I dist/mediainfoparser-0.1.?-py3-none-any.whl
