#!/usr/bin/python

import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(node_list, node_pairs):
    G = nx.Graph()
    length = len(node_list)
    # print "length is %s\n" % length
    # node_list = [item for item in _list] # item VARIABLE MUST BE A STRING
    for item in node_pairs:
        G.add_edge(item[0], item[1])
    pos = nx.circular_layout(G)
    draw_lifted(G, pos)     #DRAW LIFETED LABLES


def draw_lifted(G, pos=None, offset=0.08, fontsize=8):
    pos = nx.circular_layout(G) if pos is None else pos
    nx.draw(G, pos, font_size = fontsize, with_labels=False, node_color='yellow')
    for p in pos:
        pos[p][1] -= offset
    nx.draw_networkx_labels(G,pos,offset=0.08,font_size=10,font_color='b' )
    plt.show()

if __name__ == '__main__':
    array = [ str(i) for i in range(3)]
    draw_graph(array)
