import array as a

val = a.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(0,len(val)):
    print(val[i] , end=" ")
    
# print('\n')
# for x in val:
#     print(x, end= ' , ')
    
# print('\n')
    
# print(val.typecode)

# val.reverse()

# for i in range(0,len(val)):
#     print(val[i] , end=" ")
    
# print('\n')   

# val.insert(1, 50)
# val.append(100)
# val[2] = 100

copyArray = a.array(val.typecode, (x for x in val))

for i in range(0,len(val)):
    print(copyArray[i] , end=" ")