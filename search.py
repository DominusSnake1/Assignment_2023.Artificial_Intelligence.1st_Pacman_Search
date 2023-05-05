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

    def getInitialState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isFinalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getNextStates(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getActionCost(self, actions):
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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getInitialState())
    print("Is the start a goal?", problem.isFinalState(problem.getInitialState()))
    print("Start's successors:", problem.getNextStates(problem.getInitialState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    stack = Stack()     # Create the node stack.
    stack.enqueue(problem.getInitialState())        # Add to node and path stack the agent's starting node.
    visitedNodesList = []       # Create an empty list with all the visited nodes.
    pathList = []       # Create an empty list with the final path from start node to current node.
    currentState = stack.dequeue()      # currentState represents the current node the agent is examining.

    while not (problem.isFinalState(currentState)):     # Checks if currentState is goal.
        if (currentState in visitedNodesList) and (not stack.isEmpty()):        # If visited before or
            currentState, pathList = stack.dequeue()        # queue is not empty, then skip this iteration.
            continue

        visitedNodesList.append(currentState)       # Add it to the visited list.
        childrenList = problem.getNextStates(currentState)        # List with currentState's child nodes.

        for child, direction, cost in childrenList:       # For each child node of currentState.
            tempPath = pathList + [direction]       # Temporary list with the path to goal and new direction.
            stack.enqueue((child, tempPath))       # Add child and path to stack.
    return pathList     # If currentState was the goal, then we return the list with the path from start to goal.

    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()     # Create the node and path queue.
    queue.enqueue(problem.getInitialState())        # Add to node and path queue the agent's starting node.
    visitedNodesList = []       # Create an empty list with all the visited nodes.
    pathList = []       # Create a list with the path from start node to current node.
    currentState = queue.dequeue()     # currentState represents the current node the agent is examining.

    while not (problem.isFinalState(currentState)):     # Checks if currentState is goal.
        if (currentState in visitedNodesList) and (not queue.isEmpty()):        # If visited before or
            currentState, pathList = queue.dequeue()        # queue is not empty, then skip this iteration.
            continue

        visitedNodesList.append(currentState)       # Add it to the visited list.
        childrenList = problem.getNextStates(currentState)      # List with currentState's child nodes.

        for child, direction, cost in childrenList:     # For each child node of currentState.
            tempPath = pathList + [direction]       # Temporary list with the path to goal and new direction.
            queue.enqueue((child, tempPath))        # Add child and path to queue.

    return pathList     # If currentState was the goal, then we return the list with the path from start to goal.

    # util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of the least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    priorityQueue = PriorityQueue()
    priorityQueue.enqueue(problem.getInitialState(), 0)
    visitedNodesList = []
    pathList = []
    pathToCurrentNodePrioQueue = PriorityQueue()
    currentState = priorityQueue.dequeue()

    while not (problem.isFinalState(currentState)):
        if currentState in visitedNodesList:
            currentState = priorityQueue.dequeue()
            pathList = pathToCurrentNodePrioQueue.dequeue()
            continue

        visitedNodesList.append(currentState)
        childrenList = problem.getNextStates(currentState)

        for child, direction, cost in childrenList:
            if child in visitedNodesList: continue

            tempPath = pathList + [direction]
            visitCost = problem.getActionCost(tempPath)
            priorityQueue.enqueue(child, visitCost)
            pathToCurrentNodePrioQueue.enqueue(tempPath, visitCost)
    return pathList

    # util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    priorityQueue = PriorityQueue()
    priorityQueue.enqueue(problem.getInitialState(), 0)
    visitedNodesList = []
    pathList = []
    currentState = priorityQueue.dequeue()

    while not (problem.isFinalState(currentState)):
        if (currentState in visitedNodesList) and (not priorityQueue.isEmpty()):
            currentState, pathList = priorityQueue.dequeue()
            continue

        visitedNodesList.append(currentState)
        childrenList = problem.getNextStates(currentState)

        for child, direction, cost in childrenList:
            if child in visitedNodesList: continue

            tempPath = pathList + [direction]
            visitCost = problem.getActionCost(tempPath) + heuristic(child, problem)
            priorityQueue.enqueue((child, tempPath), visitCost)
    return pathList

    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
