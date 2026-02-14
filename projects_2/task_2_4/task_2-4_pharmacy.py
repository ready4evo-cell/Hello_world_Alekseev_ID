overall=int(input("Общее число капсул: "))
package=int(input("Число капсул в одной "))
int=overall // package
rest=overall % package
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {int}")
print(f"Остаток капсул: {rest}")

