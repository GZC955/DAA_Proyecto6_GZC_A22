from Random_Graphs import *
import random

def run():

    print("-------Grafo Original--------")
    g = randomDoroMendes(50,False,False,'Doro50')
    g.addRandomWeights(1,100)
    g.toGVWeights()
    #g.printEdges()
    print("")  

    print("######### PRIM ##############")
    gPMST = g.Prim()
    #gPMST.printEdges()
    gPMST.toGVWeights() 

    print("######### KIMST #############")
    gKIMST = g.KruskalI()
    #gKIMST.printEdges()
    gKIMST.toGVWeights()

    print("######### KDMST #############")
    gKDMST = g.KruskalD()
    #gKDMST.printEdges()
    gKDMST.toGVWeights()

    
    
    
if __name__ == '__main__':
    run()
