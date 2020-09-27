"""
二叉树：
    根节点
    叶子节点
        左叶子节点
        右叶子节点
    树的层级
    树的深度
二叉树的遍历
    广度优先遍历
        一层一层的对节点进行遍历
    深度优先遍历
        前序：先根    根左右
        中序：中根    左根右
        后序：后根    左右根
"""
class Node():
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
    def addNode(self, item):
        node = Node(item)
        # 如果插入的是根节点
        cur = self.root
        if cur == None:
            self.root = node
            return
        q = [cur]  # 其实是一个队列,里边的元素是进行遍历判断的节点
        while len(q) != 0:
            nd = q.pop(0)
            if nd.left == None:
                nd.left = node
                return
            else:
                q.append(nd.left)
            if nd.right == None:
                nd.right = node
                return
            else:
                q.append(nd.right)
    def travel(self):
        cur = self.root
        q = [cur]
        while len(q) != 0:
            nd = q.pop(0)
            print(nd.item)
            if nd.left:
                q.append(nd.left)
            if nd.right:
                q.append(nd.right)

    def forword(self, root):
        """前序"""
        if root == None:
            return
        print(root.item)
        self.forword(root.left)
        self.forword(root.right)

    def middle(self, root):
        """中序"""
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)

    def backword(self, root):
        """后序"""
        if root == None:
            return
        self.backword(root.left)
        self.backword(root.right)
        print(root.item)


tree = Tree()
tree.addNode(1)
tree.addNode(2)
tree.addNode(3)
tree.addNode(4)
tree.addNode(5)
tree.addNode(6)
tree.addNode(7)
tree.travel()
print("-" * 30)
tree.forword(tree.root)
print("-" * 30)
tree.middle(tree.root)
print("-" * 30)
tree.backword(tree.root)



