# test multithread
import threading
import time
import multiprocessing

no = 100000000


def addition(a, b):
    result = a
    for i in range(a + 1, b + 1):
        result += i
    print(result)

def sqrt(x):
    return x * x

xs = range(no)



# t1 = threading.Thread(target=addition(1,no))
# t2 = threading.Thread(target=addition(1,no))
# t1.start()
# t2.start()
# print(time.time() - t)
# t = time.time()
if __name__ == '__main__' :
    t = time.time()
    coreNo = multiprocessing.cpu_count()
    print(coreNo)
    pool = multiprocessing.Pool(processes=coreNo)

    array = pool.map(sqrt, xs)
    print(len(array))

    print(time.time() - t)

# t = time.time()
# for i in xs:
#     aa = sqrt(i)
# print(time.time() - t)