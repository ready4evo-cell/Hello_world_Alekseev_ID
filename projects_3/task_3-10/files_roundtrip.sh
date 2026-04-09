#!/bin/bash
for i in {1..10}; do
touch file"$i".txt
echo "file$i.txt"
done
echo ""
i=10 
while [ $i -ge 1 ]; do
rm file"$i".txt
echo "file$i.txt"
((i--))
done
