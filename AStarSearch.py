from search import *
import math
import heapq

class RoutingGraph(Graph):    
    def starting_state(self):
        starting_state = []  
        for i in range(self.row_count): 
            for j in range(self.column_count): 
                if self.map_graph[i][j] == 'S':
                    starting_state.append((i,j))  
        return list(starting_state)
            
    def __init__(self, map_str):
        self.map_str = map_str
        self.map_graph = self.map_str.strip().splitlines() 
        self.row_count, self.column_count  = len(self.map_graph), len(self.map_graph[0])     
        self.starting_state = self.starting_state()
        self.goals = []
        
    def is_goal(self, node):
        if self.map_graph[node[0]][node[1]] == 'G':
            self.goals.append(node)
        return self.map_graph[node[0]][node[1]] == 'G'

    def starting_nodes(self):
        return list(self.starting_state)
  
    def outgoing_arcs(self, tail_node):
        wa_ob, di_list, direct = ['X', '-', '+','|'], [(-1, 0),(0, 1),(1, 0),(0, -1)],  ['N', 'E', 'S', 'W']
        d_len = len(di_list)
        arcs, head =[], []*d_len
     
        for i in range(d_len):
            head = tuple(a + b for a, b in zip(tail_node, di_list[i]))
            if self.map_graph[head[0]][head[1]] not in wa_ob:
                arcs.append(Arc(tail_node, head, direct[i], 5))
        return arcs    
        
    def estimated_cost_to_goal(self, node):
        if len(node) != 0:
            ni, nj = node
            res = []
            for i in range(self.row_count):
                for j in range(self.column_count):
                    if self.map_graph[i][j] == 'G':
                        res.append((abs(ni - i) + abs(nj - j)) * 5)
            return min(res)
        else: 
            return 0
    
class AStarFrontier(Frontier):
    def __init__(self,map_graph):
        self.container = []
        self.map_graph = map_graph
        self.expanded_list = []

    def add(self, path):
        if path[-1].head not in self.expanded_list:
            cost = sum([p.cost for p in path])
            total_cost = self.map_graph.estimated_cost_to_goal(path[-1].head) + cost 
            
            found = False
            for cost2, path2 in self.container:
                if cost2 == total_cost:
                    path2.append(path)
                    found = True
                    break
            if found == False:
                heapq.heappush(self.container, (total_cost,[path]))
             
    def __next__(self):
        return self
    
    def __iter__(self):   
        while len(self.container) > 0:
            item = self.container[0][1]
            if len(item) > 1:
                path = item.pop(0) 
            else:
                path = heapq.heappop(self.container)[1][0]
            
            if path[-1].head not in self.expanded_list:
                self.expanded_list.append(path[-1].head)
                yield path   
        
def print_map(map_graph, frontier, solution):  
    mapmap = map_graph.map_graph
    for i, j in frontier.expanded_list:  
        if (i, j) not in map_graph.goals and (i, j) not in map_graph.starting_nodes():
            res = "".join((mapmap[i][:j], '.', mapmap[i][j+1:]))
            mapmap[i] = res
    if solution is None:
        for row in mapmap:
            print(row)      
    else:
        for item in solution[1:-1]:
            i, j = item.head
            if (i, j) not in map_graph.goals and (i, j) not in map_graph.starting_nodes():
                res = "".join((mapmap[i][:j], '*', mapmap[i][j+1:]))
                mapmap[i] = res
        for row in mapmap:
            print(row)    
            
def main():
    map_str =  """\
+-------------+
|         G   |
| S           |
|         S   |
+-------------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


if __name__ == "__main__":
    main()
        

    
    
