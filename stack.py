class Stack:
    def __init__(self) -> None:
        self.stack = list()


    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0 :
            print("Stack Empty")
            return

        popped = self.stack.pop()
        print("{} popped from stack".format(popped))


st = Stack()
st.push(10)  
st.push(100)
st.push(1000)
st.push(10000)  
st.pop() 