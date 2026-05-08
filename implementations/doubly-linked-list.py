class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        ret_str = '['
        temp = self.head

        while temp is not None:
            # print (id(temp.prev), id(temp), id(temp.next))
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'

        return ret_str

    ## Push operation
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        #other wise do that
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    
    # Pop operation
    def pop(self):
        if self.head is None:
            raise Exception("Cannot have any thing to pop")

        if self.head.next is None:
            ret_val = self.head.val
            self.head = None
            return ret_val

        #other cases
        last = self.head 
        while last.next is not None:
            prev = last
            last = last.next

        ret_val = last.val
        prev.next = None

        return ret_val


    # Insert Operation
    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return 

        # for other cases
        temp = self.head
        index_coutner = 0
        while temp is not None and index_coutner < index:
            prev = temp
            temp = temp.next
            index_coutner += 1

        prev.next = new_node
        new_node.prev = prev

        new_node.next = temp
        if temp is not None:
            temp.prev = new_node

        return 
    
    # Remove operation
    def remove(self, val):

        if self.head is None:
            raise Exception("Cannot have any value to remove")

        if self.head.val == val:
            ret_val = self.head.val
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            return ret_val

        temp = self.head
        while temp is not None:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            return

        ret_val = temp.val
        prev.next = temp.next
        if prev.next is not None:
            temp.next.prev = prev

        return ret_val



if __name__ == "__main__":
        # Assuming your class is named DoublyLinkedList
    dll = Doubly()

    # Checking the push operation (Adding to the end)
    print("Push (Append):")
    dll.push(10)
    dll.push(20)
    dll.push(30)

    # Printing the list
    print(dll)

    print("-----------------")

    # Checking the pop operation (Removing from the end)
    print("Pop:")
    popped_val = dll.pop()
    print(f"Popped value: {popped_val}")

    # Printing the list
    print(dll)

    print("-----------------")

    # Checking the insertion operation
    # Doubly linked lists are great for this as they can traverse from both ends
    print("Insert:")
    dll.insert(0, 5)      # Insert 5 at index 0 (New Head)
    dll.insert(2, 25)     # Insert 25 at index 2

    # Printing the list
    print(dll)

    print("-----------------")

    # Checking the remove operation
    print("Remove:")
    # This usually removes the first occurrence of a specific value
    dll.remove(20) 

    # Printing the list
    print(dll)

    print("-----------------")

    # Unique to Doubly Linked Lists: Reverse Traversal
    # It's always good to verify the 'prev' pointers are working correctly
    if hasattr(dll, 'display_backward'):
        print("Reverse Traversal (Verifying 'prev' pointers):")
        dll.display_backward()