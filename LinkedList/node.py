class Node(object):
    """
    Node object for a singly-linked list that contains only references to the next node. There is no back pointer.
    """
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return self.data
