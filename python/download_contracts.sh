#!/usr/bin/env bash

cd ~/declaranet/data/tables

downPaths=("https://compranetinfo.hacienda.gob.mx/descargas/cnet/Contratos2013.zip"
             "https://compranetinfo.hacienda.gob.mx/descargas/cnet/Contratos2014.zip"
             "https://compranetinfo.hacienda.gob.mx/descargas/cnet/Contratos2015.zip"
             "https://compranetinfo.hacienda.gob.mx/descargas/cnet/Contratos2016.zip"
             "https://compranetinfo.hacienda.gob.mx/descargas/cnet/Contratos2017.zip"
             "https://upcp.hacienda.gob.mx/descargas/Contratos2018.zip"
             "https://upcp.hacienda.gob.mx/descargas/Contratos2019.zip")

for p in "${downPaths[@]}"
do
    wget $p
    zip="$(basename $p)"
    unzip $zip
    rm $zip
done
