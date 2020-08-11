import timeit

def getSum():
    inputedSum = int(input('Note* : value must be more than 14 and less than 171\
                            \n Please type value : '))
    if inputedSum < 15 or inputedSum > 170:
        print('Not acceptible sum value, type again')
        getSum()
    return inputedSum

def calcSum(value):
    with open('result.txt', 'w') as resultFile:
        for n in range(5,37):
            for m in range(4,36):
                for l in range(3,35):
                    for k in range(2,34):
                        for j in range(1,33):
                            if j < k and k < l and l < m and m < n:
                                t = (j,k,l,m,n)
                                if sum(t) == value:
                                    resultFile.write("%s\r" % str(t))
    resultFile.close()
calcSum(getSum())