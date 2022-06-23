from Random_Graphs import *
import random

def run():

    print("############ Grafo Original #############")
    g = randomDoroMendes(10,False,False,"DoroTest")
    g.addRandomWeights(1,100)
    g.toGVWeights()

    print("############ Kruskal #############")
    gKIMST = g.KruskalI()
    gKIMST.toGVWeights()


    '''
    a = set(['c','b','b','a'])
    print('a: ' + str(a))
    b = set(['a','b','c','c'])
    print('b: ' + str(b))
    print('Iguales: ')
    print(a == b)
    '''    

    

    

    

if __name__ == '__main__':
    run()
