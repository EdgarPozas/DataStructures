class BinaryTree:
    def __init__(self):
        self.root=None

    def add(self,value):
        node=NodeBinaryTree(value)
        if not node:
            return -1
        if not self.root:
            self.root=node
        else:
            self._add(None,self.root,node)
        return 1

    def _add(self,nodeAnt,node,newNode):
        if not node:
            if newNode.value>nodeAnt.value:
                nodeAnt.right=newNode
                return 1
            else:
                nodeAnt.left=newNode
                return 1
        if newNode.value>node.value:
            return self._add(node,node.right,newNode)
        else:
            return self._add(node,node.left,newNode)

    def remove(self,value):
        if not self.root:
            return -1
        return self._remove(None,self.root,value)

    def _remove(self,nodeAnt,node,value):
        if not node:
            return -1
        if node.value==value:
            if node==self.root:
                self.root=None
            else:
                if value>nodeAnt.value:
                    nodeAnt.right=None
                else:
                    nodeAnt.left=None
            return 1
        if value>node.value:
            return self._remove(node,node.right,value)
        else:
            return self._remove(node,node.left,value)

    def toArrayPreOrder(self):
        return list(map(lambda y:int(y),filter(lambda x:x!="",self._toArrayPreOrder(self.root,"").split(','))))

    def _toArrayPreOrder(self,node,cad):
        if not node:
            return ""
        return str(node.value)+","+self._toArrayPreOrder(node.left,cad)+","+self._toArrayPreOrder(node.right,cad)

    def toArrayInOrder(self):
        return list(map(lambda y:int(y),filter(lambda x:x!="",self._toArrayInOrder(self.root,"").split(','))))

    def _toArrayInOrder(self,node,cad):
        if not node:
            return ""
        return self._toArrayInOrder(node.left,cad)+","+str(node.value)+","+self._toArrayInOrder(node.right,cad)


    def toArrayPosOrder(self):
        return list(map(lambda y:int(y),filter(lambda x:x!="",self._toArrayPosOrder(self.root,"").split(','))))

    def _toArrayPosOrder(self,node,cad):
        if not node:
            return ""
        return self._toArrayPosOrder(node.left,cad)+","+self._toArrayPosOrder(node.right,cad)+","+str(node.value)

    def createFromArrayPre(self,arr):
        for x in arr:
            self.add(x)

    def createFromArrayPos(self,arr):
        for x in arr[::-1]:
            self.add(x)

class NodeBinaryTree:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
