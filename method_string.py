
a = 'learn python'

# method capitalize
b = a.capitalize()
print(b)
#method upper
c = a.upper()
print(c)
#method lower
d = a.lower()
print(d)
#method swapcase
e = c.swapcase()
print(e)
#method title
f = a.title()
print(f)

#method center
g = a.center(20)
print(g)
h = a.center(20,'-')
print(h)

#rjust method
i = a.rjust(20,'-')
print(i)
#ljust method

k = a.ljust(20,'-')
print(k)

#encode method

m = a.encode(encoding='utf-8',errors='strict')
print(m)

#join method

# n = a.join(['1','2','3'])
# print(n)

#join method
q = a.replace('learn ','',1)
print(q)

#strip method
r = a.strip()
print(r)

#split method

str1 = 'how kteam free education'
str2 = str1.split(' ')

print(str2)