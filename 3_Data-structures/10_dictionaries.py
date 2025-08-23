"""Ejercicio 4 
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.""" 

months = {
    "01": "January", "02": "February", "03": "March", "04": "April",
    "05": "May", "06": "June", "07": "July", "08": "August",
    "09": "September", "10": "October", "11": "November", "12": "December"
}

date = input("Enter a date (dd/mm/yyyy): ")
day, month, year = date.split("/")

print(f"{day} of {months[month]} of {year}")