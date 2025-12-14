from collections import defaultdict
import functools

data = {}
with open("11.txt") as file:
    for line in file:
        a, bs = line.strip().split(": ")
        data[a]= bs.split()




@functools.lru_cache(maxsize=None)
def num_paths_from(node):
    if node == "out":
        return 1
    else:
        return sum([num_paths_from(x) for x in data[node]])

ans1 = num_paths_from("you")
print(ans1)

@functools.lru_cache(maxsize=None)
def paths_connecting(node, destination):
    if node == destination:
        return 1
    elif node == "out":
        return 0
    else:
        return sum([paths_connecting(x,destination) for x in data[node]])


a1=paths_connecting("svr","dac")
a2=paths_connecting("dac","fft")
a3=paths_connecting("fft","out")

b1=paths_connecting("svr","fft")
b2=paths_connecting("fft","dac")
b3=paths_connecting("dac","out")

print(a1*a2*a3+b1*b2*b3)


# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.DiGraph()

# edges_to_add = []
# for x in data:
#     edges_to_add += [(x,y) for y in data[x]]
# G.add_edges_from(edges_to_add)

# # 3. Define the layout of nodes (e.g., spring layout)
# pos = nx.spring_layout(G) # positions for all nodes

# # 4. Draw the graph
# # plt.figure(figsize=(8, 6)) # Optional: adjust figure size
# nx.draw_networkx_nodes(G, pos, node_size=700)
# nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle="->", arrowsize=20) # Draw directed edges with arrows
# nx.draw_networkx_labels(G, pos, font_size=12, font_color="whitesmoke")

# # 5. Display the plot
# plt.axis('off') # Turn off the axis
# plt.title("Directed Graph Visualization with NetworkX")
# plt.show()







