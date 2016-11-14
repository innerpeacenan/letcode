#最初有几个误区，root结构没弄清楚，注意审题，然后就是分为主节点，和枝节点两部分处理，主节点存入，枝节点判断有无，有升级为主节点存入再获取其枝节点，直到无枝节点
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tree=[] #初始化树
    def levelOrder(self, root):
        self.tree=[]
        key=[]
        next_key=[]
        # if root.val=None:
        #     return key
        try:
            key.append(root.val)#根节点，如果有的话存入key，并作为一个数组存入树中
            self.tree.append(key)
        except:
            return self.tree
        if root.left!=None:#如有左右子节点，放入next_key中
            next_key.append(root.left)
        if root.right!=None:
            next_key.append(root.right)
        
        if len(next_key)>0:
            self.count(next_key)#如有左右子节点，进入count函数，重复以上过程直到next_key为空
        return self.tree
        
    def count(self,jiedian):
        key=[]
        next_key=[]
        l=len(jiedian)
        for i in range(l):
            key.append(jiedian[i].val)
            if jiedian[i].left!=None:
                next_key.append(jiedian[i].left)
            if jiedian[i].right!=None:
                next_key.append(jiedian[i].right)
        self.tree.append(key)
        if len(next_key)>0:
            self.count(next_key)
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """