import sys

n = int(sys.stdin.readline().strip())
name_dict = {}
for _ in range(n):
    name, status = sys.stdin.readline().strip().split()
    if status == 'enter':
        name_dict[name] = 1
    elif status == 'leave':
        del(name_dict[name])
names = sorted(name_dict.keys(), reverse = True)
for name in names:
    print(name)