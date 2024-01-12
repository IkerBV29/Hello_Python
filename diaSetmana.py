"""
Iker Blazuqez Valverde Asixc1A
12/1/2024
Te pido un programa que me des un número de la semana y que me devuelva el dia exacto (Lunes a Domingo)
"""
try: 
    dies =  ("" , "Dilluns" , "Dimarts", "Dimecres", "Dijous", "Divendres", "Dissabte", "Diumenge")
    dia = int(input())
    while dia =<0 or  dia => 8:
        dia = int(input("entre el 1 y el 7"))
    print(dies[ida])

except ValueError:
    print("dades no valides")
