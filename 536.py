while True:
    print('Type sum:')
    inputSum = input()
    try:
        inputSum = int(inputSum)
    except:
        print('Type numeric values')
        continue
    if(inputSum < 15 or inputSum > 171):
        print('Sum must be in range 15 to 170 included')
        continue
    with open('536-result.txt', 'w') as resultFile:
        for n in range(5,37):
            for m in range(4,36):
                for l in range(3,35):
                    for k in range(2,34):
                        for j in range(1,33):
                            if j < k and k < l and l < m and m < n:
                                t = (j,k,l,m,n)
                                if sum(t) == inputSum:
                                    resultFile.write("%s\r" % str(t))
    resultFile.close()
    break