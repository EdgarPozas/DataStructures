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


# from Tail import SimpleTail
#
# tail=SimpleTail(3)
# for value in range(1,4):
#     print("in ",tail.add(value))
#
# tail.all()
# print("out ",tail.remove())
# tail.all()
# print("in ",tail.add(3))
# tail.all()
# print("out ",tail.remove())
# print("out ",tail.remove())
# print("out ",tail.remove())
# print("out ",tail.remove())
# tail.all()
# print("in ",tail.add(4))
# print("out ",tail.remove())


from Tail import CircularTail

tail=CircularTail(3)
for value in range(1,5):
    print("in ",tail.add(value))

tail.all()
print("out ",tail.remove())
tail.all()
print("in ",tail.add(4))
tail.all()
print("in ",tail.add(5))
tail.all()
print("in ",tail.add(6))
tail.all()
print("in ",tail.add(7))
tail.all()
print("in ",tail.add(8))
tail.all()
print("in ",tail.add(9))
tail.all()
print("out ",tail.remove())
tail.all()
print("out ",tail.remove())
tail.all()
print("out ",tail.remove())
tail.all()
print("out ",tail.remove())
tail.all()
# print("out ",tail.remove())
# print("out ",tail.remove())
# print("out ",tail.remove())
print("in ",tail.add(4))
tail.all()
# print("out ",tail.remove())
