class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index][0] > self.heap[parent][0]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent], self.heap[index]
                )
                index = parent
            else:
                break

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return maximum

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest], self.heap[index]
                )
                index = largest
            else:
                break

    def is_empty(self):
        return len(self.heap) == 0

scheduler = MaxHeap()

jobs = [
    (2, "Job A"),
    (5, "Job B"),
    (1, "Job C"),
    (4, "Job D"),
    (3, "Job E")
]

# Add jobs to the priority queue
for priority, job_name in jobs:
    scheduler.insert((priority, job_name))

print("Jobs added:", jobs)

print("\nReleasing jobs according to priority:")

release_order = []

while not scheduler.is_empty():

    priority, job_name = scheduler.extract_max() # type: ignore
    release_order.append(job_name)
    print("Released:", job_name, "| Priority:", priority)

print("\nFinal release order:", release_order)