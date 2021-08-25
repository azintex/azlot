while True:
    print('Type sum:')
    inputSum = input()
    try:
        inputSum = int(inputSum)
    except:
        print('Type numeric values')
        continue
    if(inputSum < 21 or inputSum > 225):
        print('Sum must be in range from 21 to 225 included')
        continue
    with open('640-variations.txt', 'w') as resultFile:
        for n in range(6,41):
            for m in range(5,40):
                for l in range(4,39):
                    for k in range(3,38):
                        for j in range(2,37):
                            for i in range(1,36):
                                if i < j and j < k and k < l and l < m and m < n:
                                    t = (i,j,k,l,m,n)
                                    if sum(t) == inputSum:
                                        resultFile.write("%s\r" % str(t))
        resultFile.close()
    break