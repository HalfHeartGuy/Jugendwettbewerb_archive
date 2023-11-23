# Pfad zum Bild angeben
f = open("bild01.ppm", encoding = "utf-8")
magicNumber = f.readline().splitlines()
size_x, size_y = f.readline().split()
max = f.readline().splitlines()
body = f.read().splitlines()
f.close()

img = []
row = []
body = [[int(x) for x in row.split()] for row in body]
for i in range(len(body)):
    for j in range(0,len(body[i]),3):
        row.append(([body[i][j],body[i][j+1], body[i][j+2]]))
        if(len(row) == int(size_x)):
            img.append(row)
            row = []
print(img)
# Alternativ kÃ¶nnt ihr auch z.B. die library PIL verwenden und einfach die Bilder im *.png- oder *.tiff-Format einzulesen:
# from PIL import Image
# Pfad zum Bild angeben
# img = Image.open("bild1.tiff")
# img = Image.open("bild1.png").convert("RGB")


