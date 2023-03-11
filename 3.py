import random

list_1 = []
for i in range(0,50):
    list_1.append(random.randint(0,100))
tup1 = ()
tup1 = tuple(list_1)
print(tup1)

list_2 = []
for i in range(0,50):
    list_2.append(random.randint(0,100))
tup2 = ()
tup2 = tuple(list_2)
print(tup2)

b=[]
for i in range(0,50):
    b.append(tup1[i]+tup2[i])
tup3 = ()
tup3=tuple(b)
print(tup3)

c = [b[i] for i in range(0, 50) if b[i] > 120]
print(c,len(c))

e=[min(b),max(b),sum(b)/len(b)]
print(e)

for i in range(0,len(e)):
    b.append(e[i])
print(b)

