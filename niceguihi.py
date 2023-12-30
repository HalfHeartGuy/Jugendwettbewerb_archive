
from nicegui import ui
from nicegui import *
ui.query('body').classes('bg-gradient-to-t from-blue-200 to-blue-100')
ui.markdown("**minecraft registration**")

# Separate Listen für Namen und E-Mail-Adressen
name_list = []
email_list = []

# Funktion, die aufgerufen wird, wenn der Button gedrückt wird
def hinzufuegen():
    eingabe_name = eingabe_feld_name.value
    eingabe_email = eingabe_feld_Email.value

    # Überprüfung, ob der Name oder die E-Mail bereits existiert
    if eingabe_name in name_list or eingabe_email in email_list:
        ui.notify("Der Benutzername oder die E-Mail existiert bereits.", level='error')
    else:
        # Hinzufügen des neuen Namens und der E-Mail zur Liste
        name_list.append(eingabe_name)
        email_list.append(eingabe_email)

        # Anzeigen der aktualisierten Listen
        liste_label_name.text = "Namen: " + ", ".join(name_list)
        liste_label_email.text = "E-Mails: " + ", ".join(email_list)

    # Eingabefelder leeren
    eingabe_feld_name.value = ''
    eingabe_feld_Email.value = ''

eingabe_feld_name = ui.input('Name Eingabe')
eingabe_feld_Email = ui.input('E-Mail Eingabe')

button_name = ui.button('Benutzer hinzufügen', on_click=hinzufuegen)

liste_label_name = ui.label('Namen:')
liste_label_email = ui.label('E-Mails:')

# Server starten
ui.run()
