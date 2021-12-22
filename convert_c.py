file_path = 'rulecnf.txt'

file_text = open(file_path, "r")

a = True
array = []
numberOfLoop = 0
k = 0
while a:
    # numberOfLoop+=1
    file_line = file_text.readline()
    line = file_line.split(" v ")
    # print(line)
    arrayItem = []
    for element in line:
        # print(element)
        if element == "":
            continue
        if element[0] == "n":
            i = int(element[6])
            j = int(element[9])
            k = -1
            #not(b[i][j])
        else:
            i = int(element[2])
            j = int(element[5])
            k = 1
            #b[i][j]
        v = (8*i + j + 1)*k
        arrayItem.append(v)
    if len(arrayItem)!=0:
        array.append(arrayItem)

    if not file_line:
        # print("End Of File")
        a = False
file_text.close()