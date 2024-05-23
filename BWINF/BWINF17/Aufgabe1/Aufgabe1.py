numbers_list = [6,11,168,170,202,211,229,233,254,260,272,306,307]
numbers_list2 = [2,7,169,210,203,209,229,175,235]




anzahl_figuren = numbers_list[0]
anzahl_buecher = numbers_list[1]
buecher_hohen = numbers_list[2:]



#general task description(in german):
#Laura hat ein langes Regalbrett an ihrer Wand. Sie
#möchte es hübscher einräumen. Außer ihren Büchern
#sollen auf dem Regal auch vier Deko-Figuren stehen.
#Diese
#Abschnitte möchte sie mit ihren Büchern füllen.
#Wie breit die Abschnitte sind, ist ihr egal. Sie
#möchte aber, dass die Bücher im selben Abschnitt
#alle ungefähr gleich hoch sind. Dazu möchte sie
#sicherstellen, dass der Höhenunterschied zwischen
#dem größten und dem kleinsten Buch im selben
#Abschnitt höchstens 3 cm ist. Ob die Bücher in einem
#Abschnitt inhaltlich zusammenpassen, spielt für
#Laura keine Rolle. Nach dem Umräumen darf kein
#Buch übrig bleiben.
#Junioraufgabe 1
#Schreibe ein Programm, das berechnet, ob eine Aufstellung der Bücher und Figuren nach Lauras
#Wünschen möglich ist. Dein Programm soll auch für
#größere Anzahlen von Deko-Figuren funktionieren.
#Dazu bekommt es als Eingabe die Anzahl der
#Figuren, die Anzahl der Bücher und für jedes Buch
#dessen Höhe (in cm). Du kannst davon ausgehen,
#dass alle Bücher und die Figuren zusammen auf das
#Regal passen.
#Gib zunächst aus, ob eine Aufstellung möglich ist.
#Wenn ja, gib für jeden Abschnitt die Höhen der Bücher
#aus.


#write a function, that compares two numbers.If the two numbers have a maximum difference of 3 then the function should return True, otherwise False
def _compare_numbers(num1:int,num2:int)->bool:
    if abs(num1-num2) <= 3:
        return True
    return False    

#Schreibe eine Funktion, die die Bücher in 5 Abschnitte unterteilt. 
#Die Funktion sortiert zuerst die Bücher nach ihrer Größe.
#Dann teilt die Funktion die Bücher in Abschnitte. Das soll folgendermaßen geschehen:
#Die Funktion geht die sortierte Bücherliste vom Anfang bis zum Ende durch. Dabei wird ein Element aus der Liste genommen und alle Elemente, die einen Differenz zum vorderem Element unter 3cm haben, werden in einem Abschnitt gespeichert.
#Falls einen Höhenunterschied von mehr als 3cm gibt, dann wird ein neuer Abschnitt erstellt.
def _divide_books_into_sections(buecher_hohen:list[int])->list[list[int]]:
    buecher_hohen.sort()
    sections = []
    current_section = []
    for i in range(len(buecher_hohen)):
        if i == 0:
            current_section.append(buecher_hohen[i])
        else:
            if _compare_numbers(buecher_hohen[i], buecher_hohen[i-1]) and _compare_numbers(buecher_hohen[i], current_section[0]):
                current_section.append(buecher_hohen[i])
            else:
                sections.append(current_section)
                current_section = []
                current_section.append(buecher_hohen[i])
    sections.append(current_section)
    return sections



#Schreibe ein Funktion, falls die Anzahl der Abschnitte gleich 5 ist, dann wird True zurückgegeben, sonst False
def _check_sections(sections:list[list[int]])->bool:
    if len(sections) == anzahl_figuren + 1:
        return True
    return False
#Schreibe eine Funktion, die die jedem Abschnitt mit deren Buch zurückgibt, falls true, aber falls false, dann wird Sortierung nicht möglich zurückgegeben
def _get_sections(sections:list[list[int]]):
    if _check_sections(sections):
    
        return sections
    return "Sortierung nicht möglich"
#Wandle die Höhen der Bücher von aktuell mm zu cm um
buecher_hohen = [i/10 for i in buecher_hohen]
print(_get_sections(_divide_books_into_sections(buecher_hohen)))

