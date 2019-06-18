
class MinHeap:

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def add(self, element):
        print("Adding {ELEMENT} to {LIST}".format(ELEMENT=element, LIST=self.heap_list))
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        print("Restoring the heap property...")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:
                print("Swapping {PARENT} with {CHILD}".format(PARENT=parent, CHILD=child))
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        print("Heap Restored {LIST}".format(LIST=self.heap_list))

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying Down!")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[smaller_child_idx] = parent
                self.heap_list[idx] = child
            idx = smaller_child_idx
        print("Heap Restored!")

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left = self.heap_list[self.left_child_idx(idx)]
            right = self.heap_list[self.right_child_idx(idx)]
            if left < right:
                print("The left child is smaller")
                return self.left_child_idx(idx)
            else:
                print("The right child is smaller")
                return self.right_child_idx(idx)

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        minimum = self.heap_list[1]
        print("Removing {MIN} from {LIST}".format(MIN=minimum, LIST=self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.count += -1
        self.heap_list.pop()
        print("Last element moved to first: {LIST}".format(LIST=self.heap_list))
        self.heapify_down()
        return minimum



# import heap class

# make an instance of MinHeap
min_heap = MinHeap()

# set internal list for testing purposes...
min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

while len(min_heap.heap_list) != 1:
  print(min_heap.heap_list)
  min_heap.retrieve_min()
