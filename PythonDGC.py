class GarbageCollector:
    #Constructor to initialise a GC object with an empty heap with specified size
    def __init__(self, heap_size):
        self.heap = [None] * heap_size
        self.moved_roots = set() #Initialising the moved_roots set
        self.mapping_table = {} #Initialising the mapping_table dictionary

    #Function to simulate allocation of an object on the heap
    def allocate_object(self, value):
        #Simulating object allocation on the heap
        for i in range(len(self.heap)):
            if self.heap[i] is None:
                self.heap[i] = value
                return i
        return -1  #Unable to allocate

    #Function to simulate the processing of a pointer
    def process_pointer(self, root_index):
        #Simulating processing of a pointer
        if 0 <= root_index < len(self.heap) and self.heap[root_index] is not None:
            #Simulating updating references or traversing the object graph
            return root_index
        return -1  #Invalid pointer

    #Function to simulate the GC process, it creates a new heap and iterates through the provided root indices
    def collect_garbage(self, roots):
        #Simulating garbage collection
        new_heap = [None] * len(self.heap)
        to_index = 0

        for root in roots:
            to_index = self.process_pointer(root)

        #Updating the moved roots
        self.moved_roots.update(range(to_index, len(self.heap)))

        #Swapping the old heap with the new heap
        self.heap, new_heap = new_heap, self.heap

    #Function to imulate printing the status of the GC. (Heap, moved roots, mapping table)
    def print_status(self, desc):
        #Simulating printing of the heap status
        print("--------------")
        print(desc.upper())
        print("Heap: ")
        print(self.heap)
        print("Moved Roots: ")
        print(list(self.moved_roots))
        print("Mapping Table: ")
        print(self.mapping_table)
        print("______________")

#Function to show an example of how to use this garbage collector
def example_usage():
    #Creating a GarbageCollector with a heap size of 20
    gc = GarbageCollector(20)

    #Printing the initial status
    gc.print_status("Initial")

    #Simulating allocation. (Adding objects to the heap)
    obj_a_index = gc.allocate_object("Object A")
    obj_b_index = gc.allocate_object("Object B")

    #Printing the status after allocation
    gc.print_status("After Allocation")

    #Simulating garbage collection with roots at indices of allocated objects
    gc.collect_garbage([obj_a_index, obj_b_index])

    #Printing the final status after garbage collection
    gc.print_status("After Garbage Collection")

#Running the example usage
example_usage()