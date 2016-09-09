from blocktile import *
import ctypes

initial_state = [["1","2","3"],["4","5","6"],["7"," ","8"]]
nodeA = Node(0, initial_state)

sons = nodeA.generate()
for son in sons:
    print son.state

print ctypes.cast(id(nodeA), ctypes.py_object).value