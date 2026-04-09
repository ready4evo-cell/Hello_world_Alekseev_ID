#!/bin/bash
read -p "Введите массу тела: " MASS
read -p "Введите рост(м): " HEIGHT
BMI=$((MASS/(HEIGHT**2)))
echo "Индекс массы тела: $BMI"
