import heapq
from dataclasses import dataclass, field
from typing import AnyStr


@dataclass(order=True)
class BucketItem:
    item: AnyStr = field(compare=False)
    priority: int = 1


class BucketList:
    def __init__(self, initial_elems=[]):
        self.queue = []
        self.tasks = {}

        for elem in initial_elems:
            self.add(elem)

    def add(self, task: str, priority: int = 1):
        if task in self.tasks.keys():
            self.remove(task)

        entry = BucketItem(task, priority)
        heapq.heappush(self.queue, entry)
        self.tasks[task] = entry
        heapq.heapify(self.queue)

    def remove(self, task: str):
        self.tasks.pop(task)

    def get(self):
        """Get the current highest priority task"""
        return self.queue[0].item

    def finish(self, task: str):
        """Finish a task?  Great job!  Remove it from the queue"""
        self.remove(task)
        print(f"You've finished {task}, great job!")

    def prioritize(self, task):
        """Have an itch to do something?  Move it
        to the top of thr queue"""
        pass  # self.add(task)

    @property
    def n_items(self):
        return len(self.queue)

    def print(self):
        print(self.queue)
