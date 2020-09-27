"""
# 二叉排序树
# 乱序数据插入的时候，需要准从一个准则：
# 比根节点小的在根节点左边，大的在右边。
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class SortTree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        cur = self.root
        if self.root is None:
            self.root = node
            return
        while True:
            if item > cur.item:  # 向右侧插入
                if cur.right is None:
                    cur.right = node
                    break
                else:
                    cur = cur.right
            else:  # 向左插
                if cur.left is None:
                    cur.left = node
                    break
                else:
                    cur = cur.left

    def forword(self, root):
        """前序"""
        if root is None:
            return
        print(root.item)
        self.forword(root.left)
        self.forword(root.right)

    def middle(self, root):
        """中序"""
        if root is None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)

    def backword(self, root):
        """后序"""
        if root is None:
            return
        self.backword(root.left)
        self.backword(root.right)
        print(root.item)


tree = SortTree()
alist = [3,8,5,7,6,2,9,4,1]
for i in alist:
    tree.add(i)
tree.forword(tree.root)
print('-' * 30)
tree.middle(tree.root)  # 中序遍历是有序的
print('-' * 30)
tree.backword(tree.root)
