#Implement Priority Queue using Binary Heap
# Class of Binary Heap
class MinHeap:
    def __init__(self):
        self.heap =[]

    def get_parent(self, i):
        return int((i-1)/2)
    def get_left_child(self, i):
        return 2*i+1
    def get_right_child(self, i):
        return 2*i+2

    def has_parent(self, i):
        return self.get_parent(i)>=0
    def has_left_child(self, i):
        return self.get_left_child(i) > len(self.heap)
    def has_right_child(self, i):
        return self.get_right_child(i) > len(self.heap)

    # Swap and continue heapifying
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Function to insert an element into the tree
    def insert_key(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap)-1)

    # Function to heapify the tree
    def heapify_up(self, i):
        size = len(self.heap)
        while(self.has_parent(i) and self.heap[i] < self.heap[self.get_parent(i)]):
            self.swap(i, self.get_parent(i))
            i = self.get_parent(i)
    def print_heap(self):
        print(self.heap)

    # Function to delete an element from the tree
    def delete_root(self):
        if len(self.heap)==0:
            return -1
        last_index = len(self.heap)-1
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root
    def heapify_down(self,i):
        while(self.has_left_child(i)):
            min_child_ind = self.get_min_child_index(i)
            if min_child_ind == -1:
                break
            if(self.heap[i] < self.heap[min_child_ind]):
                self.swap(i, min_child_ind)
                i = min_child_ind
            else:
                break

    def get_min_child_index(self, i):
        if(self.has_left_child(i)):
            left_c =self.get_left_child(i)
            if(self.has_right_child(i)):
                right_c =self.has_right_child(i)
                if(self.heap[left_c]<self.heap[right_c]):
                    return left_c
                else:
                    return right_c

        else:
            return 1

# Driver code
min_heap = MinHeap()

array = [9, 5, 11, 14, 18, 19, 21, 33, 17, 27]

for i in array:
    min_heap.insert_key(i)

print("Initial heap")
min_heap.print_heap()
print("Insert key 12")
min_heap.insert_key(12)
min_heap.print_heap()