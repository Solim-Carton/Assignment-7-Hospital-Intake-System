class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency
class MinHeap:
    def __init__(self):
        self.data = []
 
    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency >= self.data[parent].urgency:
                break
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            index = parent
 
    def heapify_down(self, index):
        n = len(self.data)
        while True:
            smallest = index
            for child in (2 * index + 1, 2 * index + 2):
                if child < n and self.data[child].urgency < self.data[smallest].urgency:
                    smallest = child
            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest
 
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)
 
    def peek(self):
        return self.data[0] if self.data else None
 
    def remove_min(self):
        if not self.data:
            return None
        top = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return top
 
    def print_heap(self):
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")
 
# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    assert heap.peek() is None and heap.remove_min() is None  # empty heap
 
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    assert heap.peek().name == "Taylor"
 
    assert heap.remove_min().name == "Taylor"
    heap.print_heap()
 
    for name, u in [("A", 9), ("B", 2), ("C", 7), ("D", 1), ("E", 4)]:
        heap.insert(Patient(name, u))
    order = [heap.remove_min().urgency for _ in range(len(heap.data))]
    assert order == sorted(order)
    print("All emergency_queue tests passed")
 



