import sys
n = int(sys.stdin.readline().strip())
cnt = [1]*n

for i in range(n):
    alphabet = []
    word = sys.stdin.readline().strip()
    for j in range(len(word)):
        if word[j] not in alphabet:
            alphabet.append(word[j])
        else:
            if word[j] == word[j-1]:
                continue
            elif word[j] != word[j-1]:
                cnt[i] = 0
print(sum(cnt))