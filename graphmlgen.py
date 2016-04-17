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

def generate_graphml(graph,Actor,UseCase):
    f = open('./file.graphml','w');
    eid = 1;
    if(f is None):
        print 'Error'
        return
    f.write(docHeaderTag)
    f.write(docStartTag)
    for i in graph.keys():
        if i in Actor:
            f.write(create_node(i, Actor[i]))
        else:
            f.write(create_node(i, UseCase[i]))
    for i in graph.keys():
        for j in graph[i]:
            f.write(create_edge(str(eid), i, j , 'xx'))
            eid = eid + 1
    f.write(docEndTag)
    f.close()



def main():
    print 'Python Module for GraphML file generator'

if __name__ == '__main__':
    main()
