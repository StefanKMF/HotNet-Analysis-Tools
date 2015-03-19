import json
from Tkinter import Tk
from tkFileDialog import askopenfilename
from pprint import pprint


Tk().withdraw()
resultsOne = askopenfilename(title="First Result File to compare",defaultextension=".json")
resultsTwo = askopenfilename(title="Second Result File to compare",defaultextension=".json")

if resultsOne == resultsTwo:
    print "Error, files identical"


json_data=open('subnetworks.json')

data = json.load(json_data)
SubgraphCounter = 0;
nonMalig = {}

for row in data['subnetworks']:
    #print row, len(data['subnetworks'][row])
    for x in xrange(len(data['subnetworks'][row])):
        #print len(data['subnetworks'][row][x])
        for y in data['subnetworks'][row][x]:
            if y =='nodes':
                substring = []
                for z in data['subnetworks'][row][x][y]:
                    substring.append(str(z['name']))
                nonMalig[str(row)] = substring
                #("Subgraph_" + str(SubgraphCounter)) = Subgraph('Test',substring)
                #SubgraphCounter += 1

json_data.close()
print nonMalig


class Subgraph():

    def __init__(self,name,nodes):
        self.name_ = name
        self.nodes_ = nodes

    def nodes(self):
        return nodes_

    def name(self):
        return name
