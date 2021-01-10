import os, threading, random, time
from queue import Queue


# ALl Shared variables and counting and binary semaphore
class SharedVariables:
    def __init__(self, bufferSize):
        self.buffer = Queue(maxsize=bufferSize)
        self._full = threading.BoundedSemaphore(bufferSize)
        self._empty = threading.Semaphore(bufferSize)
        self._binSemaphore = threading.Lock()

        for i in range(bufferSize):
            self.full.acquire()

    def down_empty(self):
        self._empty.acquire()

    def up_empty(self):
        self._empty.release()

    def down_full(self):
        self._full.acquire()

    def up_full(self):
        overFlow = False

        try:
            self._full.release()
        except ValueError:
            overFlow = True

        return overFlow

    def acquire_buffer(self):
        self._binSemaphore.acquire()

    def release_buffer(self):
        self._binSemaphore.release()


class Producer:
    def __init__(self, id):
        self.id = id
        self.productId = 0

    def produce(self, variables):
        # Produce Item
        # Product ID : Producer Id : payload
        item = f'{self.productId}:Producer_{self.id}:{random.randint(1,10)}'
        self.productId += 1
        time.sleep(random.random())

        variables.down_empty()
        variables.acquire_buffer()

        variables.buffer.put(item)

        variables.release_buffer()
        variables.up_full()

        print(f"Item Produced: {item}")

class Consumer:
    def __init__(self, id):
        self.id = id

    def consume(self, variables):
        time.sleep(random.random() + 0.2)

        variables.down_full()
        variables.acquire_buffer()

        item = variables.buffer.get()

        variables.release_buffer()
        variables.up_empty()


        print(f"Consumer_{self.id} consumed {item}")


def handle_producer(id, variables, num_product):
    prod_i = Producer(id)

    for i in range(num_product):
        prod_i.produce(variables)


def handle_consumer(id, variables, num_product):
    con_i = Consumer(id)

    for i in range(num_product):
        con_i.consume(variables)

if __name__ == '__main__':
    producerCnt, consumerCnt, bufferSize = map(int, input("Enter producer, consumer count and buffer size: ").split())
    variables = SharedVariables(bufferSize)

    prodThreads = []
    conThreads = []


    for i in range(producerCnt):
        prodThreads.append(threading.Thread(target=handle_producer, args=(i, variables, consumerCnt)))

    for i in range(consumerCnt):
        conThreads.append(threading.Thread(target=handle_consumer, args=(i, variables, producerCnt)))


    for prodThread in prodThreads:
        prodThread.start()

    for conThread in conThreads:
        conThread.start()

    for prodThread in prodThreads:
        prodThread.join()

    for conThread in conThreads:
        conThread.join()
    
    




