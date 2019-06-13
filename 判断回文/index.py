def index(s):
    s1 = s = s.upper()
    s2 = s1[-1::-1]
    l1 = ''
    l2 = ''
    for i in s1:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            l1+=i
    for i in s2:
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            l2+=i
    return (l1==l2)




print(index("t,n8'`q`?55t`q`'8n,?"))