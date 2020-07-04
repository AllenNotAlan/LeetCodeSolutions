"""

Leet Code 707

Design your implementation of the linked list. 
You can choose to use the singly linked list or the doubly linked list. 
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. 
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.

This question asked for these implementation:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtBeginning(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtEnd(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid

"""


#create a class called node (the data to be inserted)
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

#create the linked list class
class SLinkedList:
    def __init__(self):
        self.headval = None
        self.size = 0

    def getSize(self):
        
        currentVal = self.headval
        while currentVal is not None:
            self.size += 1
            currentVal = currentVal.nextval
        return self.size


    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AddAtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

        self.size += 1

    def AddAtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while last.nextval is not None:
            last = last.nextval
        last.nextval = NewNode

        self.size += 1
    
    def AddMiddle(self, middleVal, newdata):
        
        if middleVal is None:
            print("middle value not in list")
            return
        
        NewNode = Node(newdata) # create a new node for the 'newdata variable'
        NewNode.nextval = middleVal.nextval #node next to the new node is the value next to the chosen node index
        middleVal.nextval = NewNode #new middle value (relative to initial linked list) is now the new node

        self.size += 1

    def RemoveNode(self, key):

        newhead = self.headval

        # this handles if the first node is the key we need:
        if newhead is not None:
            if newhead.dataval == key:
                self.headval = newhead.nextval # self.headval == 'wed'
                newhead = None
                return

        # this handles if the key is in a middle node or last node.
        while newhead is not None:
            if newhead.dataval == key:
                break
            prev = newhead
            newhead = newhead.nextval
        
        # this is what happens if the key is not in the list
        if newhead == None:
            return

        prev.nextval = newhead.nextval
        newhead = None

    def get(self, index):

        if index < 0 or index >= self.size:
            return -1
        
        if index is None:
            return -1

        currentVal = self.headval
        for i in range(index):
            currentVal = currentVal.nextval
        return currentVal.dataval

        #my solution was to create a dictionary with keys. This works but adds complexity. Which means linked list will be slower
    
    def addAtIndex(self, index, val):

        if index < 0 or index > self.size:
            return -1

        if index is None:
            return -1

        NewNode = Node(val)

        newhead = self.headval
        if index == 0:
            NewNode.nextval = newhead
            self.headval = NewNode
        else:
            for i in range(index):
                newhead = newhead.nextval

            NewNode.nextval = newhead.nextval
            newhead.nextval = NewNode

        
    def deleteAtIndex(self, index):
        
        if index < 0 or index >= self.size:
            return -1

        if index is None:
            return -1

        newhead = self.headval
        if index == 0:
            self.headval = newhead.nextval
        else:
            #Gets the nextval for the new value at index
            for i in range(index):
                newhead = newhead.nextval
                if newhead.nextval is not None:
                    valNextToIndex = newhead.nextval
                else:
                    valNextToIndex = None
                
            #gets the new value at the index
            newhead = self.headval
            for i in range(index-1):
                newhead = newhead.nextval
            
            newhead.nextval = valNextToIndex
        
        

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link first node to second node
list1.headval.nextval = e2

#Link second Node to third node
e2.nextval = e3

# list1.AddAtBeginning("Sun")
# list1.AddAtEnd("Thur")
list1.AddMiddle(e2, "Fri")
# list1.RemoveNode("Mon")
# list1.listprint()

print(list1.get(0))
print()
# list1.listprint()
# print()
print(list1.getSize())

# print(list1.get(0))
# list1.addAtIndex(3, "Day")

# list1.deleteAtIndex(4)

list1.listprint()