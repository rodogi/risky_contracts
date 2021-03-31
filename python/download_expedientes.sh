#!/usr/bin/env bash

cd ~/declaranet/data/tables

downPaths=("https://compranetinfo.hacienda.gob.mx/descargas/cnet/ExpedientesPublicados2010-2017.zip"
           "https://compranetinfo.hacienda.gob.mx/descargas/cnet/ExpedientesPublicados2018.zip"
           "https://upcp.hacienda.gob.mx/descargas/ExpedientesPublicados.zip"
           "https://upcp.hacienda.gob.mx/descargas/ExpedientesPublicados2020.zip"
           "https://upcp.hacienda.gob.mx/descargas/Instituciones.zip"
           "https://upcp.hacienda.gob.mx/descargas/InstitucionesLocales.zip"
           "https://upcp.hacienda.gob.mx/descargasy/UC.zip"
           "https://upcp.hacienda.gob.mx/descargas/CUCOP.zip"
           "https://upcp.hacienda.gob.mx/descargas/Instituciones.zip"
           "https://upcp.hacienda.gob.mx/descargas/InstitucionesLocales.zip")

for p in "${downPaths[@]}"
do
    wget $p
    zip="$(basename $p)"
    unzip $zip
    rm $zip
done
