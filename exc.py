
#####? ESERCIZIO 001 ##### 
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

#####? ESERCIZIO 002 ##### 
# nome = "Andrea"
# nome.upper()
# print(nome) --> RIMANE Andrea

# cognome = "Bardi"
# print(cognome.replace("a", "e")) --> Berdi

# indirizzo = "Via Massarenti"
# print(indirizzo.split()) --> ['Via', 'Massarenti']
# print(cognome[int(len(cognome)) - 1]) --> i

#####? ESERCIZIO 003 ##### 
# x = 30
# y = 50
# z = 20
# risultato = pow((x + y), 2) - z
# print(risultato) --> 6380
# eta = "25"
# ris = eta * 3
# print(ris) --> 252525
# risultato = int(eta) * 3
# print(risultato) --> 75

#####? ESERCIZIO 004 ##### 
# numero = int(input("Inserisci un numero intero: "))
# if numero % 2 == 0:
#     print("il numero è pari")
# else:
#     print("il numero è dispari")

# numero = int(input("Inserisci un numero intero compreso tra 1 e 10: "))
# if numero > 0 and numero < 10:
#     print("il numero è compreso tra 1 e 10")
# elif numero == 0 or numero == 10:
#     if numero == 0:
#         print("il numero è ugulae a 0")
#     else:
#         print("il numero è uguale a 10")
# else:
#     print("il numero non è compreso tra 1 e 10")

# lettera = input("Inserisci una lettera: ")
# if lettera in "aeiou":
#     print("la lettera è una vocale")
# else:
#     print("la lettera è una consonante")

# taglia = "L"
# colore = "nero"
# if colore == "nero" and (taglia == "L" or taglia == "M"):
#     print("maglietta da acquistare")
# else:
#     print("maglietta non da acquistare")

# numero = int(input("inserisci un numero: "))
# lettera = input("inserisci un lettera: ")
# alfabeto ="abcdefghijklmnopqrstuvwxyz"

# if numero < 0 or len(lettera) > 1:
#     print("valori non validi!")
# else:
#     if numero < 10 and numero % 2 == 0 and lettera in "mpz":
#         print("lettera OK, compresa tra m,p,z")
#     elif 50 <= numero <= 70 and lettera not in "aeiou":
#         print("lettera OK, non è una vocale")
#     elif numero <= len(alfabeto) - 1 and alfabeto[numero] == lettera:
#         print("lettera OK")
#     else:
#         print("lettera sbagliata")

#####? ESERCIZIO 005 ##### 
# while True:
#     numero = int(input("Inserisci un numero"))
#     if numero %2 == 0:
#         break

# n = 1 
# while numero <= 100:
#     print(numero)
#     n += 1
