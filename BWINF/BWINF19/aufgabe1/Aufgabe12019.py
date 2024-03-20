def check_poem(poem):
    words = poem.split()
    word_count = len(words)
    for i in range(word_count // 2):
        index = i
        while index < word_count:
            if index >= word_count:
                break
            index += len(words[index])
        if index >= word_count:
            index = word_count - 1
        if words[index] != words[word_count - 1]:
            return False
    return True

poem = """
Es gingen zwei Parallelen ins Endlose hinaus, zwei kerzengerade Seelen und aus solidem Haus.
Sie wollten sich nicht schneiden bis an ihr seliges Grab: Das war nun einmal der beiden geheimer Stolz und Stab.
Doch als sie zehn Lichtjahre gewandert neben sich hin, da wards dem einsamen Paare nicht irdisch mehr zu Sinn.
Warn sie noch Parallelen? Sie wußtens selber nicht, – sie flossen nur wie zwei Seelen zusammen durch ewiges Licht.
Das ewige Licht durchdrang sie, da wurden sie eins in ihm; die Ewigkeit verschlang sie als wie zwei Seraphim.
"""

poem = poem.replace(",", "").replace(":", "").replace(";", "").replace(".", "").replace("–", "").lower()
print(check_poem(poem))