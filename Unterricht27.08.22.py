#Wortregeln (infinitive form vom Verb ->
#Wortregeln (infinitiv form von verb ->).
#sagen" -> (er/sie/ihr) "sagt",(du) "sagst" (3 Regeln:Präsens)
#"sagen" -> (ich/sie/er) "sagte", (ihr) sagtet, (Plura) "sagten" (4Regeln Präteritum)
#"sagen" -> gesagt (1 Regel Perfekt):

#"leiten" ->(sie/er/ihr) "leitet",(du) "leitest".(ich) "leite" (3 Regel Präsens
#"leiten" -> (er/sie/es/ich) "leitete", (ihr) "leitetet", (du) (leitetest",(wir) "Leiteten" (4 Regeln Präteretum)
#"leiten" -> (hat/habe) geleitet (1 Regel Perfekt

#"schweigen" -> (er/sie/ihr) schweigt,(ich) schweige,(3 Regeln Präsenz)
#"schweigen" -> (er/sie/ich) schwieg,(ihr) schwiegt,(du) schwiegst, "schwiegen" (4 Regeln Präteritum)
#"schweigen" -> (hat/haben) "geschwiegen" (1 Regel Perfekt)

#"tragen" -> (er/sie) trägt,(du) trägst,(ich) trage, (ihr) trägt (4 Präteritum Präsenz)
#"tragen" -> (er/sie/ich) trug,(du) trugst,(ihr) trugt, (sie/wir) trugen (4 Regeln Präteritum)
# "tragen" -> (hat/haben) getragen (1 Regel Perfekt)

def findInfinitivFormPraesenz(einPraesenzWort:str):
    endungen = ["gst","gt","ge"]
    isPraesenzForm = False
    pos = []
    for oneEndung in endungen:
        if einPraesenzWort.endswith(oneEndung):
            result = einPraesenzWort.removesuffix(oneEndung)


            break

    return result    + "en"


#    if einPraesenzWort.endswith("gst") or einPraesenzWort.endswith("gt") or einPraesenzWort.endswith("ge"):

