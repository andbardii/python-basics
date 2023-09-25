##### LEZIONE 001 ##### 
# print("Here my first line of python!")

#* CREARE ENVIRONMENT SEPARATI PER I PROGETTI 
# print("python3 -m venv NOME_VIRTUAL_ENVIRONMENT")

##### LEZIONE 002 ##### 
# messaggio = input("inserisci il tuo nome:")
# print("Ciao " + messaggio + "!") --> Ciao Andrea!

#* FARE ATTENZIONE ALL'INDENTAZIONE DEL CODICE
#* NON SI USANO ;

# if 1 < 5:
#     print("minore")
# else:
#     print("maggiore")

##### LEZIONE 003 ##### 
#* NON SI PUO DICHIARARE UNA VARIABILE SENZA SPECIFICARE IL SUO VALORE
#* ATTENZIONE AL CASE SENSITIVE, NON CREARE NOMI CHE USINO - O CHE INIZINO CON NUMERI O SPAZI

# x, y, z = 10, 20, 30
# print(x + y + z)
# w = x + y + z

# citta = ["roma", "milano", "napoli"]
# a, b, c = citta
# print(a , b , c)

##### LEZIONE 004 ##### 
#* TIPI DI DATO IN PYTHON

# str: x = "ciao"
# int: x = 10
# float: x = 20.5
# bool: x = True

# list: x = ["roma", "milano", "napoli"]
# tuple: x = ("roma", "milano", "napoli")
# range: x = range(6)
# dict: x = {"nome":"Andrea", "age":20}
# set: x = {"roma", "milano", "napoli}

#* MENO TIPIZZAZIONE RISPETTO AD ALTRI LINGUAGGI
#* STAMPA IL TIPO DI DATO DELLA VARIABILE print(type(x))

##### LEZIONE 005 ##### 
#* CASTING TRA TIPI DI DATI

# x = int("5")
# y = 5
# print(x + y) --> 10

##### ESERCIZI ##### 

# numero = 5
# nome = "Mario"
# pi = 3.14
# vero_o_falso = True
# numero_come_stringa = str(numero)
# pi_come_intero = int(pi)
# vero_o_falso_come_striga = str(vero_o_falso)

# x = 10
# y = 10
# z = "30"
# print(x + y + int(z)) --> 50

# strfirst = "Hello"
# secondfirst = "World"
# print(strfirst + " " + secondfirst ) --> Hello World

# variabile_bool = True
# print(type(variabile_bool) == False) --> False
# print(type(variabile_bool) == bool) --> True

# lista = [1,2,3,4,5,6,7,8,9]
# print(type(lista) == list) --> True

##### LEZIONE 006 ##### 
