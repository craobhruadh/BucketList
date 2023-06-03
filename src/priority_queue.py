import heapq
from dataclasses import dataclass, field
from typing import AnyStr


@dataclass(order=True)
class BucketItem:
    priority: int
    item: AnyStr = field(compare=False)


class BucketList:

    def __init__(self, initial_elems=[]):
        self.queue = []
        self.tasks = {}

        for elem in initial_elems:
            self.add(elem)
        # self.min_priority = 0
        # self.max_priority = 0

    def add(self, task: str, priority: int = 1):
        # self.max_priority += 1
        if task in self.tasks.keys():
            self.remove(task)

        entry = (priority, task)
        heapq.heappush(
            self.queue,
            entry
        )
        self.tasks[task] = entry
        heapq.heapify(self.queue)

    def remove(self, task: str):
        self.tasks.pop(task)

    def get(self):
        """Get the current highest priority task"""
        return self.queue[0][1]

    def finish(self, task: str):
        """Finish a task?  Great job!  Remove it from the queue"""
        self.remove(task)
        print(f"You've finished {task}, great job!")

    def prioritize(self, task):
        """Have an itch to do something?  Move it
        to the top of thr queue"""
        pass#self.add(task)

    @property
    def n_items(self):
        return len(self.queue)

    def print(self):
        print(self.queue)