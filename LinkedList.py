class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node         
        self.length += 1   
        
    def pop(self):
        if self.length == 0:
            return("Cannot pop, the list is empty")
        else:
            temp = self.head
            prev = temp
            while temp.next != None:
                prev = temp
                temp = temp.next
            prev.next = None
            self.tail = prev
            self.length -= 1
            print("Popping {} from list".format(temp.value))
            return(temp.value)
            
    def pop_first(self):
        if self.length == 0:
            return("Cannot pop, the list is empty")
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return(temp.value)    
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            print("Popping {} from list".format(temp.value))
            return(temp.value)
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node
        if self.length == 0:
            self.tail = new_node
        self.length += 1
        
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return("Invalid Index")
        else:
            temp = self.head
            counter = 0
            while counter != index:
                temp = temp.next
                counter += 1
            return(temp)
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return("Invalid Index")
        else:
            temp_node = self.get_node(index)
            temp_node.value = value 
            
    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        else:
            prev = self.get_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.length += 1
        
    def remove(self, index):
        if self.length == 0:
            return("Cannot remove from empty list")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif index == 0:
            temp = self.head
            self.head = temp.next
            self.length -= 1      
        else:
            temp = self.get_node(index)
            prev = self.get_node(index - 1)
            prev.next = temp.next
            self.length -= 1
            
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before_temp = None
        after_temp = temp.next
        
        for _ in range(self.length):
            after_temp = temp.next
            temp.next = before_temp
            before_temp = temp
            temp = after_temp
                
    def print_list(self):
        if self.length <= 0:
            print("Cannot print an empty list")
        else:
            temp = self.head
            print("Printing list:", end = " ")
            while temp.next != None:
                print(temp.value, end = " ")
                temp = temp.next
            print(temp.value)
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None






            