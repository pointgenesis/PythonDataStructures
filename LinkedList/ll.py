class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0


    def insertStart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:

            print("NOT not self.head <<< EXECUTED" + str(self.head.data))
            newNode.nextNode = self.head
            self.head = newNode


    def size(self):
        return self.size


    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode


    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode


linkedlist = LinkedList()
linkedlist.insertStart(5)
linkedlist.insertStart(15)
linkedlist.insertStart(25)
linkedlist.insertStart(35)

linkedlist.traverseList()