import array as a

val = a.array('d', [1, 2, 3, 4, 5, 6, 7, 8, 9.5])

for i in range(0,len(val)):
    print(val[i] , end=" ")
    
print('\n')
for x in val:
    print(x, end= ' , ')