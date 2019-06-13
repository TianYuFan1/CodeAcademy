from Node import Node


class Stack:

    def __init__(self, name, limit=1000):
        self.name = name
        self.top_node = None
        self.limit = limit
        self.size = 0

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def push(self, value):
        if self.has_space():
            node = Node(value)
            node.set_next_node(self.top_node)
            self.top_node = node
            self.size += 1
        else:
            print("The stack is full")

    def pop(self):
        if not self.is_empty():
            return_node = self.top_node
            self.top_node = return_node.get_next_node()
            self.size += -1
            return return_node.get_value()
        else:
            print("The stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top_node.get_value()
        else:
            print("The stack is empty")

    def print_nodes(self):
        current = self.top_node
        print_list = []
        while current:
            print_list.append(current.get_value())
            current = current.get_next_node()
        print_list.reverse()
        print("{NAME} Stack: {STACK}".format(NAME=self.get_name(), STACK=print_list))
