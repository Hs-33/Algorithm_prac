import sys
num1, num2 = map(int,sys.stdin.readline().strip().split())
a = min(num1, num2)
b = max(num1, num2)
while b != 0:
    r = a%b
    a = b
    b = r
print(a)
print((num1*num2)//a)