import sys
money = int(sys.stdin.readline().strip())
cnt = 0
N = (1000-money)
coins = [500,100,50,10,5,1]
for coin in coins:
    cnt += N // coin
    N = N%coin

print(cnt)