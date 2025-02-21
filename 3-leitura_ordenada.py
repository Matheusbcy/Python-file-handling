names = []

with open("dados/names.txt", "r", encoding="UTF-8") as file:
    for file in file:
        names.append(file.rstrip())


for name in sorted(names):
    print(f"Olá, {name}")
