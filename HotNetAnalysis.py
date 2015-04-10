#Currently works by comparing the gene sets, doesn't compare the graphes as of yet. Graph comparsion will be a future addition.

import json, difflib
from Tkinter import Tk
from tkFileDialog import askopenfilename
from pprint import pprint

File1 = ""


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

def findSubnetworksByGene(Genes, SubNetworks ): #Takes in a Gene name and a Subnetwork Dictionary, returns all subnetworks containing the gene.
    inSubNetworks = {}

    for x in SubNetworks:
        if isinstance(Genes, str): #Check if single Gene is and subnetwork and return Subnetwork if True.
            if Genes in SubNetworks[x]:
                inSubNetworks[x] = SubNetworks[x]
        elif isinstance(Genes, list): #Check if all Genes are in subnetwork and return Subnetwork if True.
            if all(gene in SubNetworks[x] for gene in Genes):
                inSubNetworks[x] = SubNetworks[x]

    return inSubNetworks


def percentSimilarity(Subnetwork1,Subnetwork2): #Returns the percent similarity between two subnetworks.
    sm = diffib.SequenceMatcher(None, Subnetwork1,Subnetwork2)
    return sm.ratio()

def setdiff(Alpha, Beta, tolerance = 1.0): #Takes two Dict containg subnetworks and returns the exclusive subnetworks in Alpha.
    exclusiveNetworks = {}

    for x in Alpha:
        isExclusive = True
        for y in Beta:
            if (percentSimilarity(sorted(Alpha[x]),sorted(Beta[y])) >= tolerance):
                isExclusive = False
        if isExclusive == True:
            exclusiveNetworks[x] = Alpha[x]

    return exclusiveNetworks

def returnSymbol(Genes): #Takes in a list of Genes, returning a + or - value depending on if the Gene experience in increase or decrease of methylation levels.
    return NULL

def startMenu():
    input = 0
    while input != '4':
        print "1. Select a JSON File" + "\n" +"2. Select a 2nd JSON File" + "\n" + "3. Search for a Gene(s)" + "\n" + "4. Exit"
        input = raw_input("")
        if input == '3':
            temp = raw_input("Enter a List of Genes to Search" + "\n")
            #genes = map(str, temp.split())
            genes = 'MLC1'
            #print genes
            subnetworks = findSubnetworksByGene(genes, File1)
            for x in subnetworks:
                print subnetworks[x]


def main():



    Tk().withdraw()
    global File1
    File1 = askopenfilename(title="First JSON File.",defaultextension=".json")
    #File2 = askopenfilename(title="Second Result File to compare.",defaultextension=".json")

    Alpha = getSubnetworks(File1)
    #Beta = getSubnetworks(File2)

    startMenu()

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
