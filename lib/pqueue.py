import heapq
import itertools

REMOVED = '__removed__'

# Based on https://docs.python.org/3/library/heapq.html
class PQueue:
    def __init__(self) -> None:
        self.pq = []
        self.finder = {}
        self.counter = itertools.count()
    
    def empty(self) -> bool:
        return len(self.pq) == 0

    def contains(self, task) -> bool:
        return task in self.finder

    def add(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.finder:
            self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
