def index(K,N):
    i = 1
    while (deal(i,K)<N):
        i+=1
    return i 
def deal(i,K):
    if i==1 or K==1:
        return i
    else:
        return (deal(i-1,K)+deal(i-1,K-1)+1)
    


print(index(2,3))