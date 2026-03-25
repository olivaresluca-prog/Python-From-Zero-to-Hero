print('esercizio 1') 
frase = input('inserisci una frase: ')
separazione = frase.split()
print(separazione)
inversione_frase = separazione[::-1]
risultato = " ".join(inversione_frase)
print (risultato)

print('esercizio2')
frase_2 = "I topi non avevano nipoti"
print(frase_2)
normalizzazione = frase_2.lower().replace(" ", "")
print(normalizzazione)
print(normalizzazione[::-1])
if normalizzazione == normalizzazione [::-1]:
    print('la frase é palindroma')
else:
    print('la frase non é palindroma')