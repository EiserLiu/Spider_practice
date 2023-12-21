import threading
import time


def run(i):
    print('开启线程', i, threading.current_thread().name)
    time.sleep(2)


thr1 = threading.Thread(target=run, args=(1,), name='lucky-1')
thr2 = threading.Thread(target=run, args=(2,), name='lucky-2')

thr1.start()
thr2.start()

thr1.join()
thr2.join()

print('开启线程', threading.current_thread().name)
print('over')
