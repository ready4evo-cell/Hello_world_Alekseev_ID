#!/bin/bash
read -p "Название гена: " GENE
read -p "Уровень экспрессии: " EXPRESS
if  [[ "$GENE" == "" || "$EXPRESS" == "" ]]; then
	echo "Недостаточнго данных."
else
	echo "Экспрессия гена $GENE составляет $EXPRESS единиц."
fi
