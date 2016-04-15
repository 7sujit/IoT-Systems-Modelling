#!/usr/bin/python

docHeaderTag = '<?xml version="1.0" encoding="UTF-8"?>\n'
docStartTag = '<graphml>\n'
docEndTag = '</graphml>\n'


"""
    generate an adjacency list for the graph and later generate graphml tags and
    form the document
"""

def create_node(node_id, node_name):
    return '<node id="'+ node_id +'" name="'+ node_name +'"/>\n'

def create_edge(edge_id, source_id, dest_id, edge_type):
    # edge type ??? not resolved yet
    return '<edge id="'+ edge_id +'" type="'+ edge_type +'" source="'+ source_id +'" target="'+ dest_id +'"/>\n'

def generate_graphml(graph):
    f = open('./file.graphml','w');
    if(f is None):
        print 'Error'
        pass
    f.write(docHeaderTag)
    f.write(docStartTag)
    for i in graph.keys():
        f.write(create_node(i, 'xxxx'))
    for i in graph.keys():
        for j in graph[i]:
        	f.write(create_edge('0', i, j , 'xx'))
    f.write(docEndTag)
