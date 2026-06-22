
# Progetto: Gestione Biblioteca Digitale

# Parte 1 - Variabili e tipi di dati


titolo = "L'ultimo cavaliere"
copie = 5
prezzo_medio = 18.50
disponibile = True

print("Esempio variabili:")
print("Titolo:", titolo)
print("Copie disponibili:", copie)
print("Prezzo medio:", prezzo_medio)
print("Disponibile:", disponibile)

print("\n" + "-" * 50 + "\n")



# Parte 2 - Strutture dati

lista_libri = [
    "L'ultimo cavaliere",
    "La chiamata dei tre",
    "Terre desolate",
    "La sfera del buio",
    "I lupi del Calla",
    "La canzone di Susannah",
    "La Torre Nera",
    "IT",
    "Shining",
    "Misery"
]

copie_libri = {
    "L'ultimo cavaliere": 3,
    "La chiamata dei tre": 2,
    "Terre desolate": 1,
    "La sfera del buio": 2,
    "I lupi del Calla": 1,
    "La canzone di Susannah": 1,
    "La Torre Nera": 2,
    "IT": 4,
    "Shining": 3,
    "Misery": 2
}

utenti_registrati = {
    "Luca Olivares",
    "Marco Rossi",
    "Sara Bianchi"
}

print("Lista libri:")
print(lista_libri)

print("\nDizionario copie disponibili:")
print(copie_libri)

print("\nUtenti registrati:")
print(utenti_registrati)

print("\n" + "-" * 50 + "\n")



# Parte 3 - Classi e OOP


class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        return f"{self.titolo}, scritto da {self.autore}, pubblicato nel {self.anno}. Copie disponibili: {self.copie_disponibili}"


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print("Scheda utente:")
        print("Nome:", self.nome)
        print("Età:", self.eta)
        print("ID utente:", self.id_utente)


class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print("Dettagli prestito:")
        print("Utente:", self.utente.nome)
        print("Libro:", self.libro.titolo)
        print("Autore:", self.libro.autore)
        print("Giorni di prestito:", self.giorni)


# ------------------------------------------------------------
# Parte 4 - Funzionalità
# ------------------------------------------------------------

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili -= 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        print(f"Prestito effettuato: {libro.titolo} a {utente.nome}")
        return nuovo_prestito
    else:
        print(f"Errore: il libro '{libro.titolo}' non ha copie disponibili.")
        return None


# ------------------------------------------------------------
# Creazione oggetti Libro
# ------------------------------------------------------------

libro1 = Libro("L'ultimo cavaliere", "Stephen King", 1982, 3)
libro2 = Libro("La chiamata dei tre", "Stephen King", 1987, 2)
libro3 = Libro("Terre desolate", "Stephen King", 1991, 1)
libro4 = Libro("IT", "Stephen King", 1986, 4)
libro5 = Libro("Shining", "Stephen King", 1977, 3)


# ------------------------------------------------------------
# Creazione oggetti Utente
# ------------------------------------------------------------

utente1 = Utente("Luca Olivares", 39, "U001")
utente2 = Utente("Marco Rossi", 35, "U002")
utente3 = Utente("Sara Bianchi", 30, "U003")


# ------------------------------------------------------------
# Simulazione prestiti
# ------------------------------------------------------------

prestiti_effettuati = []

prestito1 = presta_libro(utente1, libro1, 30)
prestito2 = presta_libro(utente2, libro2, 20)
prestito3 = presta_libro(utente3, libro4, 15)

if prestito1 is not None:
    prestiti_effettuati.append(prestito1)

if prestito2 is not None:
    prestiti_effettuati.append(prestito2)

if prestito3 is not None:
    prestiti_effettuati.append(prestito3)


print("\n" + "-" * 50 + "\n")


# ------------------------------------------------------------
# Stampa elenco aggiornato copie disponibili
# ------------------------------------------------------------

print("Elenco aggiornato copie disponibili:")

tutti_i_libri = [libro1, libro2, libro3, libro4, libro5]

for libro in tutti_i_libri:
    print(libro.info())


print("\n" + "-" * 50 + "\n")


# ------------------------------------------------------------
# Stampa dettagli dei prestiti effettuati
# ------------------------------------------------------------

print("Prestiti effettuati:\n")

for prestito in prestiti_effettuati:
    prestito.dettagli()
    print()