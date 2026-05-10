class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class Ring:
    def __init__(self):
        self.head = None

    def __str__(self):
        ret_str = '['

        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

            if temp == self.head:
                break

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'

        return ret_str
    
    def _get_last(self):
        # if no node exist
        if self.head is None:
            return None

        # if one node exist
        if self.head.next == self.head:
            return self.head

        # at least two nodes
        temp = self.head.next
        while temp.next != self.head:
            temp = temp.next

        return temp


    ## Insert Operation ##
    def insert(self, index, val):
        new_node = Node(val)
        last = self._get_last()

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if last is None:
                self.head.next = self.head
            else:
                last.next = new_node

            return 

        if self.head is None and index > 0:
            raise IndexError("Cannot inset at" + str(index) + "because list is empty")

        # for other indices
        temp = self.head
        index_counter = 0
        while temp is not None and index_counter < index:
            prev = temp
            temp = temp.next
            index_counter += 1

        prev.next = new_node
        new_node.next = temp

        return 

    ## Remove operation  ##
    def remove(self, val):
        if self.head is None:
            raise Exception("Nothing to remove")

        temp = self.head
        last = self._get_last()
        # first node matches case
        if temp.val == val:
            if last == self.head:
                self.head = None
            else:
                self.head = temp.next
                last.next = self.head

            return

        prev = temp
        temp = temp.next
        while temp != last.next:
            if temp.val == val:
                break

            prev = temp 
            temp = temp.next

        if temp == last.next:
            return

        prev.next = temp.next

    ## Length operation ##
    def len(self):
        if self.head is None:
            return 0

        if self.head.next == self.head:
            return 1

        #for all other cases
        temp = self.head.next
        counter = 1
        while temp != self.head:
            counter += 1
            temp = temp.next

        return counter
    
    ## Push operation  ##
    def push(self, value):
        self.insert(self.len(), value)

    
    ## Pop Operation  ##
    def pop(self):
        if self.head is None:
            raise Exception("Nothing have to pop")

        if self.head.next == self.head:
            self.head = None
            return

        prev = self.head
        temp = self.head.next
        while temp.next != self.head:
            prev = temp 
            temp = temp.next

        prev.next = self.head


    ## Get operation  ##
    def get(self, index):
        if self.head == None:
            return 

        temp = self.head
        index_counter = 0
        while temp is not None and index_counter < index:
            temp = temp.next
            index_counter += 1
        
        return temp.val

if __name__ == "__main__":
    l = Ring()
    print("Push:")
    l.push(1)
    l.push(2)
    l.push(3)
    print(l) # Output: 1 -> 2 -> 3 -> (Head)

    print("-" * 17)

    print("Pop:")
    l.pop()
    print(l) # Output: 1 -> 2 -> (Head)

    print("-" * 17)

    print("Insert:")
    l.insert(0, 0)      # Insert at start
    l.insert(1, 1.5)    # Insert in middle
    print(l) # Output: 0 -> 1 -> 1.5 -> 2 -> (Head)

    print("-" * 17)

    print("Remove:")
    l.remove(1)
    print(l) # Output: 0 -> 1.5 -> 2 -> (Head)

    print("-" * 17)

    print("Length:")
    print(l.len()) # Output: 3

    print("-" * 17)

    print("Get:")
    print(l.get(1)) # Output: 1.5
    print(l.get(0)) # Output: 0