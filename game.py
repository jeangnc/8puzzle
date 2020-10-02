#!/usr/bin/env python

from copy import deepcopy

import sys
import constants
import serialization
import algorithms

def solve(initial_state, algorithm):
    if not solvable(initial_state):
        raise ValueError("Initial state unsolvable")

    visited = set()
    seen = {}

    initial_position = value_position(initial_state, constants.EMPTY_VALUE)
    algorithm.add(initial_state, initial_position, [])

    max_available = 0

    while True:
        max_available = max(max_available, algorithm.available())
        state, position, path = algorithm.next()

        if state == constants.FINAL_STATE:
            break

        visited.add(state)

        for direction in available_directions(position):
            new_position = calculate_position(position, direction)
            new_state = swap(state, position, new_position)
            new_cost = len(path)

            if new_state in seen:
                current_cost = seen[new_state]
                if new_cost >= current_cost:
                    continue

            seen[new_state] = new_cost
            algorithm.add(new_state, new_position, path + [direction])

    return {
        'visited': len(visited),
        'available': algorithm.available(),
        'max_available': max_available,
        'solution': path,
        'steps': len(path),
    }

def solvable(state):
    inversions = 0
    seen = []

    for row in state:
        for cell in row:
            if cell == constants.EMPTY_VALUE:
                continue

            inversions += len([i for i in seen if cell < i])
            seen.append(cell)

    return inversions % 2 == 0

def value_position(state, value):
    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            if value == cell:
                return (y,x)
    raise ValueError("Unknown value")

def available_directions(position):
    f = lambda d: is_position_valid(calculate_position(position, d))
    return list(filter(f, constants.DIRECTIONS))

def is_position_valid(position):
    invalid_values = [x for x in position if x < 0 or x >= constants.BOARD_SIZE]
    return len(invalid_values) == 0

def calculate_position(position, direction):
    displacement = constants.DIRECTIONS[direction]
    return tuple(map(sum, zip(position, displacement)))

def swap(state, position_1, position_2):
    y1, x1 = position_1
    value_1 = state[y1][x1]

    y2, x2 = position_2
    value_2 = state[y2][x2]

    if constants.EMPTY_VALUE not in [value_1, value_2]:
        raise ValueError("Can't swap two filled positions")

    new_state = list(map(list, state))
    new_state[y1][x1] = value_2
    new_state[y2][x2] = value_1
    return tuple(map(tuple, new_state))


arg = sys.argv[1]
initial = tuple(map(tuple, serialization.unserialize(arg)))

print("Uniform cost", solve(initial, algorithms.UniformCost()))
print("\n")
print("Simple heuristic", solve(initial, algorithms.SimpleHeuristic()))
print("\n")
print("Sophisticated heurístic", solve(initial, algorithms.SophisticatedHeuristic()))
