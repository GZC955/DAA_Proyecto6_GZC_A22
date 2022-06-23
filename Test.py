from Random_Graphs import *
import random

def run():

    '''
    g = Graph(False,False,"Test_DAA_Rene")
    g.addEdge('0 -> 1', '0', '1', 2)
    g.addEdge('1 -> 0', '1', '0', 2)
    g.addEdge('0 -> 5', '0', '5', 3)
    g.addEdge('5 -> 0', '5', '0', 3)
    g.addEdge('1 -> 2', '1', '2', 2)
    g.addEdge('2 -> 1', '2', '1', 2)
    g.addEdge('1 -> 3', '1', '3', 1)
    g.addEdge('3 -> 1', '3', '1', 1)
    g.addEdge('1 -> 4', '1', '4', 4)
    g.addEdge('4 -> 1', '4', '1', 4)
    g.addEdge('2 -> 3', '2', '3', 1)
    g.addEdge('3 -> 2', '3', '2', 1)
    g.addEdge('2 -> 6', '2', '6', 2)
    g.addEdge('6 -> 2', '6', '2', 2)
    g.addEdge('6 -> 5', '6', '5', 2)
    g.addEdge('5 -> 6', '5', '6', 2)
    g.addEdge('6 -> 3', '6', '3', 1)
    g.addEdge('3 -> 6', '3', '6', 1)
    g.addEdge('6 -> 4', '6', '4', 4)
    g.addEdge('4 -> 6', '4', '6', 4)
    g.addEdge('4 -> 3', '4', '3', 3)
    g.addEdge('3 -> 4', '3', '4', 3)
    '''
    
    
    # g = randomBarabasi(30,3,False,False,"Test_Barabasi")
    # g.addRandomWeights(5,100)
    


    
    #Grafo Profe rollando
    g = Graph(False,False,"DAA_Test")
    g.addEdge("0 -> 1","0","1",4)
    g.addEdge("0 -> 5","0","5",6)
    g.addEdge("0 -> 6","0","6",16)
    g.addEdge("1 -> 2","1","2",24)
    g.addEdge("5 -> 2","5","2",23)
    g.addEdge("5 -> 6","5","6",8)
    g.addEdge("5 -> 4","5","4",5)
    g.addEdge("6 -> 4","6","4",10)
    g.addEdge("6 -> 7","6","7",21)
    g.addEdge("4 -> 3","4","3",11)
    g.addEdge("4 -> 7","4","7",14)
    g.addEdge("2 -> 4","2","4",18)
    #g.addEdge("2 -> 7","2","7",19)
    g.addEdge("3 -> 2","3","2",9)
    g.addEdge("3 -> 7","3","7",7)

    #INVERTIDAS
    g.addEdge('1 -> 0','1','0',4)
    g.addEdge('5 -> 0','5','0',6)
    g.addEdge('6 -> 0','6','0',16)
    g.addEdge('2 -> 1','2','1',24)
    g.addEdge('2 -> 5','2','5',23)
    g.addEdge('6 -> 5','6','5',8)
    g.addEdge('4 -> 5','4','5',5)
    g.addEdge('4 -> 6','4','6',10)
    g.addEdge('7 -> 6','7','6',21)
    g.addEdge('3 -> 4','3','4',11)
    g.addEdge('7 -> 4','7','4',14)
    g.addEdge('4 -> 2','4','2',18)
    #g.addEdge('7 -> 2','7','2',19)
    g.addEdge('2 -> 3','2','3',9)
    g.addEdge('7 -> 3','7','3',7)   
        


    print("-------Grafo Original--------")
    g.printEdges()
    g.toGVWeights()
    print("")


    print("######### KIMST #############")
    gKIMST = g.KruskalI()
    gKIMST.toGVWeights()



    '''
    print("######### KIMST #############")
    gKIMST = g.KruskalI()
    gKIMST.printEdges()
    gKIMST.toGVWeights()
    
    print("######### KDMST #############")
    gKDMST = g.KruskalD()
    gKDMST.printEdges()
    gKDMST.toGVWeights()

    print("######### PRIM ##############")
    gPMST = g.Prim()
    gPMST.toGVWeights()
    '''
    

if __name__ == '__main__':
    run()
