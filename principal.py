def sumar(num1, num2):
  """Suma dos números."""
  return num1 + num2

# Obtener los números del usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar la suma
resultado = sumar(numero1, numero2)

# Mostrar el resultado
print("La suma es:", resultado)