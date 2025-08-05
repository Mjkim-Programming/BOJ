node_num = int(input())
nodes = list(input().split())
nodes = [int(i) for i in nodes]
node_to_delete = int(input())
nodes_to_delete = [node_to_delete]

children = {}

for i in range(node_num):
    p = nodes[i]
    if p == -1: pass
    if p not in children:
        children[p] = []
    children[p].append(i)

deleted = set()

while nodes_to_delete:
    current = nodes_to_delete.pop()
    deleted.add(current)
    if current in children:
        for child in children[current]:
            nodes_to_delete.append(child)
            
leaf_count = 0

for i in range(node_num):
    if i in deleted:
        continue

    if i not in children:
        leaf_count += 1
    else:
        if all(child in deleted for child in children[i]):
            leaf_count += 1
            
print(leaf_count)