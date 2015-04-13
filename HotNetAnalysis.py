#Currently works by comparing the gene sets, doesn't compare the graphes as of yet. Graph comparsion will be a future addition.

import json, difflib, csv
import scipy.io as sio
import networkx as nx
import matplotlib.pyplot as plt
from Tkinter import Tk
from tkFileDialog import askopenfilename
from pprint import pprint

File1 = ""
legend = {}


def getSubnetworks(filename): #Takes in a file and returns a Dict containinng all the subnetworks in the JSON file.
    json_data = open(filename)
    data = json.load(json_data)
    Networks = {}
    Edges = {}
    SubNetworkCounter = 0
    EdgeCounter = 0


    for row in data['subnetworks']:
        for x in xrange(len(data['subnetworks'][row])):
            for y in data['subnetworks'][row][x]:
                if y =='nodes':
                    substring = []
                    edges = []
                    for z in data['subnetworks'][row][x][y]:
                        substring.append(str(z['name']))
                    for z in data['subnetworks'][row][x]['edges']:
                        edges.append((str(z['source']),str(z['target'])))

                    tupleA = substring
                    Networks[('Subnetwork' + str(SubNetworkCounter))] = (substring, edges)
                    SubNetworkCounter += 1
    json_data.close()

    return Networks

def findSubnetworksByGene(Genes, SubNetworks ): #Takes in a Gene name and a Subnetwork Dictionary, returns all subnetworks containing the gene.
    inSubNetworks = {}
    #print "FINDING"
    #print type(Genes)
    #(nodes, edges) = SubNetworks

    for x in SubNetworks:
        #print x
        #(nodes,edges) = x

        (nodes,edges) = SubNetworks[x]
        #print nodes

        if isinstance(Genes, str): #Check if single Gene is and subnetwork and return Subnetwork if True.
            if Genes in nodes:
                #print "FOUND"
                inSubNetworks[x] = SubNetworks[x]
        elif isinstance(Genes, list): #Check if all Genes are in subnetwork and return Subnetwork if True.
            if all(gene in nodes for gene in Genes):
                #print "FOUND"
                inSubNetworks[x] = SubNetworks[x]

    #print inSubNetworks
    if not inSubNetworks:
        print "No Results Found" + "\n"

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
    while input != '2':
        print "\n"  + "1. Search for a Gene(s)" + "\n" + "2. Exit" + "\n"
        input = raw_input("")
        if input == '1':
            temp = raw_input("Enter a List of Genes to Search" + "\n" + "\n")
            genes = map(str, temp.split())
            #print genes
            subnetworks = getSubnetworks(File1)
            #print subnetworks
            results = findSubnetworksByGene(genes, subnetworks)
            for x in results:
                #print x
                showGraph(results[x])



def showGraph(subnetwork):
    plt.figure()
    G = nx.Graph()
    (nodes, edges) = subnetwork

    G.add_edges_from(edges)
    G.add_nodes_from(nodes)

    for node in G.nodes():
        G.node[node]['category'] = legend[' ' + node + ' ']

    color_map = {'+':'#ff0000','-':'b', '0':'#C0C0C0'}
    pos = nx.spring_layout(G, k=0.10, iterations=20)

    nx.draw(G,pos=pos,node_size=2000,node_color=[color_map[G.node[node]['category']] for node in G])
    nx.draw_networkx_labels(G,pos=pos,font_size=10,font_family='sans-serif',font_color="w")

    plt.show()


def main():

    #print legend
    global legend
    with open('Legend.csv',mode='r') as infile:
        reader = csv.reader(infile)
        legend = {rows[0]:rows[1] for rows in reader}


    Tk().withdraw()
    global File1
    File1 = askopenfilename(title="First JSON File.",defaultextension=".json")

    Alpha = getSubnetworks(File1)

    #x = 'Subnetwork450'
    #showGraph(Alpha['Subnetwork450'])

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
