numeros = list(range(100, 200))

primos = []
compuestos = []

for num in numeros:
    if num < 2:
        compuestos.append(num)
        continue
    
    es_primo = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
            
    if es_primo:
        primos.append(num)
    else:
        compuestos.append(num)

print(f"Números Primos encontrados ({len(primos)}):")
print(primos)

print(f"\nNúmeros Compuestos (primeros 14):")
print(compuestos[:14]) 