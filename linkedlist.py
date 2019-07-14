class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def append_end(self,data):
        if self.tail==None:
            self.tail=Node(data)
            self.head=self.tail
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
    def append_beg(self,data):
        if self.tail==None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=Node(data)
            temp.next=self.head
            self.head=temp
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

    def del_beg(self):
        temp=Node(None)
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.data

    def del_end(self):
        temp=Node(None)
        temp1=Node(None)
        temp=self.head
        while temp.next is not None:
            temp1=temp
            temp=temp.next
        self.tail=temp1
        temp1.next=None
        return temp.data

list1=LinkedList()
while(1):
    ch=int(input("enter 1.append_end 2.display 3.del beg 4.del end 5.append_beg 6.exit "))
    if ch==1:
        data=int(input("enter element"))
        list1.append_end(data)
    elif ch==2:
        list1.display()
    elif ch==3:
        print(list1.del_beg())
    elif ch==4:
        print(list1.del_end())
    elif ch==5:
        data=int(input("Enter element"))
        list1.append_beg(data)
    else:
        break
