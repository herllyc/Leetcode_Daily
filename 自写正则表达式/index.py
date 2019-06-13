def isMatch(s,p):
    ls_s = list(s)#完整列表
    ls_p = list(p)
    ls_s_processing = list(s)#流程列表
    ls_deal = []
    #print(ls_s,ls_p)
    #try:
    for i in range(len(ls_p)):
        if len(ls_s_processing)==0 :
            if ls_deal == ls_s:
                return True
        if i>0 and ls_p[i-1]=='*':
            try:
                if ls_deal[-1]==ls_p[i]:
                    continue
        if ls_p[i] == '.':#如果该位为.
            ls_deal.append(ls_s_processing[0])
            ls_s_processing = ls_s_processing[1:]
            continue
        if ls_p[i] == ls_s_processing[0]:#如果该位相等
            ls_deal.append(ls_s_processing[0])
            ls_s_processing = ls_s_processing[1:]
            continue
        if ls_p[i] == '*':
            last = ls_p[i-1]
            if last =='.':
                if len(ls_p)==i+1:
                    return True
                beh = ls_p[i+1]
                while len(ls_s_processing):
                    if ls_s_processing[0]==beh:
                        ls_deal.append(ls_s_processing[0])
                        ls_s_processing = ls_s_processing[1:]
                        break
                    ls_deal.append(ls_s_processing[0])
                    ls_s_processing = ls_s_processing[1:]
                continue
            while len(ls_s_processing):
                if last ==ls_s_processing[0]:
                    ls_deal.append(ls_s_processing[0])
                    ls_s_processing = ls_s_processing[1:]
                    continue
                if last != ls_s_processing[0]:
                    break
            continue
        if ls_p[i]!=ls_s_processing[0] and ls_p[i+1]!='*':
            return False
    # except IndexError:
    #     return (1)
         

if __name__=='__main__':
    s = 'aaa'
    p = 'a'
    print(isMatch(s,p))