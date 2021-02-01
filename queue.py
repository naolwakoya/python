tmax = 10
x = []
counter = 0

class Queue(object):
    def isEmpty():
        return len(x) == 0

    def enqueue(k):
        if len(x) < tmax:
            i.append(k)
            return True
        else:
            return False

    def dequeue():
        if x.isEmpty():
            return None
        else:
            x.pop(0)

    def peeK():
        if x.isEmpty():
            print ("Peek at Empty queue")
            return None
        else:
            return x[0]

    def getlist():
        return x

    def multienqueue(lst):
        for i in range(len(lst)):
            if len(x) < tmax:
                x.append(list[i])

    def multidequeue(s):
        y = []
        for j in range(len(s)):
            if len(y) > len(x):
                y.clear(s[j])


#while True:
#    print("Queueusing liked list ")
#    q = Queue()
'''
while True:
    q = Queue()
    x = input("Please enter a number you want to add, or enter 0 to remove: ")
    q.enqueue(x)
    print("Queue: " + str(n))
    print("current queue: " + str(q))


    if q.isEmpty():
        print("Queue is Empty")
        break
        print("Dequeue: " + str(q.dequeue()))
        print("Current queue" + str(q))
'''
while True:
    q = Queue()
    x = int(input("Please enter a number you want to add, or enter 0 to remove: "))
    if x:
        q.enqueue(x)
        print("Queue: " + str(n))
        print("current queue: " + str(q))

    else:
        if q.isEmpty():
            print("Queue is Empty")
            break
        print("Dequeue: " + str(q.dequeue()))
        print("Current queue" + str(q))
    
