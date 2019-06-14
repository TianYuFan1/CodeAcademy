from Node import Node


class Queue:

    def __init__(self, max_size = None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.get_size() < self.max_size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        return "The queue is empty"

    def enqueue(self, value):
        if self.has_space():
            new_node = Node(value)
            print("Adding " + str(new_node.get_value() + " to the queue"))
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
                self.size += 1
            else:
                self.tail.set_next_node(new_node)
                self.tail = new_node
                self.size += 1
        else:
            print("The queue is full")

    def dequeue(self):
        if not self.is_empty():
            remove_node = self.head
            print("Removing " + str(remove_node.get_value() + " from the queue"))
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = remove_node.get_next_node()
            self.size += -1
            return remove_node.get_value()
        else:
            print("The queue is empty")


print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #