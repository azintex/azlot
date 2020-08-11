result = open('result.txt', 'w')

inputedSum = int(input('Type sum : '))

if(inputedSum < 15 or inputedSum > 170):
    print('Sum must be more than 14 and less 171')


# def showPrompt():
#     return int(input('Type sum more than 15 and less 170 : '))


# def getSum():
#     #inputedSum = int(input('Sum must be more than 15 and less 170 : '))
#     value = showPrompt()
#     if value < 15 or value > 170:
#         print('Not acceptible sum value, type again')
#         showPrompt()
#     return value

# def calcSum(value):
#     for n in range(5,37):
#         for m in range(4,36):
#             for l in range(3,35):
#                 for k in range(2,34):
#                     for j in range(1,33):
#                         if j < k and k < l and l < m and m < n:
#                             t = (j,k,l,m,n)
#                             if sum(t) == value:
#                                 result.write("%s\r" % str(t))
#                                 result.close()

# calcSum(getSum())