class Queue:
    def __init__(self,n):
        self.item=[]
        self.len=n
    def is_empty(self):
        return self.item==[]
    def is_len(self):
        return len(self.item)==self.len
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        return self.item.pop(0)
    def display(self):
        print(self.item)

n=int(input("enter length of queue"))
q=Queue(n)
while(1):
    ch=int(input("enter choice 1.enqueue 2.dequeue 3.display 4. exit"))
    if ch==1:
        if q.is_len():
            print("overflow")
        else:
            data=int(input("enter data"))
            q.enqueue(data)
    elif ch==2:
        if q.is_empty():
            print("empty queue")
        else:
            print("dequeued data",q.dequeue())
    elif ch==3:
        q.display()
    else:
        break

