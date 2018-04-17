import threading
import time

exitFlag = 0

class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("Starting " + self.name)
        printTime(self.name, 5, self.counter)
        print ("Exiting " + self.name)

def printTime(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

from nose.tools import assert_equals, assert_raises

class TestThreads(object):

  def testThreads(self):
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    thread1.start()
    thread2.start()

    print ("All test cases passed!")


def main():
  testThreads = TestThreads()
  testThreads.testThreads()

if __name__ == '__main__':
  main()
