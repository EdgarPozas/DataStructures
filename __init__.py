# from Stack import Stack
#
# stack=Stack(3)
#
# for value in range(3):
#     print("in ",stack.add(value))
#
# stack.all()
# print("out ",stack.remove())
# stack.all()
# print("in ",stack.add(3))
# stack.all()
# print("out ",stack.remove())
# print("out ",stack.remove())
# print("out ",stack.remove())
# print("out ",stack.remove())
# stack.all()
# print("in ",stack.add(4))
# print("out ",stack.remove())
#
#
# from Queue import SimpleQueue
#
# queue=SimpleQueue(3)
# for value in range(1,4):
#     print("in ",queue.add(value))
#
# queue.all()
# print("out ",queue.remove())
# queue.all()
# print("in ",queue.add(3))
# queue.all()
# print("out ",queue.remove())
# print("out ",queue.remove())
# print("out ",queue.remove())
# print("out ",queue.remove())
# queue.all()
# print("in ",queue.add(4))
# print("out ",queue.remove())
#
#
# from Queue import CircularQueue
#
# queue=CircularQueue(3)
# for value in range(1,5):
#     print("in ",queue.add(value))
#
# queue.all()
# print("out ",queue.remove())
# queue.all()
# print("in ",queue.add(4))
# queue.all()
# print("in ",queue.add(5))
# queue.all()
# print("in ",queue.add(6))
# queue.all()
# print("in ",queue.add(7))
# queue.all()
# print("in ",queue.add(8))
# queue.all()
# print("in ",queue.add(9))
# queue.all()
# print("out ",queue.remove())
# queue.all()
# print("out ",queue.remove())
# queue.all()
# print("out ",queue.remove())
# queue.all()
# print("out ",queue.remove())
# queue.all()
# # print("out ",queue.remove())
# # print("out ",queue.remove())
# # print("out ",queue.remove())
# print("in ",queue.add(4))
# queue.all()
# print("out ",queue.remove())
#
# from List import SimpleList
#
# list=SimpleList()
# list.remove(0)
# for value in range(0,5):
#     print("in ",list.add(0,value))
#     print(list.toArrayValues())
#
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
#
#
# from List import DoubleList
#
# list=DoubleList()
# list.remove(0)
# for value in range(0,5):
#     print("in ",list.add(0,value))
#     print(list.toArrayValues())
#
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
# list.remove(1)
# print(list.toArrayValues())
#
#
# from Tree import BinaryTree
#
# btree=BinaryTree()
#
# base=[10,5,6,7,4,15,12,16,2]
# print("base->",base)
# for x in base:
#     print("in ",btree.add(x))
#
# print("preorder->",btree.toArrayPreOrder())
# print("inorder->",btree.toArrayInOrder())
# print("posorder->",btree.toArrayPosOrder())
#
# btree.remove(10)
# target=[10, 5, 4,2, 6,7, 15, 12, 16]
# btree.createFromArrayPre(target)
# print("---")
# print("preorder->",btree.toArrayPreOrder())
# print("inorder->",btree.toArrayInOrder())
# print("posorder->",btree.toArrayPosOrder())
# btree.remove(10)
# print("vacio->",btree.toArrayPreOrder())
#
# target=[2, 4, 7, 6, 5, 12, 16, 15, 10]
# btree.createFromArrayPos(target)
# print("---")
# print("preorder->",btree.toArrayPreOrder())
# print("inorder->",btree.toArrayInOrder())
# print("posorder->",btree.toArrayPosOrder())
# btree.remove(10)
# print("vacio->",btree.toArrayPosOrder())


from Graph import Graph

graph=Graph()

n1=graph.addNode(1)
n2=graph.addNode(2)
n3=graph.addNode(3)
n4=graph.addNode(4)
n5=graph.addNode(5)
n6=graph.addNode(6)

graph.addWeight(n1,n2,2)
graph.addWeight(n1,n3,3)

graph.addWeight(n2,n1,2)
graph.addWeight(n2,n4,5)
graph.addWeight(n2,n5,2)

graph.addWeight(n3,n1,3)
graph.addWeight(n3,n5,5)

graph.addWeight(n4,n2,5)
graph.addWeight(n4,n5,1)
graph.addWeight(n4,n6,2)

graph.addWeight(n5,n2,2)
graph.addWeight(n5,n3,5)
graph.addWeight(n5,n4,1)
graph.addWeight(n5,n6,4)

graph.addWeight(n6,n4,2)
graph.addWeight(n6,n5,4)


# print(graph.listOfAdjacency())
# graph.removeNode(2)
# print(graph.listOfAdjacency())
# graph.removeWeight(n1,3)
#
# print(graph.listOfAdjacency())
# print(graph.matrixOfAdjacency())
#
# print(graph.pathBetweenNodes(n1,n8))

print(graph.shortestPathBetweenNodes(n1,n6))
