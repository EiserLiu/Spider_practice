from concurrent.futures import ThreadPoolExecutor,as_completed
import time


def run(i):
    print("开启线程", i)
    time.sleep(2)
    print("结束线程", i)
    return i


pool = ThreadPoolExecutor(5)

# for i in range(5):
#     pool.submit(run, i)

# tasks = [pool.submit(run,i) for i in range(5)]
#
# for val in as_completed(tasks):
#     print(val.result())

for val in pool.map(run,list(range(5))):
    print(val)