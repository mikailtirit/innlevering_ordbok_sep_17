


# oppgave 2 - lage en funksjon som viser alle

def vis_alle():
    if not telefonbok:    #sjekker om listen er tom
        print("telefonboka er tom.")

    else:
        print("\n--- telefonbok ---")
        for person in telefonbok:    #går gjennom alle personer
            print(f"{person['navn']}: {person['nummer']}")  #f-string
            print("--------------\n")  #litt pynt + linjeskrift



