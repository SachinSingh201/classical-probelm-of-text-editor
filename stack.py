class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

        
        
class Stack:
    def __init__(self):
        self.top = None
        self.n= 0


    def isEmpty(self):
         return self.top== None
    
    def push(self,value):
        new_node = Node(value)
        
        new_node.next = self.top
        self.top = new_node
        self.n+=1 

    def pop(self):
        # print("the popped element is ", self.top.data)
         popped_data = self.top.data
         self.top = self.top.next
         return popped_data

    def size(self):
        if (self.isEmpty()):
            return print('Stack Empty and Size is 0')
        return print('the Size of stack is',self.n)    


    def peek(self):
        if (self.isEmpty()):
            return print("Stack Empty")
            
        return print ("the peek value is ",self.top.data)
    
    def reverse_string(self,text):
        for i in text:
            self.push(i)

        res = ''
        while(not self.isEmpty()):
            res =   res+ self.pop()
        print(res)

    def __str__(self):
        if (self.isEmpty())  :
            return print('Stack is Empty')
        
        current = self.top
        result = ''
        while current != None:
            result = result + str(current.data)+','

            current = current.next   
        return result  



    def traverse (self):
        if self.top == None :
            return print("Stack is Empty ")
            
        print("your current stack is")
        curr = self.top
        while curr != None:
            print(curr.data)
            curr = curr.next


def text_editor(text,pattern):
    u = Stack()
    r = Stack()
    for i in text :
        u.push(i)

    for i in pattern :
        if i == 'u':
            data = u.pop()
            r.push(data)
        else :
            data = r.pop()
            u.push(data)

    res = ''
    while(not u.isEmpty()):
        res = u.pop() + res        
    print (res)    




s= Stack()
'''s.isEmpty()
s.push(1)
s.push(2)
s.push(3)
s.traverse()

s.peek()
s.size()
s.pop()
s.pop()
s.pop()

s.peek()
s.reverse_string('Hello')

s.traverse()'''
text_editor('kolkata', 'uurruru')
