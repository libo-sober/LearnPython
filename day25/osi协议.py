# osi7/5层协议
# 应用层 表示层 会话层(三层合并成应用层)  python  5 6  7层
# 传输层  port    4层  四层路由器/交换机
# 网络层  ip      3层  路由器 三层交换机
# 数据链路层  mac  2层  网卡 二层交换机
# 物理层  二进制串  1层
#
# tcp 和 udp  传输层
# tcp （语音聊天/视频聊天）- 线下缓存/qq远程控制
#     需要先建立链接 然后才能通信
#     占用连接/可靠（消息不会丢失）/实时性高/慢
#     建立连接 - 三次握手
#     全双共通信
#        server         SYN    < -    client
#        server  - >    ACK SYN       client
#        server      ACK       < -    client
#     断开连接 - 四次挥手
#        server         FIN    < -    client
#        server  - >    ACK           client
#        server   - >   FIN           client
#        server      ACK       < -    client
#     因为对方可能还有一些数据没传完，要双方都确定断开才断开
# udp （发消息）-在线播放视频
#     不需要建立链接
#     不占用连接/不可靠（消息因为网络不稳定而丢失）/快
#
#
#
