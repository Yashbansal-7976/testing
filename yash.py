x=int(input("Enter the number: "))
a=0
b=1
print(a, b, end=' ')
for i in range(x-2):
    c=a+b
    a=b
    b=c
    print(b, end=' ')
