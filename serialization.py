import math
import constants

def serialize(state):
    flattened_state = []

    for row in state:
        for cell in row:
            flattened_state.append(str(cell) if cell != constants.EMPTY_VALUE else "_")

    return ''.join(flattened_state)

def unserialize(string):
    if len(string) != constants.BOARD_SIZE ** 2:
        raise ValueError("Invalid state")

    state = [[] for i in range(constants.BOARD_SIZE)]

    for i in range(len(string)):
        char = int(string[i]) if string[i] != '_' else constants.EMPTY_VALUE
        state[math.floor(i / constants.BOARD_SIZE)].append(char)

    return state
