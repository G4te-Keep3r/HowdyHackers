#!/usr/bin/env bash

for i in *.py
do
	echo python $i file.${i%.py}
done