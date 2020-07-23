class Stack:
    def __init__(self, length = 5):
        self.st = []
        self.top = -1
        self.n = length

    def push(self, data):
        if self.top == self.n-1:
            print('Stack Overflow')
            return
        self.top+=1
        self.st.insert(0, data)
        print(f'{data} pushed')
    
    def pop(self):
        if self.top == -1:
            print('Stack Underflow')
            return
        print(f'{self.st[0]} popped')
        self.st.remove(self.st[0])
        self.top-=1

    def display(self):
        if self.top == -1:
            print("Stack Empty!!")
        else:
            i = 0
            print('Stack is as follows.')
            while i<=self.top:
                print(self.st[i])
                i+=1

s = Stack(2)
s.pop()
s.push(1)
s.push(2)
s.display()
s.push(3)
s.display()
s.pop()
s.pop()
s.pop()
s.display()
