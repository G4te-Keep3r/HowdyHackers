#!/usr/bin/env bash

for i in *.py
do
	python $i file.${i%.py}
done
