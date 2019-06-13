class Trie:
    def __init__(self):
        self.dic = {}
    def insert(self,word):
        dic_todo = self.dic
        for i in word:
            if i in dic_todo:
                dic_todo = dic_todo[i]
            else:
                dic_todo[i] = {}
                dic_todo = dic_todo[i]
        dic_todo['99999'] = 1
        print(self.dic)
    def search(self,word):
        dic_todo = self.dic
        for i in word:
            if i in dic_todo:
                dic_todo = dic_todo[i]
            else:
                return False
        if '99999' in dic_todo:
            return True
        return False
    def startWith(self,prefix):
        dic_todo = self.dic
        for i in prefix:
            if i in dic_todo:
                dic_todo = dic_todo[i]
            else:
                return False
        return True

t = Trie()
t.insert('apple')
t.insert('app')
print(t.search('app'))
print(t.startWith('apple'))

        #{'a':{'p':{}}}