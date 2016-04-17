#!/usr/bin/python

# from printing import print_dict;
import disp
import graphmlgen

f = open('./check.xmi','r');

s=[]
t=[]
UseCase = {}
Actor = {}
Adj={}

for i in f:
    #   print  ' -********************'
    #   print i
      s.append(' '.join(i.split()))
    #   print ' '.join(i.split())


## SCANNING THROUGH "<UML:UseCase"
for i in s:
    if(i.startswith('<UML:UseCase')):
        t.append(i)

xmi_id_len = len('xmi.id="')
xmi_name_len = len('name="')
# xmi_name_start = t[0].find('name="')

z = 0
y=0
p=0
q=0

for i in t:
    xmi_name_start = i.find('name="')
    l = len(i)
    xmi_id_start = i.find('xmi.id');
    p=xmi_id_start
    q=xmi_name_start + xmi_name_len + 1
    while(p < l):
        if(i[p] is ' '):
            z=p
            break
        p = p + 1
    while(q < l):
        if(i[q] is '"'):
            y=q
            break
        q = q + 1
    UseCase[i[xmi_id_start+xmi_id_len :z-1]] = i[xmi_name_start + xmi_name_len: y ]
    # print i[xmi_name_start + xmi_name_len: y+2]


disp.print_dict(UseCase)

t = []
for i in s:
    if(i.startswith('<UML:Actor')):
        t.append(i)
        # print i

####### producing ACTOR dependecy

z = 0
y=0
p=0
q=0

for i in t:
    xmi_name_start = i.find('name="')
    l = len(i)
    xmi_id_start = i.find('xmi.id');
    p=xmi_id_start
    q=xmi_name_start + xmi_name_len + 1
    while(p < l):
        if(i[p] is ' '):
            z=p
            break
        p = p + 1
    while(q < l):
        if(i[q] is '"'):
            y=q
            break
        q = q + 1
    Actor[i[xmi_id_start+xmi_id_len :z-1]] = i[xmi_name_start + xmi_name_len: y ]
    # print i[xmi_name_start + xmi_name_len: y+2]

print 'actor : ',Actor



type_len = len('type="')
i=0

#Adjacency list in Adj

for gg in s:
    #Simple association
    if(gg.startswith('<UML:Association.connection>')):
        p=0
        q=0
        #finding first node id
        line = s[i+1]
        start_first = line.find('type')
        length = len(line)
        p=start_first+type_len
        while(p<length):
            if(line[p] is ' '):
                break
            p+=1

        #finding second node of association
        line2 = s[i+2]
        start_second = line2.find('type')
        length = len(line2)
        q = start_second +type_len
        while(q<length):
            if(line2[q] is ' '):
                break
            q+=1
        #making adjacency list for undirected graph
        if(line[start_first+type_len:p-1] in Adj):
            Adj[line[start_first+type_len:p-1]].append(line2[start_second+type_len:q-1])
        else:
            Adj[line[start_first+type_len:p-1]]=[line2[start_second+type_len:q-1]]

        if(line2[start_second+type_len:q-1] in Adj):
            Adj[line2[start_second+type_len:q-1]].append(line[start_first+type_len:p-1])
        else:
            Adj[line2[start_second+type_len:q-1]]=[line[start_first+type_len:p-1]]

    #For dependency
    elif(gg.startswith('<UML:Dependency')):
        p=0
        q=0
        #finding client of dependency
        line = s[i]
        start_first = line.find('client')
        length = len(line)
        client_len = len('client="')
        p=start_first+client_len
        while(p<length):
            if(line[p] is ' '):
                break
            p+=1
        #finding finding supplier of dependency
        start_second = line.find('supplier')
        supplier_len = len('supplier="')
        q = start_second +supplier_len
        while(q<length):
            if(line[q] is ' '):
                break
            q+=1
        #for dependency only adding edge from client to supplier hence making only one entry in adjacency list i.e in client adjacency list
        if(line[start_first+client_len:p-1] in Adj):
            Adj[line[start_first+client_len:p-1]].append(line[start_second+supplier_len:q-1])
        else:
            Adj[line[start_first+client_len:p-1]]=[line[start_second+supplier_len:q-1]]
    i+=1
print ""
print "*************************************"
print 'Adjacency list: ',Adj
print "*************************************"

disp.print_dict(Actor)

print Adj
graphmlgen.generate_graphml(Adj, Actor, UseCase);
