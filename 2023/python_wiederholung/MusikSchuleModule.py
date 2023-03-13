
## Hausaufgaben:
## Violin: maximal 8 Studenten, Piano: maximal 10 Studenten, Cello: maximal 3, Fläto: maximla 5
## Augabe 1: erstelle eine Variable "capacity" um diese Information "LehrerKapazität" zu speichern.
## Aufgabe 2: Funktion "addNewInstrument" erweitern um capacity.
## Aufgabe 3: Funktion "registerOneStudentForInstrument" so anzupassen, dass wenn die Studentliste eines Instrument an der Kapazitätgrenze ist,
# dann wird der Satz geprintet "Leider für dies Instrument {} gibt es aktuell keinen Platz mehr!". Im Fall von erfolgreicher Registrierung wird die Liste "students" erweitert, und der Satz "Gratuliere, du {} bist für das Instrument {} erfolgreich registiert!".



file_open = open("Example_input","r")





list_instrument = {"Piano", "Violin", "Cello"}
teachers = {"Violin": "Rehbronn", "Piano": "Stock", "Cello": "Bauer"}
students = {}
students_list = []
teacher_capacities = {"Rehbronn":8,"Stock":10,"Bauer":5}
counter = 0
for x in file_open:
    students_list.append(x)

print(students_list)







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


    try:
        teacher_name = teachers[instrument]
        teacher_capacity = teacher_capacities[teacher_name]

        if len(students[instrument]) < teacher_capacity:
            students[instrument].append(student_name)
            print("Gratuliere, du {} bist für das Instrument {} erfolgreich registiert!".format(student_name,instrument))
        else:
            print("Leider gibt es für das Instrument {} keinen Platz mehr!".format(instrument))
    except:
        print("Leider ist für das Instrument {} gibt es aktuell keinen Lehrer".format(instrument))
