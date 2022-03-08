# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    s = problem.getStartState() # Get the starting state of the problem
    open = util.Stack() # LIFO queue containing nodes to be checked
    closed = util.Stack() # LIFO queue containing nodes that have been checked
    parents = {s: None} # dictionary that records parent-child relationship between nodes
    fwd_path = [] # the final answer to be returned; a forward path from the start state to the goal state

    if not problem.isGoalState(s):
        open.push([s]) # We need the brackets since problem.getStartState returns only a tuple.
    
    while not open.isEmpty(): # Continue until we reach a point where there are no more nodes to check.
        x_obj = open.pop() # contains ((x, y), dir, cost)
        x = x_obj[0] # only (x, y)

        if(problem.isGoalState(x)):
            path = util.Stack() # Data structure used to hold backwards path from goal state to start state

            while x_obj is not None: # Go until we find a node who has no parent, namely the starting node
                path.push(x_obj) # Add node x_obj to the path
                x_obj = parents[x_obj[0]] # Change focus to x_obj's parent (0th element is coords)

            path.pop() # pop the start node off the stack, since we don't include it in the path.

            while not path.isEmpty(): # Pop nodes off the stack until empty to reverse it
                x = path.pop()
                fwd_path.append(x[1]) # Only include the direction
            return fwd_path

        else:
            children = problem.getSuccessors(x) # Find the child nodes of x
            closed.push(x) # We have visited x and seen is it not the goal state, so put it away into closed

            for child in children:
                coords = child[0]
                if not coords in closed.list:
                    parents[coords] = x_obj # Use this instead of x bcs we need direction and cost values later on.
                    open.push(child) # Push the entire child obj into the open queue to be checked later.

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from util import Queue
    open = Queue()
    closed = []         # checked path
    start = problem.getStartState()
    parents = {start: None} # dictionary that records parent-child relationship between nodes
    fwd_path = []       # the final answer to be returned; a forward path from the start state to the goal state

    open.push([start])
    while not open.isEmpty():
        cur = open.pop()    # contains (x,y), dir, cost
        curCoord = cur[0]   # only (x,y)

        if problem.isGoalState(curCoord):
            #print("end")
            path = util.Stack() # Data structure used to hold backwards path from goal state to start state

            while cur is not None: # Go until we find a node who has no parent, namely the starting node
                path.push(cur) # Add node cur to the path
                cur = parents[cur[0]] # Change focus to cur's parent (0th element is coords)

            path.pop() # pop the start node off the stack, since we don't include it in the path.

            while not path.isEmpty(): # Pop nodes off the stack until empty to reverse it
                x = path.pop()
                fwd_path.append(x[1]) # Only include the direction

            return fwd_path # cur is end state

        successors = problem.getSuccessors(curCoord)
        closed.append(curCoord)

        for suc in successors:
            if suc[0] not in closed and suc[0] not in list(map(lambda x : x[0], open.list)):
                parents[suc[0]] = cur
                open.push(suc)
        
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
