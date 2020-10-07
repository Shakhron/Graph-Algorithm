import xml.etree.ElementTree as ET
from heapq import *
def start(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    task = root[1].attrib
    start_i = task.get('start.i')
    start_j = task.get('start.j')
    s = (int(start_i),int(start_j))
    return s
def finish(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    task = root[1].attrib
    goal_i = task.get('goal.i')
    goal_j = task.get('goal.j')
    goal = (goal_i,goal_j)
    return goal
def inputfromxml(filename):
    grid = []
    tree = ET.parse(filename)
    root = tree.getroot()
    graph_ = root.find('graph')
    for i in range(0, 10):
        row = graph_[i].attrib
        source = row.get('n')
        source = source.split(' ')
        grid.append(source)
    return grid
gr = inputfromxml('grid.xml')
start('grid.xml')
finish('grid.xml')
def manhattan_heuristik(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
def diaginal_heuristik(a,b):
    return max(abs(a[0]-b[0]),abs(a[1]-b[1]))
def astar(start,goal,graph):
    opened = []
    heappush(opened,(0,start))
    weight = {start:0}
    closed = {start: None}

    while opened:
        cost,node = heappop(opened)
        if node == goal:
            break
        V = graph[node]
        for x in V:
            sosed_cost,sosed_node = x
            new_cost = weight[node] + sosed_cost
            if sosed_node not in weight or new_cost < weight[sosed_node]:
                priority = new_cost + evristic(sosed_node,goal)
                heappush(opened,(priority,sosed_node))
                weight[sosed_node] = new_cost
                closed[sosed_node] = node