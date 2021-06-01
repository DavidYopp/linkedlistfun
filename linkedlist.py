class Node:
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.nextnode = None

class LinkedList:
    def __init__ (self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextnode

    def insertbeginning(self, data):
        newnode = Node(data)

        newnode.nextnode = self.headval
        self.headval = newnode

    def insertatend(self, data):
        newnode = Node(data)
        if self.headval is None:
            self.headval = newnode
            return
        last  = self.headval
        while(last.nextnode):
            last = last.nextnode
        last.nextnode = newnode


linkedlist = LinkedList()
linkedlist.headval = Node("Mon")
node2 = Node("Tue")
node3 = Node("Wed")

linkedlist.headval.nextnode = node2
node2.nextnode = node3


linkedlist.insertbeginning("Sun")
linkedlist.insertatend("Thurs")

linkedlist.printlist()
