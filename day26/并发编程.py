# 操作系统
# 人机矛盾：cpu100%工作
# I/O操作  输入输出  相对内存来讲的
# 多道操作系统：一个程序遇到IO就把cpu让给别人
#   顺序的一个个的执行的思路变成
#   共同存在在一台计算机中，其中以恶搞程序执行让出cpu之后，另一个程序能继续使用cpu
#   来提高cpu利用率
#   单纯的切换会占用时间，但是多道操作系统的原理整体上还是节省了时间，提高了cpu的利用率
#   时空复用的概念

"""
单cpu  分时操作系统：每一个程序轮流执行一个时间片，时间片轮转，提高了用户体验
    先来先服务为  FCFS
    时间片

实时操作系统

分布式操作系统：把一个大任务，分解成许多个小任务，分别给不同的操作系统去执行，最后汇总。
    任务可分解
    celery python分布式框架

进程：进行中的程序。
    占用资源 需要操作系统调用
    pid:能够唯一标识进程
    计算机中最小的资源分配单位
并发：
    多个程序同时进行：只有一个cpu,多个程序轮流在一个cpu上执行。
并行
    多个程序同时执行，并且同时在多个cpu上执行。
同步
    在做一件事的时候发起另一件事，必须等待上一次事件结束后才能执行
异步
    在做A事件时发起B事件，不需要等待A事件结束就可以开始B事件
阻塞
    cpu不工作
非阻塞
    cpu工作
同步阻塞：
    input sleep（cpu不工作）
异步阻塞

线程
    是进程中的一个单位，不能脱离进程存在
    线程是计算机中能够被cpu调度的最小单位

进程的三状态图：
    就绪 <-> 运行 -> 阻塞 -> 就绪 -> 运行
进程的调度算法
    给所有的进程分配资源或者分配cpu使用权的一种方法
    短作业优先
    先来先服务
    多级反馈算法
"""