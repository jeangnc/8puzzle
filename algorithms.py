from heapq import heappop, heappush

class UniformCost:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def add(self, state, position, path):
        node = (state, position, path)
        self.counter += 1
        heappush(self.queue, (len(path), self.counter, node))

    def next(self):
        if self.available() == 0:
            raise ValueError("There is no nodes available")

        _,_, node = heappop(self.queue)
        return node

    def available(self):
        return len(self.queue)

class SimpleHeuristic:
    def __init__(self):
        self.queue = []

    def add(self, state, position, path):
        self.queue.append()

    def next(self):
        return self.queue.pop(0)

    def available(self):
        return len(self.queue)

class MyHeuristic:
    def __init__(self):
        self.queue = []

    def add(self, state, position, path):
        self.queue.append(node)

    def next(self):
        return self.queue.pop(0)

    def available(self):
        return len(self.queue)
