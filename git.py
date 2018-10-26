def is_prime(a):
    for i in range (2,a):
        if a%i==0:
            return False
    else:
        return True
a=int(input("which number you would like to check?: "))
print(is_prime(a))
a=0
print(a)
b=1
