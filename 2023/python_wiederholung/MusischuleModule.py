list_instrument = ["Piano","Violin","Cello"]

teachers = {"Violin":"Frau Rehbronn","Piano":"Frau Stock","Cello":"Herr Wong"}
students = {"Piano":["John","Mark"],"Violin":["Mark"],"Cello":[]}
teacher_capacity = 10
instrument_capacity = 20
def getListofInstrument():
    return list_instrument
def getTeacherForinstrument(instrument:str):
    return teachers[instrument]

def getStudentsForINstrument(instrument:str):
    return students.get(instrument)

def registerOneStudentForInstrument(student_name:str,instrument:str):
    if len(students[instrument]) <= teacher_capacity - 1:
        students[instrument].append(student_name)

def addNewInstrument(new_instrument:str):
    list_instrument.append(new_instrument)
    if new_instrument not in list_instrument and len(list_instrument) < 20:

        list_instrument.append(new_instrument)

def updateInstrumentTeacher(teacher:str,instrument:str):

    teachers[instrument] = teacher

def building_the_building_bigger(teacher_capacity,instrument_capacity,valuefortheBiggerBuilding):
    teacher_capacity = teacher_capacity + valuefortheBiggerBuilding
    instrument_capacity = instrument_capacity + valuefortheBiggerBuilding
    return teacher_capacity,instrument_capacity


def istInstrumentAvailable(instrument:str):
    if instrument in list_instrument:

        print("Ja,das Instrument {} ist verfügbar.".format(instrument))
    else:
        print("Nein, das Instrument {} ist nicht verfürbar.".format(instrument))



