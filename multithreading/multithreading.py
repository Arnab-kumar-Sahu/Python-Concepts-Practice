import threading
import time
def gf(n):
    for i in range(n):
        print("i love u")
        time.sleep(2)
def exgf(n):
    for i in range(n):
        print("i still love u")
        time.sleep(2)
start = time.time()
anks=threading.Thread(target=gf,args=(5,),name='kala')
ada=threading.Thread(target=exgf,args=(5,),name='bala')
anks.start()
ada.start()
print(threading.active_count())
print(threading.enumerate())
anks.join()
ada.join()
print(threading.active_count())
print(threading.enumerate())
end = time.time()
print(end - start)
