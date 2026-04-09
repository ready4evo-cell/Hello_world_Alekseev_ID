#!/bin/bash

printf "%-16s %-3s %-3s %-3s %-3s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do

    if [ ! -s "$file" ]; then
        continue
    fi

    count_A=$(echo "$(grep -v "^>" "$file" | tr -d '\n')" | grep -o "A" | wc -l)
    count_T=$(echo "$(grep -v "^>" "$file" | tr -d '\n')" | grep -o "T" | wc -l)
    count_G=$(echo "$(grep -v "^>" "$file" | tr -d '\n')" | grep -o "G" | wc -l)
    count_C=$(echo "$(grep -v "^>" "$file" | tr -d '\n')" | grep -o "C" | wc -l)
    
    printf "%-11s %-3d %-3d %-3d %-3d\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done
