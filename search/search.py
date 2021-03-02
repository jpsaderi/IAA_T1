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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    - retorna (x, y) posicao inicial
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    - retorna booleano (True ou False) se encontrou a bolinha
    print "St art's successors:", problem.getSuccessors(problem.getStartState())
    - retorna os adjacentes a posicao atual, em 3 variaveis (posicao, direcao e custo) ((x, y), (North/West/South,East) e custo inteiro)
    """

    "*** YOUR CODE HERE ***"

    from util import Stack  # utilizar a pilha contida em util

    Pos_inicial = problem.getStartState()  # obtem a posicao inicial
    if problem.isGoalState(Pos_inicial):  # se a posicao inicial for a da bolinha, finaliza
        return []

    pilha = Stack()
    visitados = []  # vetor de visitador, contendo (no, caminho)

    pilha.push((Pos_inicial, []))  # inicializa com posicao inicial e o caminho ate chegar nela

    while not pilha.isEmpty():  # enquanto a pilha nao for vazia
        Pos_atual, caminho = pilha.pop()  # pega o topo da pilha
        if Pos_atual not in visitados:  # se a posicao atual ainda nao foi visitada
            visitados.append(Pos_atual)  # copia o vetor

            if problem.isGoalState(Pos_atual):  # encontrou a bolinha
                return caminho  # retorna o caminho usado para chegar nessa bolinha

            for Pos_proxima, direcao, custo in problem.getSuccessors(Pos_atual):
                Nova_acao = caminho + [direcao] #atribui novo custo para o proximo no
                pilha.push((Pos_proxima, Nova_acao)) #inseri os adjascentes a pilha

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    from util import Queue  # utilizar a fila contida em util

    Pos_inicial = problem.getStartState()  # obtem a posicao inicial
    if problem.isGoalState(Pos_inicial):  # se a posicao inicial for a da bolinha, finaliza
        return []

    fila = Queue()
    visitados = []  # vetor de visitador, contendo (no, caminho)

    fila.push((Pos_inicial, []))  # inicializa com posicao inicial e o caminho ate chegar nela

    while not fila.isEmpty():  # enquanto a fila nao for vazia
        Pos_atual, caminho = fila.pop()  # pega o topo da fila
        if Pos_atual not in visitados:  # se a posicao atual ainda nao foi visitada
            visitados.append(Pos_atual)  # copia o vetor

            if problem.isGoalState(Pos_atual):  # encontrou a bolinha
                return caminho  # retorna o caminho usado para chegar nessa bolinha

            for Pos_proxima, direcao, custo in problem.getSuccessors(Pos_atual):
                Nova_acao = caminho + [direcao]  # atribui novo custo para o proximo no
                fila.push((Pos_proxima, Nova_acao))  # inseri os adjascentes a fila

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue  # utilizar a fila contida em util

    Pos_inicial = problem.getStartState()  # obtem a posicao inicial
    if problem.isGoalState(Pos_inicial):  # se a posicao inicial for a da bolinha, finaliza
        return []

    visitados = []  # vetor de visitador, contendo (no, caminho)

    fila_prioridade = PriorityQueue() #((x,y), direcao, custo), prioridade)
    fila_prioridade.push((Pos_inicial, [], 0), 0)  # inicializa com posicao inicial, o caminho ate chegar nela, o custo e a prioridade

    while not fila_prioridade.isEmpty():  # enquanto a fila nao for vazia
        Pos_atual, caminho, custo_atual = fila_prioridade.pop()  # pega o topo da fila
        if Pos_atual not in visitados:  # se a posicao atual ainda nao foi visitada
            visitados.append(Pos_atual)  # copia o vetor

            if problem.isGoalState(Pos_atual):  # encontrou a bolinha
                return caminho  # retorna o caminho usado para chegar nessa bolinha

            for Pos_proxima, direcao, custo in problem.getSuccessors(Pos_atual):
                Nova_acao = caminho + [direcao]  # atribui novo custo para o proximo no
                prioridade = custo_atual + custo  # soma o custo do caminho com o atual
                fila_prioridade.push((Pos_proxima, Nova_acao, prioridade),prioridade)  # inseri os adjascentes a fila

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    from util import PriorityQueue  # utilizar a fila contida em util

    Pos_inicial = problem.getStartState()  # obtem a posicao inicial
    if problem.isGoalState(Pos_inicial):  # se a posicao inicial for a da bolinha, finaliza
        return []

    visitados = []  # vetor de visitador, contendo (no, caminho)

    fila_prioridade = PriorityQueue()  # ((x,y), direcao, custo), prioridade)
    fila_prioridade.push((Pos_inicial, [], 0), 0)  # inicializa com posicao inicial, o caminho ate chegar nela, o custo e a prioridade

    while not fila_prioridade.isEmpty():  # enquanto a fila nao for vazia
        Pos_atual, caminho, custo_atual = fila_prioridade.pop()  # pega o topo da fila
        if Pos_atual not in visitados:  # se a posicao atual ainda nao foi visitada
            visitados.append(Pos_atual)  # copia o vetor

            if problem.isGoalState(Pos_atual):  # encontrou a bolinha
                return caminho  # retorna o caminho usado para chegar nessa bolinha

            for Pos_proxima, direcao, custo in problem.getSuccessors(Pos_atual):
                Nova_acao = caminho + [direcao]  # atribui novo custo para o proximo no
                prioridade = custo_atual + custo  # soma o custo do caminho com o atual
                Custo_heuristico = prioridade + heuristic(Pos_proxima, problem)
                fila_prioridade.push((Pos_proxima, Nova_acao, prioridade), Custo_heuristico)  # inseri os adjascentes a fila

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
