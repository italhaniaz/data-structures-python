class Queue:
    def __init__(self):
        self.size = 5
        self.q = list(range(5))
        self.i = 0
        self.o = 0

        self.is_full = False
        self.is_empty = True

    def _inc(self, val):
        if val + 1 == self.size:
            return 0
        else:
            return val + 1
    
    def enqueue(self, val):
        if self.is_full:
            raise IndexError("Queue full. Cannot enquue")

        self.q[self.i] = val
        self.i = self._inc(self.i)

        if self.i == self.o:
            self.is_full = True

        self.is_empty = False

    def dequeue(self):
        if self.is_empty:
            raise IndexError("Queue empty. Cannot dequeue")

        ret = self.q[self.o]
        self.q[self.o] = 0
        self.o = self._inc(self.o)

        if self.i == self.o:
            self.is_empty = True

        self.is_full = False
        
        return ret
    
    def __str__(self):
        return str(self.q) + " , in: " + str(self.i) + " , out: " + str(self.o)

if __name__ == "__main__":
    q = Queue()
    
    print("-- Now Enqueueing --")

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q)

    print("-- Now Dequeueing --")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print (q)
