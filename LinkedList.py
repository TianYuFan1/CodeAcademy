from Node import Node


class LinkedList:

    def __init__(self, value = None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        current_node = self.head_node
        string = ""
        while current_node:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string

    def remove_node(self, value):
        current_node = self.head_node
        if current_node.get_value() == value:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                if current_node.get_next_node().get_value() == value:
                    current_node.set_next_node(current_node.get_next_node().get_next_node())
                    current_node = None
