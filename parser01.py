#!/usr/bin/python

f = open('/home/sujit/Downloads/thermoclass(1).xmi','r');

s=[]
t=[]
UseCase = {}
Actor = {}

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


print 'usecase :', UseCase

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
