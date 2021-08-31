# A_Star_Routing
Solve a routing problem using A* search. 

Walls are represented with characters '+' or '-' or '|'.
Goals are marked by 'G'.
Starting node is marked by 'S'.
The obstacles are marked by 'X'.
A* search is used to find the best solution. 
Heuristic function is implemented in the grach class. 
The search.py is a generic search module that provided. It is implemented by AStarSearch.py. 

Give a graph like:

map_str = """\
+-------+
|     XG|
|X XXX  |
|  S    |
+-------+
"""

Find the best solution and marked the solution by '*'.
The paths that have been explored are marked by '.'. 
Print the map to get the result:

+-------+
|     XG|
|X XXX**|
|  S***.|
+-------+


