from LinkedList.node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, data):
        """
        Given the object, data
        Then increment the linked list size by one
        And create a new node using the object, data

        When the head is not currently assigned (self.head == None)
        Then assign the newly created node to the head node
        When the head does have a valid object reference
        Then link the newly created node as the head (new_node = self.head)

        Performance: O(1)

        :param data: the object that the node will hold
        """
        self.size = self.size + 1
        new_node = Node(data)

        if self.head is not None:
            # link the new node to the current head
            new_node.next_node = self.head

        # assign the head position to the new node
        self.head = new_node


    def insert_at_tail(self, data):
        """
        Given the object, data
        Then increment the linked list size by one
        And create a new node using the object, data
        And set the current node reference to the head node

        Given that the current node is not None
        Then assign the current node to the current node's next node
        When current_node is None
        Then assign the current node to the new node (effectively inserting at the list's tail)

        :param data: the data value to insert into the linked list
        """
        self.size = self.size + 1
        new_node = Node(data)
        current_node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def remove(self, data):
        if self.head is None:
            return

        self.size = self.size - 1

        current_node = self.head
        previous_node = None

        while current_node != data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node = current_node.next_node


    def length(self):
        print("current list size %d" % self.size)
        return self.size


    def traverse(self):
        current_node = self.head

        while current_node is not None:
            print("current_node.data: %d" % current_node.data)
            current_node = current_node.next_node


list = LinkedList()
list.insert_at_head(100)
list.insert_at_head(2)
list.insert_at_head(-55)
list.insert_at_head(3454)

list.length()
list.traverse()

print("="*25)

list.insert_at_tail(43)
list.insert_at_tail(99)

list.length()

list.traverse()