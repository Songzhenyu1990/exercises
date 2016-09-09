import copy


class Node(object):
    def __init__(self, depth, state_input):
        self.block_position = {"1":[0,0],"2":[0,1],"3":[0,2],"4":[1,0],"5":[1,1],"6":[1,2],"7":[2,0],"8":[2,1]}    # target position
        self.depth = depth
        self.state = state_input  # state is list of list
        self.est = self.hamilton_distance()    # cost is hamilton distance
        self.blank_block_position = self.find_block(" ")

    def action(self):   # Determine how many directions can have
        list_action = ["up", "down", "left", "right"]
        if self.blank_block_position[0] == 0:
            list_action.remove("up")
        if self.blank_block_position[0] == 2:
            list_action.remove("down")
        if self.blank_block_position[1] == 0:
            list_action.remove("left")
        if self.blank_block_position[1] == 2:
            list_action.remove("right")
        if not list_action:
            print "empty successors"
            return []
        else:
            return list_action

    def hamilton_distance(self):
        result = 0
        for index in range(1, 9):
            pos = self.find_block(str(index))
            for idx, value in enumerate(pos):
                result += abs(value - self.block_position[str(index)][idx])
        return result

    def find_block(self, letter):
        for row, lst in enumerate(self.state):
            for col, block in enumerate(lst):
                if block == letter:
                    return [row,col]
        return False

    def generate(self):
        list_successors = []
        for action in self.action():
            #for item in action:
            state = self.result(self.state, action)
            successor = Node(self.depth + 1, state)
            list_successors.append(successor)
        return list_successors

    def result(self, state1, action):
        state = copy.deepcopy(state1)
        if action == "up":
            state[self.blank_block_position[0]][self.blank_block_position[1]] = state[self.blank_block_position[0] - 1][self.blank_block_position[1]]
            state[self.blank_block_position[0] - 1][self.blank_block_position[1]] = " "
        if action == "down":
            state[self.blank_block_position[0]][self.blank_block_position[1]] = state[self.blank_block_position[0] + 1][
                self.blank_block_position[1]]
            state[self.blank_block_position[0] + 1][self.blank_block_position[1]] = " "
        if action == "left":
            state[self.blank_block_position[0]][self.blank_block_position[1]] = state[self.blank_block_position[0]][
                self.blank_block_position[1] - 1]
            state[self.blank_block_position[0]][self.blank_block_position[1] - 1] = " "
        if action == "right":
            state[self.blank_block_position[0]][self.blank_block_position[1]] = state[self.blank_block_position[0]][
                self.blank_block_position[1] + 1]
            state[self.blank_block_position[0]][self.blank_block_position[1] + 1] = " "
        return state

