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
        new_node = SLNode(val)
        runner = self.head             # set an iterator to start at the front of the list
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node

        return self







    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self	                # once the loop is done, return self to allow for chaining


New_list = SList()

New_list.add_to_front("mohannad").add_to_front("aman").add_to_back("nawwar")

New_list.print_values()

