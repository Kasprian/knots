import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def parse_gauss_code(gauss_code):
    crossings = {}
    for i, num in enumerate(gauss_code):
        if abs(num) not in crossings:
            crossings[abs(num)] = [None, None]
        if num > 0:
            crossings[abs(num)][0] = i
        else:
            crossings[abs(num)][1] = i
    return crossings

def plot_knot_from_gauss_code(gauss_code):
    crossings = parse_gauss_code(gauss_code)
    
    G = nx.Graph()
    pos = {}
    
    # Define positions for a simple circular layout
    num_crossings = len(crossings)
    angle_step = 2 * np.pi / num_crossings
    radius = 5
    
    # Add nodes with positions
    for i, crossing in enumerate(crossings):
        angle = i * angle_step
        pos[crossing] = (radius * np.cos(angle), radius * np.sin(angle))
        G.add_node(crossing, pos=pos[crossing])
    
    # Add edges based on Gauss code
    for crossing, (first, second) in crossings.items():
        if first is not None and second is not None:
            next_node_first = gauss_code[(first + 1) % len(gauss_code)]
            next_node_second = gauss_code[(second + 1) % len(gauss_code)]
            if next_node_first in G.nodes and next_node_second in G.nodes:
                G.add_edge(crossing, next_node_first)
                G.add_edge(crossing, next_node_second)
    
    # Plot the graph
    nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=16)
    plt.title("Knot Visualization from Gauss Code")
    plt.show()

# Example Gauss code for a trefoil knot
gauss_code = [1, -2, 3, -1, 2, -3]
plot_knot_from_gauss_code(gauss_code)