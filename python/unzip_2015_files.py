#!/usr/bin/env python3
"""Script to unzip downloades work-experience files from 2015"""

import zipfile
from glob import glob
import pandas as pd
import os


save_name = "/home/rdora/declaranet/data/2015/2015_experiencia_DBP.csv"
base_dir = "/home/rdora/declaranet/data/2015/experiencia/*.zip"
zip_files = glob(base_dir)
columns = ['ACUSE',
           'SECTOR',
           'PODER',
           'AMBITO',
           'INSTITUCION_EMPRESA',
           'AREA_O_UNIDAD_ADMINSITRATIVA',
           'PUESTO',
           'FUNCION_PRINCIPAL',
           'INGRESO_EGRESO']

data = []
for zip_file in zip_files:
    file = zipfile.ZipFile(zip_file)
    inside_files = file.namelist()
    for inside_file in inside_files:
        extension = os.path.splitext(inside_file)[1]
        if extension == ".csv":
            with file.open(inside_file) as f:
                inside_file = [line.decode(
                    'utf-8').strip().split('","') for line in f]
            data.extend(inside_file[1:])

df = pd.DataFrame(data, columns=columns)
df.to_csv(save_name, index=False)
