import os
import sys

import subprocess as sp
from tempfile import TemporaryDirectory
import shutil
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))

import common


def test_a():

    with TemporaryDirectory() as tmpdir:
        workdir = Path(tmpdir) / "workdir"
        data_path = ".tests/unit/a/data"
        expected_path = ".tests/unit/a/expected"

        # copy data to the temporary workdir
        shutil.copytree(data_path, workdir)

        # run the test job
        sp.check_output([
            "snakemake", 
            "test/0.txt", 
            "-F", 
            "-j1",
            "--directory",
            workdir,
        ])

        # check the output
        common.OutputChecker(data_path, expected_path, workdir).check()
