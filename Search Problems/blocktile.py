class node(object):
    def __init__(self, depth, state):
        self.block_position = {"1":[0,0],"2":[0,1],"3":[0,2],"4":[1,0],"5":[1,1],"6":[1,2],"7":[2,0],"8":[2,1]}
        self.depth = depth
        self.est = self.hamilton_distance()    # cost is hamilton distance
        self.state = state  # state is list of list
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
            return False
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
        for row, lst in self.state:
            for col, block in lst:
                if block == letter:
                    return [row,col]
        return False

    def generate(self):
        list_successors = []
        for action in self.action():
            for item in action:
                state = self.state
                successor = node( self.depth + 1, )

        return list_successors

    def result(self, state, action):
        if action == "up":
            result_state = 1
        if action == "down":
            result_state = 1
        if action == "left":
            result_state = 1
        if action == "right":
            result_state = 1
        return 0