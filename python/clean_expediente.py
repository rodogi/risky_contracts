#!/usr/bin/env python3

import re
import unidecode
import pandas as pd
from glob import glob


main_cols = [
    'CODIGO_EXPEDIENTE',
    'ENTIDAD_FEDERATIVA']


cols_2018 = [
    'Código del expediente',
    'Entidad federativa']

new_cols = dict(zip(cols_2018, main_cols))
regex = re.compile("\d+")
files = glob("/home/rdora/declaranet/data/tables/Expedientes*.csv")
dfs = []
for file in files:
    year = regex.search(file).group()
    print(year)
    if year in ["2018", "2019", "2020"]:
        cols = cols_2018
        df = pd.read_csv(file, usecols=cols)
    else:
        cols = main_cols
        df = pd.read_csv(file, usecols=cols, encoding='latin')
    if year in ["2018", "2019", "2020"]:
        df = df.rename(columns=new_cols)
    df.columns = df.columns.str.lower()
    df['entidad_federativa'] = df['entidad_federativa'].str.lower()
    df['entidad_federativa'] = df['entidad_federativa'].apply(
        unidecode.unidecode)
    dfs.append(df)
    print("-" * 20)
df = pd.concat(dfs)
df.to_csv("/home/rdora/declaranet/data/pre-process/expedientes.csv", index=False)
