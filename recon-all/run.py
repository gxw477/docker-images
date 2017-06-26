#!/usr/bin/env python

import docopt

"""
Run recon-all and generate XNAT Freesurfer assessor

Usage:
    run.py <input-dir> <output-dir> <subject-id> [<other-args>...]
    run.py --help | --version

Options:
    <input-dir>         Directory holding input DICOM data [default: /input]
    <output-dir>        Directory into which output files will be placed [default: /output]
    <subject-id>        Freesurfer subject ID / XNAT session label
    <other-args>        Other arguments to pass to recon-all [default: -all]
    --help              Show this help message and exit
    --version           Show version and exit
"""

__version__ = 1
__author__ = "Flavin"

import subprocess
from docopt import docopt

args = docopt(__doc__, version=__version__)

cmd="whatever"
print("Launching recon-all")
print(cmd)
print(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT))
print("Done")

# Generate assessor