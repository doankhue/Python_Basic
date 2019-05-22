list1 = [1,5,3,21,8,91]

#indexing return the item

print(list1[1]) 

print(list1[-1])

#slicing return new list

print(list1[3:])

#oparator + in list

list2 = list1 + [4,5,6,7]

#replace a value of list

list1[0] = 0

print(list1[0])

#function append in list

list1.append(30)
print(list1[-1])

#replace some value

list1[0:3] = [1,2,3]
print(list1[:3])

#count list using function len

print(len(list1))

a,b = 0,1
while a < 10 :
    print(b)
    print(a)
    a,b = b,a+b
