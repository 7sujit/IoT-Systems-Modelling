#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(_list):
    G = nx.Graph()
    length = len(_list)
    print "length is %s\n" % length
    node_list = [item for item in _list] # item VARIABLE MUST BE A STRING
    G.add_cycle(node_list);
    pos = nx.circular_layout(G)
    draw_lifted(G, pos)     #DRAW LIFETED LABLES


def draw_lifted(G, pos=None, offset=0.1, fontsize=12):
    pos = nx.spring_layout(G) if pos is None else pos
    nx.draw(G, pos, font_size = fontsize, with_labels=False)
    for p in pos:
        pos[p][1] += offset
    nx.draw_networkx_labels(G,pos)
    plt.show()

if __name__ == '__main__':
    array = [ str(i) for i in range(10)]
    draw_graph(array)
