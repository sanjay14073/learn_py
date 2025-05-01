class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def addNode(self,data):
        newn=Node(data)
        if self.head==None:
            self.head=newn
            return
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newn  
    def printList(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

if __name__=="__main__":
    ll=LinkedList()
    ll.addNode(1)
    ll.addNode(2)
    ll.addNode(3)
    ll.printList()
