






# Oppgave 5 – Lag en hovedmeny

def hovedmeny():
    while True:  # kjør helt til brukeren velger å avslutte
        print("Hva vil du gjøre?")
        print("1. Vis alle")
        print("2. Legg til ny")
        print("3. Søk")
        print("4. Avslutt")

        valg = input("Skriv inn ditt valg (1-4): ")

        if valg == "1":
            vis_alle()
        elif valg == "2":
            legg_til()
        elif valg == "3":
            sok()
        elif valg == "4":
            print("Avslutter programmet...")
            break  # avslutter while-løkken
        else:
            print("Ugyldig valg, prøv igjen.\n")




