import threading, time, random
from queue import Queue

class Monitor(object):
    ''' Monitor class for thread sychronization,
        protected with a threading.Lock() by default
    when you inherit from this class:
    . in you __init__, you should set up the monitor's _lock like this:
        - self._init_lock() #auto generated lock
      or with your lock:
        - self._init_lock(lock = you_lock)
    . you can simply init your 'Condition' object like this :
        self.cond = self.Condition()
    '''

    def __init__(self, lock = threading.Lock()):
        ''' initializes the _lock, threading.Lock() is used by default '''
        self._lock = lock
        

    def Condition(self):
        ''' returns a condition bound to this monitor's lock'''
        return threading.Condition(self._lock)

    init_lock = __init__

def run_as_thread(func):
    ''' returns the thread to the function ! so you can gather them out in a list or something :3'''
    def wrapper(*args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        return t
    return wrapper

class ProducerConsumerMonitor(Monitor):
    def __init__(self, bufferSize):
        self.init_lock()
        self.buffer = Queue(maxsize=bufferSize)
        self._bufferSize = bufferSize
        self._full = 0
        self._empty = bufferSize
        self._fullLock = threading.Lock()
        self._emptyLock = threading.Lock()
        self._fullCondition = threading.Condition(self._fullLock)
        self._emptyCondition = threading.Condition(self._emptyLock)

    def _up_full(self):
        with self._fullLock:
            if self._full == self._bufferSize:
                self._fullCondition.wait_for(lambda: self._full < self._bufferSize)

            self._full += 1
            self._fullCondition.notify_all()

    def _down_full(self):
        with self._fullLock:
            if self._full == 0:
                self._fullCondition.wait_for(lambda: self._full > 0)
            self._full -= 1

            self._fullCondition.notify_all()

    def _up_empty(self):
        with self._emptyLock:
            if self._empty == self._bufferSize:
                self._emptyCondition.wait_for(lambda: self._empty < self._bufferSize)
            self._empty += 1
            self._emptyCondition.notify_all()

    def _down_empty(self):
        with self._emptyLock:
            if self._empty == 0:
                self._emptyCondition.wait_for(lambda: self._full > 0)
            self._empty -= 1
            self._emptyCondition.notify_all()


    def put(self, product):
        self._down_empty()
        with self._lock:
            self.buffer.put(product)
        print(f"Produced: {product}\n")
        self._up_full()

    def get(self, id):
        self._down_full()
        with self._lock:
            product = self.buffer.get()

        print(f"Consumer_{id} consumed {product}\n")
        self._up_empty()


class Producer:
    def __init__(self, id):
        self.id = id
        self.productId = 0

    def produce(self, monitor):
        # Produce Item
        # Product ID : Producer Id : payload
        item = f'{self.productId}:Producer_{self.id}:{random.randint(1,10)}'
        self.productId += 1

        monitor.put(item)

    @run_as_thread
    def run(self, cnt, monitor):
        for i in range(cnt):
            time.sleep(0.2 + random.random())
            self.produce(monitor)


class Consumer:
    def __init__(self, id):
        self.id = id

    def consume(self, monitor):
        monitor.get(self.id)

    @run_as_thread
    def run(self, cnt, monitor):
        for i in range(cnt):
            time.sleep(0.2 + random.random())
            self.consume(monitor)


if __name__ == "__main__":
    producerCnt, consumerCnt, bufferSize = map(int, input("Enter producer, consumer count and buffer size: ").split())
    
    # Create Monitor
    monitor = ProducerConsumerMonitor(bufferSize)

    prod = []
    con = []
    prodThreads = []
    conThreads = []

    for i in range(producerCnt):
        prod.append(Producer(i))

    for i in range(consumerCnt):
        con.append(Consumer(i))


    for p in prod:
        prodThreads.append(p.run(consumerCnt, monitor))

    for c in con:
        conThreads.append(c.run(producerCnt, monitor))


    for prodThread in prodThreads:
        if prodThread.is_alive():
            prodThread.join()

    for conThread in conThreads:
        if conThread.is_alive():
            conThread.join()