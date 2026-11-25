class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = (
                    self.heap[parent], self.heap[index]
                )
                index = parent
            else:
                break

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return minimum

    def heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest], self.heap[index]
                )
                index = smallest
            else:
                break

    def is_empty(self):
        return len(self.heap) == 0


def merge_k_sorted_arrays(arrays):
    heap = MinHeap()

    # Insert the first element of each array
    for i in range(len(arrays)):
        if len(arrays[i]) > 0:
            heap.insert((arrays[i][0], i, 0))

    result = []

    while not heap.is_empty():

        value, array_index, element_index = heap.extract_min() # type: ignore

        result.append(value)

        next_index = element_index + 1

        # Insert the next element from the same array
        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            heap.insert((next_value, array_index, next_index))

    return result

arrays = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print("Input arrays:", arrays)

result = merge_k_sorted_arrays(arrays)

print("Merged array:", result)

arrays2 = [
    [1, 5],
    [2, 3, 8, 10],
    [],
    [4, 7]
]

print("Different lengths:", merge_k_sorted_arrays(arrays2))