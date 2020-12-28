class Stack:
    def __init__(self,size):
        self.size=size
        self.top=0
        self.items=[0 for x in range(self.size)]

    def add(self,value):
        if self.top>=self.size:
            return -1
        self.items[self.top]=value
        self.top+=1
        return value

    def remove(self):
        if self.top==0:
            return -1
        aux=self.items[self.top-1]
        self.items[self.top-1]=0
        self.top-=1
        return aux

    def all(self):
        print(self.items,"top: ",self.top)
