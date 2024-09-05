xis = dict(a = 1, b = 0.4, c = "cc", d = "dd")
print(f" dicionário original {xis} \n")

xis ["e"] = 0
print(f"dicionário ADD1 {xis} \n")

xis ["b"] = 1.4
print(f"dicionário MODIFICADO1 {xis}\n")

del xis["c"]
print(f"deleta item aenas - {xis}\n")

xis.pop("a")
print(f"pop remove item e retorna valor {xis}\n")

print("lembrando que \ n pula uma linha \n")