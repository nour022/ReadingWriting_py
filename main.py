# with open('./my_file.txt') as file:
#     # file = open('my_file.txt') # wenn man so nutze muss auch close:
#     contents = file.readline()
#     print(contents)
#     # file.close()
"""
    * mode=  'a' : abend : wenn man nicht löschen will ,
    * mode= 'w' : write  löscht alles und fügt was new
    und wenn path not existeret mach eine neue filw,
    * mode = 'r' : Read
"""
with open("text.txt",mode="a") as file:
    file.write("\nHallo world")