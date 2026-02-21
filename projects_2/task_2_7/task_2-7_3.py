sequences = ["ATATACGCGTA", "CTTCGGNGGA"]
for seq in sequences:
    print("Последовательность целиком:")
    print(seq)
    print("Та же последовательность построчно:")
    for nucleotide in seq:
        print(nucleotide)
    print("-" * 20) 
print("Цикл выполнен")