fh = open('result.txt', 'w')

inpt = int()

def showSumPrompt():
    global inpt
    inpt = int(input("5/36 : "))
    if inpt < 15 or inpt > 170:
        print("Value must be more than 15 and less than 170")
        showSumPrompt()

showSumPrompt()

for n in range(5,37):
    for m in range(4,36):
        for l in range(3,35):
            for k in range(2,34):
                for j in range(1,33):
                    if j < k and k < l and l < m and m < n:
                        t = (j,k,l,m,n)
                        if sum(t) == inpt:
                            fh.write("%s\r" % str(t))

fh.close()