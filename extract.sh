#!/bin/bash
i_scriptDir=$(cd "$(dirname "$0")"; pwd)
cd $i_scriptDir
rm dump/source/2*
rm dump/clean/2*
rm dump/extract/2*
rm dump/load/2*
echo extracting $@
cd libscrape
python master.py $@ >> $i_scriptDir/extract.log
echo end estracting $@