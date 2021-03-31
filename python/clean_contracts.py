#!/usr/bin/env python3

import re
import pandas as pd
from glob import glob


main_cols = [
    'codigo_expediente', 'codigo_contrato',
    'gobierno', 'siglas', 'dependencia', 'claveuc', 'nombre_de_la_uc',
    'responsable', 'codigo_contrato', 'fecha_apertura_proposiciones',
    'caracter', 'tipo_contratacion', 'tipo_procedimiento',
    'forma_procedimiento', 'titulo_contrato', 'fecha_inicio', 'fecha_fin',
    'importe_contrato', 'moneda', 'estatus_contrato', 'proveedor_contratista',
    'estratificacion_mpc', 'siglas_pais', 'anuncio', "folio_rupc"]

cols_2018 = [
    'código del expediente', 'código del contrato',
    'orden de gobierno', 'siglas de la institución', 'institución',
    'clave de la uc', 'nombre de la uc', 'responsable de la uc',
    'código del contrato', 'fecha de apertura', 'carácter del procedimiento',
    'tipo de contratación', 'tipo de procedimiento', 'forma de participación',
    'título del contrato', 'fecha de inicio del contrato',
    'fecha de fin del contrato', 'importe del contrato', 'moneda del contrato',
    'estatus del contrato', 'proveedor o contratista',
    'estratificación de la empresa', 'clave del país de la empresa',
    'dirección del anuncio', 'folio en el rupc']

regex = re.compile("\d+")
files = glob("/home/rdora/declaranet/data/tables/Contratos*.csv")
dfs = []
for file in files:
    year = regex.search(file).group()
    print(year)
    if year in ["2018", "2019", "2020"]:
        cols = cols_2018
    else:
        cols = main_cols
    df = pd.read_csv(file, usecols=cols)
    if year in ["2018", "2019", "2020"]:
        new_cols = dict(zip(cols_2018, main_cols))
        df = df.rename(columns=new_cols)
    dfs.append(df)
    print("-" * 20)
df = pd.concat(dfs)
df.to_csv("/home/rdora/declaranet/data/tables/contratos.csv", index=False)
