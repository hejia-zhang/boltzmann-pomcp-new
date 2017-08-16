from robot import *
from rocksamplegame import *
from humanPolicy import *
from humannode import *
from root import *
from robotnode import *
from rocksamplepomcp import *
import math
import pickle


rock_vector = [((1,0),0), ((2,0),1)]
theta_set = [[1,1],[1,1]]
game = Rocksample_Game(10, 10, (0,0), rock_vector, theta_set, 0.95)

# grid = [[0 for y in range(10)] for x in range(10)]
# grid[0][0] = 1

initial_history = Root(game, [((0,0),0), ((0,0),1)], 0)

#make sure to change exploration accordingly - also what should the epsilon value be?
epsilon = math.pow(0.95, 5)

for _ in range(0, 1):
#KEEP THESE PARAMETERS FOR NOW!!
	solver = Rocksample_POMCP_Solver(0.95, epsilon, 500000, initial_history, game, 0.3, 5, "rational")
	print(1)
	solver.search()
	data = solver.data
	f = open('data-pomcp.txt', 'w')
	f.write(str(data))
	print("_____________________")

"""
Things to keep in mind:
1. Make sure to change epsilon appropriately.
2. The game file has that weird shit about leaving the same state when the human and robot have the same
   action. Not sure if this matters or not? Maybe depends on epsilon?
3. Exploration should be >= 300 for >= million, maybe just a wee bit less for 10000.
4. For the Rational Function: I divide by 3. This is a cluge fix, make it like dependent on number of
   iterations...for >= 1 million this should be <= 1.
5. For the Rational Function: It's giving me a divide by zero error...this shouldn't happen, the visited
   should already be incremented.
"""