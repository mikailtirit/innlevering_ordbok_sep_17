



# Oppgave 4 – Lag en funksjon som søker etter en person

def sok():
    navn = input("Hvem vil du søke etter? ").lower()
    funnet = False  # flagg som viser om vi fant noen

    for person in telefonbok:
        if person["navn"].lower() == navn:  # sammenlign med .lower()
            print(f"Fant: {person['navn']} - {person['nummer']}\n")
            funnet = True
            break  # avslutt løkken når vi finner en match

    if not funnet:  # hvis vi ikke fant noen
        print("Personen finnes ikke i telefonboka.\n")



