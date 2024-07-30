class SLNode():
    def __init__(self, val):
        self.value = val
        self.next = None

class SList():
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)

        current_head = self.head       # save the current head > in a variable
        new_node.next = current_head   # linq the Node > SET the new node's next TO the list's current head

        self.head = new_node           # SET the list's head > TO the node we created in the last step

        return self


    def add_to_back(self, val):
        if self.head == None:          # if the list is Empty
            self.add_to_front(val)     # run the add_to_front Method
            return self

        new_node = SLNode(val)
        runner = self.head             # set an iterator to start at the front of the list
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node

        return self


    def print_values(self):
        print ("______________START_____________")

        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        print ("_______________END______________")
        return self	                # once the loop is done, return self to allow for chaining


Fst_list = SList()
Fst_list.add_to_front("Mohannad").add_to_front("Yana").add_to_back("Aman").add_to_back("Nawwar")
Fst_list.print_values()

# As a logic above > 
# print this :
# my name is Mohannad Saadeh

Sec_list = SList() 
Sec_list.add_to_front("Mohanad").add_to_front("is").add_to_front("My Name").add_to_front("Hi").add_to_back("Saadeh").print_values()






