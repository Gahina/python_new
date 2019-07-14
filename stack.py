class Stack:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return self.item==[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop()
    def display(self):
        print(self.item)
    def sum(self):
        s=0
        for i in self.item:
            s+=i
        return s

s=Stack()
while(1):
    ch=int(input("Enter your choice"
      "1.push"
      "2.pop"
      "3.display"
      "4.sum"
      "5.exit"))

    if ch==1:
        data=int(input("enter data"))
        s.push(data)
        #break
    elif ch==2:
        if(s.is_empty()):
            print("empty stack")
        else:
            val=s.pop()
            print("popped element:",val)
        #break
    elif ch==3:
        s.display()
        #break
    elif ch==4:
        print("sum of stack is",s.sum())
    else:
        break

