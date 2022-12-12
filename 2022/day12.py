from tqdm import tqdm

class Point:
    def __init__(self, x, y, value, type=None):
        self.x = x
        self.y = y
        self.value = value
        self.type = type
    def __repr__(self):
        return f"({self.x},{self.y})={self.value}"
    def __str__(self):
        return f"({self.x},{self.y})={self.value}"
    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self) -> int:
        return hash((self.x, self.y))

def get_valid_neighbors(graph, point):
        neighbors = []
        x = point.x
        y = point.y
        if x > 0 and graph[x-1][y].value - point.value < 2 :
            neighbors.append(graph[x-1][y])
        if x < len(graph)-1 and graph[x+1][y].value - point.value < 2:
            neighbors.append(graph[x+1][y])
        if y > 0 and graph[x][y-1].value - point.value < 2:
            neighbors.append(graph[x][y-1])
        if y < len(graph[0])-1 and graph[x][y+1].value - point.value < 2:
            neighbors.append(graph[x][y+1])
        
        return neighbors

def shortest_path(graph, start, end):
    path_list = [[start]]
    path_index = 0
    previous = {start}

    if start == end:
        return path_list[0]
    while path_index < len(path_list):
        curr_path = path_list[path_index]
        last_point = curr_path[-1]
        next_points = graph[last_point]
        # Search goal node
        if end in next_points:
            curr_path.append(end)
            return curr_path
        # Add new paths
        for np in next_points:
            if not np in previous:
                new_path = curr_path[:]
                new_path.append(np)
                path_list.append(new_path)
                # To avoid backtracking
                previous.add(np)
        # Continue to next path in list
        path_index += 1
    return []

def day_twelve(input):
    matrix = []
    start = (0,0)
    end = (0,0)
    with open (input, "r") as f:
        for i,line in enumerate(f.readlines()):
            row = []
            for j, char in enumerate(line.strip()):
                type = None
                value = ord(char)
                if char == "S":
                    start = (i,j)
                    type = "start"
                elif char == "E":
                    end = (i,j)
                    type = "end"
                
                if type == "start":
                    value = ord("a")
                elif type == "end":
                    value = ord("z")
                row.append(Point( i, j, value, type))

            matrix.append(row)

    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            graph[matrix[i][j]] = get_valid_neighbors(matrix, matrix[i][j])

    starting_points = [start]
    for point in graph:
        if point.value == ord("a") and point != start:
            starting_points.append(point)

    paths = []
    for point in tqdm(starting_points):
        length = len(shortest_path(graph, point, end))
        if length > 0:
            paths.append(length-1)

    return (paths[0],min(paths))

if __name__ == '__main__':
    one,two = day_twelve("2022/inputs/day12/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)
