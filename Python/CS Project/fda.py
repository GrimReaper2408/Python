a = int(input("Enter length of dictionary: "))
dict1 = {}
for x in range(0,a):
    key = int(input("Enter key: "))
    value  = int(input("Enter value for given key: "))
    dict1[x] = [key,value]
print(dict1)
    
