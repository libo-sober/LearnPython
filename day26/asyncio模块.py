import asyncio

async def func(name):
    print(f'start{name}')
    # await 可能会发生阻塞的方法
    # await 关键字必须写在一个async函数里 , py3.8的不需要
    await asyncio.sleep(1)
    print('end')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([func('alex'), func('taibai')]))  # 异步

# 原理


