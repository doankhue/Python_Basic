
with open('draft.txt','r+') as drFile:
    content = drFile.readlines()
i = 0 
while i< len(content):
    content[i] = content[i].split()
    j = 0 
    while j < len(content[i]):
        if content[i][j] == 'Kteam':
            content[i][j-1] = 'How'
        j +=1
    i +=1
k = 0
with open('newFile.txt','a+') as newFile:
    while k < len(content):
        newFile.write(' '.join(content[k]) + '\n')
        k +=1
print(content)
