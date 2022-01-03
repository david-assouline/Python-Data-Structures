class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
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
            
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node       
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
            
    
    def pop(self):
        if self.length == 0:
            return("Cannot pop, the list is empty")
        temp_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp_node.prev = None
        print("Popping {} from list".format(temp_node.value))
        self.length -= 1
        return(temp_node.value)
    
    def pop_first(self):
        if self.length == 0:
            return("Cannot pop, the list is empty")
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None  
        else:
            self.head = self.head.next
            self.head.prev = None
            print("Popping {} from list".format(temp.value))
        self.length -= 1
        return(temp.value)
        
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return("Invalid Index")
        else:
            counter = 0
            if index < self.length/2:
                temp = self.head
                while counter != index:
                    temp = temp.next
                    counter += 1
            else:
                counter = self.length - 1
                temp = self.tail
                while counter != index:
                    temp = temp.prev
                    counter -= 1
            return(temp)
        
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return("Invalid Index")
        else:
            temp_node = self.get_node(index)
            temp_node.value = value 
            
    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            prev_node = self.get_node(index - 1)
            new_node.next = self.get_node(index)
            new_node.prev = prev_node
            prev_node.next = new_node
        self.length += 1
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return("Cannot remove from empty list")
        elif index == 0:
            return self.pop_first()     
        elif index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        self.length -= 1
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
