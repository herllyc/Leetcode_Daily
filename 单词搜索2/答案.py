class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        node = Trie()
        for word in words:
            node.insert(word)
        node = node.root

        visited = [[0] * len(board[0]) for i in range(len(board))]
        result = []
        temp = ''
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] in node:
                    self.sea(board, i, j, visited, node, temp, result)
        return result
    def sea(self, board, i, j, visited, node, temp, result):
        row = len(board)
        col = len(board[0])

        if '#' in node and temp not in result:#判断是否到头
            result.append(temp)
            return
        if i > row-1 or i < 0 or j > col-1 or j < 0:#越界
            return
        if board[i][j] not in node or visited[i][j] == 1:#如果不匹配或路径不通
            return

        temp += board[i][j]
        visited[i][j] = 1
        self.sea(board, i + 1, j, visited, node[board[i][j]], temp, result)
        self.sea(board, i - 1, j, visited, node[board[i][j]], temp, result)
        self.sea(board, i, j + 1, visited, node[board[i][j]], temp, result)
        self.sea(board, i, j - 1, visited, node[board[i][j]], temp, result)        
        visited[i][j] = 0
