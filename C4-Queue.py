# python program to implement queue using array

# declaring the array of maximum capacity
ar = [0 for _ in range(10)]
n = 10

#declaring the front and rear and initializing with -1
front = -1
rear = -1

#function to operate enqueue operation
def enqueue(item):
    #checking the overflow conditions
    global n
    global rear
    global front

    if rear == n-1:
        print("Overflow! ", end=" ")
        print("\n", end='')
        return
    
    else:
        # front and rear both at -1 then set front and rear
        #at 0 otherwise increment rear
        if front == -1 and rear == -1:
            front = 0
            rear = 0

        else:
            rear += 1  
         #inserting element at rear 
        ar[rear] = item
        print("Element inserted")

#function to implement dequeue operation
def dequeue():
    global n
    global rear 
    global front

    #checking underflow condition
    if front == -1 or front > rear:
        print("Underflow! ", end=' ')
        return
    
    else:
        item = ar[front]
        #Displaying deleted element 
        print("Element deleted from queue is: ", end='')
        print(item, end='')
        print('\n', end='')

        #if front and rear reach at end then initialize at -1
        if rear == front:
            rear = -1
            front = -1

        else:
            front = front +1 
        
        #incrementing the front
        front +=1

#function to display all elements of queue
def display():
    global n
    global rear
    global front
    #checking whether queue is empty or not
    if front == -1:
        #if queue is empty simply return
        print("Queue is empty")
        return
    
    else:
        #if queue is not empty print all the elements from rear to front
        print("Elements are: ")
        i = front
        while i <= rear:
            print(ar[i], end='')
            i += 1
        print('\n', end='')

#function to displa front eement of queue 
def fronte():
    global n
    global front
    global rear
        #checking  if queue is empty or not 
    if front == -1:
        #if queue is empty simply return
          print("Queue is empty. ")
          return
    else: 
            print("Front element is: ")
            print(ar[front])
            print('\n')


ch = None
#displaying options of enqueue, dequeue and front to the user

print("1: Inserting element to queue(enqueue)")
print("\n", end = '')
print("2: Deleting element from queue(dequeue)")
print("\n", end = '')
print("3: Display front element from queue")
print("\n", end = '')
print("4: Display all the elements of queue")
print("\n", end = '')
print("5: Exit")
print("\n", end = '')

condition = True
while condition:
    ch = int(input("Enter your choice: "))

    if ch == 1:
        item = int(input("Elnter element to be inserted: "))
        enqueue(item)
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        fronte()
    elif ch == 5:
        print("Exit", end = '')
        print("\n", end = '')
    else:
        print("Invalid choice", end = '')
        print("\n", end = '')
    condition = ch!=5 