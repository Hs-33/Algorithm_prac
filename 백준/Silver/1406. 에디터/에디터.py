from collections import deque
import sys
string = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
arr = [sys.stdin.readline().strip().split() for _ in range(n)]
# left = list(string)
# right = deque([])


class Cursor:
    def __init__(self, string, arr):
        self.string = string
        self.arr = arr
        self.left = list(self.string)
        self.right = deque([])
        # self.result = None
        # print(self.left, self.right)

    def L(self):
        if len(self.left)-1 > -1:
            self.right.appendleft(self.left.pop())
        # print(self.left, self.right)
    def D(self):
        if len(self.right)!=0:
            self.left.append(self.right.popleft())
        # print(self.left, self.right)
    def B(self):
        if len(self.left)>0:
        #     self.right.append(self.left.pop())
            self.left.pop()
        # print(self.left, self.right)
    def P(self,i):
        self.left.append(self.arr[i][1])
        # print(self.left, self.right)




    def main(self):
        for i in range(n):
            if self.arr[i][0] == 'L':
                self.L()
            elif self.arr[i][0] == 'D':
                self.D()
            elif self.arr[i][0] == 'B':
                self.B()
            elif self.arr[i][0] == 'P':
                self.P(i)
        print(''.join(self.left)+''.join(self.right))


cur = Cursor(string, arr)
cur.main()



