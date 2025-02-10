#Write a c and python program to randomly generate a list of 10 even numbers between 1 and 100 inclusive.
import random
a = []
def listval(a):
    for x in range(1,101):
        if x%2==0:
            a.append(x)



listval(a)
c=[]
for x in range(10):
    b = random.randint(0,49)
    c.append(a[b])
print(c)

