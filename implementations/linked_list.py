class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LindedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        ret_str = '['
        temp = self.head

        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'

        return ret_str


    #XXXXXXXXXXXXXXXXXXXXXXXXXX
    #          Push           #
    def push(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return 

        last = self.head
        
        while last.next is not None:
            last = last.next
            
        last.next = new_node
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXX


    #XXXXXXXXXXXXXXXXXXXXXXXXXX
    #          Pop           #
    def pop(self):
        if self.head is None:
            raise Exception("Cannot pop. No value")

        #Case where there is only one node 
        if self.head.next is None:
            ret_val = self.head.val
            self.head = None
            return ret_val

        #Case where there is 2 or more nodes 
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next 

        ret_val = temp.val
        prev.next = None

        return ret_val
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXX

    
    #XXXXXXXXXXXXXXXXXXXXXXXXXX
    #        Insertion        #
    def insert(self, index, val):
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return 

        # for other indices
        temp = self.head
        counter = 0
        while temp is not None and counter < index:
            if counter == index:
                break

            prev = temp 
            temp = temp.next
            counter += 1

        prev.next = new_node
        new_node.next = temp
    #XXXXXXXXXXXXXXXXXXXXXXXXXXX


    #XXXXXXXXXXXXXXXXXXXXXXXXXX
    #          Remove         #
    def remove(self, val):
        temp = self.head

        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                return 

        while temp is not None:
            if temp.val == val:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            return 

        prev.next = temp.next
    #XXXXXXXXXXXXXXXXXXXXXXXXXX


    #XXXXXXXXXXXXXXXXXXXXXXXXXX
    #          Length         #
    def length(self):
        temp = self.head

        counter = 0
        while temp is not None:
            temp = temp.next
            counter += 1

        return counter
    #XXXXXXXXXXXXXXXXXXXXXXXXXXX


    #XXXXXXXXXXXXXXXXXXXXXXXXXX
    #           Get           #
    def get(self, index):
        temp = self.head 
        counter = 0

        while temp is not None and counter < index:
            if counter == index:
                break

            temp = temp.next
            counter += 1

        if temp is None:
            return 

        val = temp.val
        return val
    #XXXXXXXXXXXXXXXXXXXXXXXXXXX



if __name__ == '__main__':
    l = LindedList()

    # Checking the push operation
    print("Push:")
    l.push(1)
    l.push(2)
    l.push(3)

    #printing
    print(l)

    print("-----------------")

    # Checking the pop operation
    print("Pop:")

    l.pop()

    #printing
    print(l)


    print("-----------------")

    # Checking the insertion operation
    print("Insert:")
    l.insert(0, 0)
    l.insert(54, -7)

    #printing
    print(l)

    print("-----------------")

    # Checking the remove operation
    print("Remove:")

    l.remove(3)
    l.remove(5)

    #printing
    print(l)

    print("-----------------")


    # Checking len operation
    print("Length:")
    print(l.length())

    print("-----------------")

    # Checking get operation
    print("Get:")
    print(l.get(3))
    print(l.get(0))


