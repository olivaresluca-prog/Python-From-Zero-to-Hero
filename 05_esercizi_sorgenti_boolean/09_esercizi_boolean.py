# verifica patente 
age = int(input(' Quanti anni hai?'))
patente = (input('hai una patente valida?')) .strip().lower()
risultato = age >= 18 and patente == 'si'
print (risultato)

#accesso libreria
check1= input('hai libri arretrati da consegnare?').strip()
check2= input('Sei in possesso di una tessera premium?').lower()
risultato = check1 == 'si' or check2 == 'si' 
print (risultato)
