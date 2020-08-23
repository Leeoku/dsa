class Node:
    #Create a node and add a pointer to the next value
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        
        self.head = None
    
    def insert_at_beginning(self, data):
    #Inititate the beginning of the linked list and call it head
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self,data):
    #If the node has no head, then set it as the head
        if self.head is None:
            self.head = Node(data, None)
            return
        
        #Set the iteration to the head and keep iterating till you reach the end, value of Null
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data,None)

    def insert_values(self, data_list):
        #Delete all the values so we can start with new one
        self.head = None
        #iterate over the list and add it to the end of the linked list
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        iterator = self.head
        while iterator:
            count+=1
            iterator = iterator.next
        return count

    def remove_at_index(self, index):
        #check to see if it is an index
        if index<0 or index>=self.get_length():
            raise Exception("Not valid index")
        #point the head to next element
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iterator = self.head
        #stop at the index prior to target index and connect it to the index after(eg, index = 3. Stop at 2 and point to 4)
        while iterator:
            if count == index - 1:
                iterator.next = iterator.next.next
            iterator = iterator.next
            count += 1

    def insert_at_index(self, index, data):
        #check to see if it is an index
        if index<0 or index>=self.get_length():
            raise Exception("Not valid index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        iterator = self.head
        while iterator:
            if count == index - 1:
                node = Node(data, iterator.next)
                iterator.next = node
                break
            iterator = iterator.next
            count +=1
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        iterator = self.head
        linked_list_string = ''
        while iterator:
            linked_list_string += str(iterator.data) + '--->'
            iterator = iterator.next
        print(linked_list_string)

if __name__ == '__main__':
    linked_list = LinkedList()
    # linked_list.insert_at_beginning(3)
    # linked_list.insert_at_beginning(45)
    # linked_list.insert_at_end(100)
    linked_list.insert_values(["apple", "orange", "grapes","pear"])
    linked_list.print()
    # linked_list.remove_at_index(2)
    linked_list.insert_at_index(1, "melon")
    linked_list.print()