import json
from Tkinter import Tk
from tkFileDialog import askopenfilename
from pprint import pprint


Tk().withdraw()
resultsOne = askopenfilename(title="First Result File to compare",defaultextension=".json")
#resultsTwo = askopenfilename(title="Second Result File to compare",defaultextension=".json")

#if resultsOne == resultsTwo:
#    print "Error, files identical"

def getSubnetworks(filename): #Takes in a file and returns a Dict containinng all the subnetworks in the JSON file.
    json_data = open(filename)
    data = json.load(json_data)
    Networks = {}
    SubNetworkCounter = 0


    for row in data['subnetworks']:
        for x in xrange(len(data['subnetworks'][row])):
            for y in data['subnetworks'][row][x]:
                if y =='nodes':
                    substring = []
                    for z in data['subnetworks'][row][x][y]:
                        substring.append(str(z['name']))
                    Networks[('Subnetwork' + str(SubNetworkCounter))] = substring
                    SubNetworkCounter += 1

    json_data.close()

    return Networks


class Subgraph():

    def __init__(self,name,nodes):
        self.name_ = name
        self.nodes_ = nodes

    def nodes(self):
        return nodes_

    def name(self):
        return name
