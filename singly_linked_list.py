class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

class linkid_list():
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head

        new_node.next = current_head
        self.head = new_node
        
        return self
    


    def  add_to_back(self, val):
        if self.head == None :
            self.add_to_front(val)
            return self


        new_node = Node(val)
        runner = self.head

        while(runner.next != None):
            runner = runner.next
        runner.next = new_node

        return self






    def print_list(self):
        while(self.head != None):
            print(self.head.value)
            self.head = self.head.next    
        return self






my_list = linkid_list()
my_list.add_to_front("saadeh").add_to_front("mohannad").add_to_back("is my name") .print_list()