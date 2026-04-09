#!/bin/bash

for i in {1..20}; do
 if [ $((i % 2)) -ne 0 ]; then 
echo "$i"
 fi
 if [ $i -eq 15 ]; then 
     break
 fi
done
echo "Цикл завершён"

