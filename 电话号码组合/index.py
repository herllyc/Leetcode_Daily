

def index(digits):
    tel_dic = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
    print(tel_dic[2])
    if digits=='':
        return['']
    ls = ['']
    for i in digits:
        ls = [x+y for x in ls for y in tel_dic[int(i)]]
    return ls

if __name__ == '__main__':
    str = '23'
    print(index(str))