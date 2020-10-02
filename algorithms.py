from heapq import heappop, heappush
import constants

class UniformCost:
    def __init__(self):
        self.__queue = []
        self.__counter = 0

    def add(self, state, position, path):
        node = (state, position, path)
        cost = len(path)

        self.__counter += 1

        heappush(self.__queue, (cost, self.__counter, node))

    def next(self):
        _,_, node = heappop(self.__queue)
        return node

    def available(self):
        return len(self.__queue)

class SimpleHeuristic:
    def __init__(self):
        self.__queue = []

    def add(self, state, position, path):
        node = (state, position, path)
        cost = len(path) + self.__wrong_values_count(state)
        heappush(self.__queue, (cost, node))

    def next(self):
        _, node = heappop(self.__queue)
        return node

    def available(self):
        return len(self.__queue)

    def __wrong_values_count(self, state):
        wrong_count = 0

        for y, row in enumerate(state):
            for x, cell in enumerate(row):
                if cell != constants.EMPTY_VALUE and cell != constants.FINAL_STATE[y][x]:
                    wrong_count += 1

        return wrong_count

class SophisticatedHeuristic:
    def __init__(self):
        self.__queue = []
        self.__right_positions = self.__calculate_right_positions()

    def add(self, state, position, path):
        node = (state, position, path)
        cost = len(path) + self.__wrong_values_count(state) + self.__wrong_values_distance_sum(state)
        heappush(self.__queue, (cost, node))

    def next(self):
        _, node = heappop(self.__queue)
        return node

    def available(self):
        return len(self.__queue)

    def __calculate_right_positions(self):
        positions = {}

        for y, row in enumerate(constants.FINAL_STATE):
            for x, cell in enumerate(row):
                positions[cell] = (y,x)

        return positions

    def __wrong_values_count(self, state):
        wrong_count = 0

        for y, row in enumerate(state):
            for x, cell in enumerate(row):
                if cell != constants.EMPTY_VALUE and cell != constants.FINAL_STATE[y][x]:
                    wrong_count += 1

        return wrong_count

    def __wrong_values_distance_sum(self, state):
        distances_sum = 0

        for y, row in enumerate(state):
            for x, cell in enumerate(row):
                if cell != constants.EMPTY_VALUE and cell != constants.FINAL_STATE[y][x]:
                    ry, rx = self.__right_positions[cell]
                    distances_sum += abs(ry - y) + abs(rx - x)

        return distances_sum
