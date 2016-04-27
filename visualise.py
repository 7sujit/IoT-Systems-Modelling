#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(_list):
    G = nx.Graph()
    length = len(_list)
    print "length is %s\n" % length
    node_list = [item for item in _list] # item VARIABLE MUST BE A STRING
    G.add_edge(node_list[0], node_list[1]) # adding edges to the graph after nodelist
    G.add_edge(node_list[1], node_list[2])
    pos = nx.circular_layout(G)
    draw_lifted(G, pos)     #DRAW LIFETED LABLES


def draw_lifted(G, pos=None, offset=0.1, fontsize=10):
    pos = nx.spring_layout(G) if pos is None else pos
    nx.draw(G, pos, font_size = fontsize, with_labels=False)
    for p in pos:
        pos[p][1] += offset
    nx.draw_networkx_labels(G,pos)
    plt.show()

if __name__ == '__main__':
    array = [ str(i) for i in range(3)]
    draw_graph(array)
