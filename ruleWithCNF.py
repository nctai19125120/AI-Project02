SIZE = 8
f = open("rulecnf.txt", "w")
#------------------------------RULES--------------------------------------------
#ONE QUEEN IN A ROW
def outputRowAtLeast1():
    for i in range (SIZE):
        for j in range (SIZE):
            # if j==0:
            #     #print("(", end="")
            if (j!=SIZE-1):
                print("b[%d][%d] v " %(i,j), end="")
                f.write("b[%d][%d] v " %(i,j))
            else:
                print("b[%d][%d] v " %(i,j), end="")
                f.write("b[%d][%d]" %(i,j))
            if j==SIZE-1 and i!=SIZE-1:
                #print(") ^ ", end="")
                print("")
                f.write("\n")
            elif j==SIZE-1 and i==SIZE-1:
                #print(")", end= "")
                print("")
                f.write("\n")
outputRowAtLeast1()

def outputRowAtMost1():
    for i in range (SIZE):
        for j in range (SIZE-1):
            for k in range(j+1, SIZE):
                print("not(b[%d][%d]) v not(b[%d][%d])" %(i,j,i,k))
                f.write("not(b[%d][%d]) v not(b[%d][%d])\n" %(i,j,i,k))
                # if (i != SIZE-1 or j != SIZE-2 or k != SIZE-1):
                #     #print("^", end="")
                #     print("")
outputRowAtMost1()

#ONE QUEEN IN A COLUMN
def outputColumnAtLeast1():
    for i in range (SIZE):
        for j in range (SIZE):
            # if j==0:
            #     #print("(", end="")
            if (j!=SIZE-1):
                print("b[%d][%d] v " %(j,i), end="")
                f.write("b[%d][%d] v " %(j,i))
            else:
                print("b[%d][%d]" %(j,i), end="")
                f.write("b[%d][%d]" %(j,i))
            if j== SIZE-1 and i!=SIZE-1:
                #print(") ^ ", end="")
                print("")
                f.write("\n")
            elif j==SIZE-1 and i==SIZE-1:
                #print(")", end= "")
                print("")
                f.write("\n")
outputColumnAtLeast1()

def outputColumnAtMost1():
    for i in range (SIZE):
        for j in range (SIZE-1):
            for k in range(j+1, SIZE):
                print("not(b[%d][%d]) v not(b[%d][%d])" %(j,i,k,i), end="")
                f.write("not(b[%d][%d]) v not(b[%d][%d])" %(j,i,k,i))
                if (i != SIZE-1 or j != SIZE-2 or k != SIZE-1):
                    #print("^", end="")
                    print("")
                    f.write("\n")
outputColumnAtMost1()
f.write("\n")
print("")

#NO MORE THAN 1 QUEEN IN THE LEFT DIAGONAL & RIGHT DIAGONAL
for i in range(SIZE * SIZE - 1):
  for j in range(i + 1, SIZE * SIZE):
    if ((i % SIZE + int(i/SIZE) == j % SIZE + int(j/SIZE)) or (i % SIZE - int(i/SIZE) == j % SIZE - int(j/SIZE))):
      print("not(b[%d][%d]) v not(b[%d][%d]) " %(i % SIZE, int(i/SIZE), j%SIZE, int(j/SIZE)) , end="")
      f.write("not(b[%d][%d]) v not(b[%d][%d])" %(i % SIZE, int(i/SIZE), j%SIZE, int(j/SIZE)))
      if i%SIZE+1 != SIZE or int(i/SIZE)+1 != SIZE-1:
        #print("^ ", end="")
        print("")
        f.write("\n")