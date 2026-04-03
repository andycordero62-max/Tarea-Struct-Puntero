valor1 = 6767676
valor2 = 1313131

resultado = valor1 * valor2

resultado_texto = str(resultado)

resultado_cambiado = f"{resultado:,}".replace(",", ".")

print(f"El primer valor es: {valor1}")
print(f"El segundo valor es: {valor2}")
print("-" * 30)
print(f"Resultado en caracteres: {resultado_texto}")
print(f"Resultado legible: {resultado_cambiado}")