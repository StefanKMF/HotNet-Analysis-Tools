# HotNet Analysis Tools

#HOW TO USE
1. Navigate to the directory that the HotNetAnalysis.py is located to in the terminal.
2. Run "python HotNetAnalysis.py" in terminal.
3. Select the JSON file you wish to search in.
4. Select the options from the interface
5. To search for a gene(s) simply type the gene name (case sensitive) followed by a space then the next gene and so forth. 
E.X to search for subnetworks containing CACNA1B & CACNB3 type (without quotes) "CACNA1B CACNB3". Gene order does not matter.

#EXAMPLE USE
Sample results from searching for genes "CCL8 CCL13". In the example case the Blue nodes are nodes that have experienced an decrease in average methylation levels and the Red an increase in average methylation.
##Figure 1
![Figure 1](http://i.imgur.com/pebcmVC.png)
##Figure 2
![Figure 2](http://i.imgur.com/LB1L29v.png)



#DEPENDENCIES
 * Pythion 2.7
 * NetworkX 1.9.1
 * Matplotlib 1.4.3
