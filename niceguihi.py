from nicegui import ui

# Eine Liste, in der die Eingaben gespeichert werden
name_eingaben_liste = []
# Funktion, die aufgerufen wird, wenn der Button gedrückt wird
def hinzufuegen():
    eingabe_name = eingabe_feld_name.value
    eingabe_email = eingabe_feld_Email.value

    name_eingaben_liste.append(eingabe_name + " ,")
    name_eingaben_liste.append(eingabe_email + " ;")
    print(name_eingaben_liste)



    liste_label_name.text = f"Name Eingaben: {', '.join(name_eingaben_liste)}"

    eingabe_feld_name.value = ''  # Eingabefeld leeren
    eingabe_feld_Email.value = ""


eingabe_feld_name = ui.input('Username Eingabe')
eingabe_feld_Email = ui.input("User Email Eingabe")

button_name = ui.button('User Hinzufügen', on_click=hinzufuegen)


liste_label_name = ui.label('User Eingaben:')




# Server starten
ui.run()
