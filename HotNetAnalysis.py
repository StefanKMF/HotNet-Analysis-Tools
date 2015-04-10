#Currently works by comparing the gene sets, doesn't compare the graphes as of yet. Graph comparsion will be a future addition.



import json
from Tkinter import Tk
from tkFileDialog import askopenfilename
from pprint import pprint



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

def findSubnetworkByGene(Gene, SubNetworks ): #Takes in a Gene name and a Subnetwork Dictionary, returns all subnetworks containing the gene.
    inSubNetworks = {}

    for x in SubNetworks:
        if Gene in SubNetworks[x]:
            inSubNetworks[x] = SubNetworks[x]

    return inSubNetworks


def setdiff(Alpha, Beta): #Takes two Dict containg subnetworks and returns the exclusive subnetworks in Alpha.
    exclusiveNetworks = {}

    for x in Alpha:
        isExclusive = 1
        for y in Beta:
            if sorted(Alpha[x]) == sorted(Beta[y]):
                isExclusive = 0
        if isExclusive == 1:
            exclusiveNetworks[x] = Alpha[x]

    return exclusiveNetworks


def main():
    Tk().withdraw()
    File1 = askopenfilename(title="First Result File to compare",defaultextension=".json")
    File2 = askopenfilename(title="First Result File to compare",defaultextension=".json")

    Alpha = getSubnetworks(File1)
    Beta = getSubnetworks(File2)

    Alpha['unique'] = 'NOT IN THE SET'
    Exc1 = setdiff(Alpha,Beta)


    print len(Exc1)
    print Exc1

if __name__ == '__main__':
    main()




class Subgraph():

    def __init__(self,name,nodes):
        self.name_ = name
        self.nodes_ = nodes

    def nodes(self):
        return nodes_

    def name(self):
        return name
