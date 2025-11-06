class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear  = None

    def isEmpty(self):
        return self.front == None
    
    #method to add an ite to the queue
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        
        self.next = temp 
        self.rear = temp

    #method to remove an item from queue
    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if(self.front == None):
            self.rear = None

#driver code

if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()

    print("Queue Front is: " + str(q.front.data if q.front != None else -1))
    print("Queue rear is: " + str(q.rear.data if q.rear != None else -1))