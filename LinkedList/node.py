class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return self.data
