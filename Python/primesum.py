def checkprime(num):
    for x in range(2,num//2 + 1):
        if num%x==0:
            return False
    return True

def prime_sum(num):
    sum = 0
    if num<2:
        print("Number less than 2. This is refute test case.")
        exit()
    for x in range(2,num+1):
        if checkprime(x):
            sum=sum+x
    return sum

num = int(input("Enter number: "))
a = prime_sum(num)
print(a)