file_open = open("Example_input","r")

for x in file_open:
    print(x)

file_write = open("Example_input","a")
for i in range(0,10):
    file_write.write("\nMartin,Tanya,Max")

file_open.close()

print(file_write.readline())
