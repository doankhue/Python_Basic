
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

