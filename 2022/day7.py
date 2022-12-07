from anytree import Node

def day_seven(input):
    nodes = []
    with open(input, 'r') as f:
        cur_node = None
        for line in f.readlines():
            line = line.strip()
            # cd commands
            if line == "$ cd /":
                root = Node("root", size=0)
                nodes.append(root)
                cur_node = root
            elif line == "$ cd ..":
                cur_node = cur_node.parent
            elif line.startswith("$ cd "):
                this_node = Node(line.split(" ")[2], parent=cur_node, size=0)
                nodes.append(this_node)
                cur_node = this_node
            # data
            elif line.split(" ")[0].isdigit():
                cur_node.size += int(line.split(" ")[0])
                to_iter = cur_node
                while to_iter.parent is not None:
                    to_iter.parent.size += int(line.split(" ")[0])
                    to_iter = to_iter.parent
            else:
                pass

    one, two = 0, None
    disk, to_free = 70_000_000, 30_000_000 # disk size, update size

    for node in nodes:
        # part 1
        if node.size <= 100_000:
            one += node.size
        # part 2
        if node.name == "root":
            to_free -= disk - node.size
        if node.size >= to_free:
            if two is None:
                two = node.size
            else:
                two = min(two, node.size)

    return (one,two)

if __name__ == '__main__':
    one,two = day_seven("2022/inputs/day7/input.txt")
    print("Part 1: ", one)
    print("Part 2: ", two)