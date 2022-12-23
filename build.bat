@echo off
rmdir /s /q build dist mediainfoparser.egg-info
python setup.py sdist bdist_wheel