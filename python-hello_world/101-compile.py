#!/usr/bin/env python3
import py_compile
import os

py_file = os.environ.get("PYFILE")
if py_file:
    output_file = py_file + "c"
    print("Compiling", py_file, "...")
    py_compile.compile(py_file, cfile=output_file, doraise=True)
else:
    print("Error: Environment variable PYFILE not set.")
    