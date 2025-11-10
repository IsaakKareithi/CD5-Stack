#program to implement stack using 2 queues

from collections import deque

class Stack:

    def __init__(self):

        #two inbuilt queues
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

            #push x first in empty q2
            self.q2.append(x)

            #push all the remaining elements in q1 into q2 
            while(self.q1):
                self.q2.append(self.q1.popleft())

                #swap the names of the two queues
                self.q1, self.q2 = self.q2, self.q1

    def pop(self):

            #if no elements are in q1
            if self.q1:
                return self.q1.popleft()
            return None

    def top(self):
            if (self.q1):
                return self.q1[0]
            return None
        
    def size(self):

            return len(self.q1)
        
#Driver code
if __name__ == '__main__':
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print("Current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())

    print("Current size: ", s.size())

    