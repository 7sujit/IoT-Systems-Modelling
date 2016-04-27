#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(node_pairs):
    G = nx.Graph()
    offset=0.1
    # print "length is %s\n" % length
    # node_list = [item for item in _list] # item VARIABLE MUST BE A STRING
    for item in node_pairs:
        G.add_edge(item[0], item[1])
    pos = nx.shell_layout(G)
    nx.draw(G, pos, font_size = 8, with_labels=False, node_color='m')
    for p in pos:
        pos[p][1] -= offset
    nx.draw_networkx_labels(G,pos,font_size=10,font_color='b' )
    plt.show()



if __name__ == '__main__':
    array = [ str(i) for i in range(3)]
    draw_graph(array)
