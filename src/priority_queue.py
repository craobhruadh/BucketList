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

    def add(self, task: str, prioritize: bool = False) -> None:
        """Add a task.  Prioritize"""

        # Handle case where task is already in bucket list
        if task in self.tasks.keys():
            if prioritize and self.queue[0].item != task:
                for entry in self.queue:
                    if entry.item == task:
                        entry.priority = self.queue[0].priority - 1
                        heapq.heapify(self.queue)
                        break
            return

        if prioritize:
            if not self.queue:
                entry = BucketItem(item=task)
            else:
                entry = BucketItem(item=task, priority=self.queue[0].priority - 1)

        else:
            entry = BucketItem(item=task, priority=len(self.queue) + 1)
        heapq.heappush(self.queue, entry)
        self.tasks[task] = entry
        heapq.heapify(self.queue)

    def remove(self, task: str) -> None:
        if task in self.tasks.keys():
            for i in range(len(self.queue)):
                if self.queue[i].item == task:
                    self.queue[i], self.queue[-1] = self.queue[-1], self.queue[i]
                    self.queue = self.queue[:-1]
                    heapq.heapify(self.queue)
                    self.tasks.pop(task)
                    return

    def get(self) -> str:
        """Get the current highest priority task"""
        return self.queue[0].item

    def finish(self, task: str):
        """Finish a task?  Great job!  Remove it from the queue"""
        self.remove(task)
        print(f"You've finished {task}, great job!")

    def prioritize(self, task):
        """Have an itch to do something?  Move it
        to the top of the queue"""
        if task in self.tasks.keys() and self.queue[0].item != task:
            for entry in self.queue:
                if entry.item == task:
                    entry.priority = self.queue[0].priority - 1
                    heapq.heapify(self.queue)
                    return

        entry = BucketItem(item=task, priority=self.queue[0].priority - 1)
        heapq.heappush(self.queue, entry)

    @property
    def current_task(self) -> str:
        return self.get()

    @property
    def size(self) -> int:
        return len(self.queue)

    def print(self, verbose=False):
        if verbose:
            print(self.queue)
        else:
            print([x.item for x in self.queue])
