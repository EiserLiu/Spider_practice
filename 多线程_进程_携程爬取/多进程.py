import time
from multiprocessing import Process


def run1():
    print("我是run函数")
    # 阻塞
    time.sleep(50)


def run2():
    print("我是run函数")
    # 阻塞
    time.sleep(50)


if __name__ == '__main__':
    t1 = time.time()
    p1 = Process(target=run1)
    p2 = Process(target=run2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("我是下面代码")
    print(time.time() - t1)
