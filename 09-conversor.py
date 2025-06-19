# Ejercicio convertir temp 


temperatura = float(input("Digite la temperatura: "))
escala = str(input("Es Fahrenheit(F) o Celcius(C)?: ")).upper() # leer y Convertir a mayusculas


if escala == "F":
    temperatura = (temperatura-32)/1.8
    print("Temperatura en celsius: ", temperatura)
elif escala == "C":
    temperatura = (temperatura*1.8)+32
    print("Temperatura en Fahrenheit: " , temperatura)
else :
    print("ERROR: Escala no reconocida")