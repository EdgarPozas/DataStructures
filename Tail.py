class SimpleTail:
    def __init__(self,size):
        self.size=size
        self.head=0
        self.tail=0
        self.items=[0 for x in range(self.size)]

    def add(self,value):
        if self.tail>=self.size:
            return -1
        self.items[self.tail]=value
        self.tail+=1
        return value

    def remove(self):
        if self.head>=self.tail:
            return -1
        aux=self.items[self.head]
        self.items[self.head]=0
        self.head+=1
        return aux

    def all(self):
        print(self.items,"head: ",self.head,"tail: ",self.tail)


class CircularTail:
    def __init__(self,size):
        self.size=size
        self.head=0
        self.tail=0
        self.empty=True
        self.items=[0 for x in range(self.size)]

    def add(self,value):
        t_aux=self.tail+1

        if t_aux>self.size:
            t_aux=0

        if t_aux==self.head:
            return -1

        inc=True
        if self.tail>=self.size:
            self.tail=0
            inc=False
        self.items[self.tail]=value
        if inc:
            self.tail+=1
        self.empty=False

        return value

    def remove(self):
        if self.empty:
            return -1

        h_aux=self.head+1

        if h_aux>self.size:
            h_aux=0

        if h_aux==self.tail:
            self.empty=True

        inc=True
        if self.head>=self.size:
            self.head=0
            inc=False
        aux=self.items[self.head]
        self.items[self.head]=0
        if inc:
            self.head+=1

        return aux

    def all(self):
        print(self.items,"head: ",self.head,"tail: ",self.tail)
