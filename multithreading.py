import time
import threading as th

def print_nums(start, end, delay):
    for i in range(start, end):
        time.sleep(delay)
        print(i)


def print_lets(delay):
    for lets in "abcdefghijklmnopqrstuvwxyz":
        time.sleep(delay)
        print(lets)


t1 = th.Thread(target = print_nums, args = (1, 11, 0.5))
# t2 = th.Thread(target = print_lets, args = (0.25,))
t2 = th.Thread(target = print_nums, args = (11, 21, 0.5))
t1.start()
t2.start()

# Wait for threads to complete before exiting
t1.join()
t2.join()
