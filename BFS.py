import xml.etree.ElementTree as ET
from collections import deque
def inputfromxml(filename):
	graph={}
	tree = ET.parse(filename)
	root = tree.getroot()
	graph_ = root.find('graph')
	for i in range(0,14):
		node = graph_[i].attrib
		source = node.get('source')
		neighbour = node.get('neighbour')
		neighbour_mas = neighbour.split(',')
		graph[source] = neighbour_mas
	return graph
def bfs(start,goal,graph):
	opened = deque([start])
	closed = {start: None}
	while opened:
		V = opened.popleft()
		if V == goal:
			break
		next_v = graph[V]
		for   i in next_v:
			if i not in closed:
				opened.append(i)
				closed[i] = V
	return closed

	


