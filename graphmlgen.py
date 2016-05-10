#!/usr/bin/python

import visualise

docEndTag = '</graphml>\n'
beginTag = '<?xml version="1.0" ?>\n\t<graphml>\n\t\t<key attr.name="label" attr.type="string" id="label"/>\n'
gStart = '<graph>'
gEnd = '</graph>'

node_list = []
node_pairs = []
x=None
y=None


def create_node(node_id, node_name):
    return '\t\t\t<node id="' + node_name+'"/>\n'

def create_edge(edge_id, source_id, dest_id, edge_type):
    # edge type ??? not resolved yet
    return '\t\t\t<edge directed="'+edge_type+'"  source="'+ source_id +'" target="'+ dest_id +'"/>\n'


def generate_graphml(graph,Actor,UseCase):
    f = open('./file.graphml','w');
    eid = 1;
    if(f is None):
        print 'Error'
        return
    f.write(beginTag);
    for i in graph.keys():
        if(i in Actor):
            node_list.append(Actor[i])
            f.write(create_node(i, Actor[i]))
        else:
            node_list.append(UseCase[i])
            f.write(create_node(i,UseCase[i]))

    for i in graph.keys():
        for j in graph[i]:
            x = Actor[i] if i in Actor else UseCase[i]
            y = Actor[j] if j in Actor else UseCase[j]
            node_pairs.append((x,y));
            f.write(create_edge(str(eid), i, j , 'false'))
            eid = eid + 1
    f.write(gEnd)
    f.write(docEndTag)
    f.close()
    visualise.draw_graph(Actor,UseCase,node_pairs)
    # for i in node_list:
    #     print i
    # for i in node_pairs:
    #     print i


def main():
    print 'Python Module for GraphML file generator'

if __name__ == '__main__':
    main()
