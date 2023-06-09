import heapq
from dataclasses import dataclass, field
from typing import AnyStr


@dataclass(order=True)
class BucketItem:
    item: AnyStr = field(compare=False)
    priority: int = 1


class BucketList:
    """Implements a bucket list through a priority queue, with some
    additions - namely it adds reprioritizing and removing items,
    which are a bit more expensive operations"""

    def __init__(self, initial_elems=[]):
        self.queue = []
        self.tasks = set()
        for elem in initial_elems:
            self.add(elem)

    def add(self, task: str, prioritize: bool = False) -> None:
        """Add a task.  Optionally prioritize it, otherwise we add it to
        the end of the queue"""

        if not self.queue:
            self.queue.append(BucketItem(item=task))
            self.tasks.add(task)
            return

        if self.queue[0].item == task:
            return

        if prioritize:
            priority = self.queue[0].priority - 1
        else:
            priority = len(self.queue) + 1

        # Handle case where task is already in bucket list
        if task in self.tasks:
            if prioritize:
                for entry in self.queue:
                    if entry.item == task:
                        entry.priority = priority
                        heapq.heapify(self.queue)
                        break
            return

        entry = BucketItem(item=task, priority=priority)
        heapq.heappush(self.queue, entry)
        self.tasks.add(task)
        heapq.heapify(self.queue)

    def remove(self, task: str) -> bool:
        """Finish a task?  Great job!  Remove it from the queue.
        Returns true if successful, and False if task is not in current bucket list"""
        if task in self.tasks:
            for i in range(len(self.queue)):
                if self.queue[i].item == task:
                    self.queue[i], self.queue[-1] = self.queue[-1], self.queue[i]
                    self.queue = self.queue[:-1]
                    heapq.heapify(self.queue)
                    self.tasks.remove(task)
                    return True
        return False

    def get(self) -> str:
        """Get the current highest priority task"""
        return self.queue[0].item

    def prioritize(self, task: str) -> None:
        """Have an itch to do something?  Move it
        to the top of the queue"""
        if task in self.tasks and self.queue[0].item != task:
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
            for i, elem in enumerate(self.queue):
                if i == 0:
                    print(f"*** {elem.item}: {elem.priority}")
                else:
                    print(f"{elem.item}: {elem.priority}")
        else:
            print([x.item for x in self.queue])

    def to_file(self, filename):
        """Saves the current object as a .csv file.  Designed to be read
        by the accompanying static method, `from_file`"""
        with open(filename, "w") as f:
            for entry in self.queue:
                f.write(f"{entry.item}, {entry.priority}\n")

    @staticmethod
    def from_file(filename):
        """Takes a file, presumably from `to_file`, and returns
        a new priority queue loaded with this bucket list"""
        with open(filename, "r") as f:
            lines = [x.strip() for x in f.readlines()]

        new_bucket_list = BucketList()
        for line in lines:
            tokens = line.split(",")
            priority = int(tokens[-1])
            item = ",".join(tokens[:-1])
            entry = BucketItem(item=item, priority=priority)
            new_bucket_list.queue.append(entry)
            new_bucket_list.tasks.add(item)
        heapq.heapify(new_bucket_list.queue)
        return new_bucket_list
