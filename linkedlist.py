class Node():
    """Node Structure"""
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    """Linked List"""
    def __init__(self) -> None:
        self.head = None

    def addnode(self,node)-> None:
        """Insert Nodes in Linke List"""
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = node

    def display(self) -> None:
        """Display Linked List Elements"""
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next

    def addbegin(self,data):
        """Add node at beginning"""
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp


    def addnext(self,data,value):
        """Add node after particular Node"""
        temp = self.head
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.data!= value):
                temp = temp.next
            temp2 = temp.next
            temp.next = Node(data)
            temp.next.next = temp2
            

    def addend(self,data):
        """Add Node at the end"""
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next!= None):
                temp = temp.next
            temp.next = Node(data)


LL = LinkedList()
LL.addnode(Node(10))
LL.addnode(Node(100))
LL.addnode(Node(1000))
LL.addnode(Node(10000))

LL.addbegin(20)

LL.display()
print("______________________________________________--")
LL.addnext(999,1000)
LL.display()