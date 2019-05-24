
# x = int(input("Please enter an interger:"))
x = 1
if x < 0:
    x = 0
    print('Negative change to zero')
elif x == 0 :
    print('Zero')
elif x == 1 :
    print('Single')
else:
    print('More')

words = ['cat','dog','tiger']
# for statement
for w in words:
    print(w,len(w))

for w in words[:]:
    if len(w) > 3:
        words.insert(0,w)
print(words[:])


#range function

for i in range(5):
    print(i)

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])

print(list(range(2,3)))

for n in range(2,10):
    for x in range(2,n):
        if n % x ==0 :
            print(n,'equals',x,'*',n)
            break
    else:
        print(n,'is a prime number')

for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number",num)
        continue
    print("Found a number",num)




