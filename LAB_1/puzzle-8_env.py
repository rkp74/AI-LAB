# initialize the puzzle with a given state
def initialize_puzzle(state):
    # state is a list of integers representing the puzzle, with 0 representing the empty square
    # for example, state = [1, 2, 3, 4, 5, 6, 7, 8, 0] represents the puzzle in the solved state
    # store the state in a global variable
    global puzzle
    puzzle = state

# return the current state of the puzzle
def get_state():
    return puzzle

# return a list of possible actions given the current state
def get_actions():
    # get the index of the empty square
    empty_index = puzzle.index(0)
    # initialize a list of actions
    actions = []
    # if the empty square is not in the first column, the "left" action is possible
    if empty_index % 3 > 0:
        actions.append("left")
    # if the empty square is not in the last column, the "right" action is possible
    if empty_index % 3 < 2:
        actions.append("right")
    # if the empty square is not in the first row, the "up" action is possible
    if empty_index > 2:
        actions.append("up")
    # if the empty square is not in the last row, the "down" action is possible
    if empty_index < 6:
        actions.append("down")
    return actions

# apply an action to the puzzle and return the resulting state
def apply_action(action):
    # get the index of the empty square
    empty_index = puzzle.index(0)
    # initialize a new state as a copy of the current state
    new_state = puzzle.copy()
    # perform the action by swapping the empty square with the appropriate neighboring square
    if action == "left":
        new_state[empty_index], new_state[empty_index - 1] = new_state[empty_index - 1], new_state[empty_index]
    elif action == "right":
        new_state[empty_index], new_state[empty_index + 1] = new_state[empty_index + 1], new_state[empty_index]
    elif action == "up":
        new_state[empty_index], new_state[empty_index - 3] = new_state[empty_index - 3], new_state[empty_index]
    elif action == "down":
        new_state[empty_index], new_state[empty_index + 3] = new_state[empty_index + 3], new_state[empty_index]
    # update the puzzle with the new state
    initialize_puzzle(new_state)
    # return the new state
    return new_state

# check if the puzzle is in the solved state
def is_solved():
    return puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 0]
