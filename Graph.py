class Graph:
    def __init__(self):
        self.nodes=[]

    def addNode(self,value):
        node=NodeGraph(value)
        if not node:
            return None
        exists=list(filter(lambda x:x.value==value,self.nodes))!=[]
        if exists:
            return None
        self.nodes.append(node)
        return node

    def findNode(self,value):
        nodes=list(filter(lambda x:x.value==value,self.nodes))
        if len(nodes)==0:
            return None
        return nodes[0]

    def addWeight(self,nodeSource,nodeDestiny,value):
        weight=WeightGraph(nodeSource,nodeDestiny,value)
        if not weight:
            return None
        nodeSource.weights.append(weight)
        return weight

    def removeNode(self,value):
        node=self.findNode(value)
        if not node:
            return -1
        self.nodes.remove(node)
        return 1

    def removeWeight(self,node,value):
        weight=list(filter(lambda x:x.value==value,node.weights))
        if len(weight)==0:
            return -1
        node.weights.remove(weight[0])
        return 1

    def listOfAdjacency(self):
        arr={}
        for node in self.nodes:
            arr[node.value]=list(map(lambda x:x.value,node.weights))
        return arr

    def matrixOfAdjacency(self):
        size=len(self.nodes)
        arr={node.value:{node_.value:0 for node_ in self.nodes} for node in self.nodes}
        for node in self.nodes:
            for weight in node.weights:
                arr[node.value][weight.destiny.value]= 1
        return arr

    def pathBetweenNodes(self,nodeSource,nodeDestiny):
        arr=[]
        return self._pathBetweenNodes(nodeSource,nodeDestiny,arr)

    def _pathBetweenNodes(self,nodeSource,nodeDestiny,arr):
        if nodeSource==nodeDestiny:
            return arr

        for weight in nodeSource.weights:
            if nodeSource==weight.destiny:
                continue
            arr.append(weight.source.value)
            return self._pathBetweenNodes(weight.destiny,nodeDestiny,arr)

class NodeGraph:
    def __init__(self,value):
        self.weights=[]
        self.value=value

class WeightGraph:
    def __init__(self,source,destiny,value):
        self.source=source
        self.destiny=destiny
        self.value=value
