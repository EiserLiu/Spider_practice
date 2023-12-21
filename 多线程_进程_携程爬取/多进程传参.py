import time
from multiprocessing import Process


def run1(num, name):
    for i in range(num):
        print(f"我是{name}函数")


if __name__ == '__main__':
    Process(target=run1, args=(1, 'lucky')).start()
