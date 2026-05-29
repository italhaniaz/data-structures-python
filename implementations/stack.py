class stack:
    def __init__(self):
        self.l = []
    
    def push(self, value):
        self.l.append(value)
    
    def pop(self):
        return self.l.pop()

    def peek(self):
        return self.l[-1]


if __name__ == "__main__":
        
    s = stack()

    # Push elements
    s.push(10)
    s.push(20)
    s.push(30)

    # Peek top element
    print("Top element is:", s.peek())

    # Pop element
    popped_value = s.pop()
    print("Popped element is:", popped_value)
