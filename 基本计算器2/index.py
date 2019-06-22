class Solution:
    def calculate(self, s):
        que = []
        for i in s:#多位数
            if i == ' ':
                continue
            if not que:
                que.append(i)
                continue
            if que[-1]!='+' and que[-1]!='-' and que[-1]!='*' and que[-1]!='/':
                if i<='9' and i>='0':
                    x = int(que[-1])*10+int(i)
                    del que[-1]
                    que.append(x)
                    continue
            que.append(i)
        print(que)
        que2 = []
        for i in que:
            if not que2:
                que2.append(i)
                continue
            if que2[-1] == '*':
                x = int(i)*int(que2[-2])
                del que2[-1]
                del que2[-1]
                que2.append(x)
                continue
            if que2[-1] == '/':
                x = int(int(que2[-2])/int(i))
                del que2[-1]
                del que2[-1]
                que2.append(x)
                continue
            que2.append(i)
        print(que2)
        todo = []
        for i in que2:
            if not todo:
                todo.append(i)
                continue
            if todo[-1] == '+':
                x = int(i)+int(todo[-2])
                del todo[-1]
                del todo[-1]
                todo.append(x)
                continue
            if todo[-1] == '-':
                x = int(todo[-2])-int(i)
                del todo[-1]
                del todo[-1]
                todo.append(x)
                continue
            todo.append(i)
        #print(todo)
        return (int(float(todo[0])))

s = Solution()
print(s.calculate("1*2-3/4+5*6-7*8+9/10"))
