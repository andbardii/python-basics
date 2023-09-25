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

# string: x = "ciao"
# int: x = 10
# float: x = 20.5
# boolean: x = True

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