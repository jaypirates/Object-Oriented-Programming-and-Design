class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    def add_values(self, data):
        self.data = data
        self.next = None
        self.prev = None