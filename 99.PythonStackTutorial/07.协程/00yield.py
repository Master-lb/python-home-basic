#__author:jack
#date 2020-02-09 13:55


import time
import queue

def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))
        #time.sleep(1)
 
if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")

    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n +=1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" %n )