class SimpleList:
    def __init__(self):
        self.head=None
        self.size=0

    def add(self,position,value):
        node=SimpleNodeList(value)
        if not node:
            return -1
        if not self.head:
            self.head=node
        else:
            if position==0:
                nodePrev=self.head
                self.head=node
                node.next=nodePrev
            else:
                nodePrev=self._getNode(self.head,0,position-1)
                if not nodePrev:
                    return -1
                nodeNext=nodePrev.next
                nodePrev.next=node
                node.next=nodeNext
        self.size+=1
        return 1

    def find(self,position):
        if not self.head:
            return -1
        return self._getNode(self.head,0,position)

    def _getNode(self,node,position,positionTarget):
        if not node.next or position==positionTarget:
            return node
        return self._getNode(node.next,position+1,positionTarget)

    def remove(self,position):
        if not self.head or position>self.size-1:
            return -1
        nodeSelected=self._getNode(self.head,0,position)
        if not nodeSelected:
            return -1
        if nodeSelected==self.head:
            self.head=nodeSelected.next
        else:
            nodePrev=self._getNode(self.head,0,position-1)
            nodePrev.next=nodeSelected.next
        self.size-=1
        return 1

    def toArrayValues(self):
        arr=[]
        if self.head:
            auxNode=self.head
            while auxNode.next:
                arr.append(auxNode.value)
                auxNode=auxNode.next
            arr.append(auxNode.value)
        return arr

    def all(self):
        print(self.toArrayValues(),self.size)

class SimpleNodeList:
    def __init__(self,value):
        self.next=None
        self.value=value

class DoubleList:
    def __init__(self):
        self.head=None
        self.size=0

    def add(self,position,value):
        node=DoubleNodeList(value)
        if not node:
            return -1
        if not self.head:
            self.head=node
        else:
            if position==0:
                nodePrev=self.head
                self.head=node
                node.next=nodePrev
                node.next.ant=self.head
            else:
                nodeAct=self._getNode(self.head,0,position)
                if not nodeAct:
                    return -1
                nodeAct.ant.next=node
                nodeAct.ant=node
                node.ant=nodeAct.ant
                node.next=nodeAct
        self.size+=1
        return 1

    def find(self,position):
        if not self.head:
            return -1
        return self._getNode(self.head,0,position)

    def _getNode(self,node,position,positionTarget):
        if not node.next or position==positionTarget:
            return node
        return self._getNode(node.next,position+1,positionTarget)

    def remove(self,position):
        if not self.head or position>self.size-1:
            return -1
        nodeSelected=self._getNode(self.head,0,position)
        if not nodeSelected:
            return -1
        if nodeSelected==self.head:
            self.head=nodeSelected.next
        else:
            nodeSelected.ant.next=nodeSelected.next
            if nodeSelected.next:
                nodeSelected.next.ant=nodeSelected.ant
        self.size-=1
        return 1

    def toArrayValues(self):
        arr=[]
        if self.head:
            auxNode=self.head
            while auxNode.next:
                arr.append(auxNode.value)
                auxNode=auxNode.next
            arr.append(auxNode.value)
        return arr

    def all(self):
        print(self.toArrayValues(),self.size)

class DoubleNodeList:
    def __init__(self,value):
        self.next=None
        self.ant=None
        self.value=value
