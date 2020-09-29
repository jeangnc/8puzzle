from copy import deepcopy

BOARD_SIZE = 3
FINAL_STATE = [[1,2,3], [4,5,6], [7,8,None]]
DIRECTIONS = { 'd': [0, 1], 'e': [0, -1], 'c': [-1, 0], 'b': [1, 0] }

def move(state, position, direction):
    displacement = DIRECTIONS[direction]
    new_position = list(map(sum, zip(position, displacement)))

    invalid_values = [i for i in new_position if i < 0 or i >= BOARD_SIZE]
    if len(invalid_values) > 0:
        raise ValueError('Invalid position')

    y1, x1 = position
    y2, x2 = new_position

    new_state = deepcopy(state)
    new_state[y1][x1] = state[y2][x2]
    new_state[y2][x2] = state[y1][x1]

    return new_state


def swap(state, position_a, position_b):

    return



def cost():
    return


i = [[1,2,3], [4,5,6], [7,None,8]]

print(move(i, [0,0], 'd'))
print(i)
