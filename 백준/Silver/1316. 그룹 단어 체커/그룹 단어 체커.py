import sys
n = int(sys.stdin.readline().strip())
lst = []
cnt = 0
for _ in range(n):
    lst = []
    word = sys.stdin.readline().strip()
    for i in range(len(word)):
        if word[i] not in lst or word[i] == lst[-1]:
            lst.append(word[i])
        else:
            continue

    if len(word) == len(lst):
        cnt += 1

print(cnt)