class PriorityQueue:
    def __init__(self):
        self.Queue = []
        
    def __len__(self):
         return len(self.Queue)
    
    def push(self, task, priority):
        self.Queue.append((task, priority))
        self.Queue.sort(key=lambda x: x[1])

    def __iter__(self):
        self.position = 0
        return self
    
    def __next__(self):
        if self.position < len(self.Queue):
            queue = self.Queue[self.position]
            self.position += 1
            return queue
        else:
            raise StopIteration

"""
priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Tasks in Priority Order:")
for task in priority_queue:
    print(task)

print("Processing tasks in Priority Order:")
while len(priority_queue) > 0:
    task = priority_queue.pop()
    print("Processing:", task)
"""