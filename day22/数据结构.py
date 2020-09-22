"""
要掌握思想
栈和队列
"""
# 栈：先进后出的数据结构，栈顶和栈尾。
# 用列表实现：我们定义列表开始的位置为栈底，末尾为栈顶。
# Stack() 创建一个空栈。它不需要参数，并返回一个空栈。
# push()
class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        """从栈返回顶部项，但不会删除它。不需要参数，不修改栈。"""
        return len(self.items) - 1
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('栈顶元素下标',stack.peek())
print(stack.isEmpty())
print(f'元素个数{stack.size()}')

# 队列：先进先出。队头和队尾。
# 我们定义列表开始位置为队头，末尾为队尾。
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

# 烫手的山芋
# 6个孩子围一圈，第一个孩子手里有个烫手的山芋，需要再自己手里放一秒后传给下一个孩子，
# 再计时器没计时7秒时，山芋再谁手里谁就推出，最后一个孩子获胜。
# 准则：手里有山芋的孩子永远排在队列的头部
kids = ['A', 'B', 'C', 'D', 'E', 'F']
queue = Queue()
for kid in kids:
    queue.enqueue(kid)  # A时队头F时队尾
while queue.size() > 1:
    for i in range(6):  # 每循环一次，山芋传递一次，手里有山芋的孩子永远再队头位置
        temp = queue.dequeue()
        queue.enqueue(temp)
    queue.dequeue()
print(f'获胜的选手：{queue.dequeue()}')

# 双端队列：队列的头和尾都可插入数据或去除数据。提供栈和队列共有的属性。
class Deque():
    def __init__(self):
        self.items = []
    def addFront(self, item):
        self.items.insert(0, item)
    def addRear(self, item):
        self.items.append(item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

dq = Deque()
dq.addFront(1)
dq.addFront(2)
dq.addFront(3)

# print(dq.removeFront())
# print(dq.removeFront())
# print(dq.removeFront())
print(dq.removeRear())
print(dq.removeRear())
print(dq.removeRear())

# 案例：回文检查
# 回文字符串左右读都一样：abssba
def is_huiwen(s):
    ex = True
    q = Deque()
    for ch in s:
        q.addFront(ch)
    while q.size() > 1:
        if q.removeFront() != q.removeRear():
            ex = False
            break
    return ex


print(is_huiwen('abiaba'))

"""
内存
计算机的作用：用来存储和运算二进制的数据
计算机如何计算1+2？
    将1和2的二进制类型的数据加载到计算机内存中，然后使用寄存器进行数值的预算
变量的概念：
    变量就是某一块内存
    内存空间是由两个默认属性：内存空间的大小（bit位，一个bit只能放一个二进制数，1字节是8bit），内存空间的地址。
    kb:1024byte.
    
顺序表：
    集合中存储的元素是有序的，顺序表可以分为两种形式：单数据类型和多数据类型。
    python中的列表和元组就是多数据类型的顺序表。
链表：相对于顺序表。
"""
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
class Link():
    def __init__(self):
        # 构造出一个空链表
        # _head存的只能是空或者第一个节点的地址
        self._head = None
    # 向链表的头部插入一个节点
    def add(self, item):
        # 创建一个新节点
        node = Node(item)
        node.next = self._head  # 先让新节点指向头节点指向的节点
        self._head = node  # 然后让头节点指向新的节点
    # 链表的遍历
    def travel(self):
        # _head在列表创建好后一定是不可变的
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
    def isEmpty(self):
        return self._head == None
    def size(self):
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self._head == None:
            """链表为空的话，需要单独处理，直接添加到头部"""
            self._head = node
            return
        cur = self._head
        while cur.next:
            cur = cur.next
        cur.next = node
    # def append(self, item):
    #     """链表尾部添加元素二"""
    #     node = Node(item)
    #     cur = self._head
    #     pre = Node
    #     while cur:
    #         pre = cur
    #         cur = cur.next
    #     pre.next = node
    # def insert(self, pos, item):
    #     """指定位置添加元素"""
    #     cur = self._head
    #     pre = Node
    #     node = Node(item)
    #     for i in range(pos):
    #         pre = cur
    #         cur = cur.next
    #     pre.next = node
    #     node.next = cur
    def insert(self, pos, item):
        """指定位置添加元素,下标从0开始"""
        cur = self._head
        node = Node(item)
        for i in range(pos - 1):
            cur = cur.next
        node.next = cur.next
        cur.next = node
    def remove(self, item):
        """删除指定节点"""
        cur = self._head
        pre = None
        if cur.item == item:
            # 删除的是第一个节点
            self._head = cur.next
            return
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """查找节点"""
        find = False
        cur = self._head
        while cur:
            if cur.item == item:
                find = True
                return find
            cur = cur.next
        return find

    def reverse(self):
        cur = self._head
        pre = None
        next_node = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = next_node
            if cur:
                next_node = cur.next
        self._head = pre



print('-' * 30)
link = Link()
link.add(3)
link.add(4)
link.travel()
print('-' * 30)
# print(link.isEmpty())
# print(link.size())
link.append(7)
link.travel()
print(link.search(7))
print(link.search(1))
print('-' * 30)
link.insert(2, 9)
link.travel()
print('-' * 30)
link.remove(9)
link.travel()
print('*' * 50)
# 如何使用两个队列实现一个栈
alist = [1,2,3,4,5]
q1 = Queue()
for i in alist:
    q1.enqueue(i)
q2 = Queue()
# 将q1中的n-1个值去除放出q2中
while q1.size() > 0:
    while q1.size() > 1:
        q2.enqueue(q1.dequeue())
    print(q1.dequeue())
    q1, q2 = q2, q1
# 如何实现将单链表倒置
print('*' * 50)
link1 = Link()
link1.append(2)
link1.append(3)
link1.append(4)
link1.append(5)
link1.append(6)
link1.travel()
link1.reverse()
link1.travel()
