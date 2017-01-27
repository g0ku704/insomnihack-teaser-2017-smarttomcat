#/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
	python apacheattack.py $line 
done < tomcatfuzz.txt

