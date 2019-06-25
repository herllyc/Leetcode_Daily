# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def __init__(self):
        self.ls = []
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        self.ls.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)
        #print(x)
        return self.ls

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == []:
            return
        self.data = data
        t = TreeNode(self.data[0])
        self.data = self.data[1:]
        t.left = self.deserialize(self.data)
        t.right = self.deserialize(self.data)
        return t



