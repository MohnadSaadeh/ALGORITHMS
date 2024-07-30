class SLNode:
    def __init__(self, value):
        self.val = value
        self.next  = None

class SLList:
    def __init__(self):
        self.head = None
    
    def addToFront(self, val):
        # create a node to hold the value
        new_node = SLNode(val)

        new_node.next = self.head
        self.head = new_node
        
x = "hello"
my_list =  SLList()

my_list.addToFront("yana")
my_list.addToFront("mohannad")
my_list.addToFront("aman")
my_list.addToFront("nawar")



print(my_list.head.val)
print(SLList.new_node.val)