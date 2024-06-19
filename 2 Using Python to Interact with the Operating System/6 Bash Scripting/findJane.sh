#!/bin/bash
>oldFiles.txt
files=$(grep " jane " ~/data/list.txt | cut -d " " -f3)
for f in $files; do
	if test -e "/home/student$f"; then
		echo "/home/student$f" >>oldFiles.txt
	fi
done