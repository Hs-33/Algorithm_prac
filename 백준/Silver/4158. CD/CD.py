import sys


while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    lst_a = set([int(sys.stdin.readline()) for _ in range(n)])
    lst_b = set([int(sys.stdin.readline()) for _ in range(m)])
    
    print(len(lst_a&lst_b))
    
    