"""
二分查找：一定是基于有序集合来进行的。
1   2   3   4   5   6   7

    key ? middle
    >        key在middle右边
    <        key在middle左边


冒泡排序

选择排序

插入排序

希尔排序

快速排序

"""
# 折半查找
alsit = [0, 1,2,3,4,5,6,7,8,9]


def find(key):
    low = 1
    high = len(alsit)
    mid = (low + high) // 2
    if key > alsit[mid]:
        low = mid + 1
    elif key < alsit[mid]:
        low = mid - 1
    else:
        return mid


print(find(5))
# # 冒泡排序
alist = [3,8,5,7,6]

def bubbl_sort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


print(bubbl_sort(alist))
# 选择排序
alist = [3,8,5,7,6]

# 将乱序中的最大值找出放在尾部交换位置
def select_sort(alist):
    for j in range(len(alist)-1):
        max_index = 0
        for i in range(1, len(alist)-j):
            if alist[max_index] < alist[i]:
                max_index = i
        alist[len(alist)-1-j], alist[max_index] = alist[max_index], alist[len(alist)-j-1]
    return alist


print(select_sort(alist))

# 插入排序
# 把右边的元素往左插，保证左侧一直有序
alist = [3,8,5,7,6]
# def insert_sort(alist):
#     for i in range(1, len(alist)):
#         temp = alist[i]
#         for j in range(i-1,-1,-1):
#             """如果左边有序列表的尾部元素比待插入的大，则往右移，再比较尾部左侧"""
#             if alist[j] > temp:
#                 alist[j+1] = alist[j]
#             else:
#                 alist[j+1] = temp
#                 break
#     return alist
def insert_sort(alist):
    for i in range(1, len(alist)):
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break
    return alist

print(insert_sort(alist))
# 希尔排序
# gap:
#   增量的值
#   拆分的组数
# 对每一组进行直接插入排序
alist = [3,8,5,7,6]
def shell_sort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap, len(alist)):
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2
    return alist
print(shell_sort(alist))
# 快速排序
#   1.指定一个基数（乱序中的第一个数据值）
#   2.将比基数小的数放置在基数的左侧，比基数大的数放在基数的右侧
#   3.从又开始偏移high
alist = [49,38,65,97,76,13,27,49]

def quikly_sort(alist, low, high):
    if low < high:
        i = low
        j = high
        key = alist[i]
        while i < j:
            while i < j and alist[j] >= key:
                j -= 1
            if i < j:
                alist[i] = alist[j]
                i += 1
            while i < j and alist[i] < key:
                i += 1
            if i < j:
                alist[j] = alist[i]
                j -= 1
        alist[i] = key
        # 基数已经有了正确的顺序位置，我们只需把基数左边的和右边的序列再递归找正确的位置
        quikly_sort(alist, low, i-1)
        quikly_sort(alist, i+1, high)


quikly_sort(alist, 0, len(alist) - 1)
print(alist)


