import sys
n = int(sys.stdin.readline().strip())
pattern = sys.stdin.readline().strip().split('*')

start = pattern[0]
end = pattern[-1]

for _ in range(n):
    string = input()
    if len(string) < len(start)+len(end):
        print('NE')
    else:

        if (string[:len(start)] == start) and (string[-len(end):] ==  end):
            print('DA')
        else:
            print('NE')
