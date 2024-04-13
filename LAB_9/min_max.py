class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

def build_min_max_tree(values):
    nodes = [TreeNode(value) for value in values]
    while len(nodes) > 1:
        new_nodes = []
        for i in range(0, len(nodes), 2):
            if i + 1 < len(nodes):
                new_nodes.append(TreeNode(max(nodes[i].value, nodes[i + 1].value), [nodes[i], nodes[i + 1]]))
            else:
                new_nodes.append(nodes[i])
        nodes = new_nodes
    return nodes[0]

def print_tree(node, level=0):
    if node:
        print('  ' * level + str(node.value))
        for child in node.children:
            print_tree(child, level + 1)

leaf_values = [7, 4, 3, 8, 2, 6, 5, 1, 9]
root = build_min_max_tree(leaf_values)

print("Min-Max Tree:")
print_tree(root)
