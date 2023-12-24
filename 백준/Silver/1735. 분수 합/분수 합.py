import sys
num1 = list(map(int,sys.stdin.readline().strip().split()))
num2 = list(map(int,sys.stdin.readline().strip().split()))

deno = num1[-1]*num2[-1]
numer = (num1[-1]*num2[0])+(num2[-1]*num1[0])

if deno == numer:
    print(f"{1} {1}")
else:
    a = min(deno, numer)
    b = max(deno, numer)
    while b != 0:
        r = a%b
        a = b
        b = r
    print(f"{numer//a} {deno//a}")