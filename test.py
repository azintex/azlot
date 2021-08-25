# balls = []

# for i in range(1,36):
    # balls.append(i)
    
# for i in range(2,37):
    # balls.append(i)
    
# for i in range(3,38):
    # balls.append(i)
    
# for i in range(4,39):
    # balls.append(i)
    
# for i in range(5,40):
    # balls.append(i)
    
# for i in range(6,41):
    # balls.append(i)

# print(len(balls))
lst = []
for j in range(1,36):
    for k in range(2,37):
        for l in range(3,38):
            for m in range(4,39):
                for n in range(5,40):
                    for p in range(6,41):
                        t = (j,k,l,m,n,p)
                        lst.append(t)
                    #lst.append((j,k,l,m,n))
print(lst)