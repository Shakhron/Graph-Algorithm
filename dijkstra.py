import xml.etree.ElementTree as ET
from heapq import *

def inputfromxml(filename):
    graph = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    graph_ = root.find('graph')
    for i in range(14, 28):
        mas = []
        edge = graph_[i].attrib
        source = edge.get('source')
        weight = edge.get('weight')
        weight_mas = weight.split(',')
        for i in weight_mas:
            i = i.split('-')
            index = int(i[0])
            i[0] = index
            mas.append(tuple(i))
        graph[source] = mas
    return graph


def dijkstra(start,goal,graph):
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
                heappush(opened,(new_cost,sosed_node))
                weight[sosed_node] = new_cost
                closed[sosed_node] = node
    fb = open('dijkstra_result.txt','w')
    fb.write('G(n): ')
    fb.write(str(weight[goal]))
    fb.close()

    return closed



