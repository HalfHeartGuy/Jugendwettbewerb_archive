
# Wortregeln (infinitive form von Verb -> ):

# "sagen" -> (er/sie/ihr) "sagt", (du) "sagst",   (ich)"sage" (3 Regel: Präsenz)
# "sagen" -> (ich/sie/er/) "sagte", (du) "sagtest", (ihr) sagtet, (Plura)"sagten"  (4 Regeln Präteritum)
# "sagen" -> gesagt   (1 Regel Perfekt)

# "leiten" -> (sie/er/ihr) "leitet", (du) "leitest", (ich) "leite" (3 Regel: Präsenz)#
# "leiten" -> (er/sie/es/ich) "leitete", (ihr) "leitetet", (du)"leitetest", (wir) "leiteten" (4 Regeln Präteritum)
# "leiten" -> (hat/habe) "geleitet" (1 Regel Perfekt)

# "schweigen" -> (er/sie/ihr) schweigt, (du) schweigst, (ich) schweige, (3 Regeln Präsenz)
# "schweigen " -> (er/sie/ich) schwieg, (ihr) schwiegt, (du) schwiegst, "schwiegen" (4 Regeln Präteritum)
# "schweigen" -> (hat/haben) "geschwiegen" (1 Regel Perfekt)

#  "tragen" -> (er/sie) trägt, (du) trägst, (ich) trage, (ihr)tragt (4 Regeln Präsenz)
#  "tragen" -> (er/sie/ich) trug, (du) trugst, (ihr) trugt, (sie/wir) trugen  (4 Regeln Präteritum)
#  "tragen" -> (hat/haben) getragen (1 Regel Perfekt)

# "geben" -> (er/sie/ihr) gibt, (du) gibst, (ich) gebe (3 Regeln Präsenz)
# "geben" -> (er/sie/ich)gab, (du)gabst, (wir/sie)gaben, (ihr) gabt (4 Regeln Präteritum)
# "geben" -> (hat/haben) gegeben (1 Regel Perfekt)


def findInfinitivFromPraesenz(einPraesenzWort: str):
    endungen = ["gst", "gt", "ge"]
    result = ""

    for oneEndung in endungen:
        if einPraesenzWort.endswith(oneEndung):
            result = einPraesenzWort.removesuffix(oneEndung)
            break

    return result + "gen"


print(findInfinitivFromPraesenz("sagst"))



