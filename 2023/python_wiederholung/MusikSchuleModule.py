
## Hausaufgaben:
## Violin: maximal 8 Studenten, Piano: maximal 10 Studenten, Cello: maximal 3, Fläto: maximla 5
## Augabe 1: erstelle eine Variable "capacity" um diese Information "LehrerKapazität" zu speichern.
## Aufgabe 2: Funktion "addNewInstrument" erweitern um capacity.
## Aufgabe 3: Funktion "registerOneStudentForInstrument" so anzupassen, dass wenn die Studentliste eines Instrument an der Kapazitätgrenze ist,
# dann wird der Satz geprintet "Leider für dies Instrument {} gibt es aktuell keinen Platz mehr!". Im Fall von erfolgreicher Registrierung wird die Liste "students" erweitert, und der Satz "Gratuliere, du {} bist für das Instrument {} erfolgreich registiert!".

list_instrument = {"Piano", "Violin", "Cello"}
teachers = {"Violin": "Frau Riebon", "Piano": "Frau Stock", "Cello": "Frau Bauer"}
students = {"Piano":["John", "Mark"], "Violin":["Mark"], "Cello": []}




def isInstrummentAvaialable(instrument:str):
    if instrument in list_instrument:
        print("Ja, dies Instrument {} ist da".format(instrument))
    else:
        print("Nein, dies Instrument {} ist nicht verfügbar".format(instrument))

def getListOfInstrument():
    return list_instrument

def addNewInstrument(new_instrument:str):
   list_instrument.append(new_instrument)


def getTecherForInstrument(instrument: str):
    return teachers[instrument]

def updateInstrumentTeacher(teacher:str, instrument:str):
    teachers[instrument] = teacher


def getStudentsForInstrument(instrument: str):
    return students.get(instrument)

def registerOneStudentForInstrument(student_name: str, instrument:str):
    students[instrument].append(student_name)

