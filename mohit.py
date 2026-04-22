n = int(input("Enter a number: "))
a = b = 1

while(b <= n):
 print(b, end = " ")
 a, b = b, a + b
   