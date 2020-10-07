import BFS
import dijkstra as dj
import xml.etree.ElementTree as ET
file = input('Введите название файла: ')
def get_type(filename):

    tree = ET.parse(filename)
    root = tree.getroot()
    algorithm = root[0].attrib
    type_ = algorithm.get('type')
    return type_

def start(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    task = root[1].attrib
    start_id = task.get('start.id')
    return start_id
def finish(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    task = root[1].attrib
    goal = task.get('goal.id')
    return goal



if get_type(file) == 'bfs':
    start = start(file)
    goal = finish(file)
    graph = BFS.inputfromxml(file)
    closed = BFS.bfs(start,goal,graph)
    V = goal
    print(f'\nКратчайщий путь от {start} до {goal}:\n', end='')
    way = []
    while V != start:
        V = closed[V]
        way.append(V)
    way.reverse()
    way.append(goal)
    for i in way:
        if way[-1] == i:
            print(i)
        else:
            print(i, end='--->')
    myString = '--->'.join(way)
    fb = open('bfs_result.txt', 'w')
    fb.write('G(n): ')
    fb.write(str(len(way)-1))
    fb.write('\nClosed : ')
    for elements in closed:
        fb.write(elements)
        fb.write(' ')
    fb.write(f"\nКратчайщий путь от {start} до {goal} :  ")
    fb.write(myString)
    print('Результат записан в файл bfs_result.txt')
    fb.close()
elif (get_type(file) == 'dijkstra'):
    start = start(file)
    goal = finish(file)
    graph = dj.inputfromxml(file)
    closed = dj.dijkstra(start, goal, graph)
    V = goal
    way = []
    while V != start:
        V = closed[V]
        way.append(V)
    way.reverse()
    way.append(goal)
    for i in way:
        if way[-1] == i:
            print(i)
        else:
            print(i,end='--->')
    myString = '--->'.join(way)
    fb = open('dijkstra_result.txt','a')
    fb.write('\nClosed : ')
    for elements in closed:
        fb.write(elements)
        fb.write(' ')
    fb.write(f"\nКратчайщий путь от {start} до {goal} :  ")
    fb.write(myString)
    print('Результат записан в файл dijkstra_result.txt')
    fb.close()

