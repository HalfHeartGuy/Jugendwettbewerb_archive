#Mose Alphabet
#A	.-	B	-...	C	-.-.	D	-..	E	.	F	..-.
#G	--.


#Regel1:Zwischen zwei Worten 7 "Dits"(Leerzeichen)
#Regel 2:Zwischen zwei Buchstaben 3 "Dits"(Leerzeichen)
#Regel 3:Zwischen jeden -/. kommt 1 "Dit"(Leerzeichen)

#Funktion 1: "MorseCoder" String zu Morse String, bsp.: "AB" -> ".--..."
#Funktion 2:"MOrseDecoder" Morse String tzu String: ".--..." -> AB

morsecode_alphabet = {
    "a" : ". -", "b" : "- . . .", "c" : "- . - .", "d" : "- . .", "e" : ".", "f" : ". . - .", "g" : "- - .", "h" : ". . . .", "i" : ". .", "j" : ". - - -", "k" : "- . -", "l" : ". - . .", "m" : "- -", "n" : "- .", "o" : "- - -", "p" : ". - - .", "q" : "- - . -", "r" : ". - .", "s" : ". . .", "t" : "-", "u" : ". . -", "v" : ". . . -", "w" : ". - -", "x" : "- . . -", "y" : "- . - -", "z" : "- - . .",
    "0" : "- - - - -", "1" : ". - - - -", "2" : ". . - - -", "3" : ". . . - -", "4" : ". . . . -", "5" : ". . . . .", "6" : "- . . . .", "7" : "- - . . .", "8" : "- - - . .", "9" : "- - - - .",

    "."	: ". - . - . -", "," : "- - . . - -", "?"	: ". . - - . .", "'"	: ". - - - - .", "!"	: "- . - . - -", "/"	: "- . . - .", "("	: "- . - - .", ")"	: "- . - - . -", "&"	: ". - . . .", ":"	: "- - - . . .", ";"	: "- . - . - .", "="	: "- . . . -", "+"	: ". - . - .", "-"	: "- . . . . -", "_"	: ". . - - . -", "$"	: ". . . - . . -", "@"	:". - - . - .", "¿"	:". . - . -", "¡"	:"- - . . . -",

    "ä" : ". - . -", "Ö":"- - - .","ẞ":". . . . . .","Ü":". . - -"}
def morseCoder(input_string) -> str:
    lowerStr = input_string.lower()
    result = []
    for one_letter in lowerStr:
        result.append(morsecode_alphabet[one_letter])


    return "   ".join(result)


def morseDecoder(input_morse) -> str:
    #Jeder Buchstabe hat in Morse Code einen Abstand von 3.
    input_morse = input_morse.split("   ")
    result = ""
    for oneletter in input_morse:
        result = result + morseDecodeOneLetter(oneletter)
    return result



def morseDecodeOneLetter(input_oneletter:str) -> str:
    input_oneletter = input_oneletter.lower()




    for key,value in morsecode_alphabet.items():
        if input_oneletter == value:
            return key
    return "error"




def test_morseCoder():
    assert morseCoder("SOS") == ". . .   - - -   . . ."
def test_morseDecoder():
    assert morseDecoder(". . .   - - -   . . .") == "sos"






