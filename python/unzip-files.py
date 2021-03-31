#!/usr/bin/env python3

import re
import os
import glob
import zipfile

PATH = "/home/rdora/declaranet/data"

files = glob.glob("/home/rdora/Downloads/[0-9]*")
bases = map(os.path.basename, files)

for f, base in zip(files, bases):
    year = re.search(r'[0-9]+', base).group()
    path = os.path.join(PATH, year)
    with zipfile.ZipFile(f) as zip_ref:
        zip_ref.extractall(path=path)
