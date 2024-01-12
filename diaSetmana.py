"""
Iker Blazuqez Valverde Asixc1A
12/1/2024
Te pido un programa que me des un número de la semana y que me devuelva el dia exacto (Lunes a Domingo)
"""
try: 
    dies =  ("" , "Dilluns Lunes Monday" , "Dimarts Martes Tuesday", "Dimecres Miercoles Wednsday", "Dijous Jueves Thursday", "Divendres Viernes Friday", "Dissabte Sábado Saturday", "Diumenge Domingo Sunday")
    dia = int(input())
    while dia =<0 or dia => 8:
        dia = int(input("entre el 1 y el 7"))
    print(dies[dia])

except ValueError:
    print("dades no valides")
