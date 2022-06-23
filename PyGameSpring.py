from Random_Graphs import *
import pygame
import sys
import time

def run():
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    Grid = False

    g = randomErdos(100,150,True,False,'Erdos100')
    #g = randomErdos(500,750,True,False,'Erdos500')

    #g = randomGilbert(100,0.05,True,False,'Gilbert100')
    #g = randomGilbert(500,0.01,True,False,'Gilbert500')

    #g = randomGeo(100,0.1,True,False,'Geo100')
    #g = randomGeo(500,0.05,True,False,'Geo500')

    #g = randomGrid(10,10,False,True,False,'Grid100')
    #g = randomGrid(25,20,False,True,False,'Grid500')

    #g = randomDoroMendes(100,True,False,'Doro100')
    #g = randomDoroMendes(500,True,False,'Doro500')

    # Attraction force (gamma) constants
    c1 = 250
    #c1 = 30 # Use this constant for Grid Graphs
    c2 = 0.4
    # Repulsive force constant
    c3 = 3000
    #c3 = 3000

    # Getting or adding nodes coordinates
    for n in g.nodes.keys():
        if g.getNode(n).coordinate[0] == 0 and  g.getNode(n).coordinate[1] == 0:
            g.getNode(n).coordinate[0] = random.random()*500
            g.getNode(n).coordinate[1] = random.random()*500
        else:
            g.getNode(n).coordinate[0] = float(g.getNode(n).coordinate[0])*50 + 200 # x factor
            g.getNode(n).coordinate[1] = float(g.getNode(n).coordinate[1])*50 + 200# y factor (Erase the 200 for Grid Graphs)

    def draw():
        
        nodes = list(g.nodes.keys())
        edges = list(g.edges.keys())

        for nodeName in nodes: 
            node = g.getNode(nodeName)
            x = node.coordinate[0]
            y = node.coordinate[1]
            A = np.array([x,y])
            N = node.neighbors
            s = np.zeros(2)

            # Neighbors atraction force calculation
            for n0name in N:
                n0 = n0name
                x0 = n0.coordinate[0]
                y0 = n0.coordinate[1]
                d = dist(node,n0)
                gamma = c2*math.log(d / c1)
                B = np.array([x0,y0])
                name =  nodeName + '->' + n0name.id
                if name not in g.edges.keys():
                   v = B - A
                else: 
                   v = A - B
                norm = np.linalg.norm(v)
                v = v / norm
                v = gamma*v
                s += v

            # Not neighbors repulsive force calculation
            for n in nodes:
                if g.getNode not in N:
                    n0 = g.getNode(n)
                    if n != n0.id:
                        x0 = n0.coordinate[0]
                        y0 = n0.coordinate[1]
                        d = dist(node,n0)
                        repforce = c3/(math.sqrt(d))
                        B = np.array([x0,y0])
                        name =  nodeName + '->' + n0name.id
                        if name not in g.edges.keys():
                            v = B - A
                        else: 
                            v = A - B
                        norm = np.linalg.norm(v)
                        v = v / norm
                        v = repforce*v
                        s += v
            
            # Calculated coordinates
            A += s
            nx = A[0]
            ny = A[1]
            node.gamex = nx  
            node.gamey = ny

        for n in nodes:
            node = g.getNode(n)
            node.coordinate[0] = node.gamex
            node.coordinate[1] = node.gamey

        for e in edges:
            edge = g.edges[e]
            node0 = edge.n0
            node1 = edge.n1
            x1 = node0.coordinate[0]
            y1 = node0.coordinate[1]
            x2 = node1.coordinate[0]
            y2 = node1.coordinate[1]

            d = dist(node0,node1)

            # Nodes and edges drawing
            pygame.draw.circle(screen,'yellow',(int(x1),int(y1)),2)
            pygame.draw.circle(screen,'yellow',(int(x2),int(y2)),2)
            pygame.draw.line(screen, 'white', (int(x1), int(y1)), (int(x2), int(y2)), 1)
        
        return g.name

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        draw()

        font = pygame.font.SysFont('Arial',30)
        title = font.render(g.name,0,(200,60,80))
        screen.blit(title,(0,0))

        pygame.display.update()
        screen.fill('black')


if __name__ == '__main__':
    run()