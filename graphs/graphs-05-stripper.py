#r: networkx
#r: matplotlib

from typing import cast, Any
import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore
import Rhino.Geometry as rg # type: ignore beaause using stubs

import graph_helpers as graph 


# DECLARE INPUT VARIABLES OF PYTHON COMPONENT
m = cast(rg.Mesh, m)  # type: ignore



strips=[]
allindexes=[]
slen=[]

G, dv, de = graph.DualGraphFromMesh(m)



while len(G.nodes) > 0 :

    startpoint = graph.getStartPoint(G)

    #upack list into four variables
    pathPoints, pathIndexes,  pathLen, pathNodes = graph.AllShortestPaths(G, startpoint)

    strips.extend(pathPoints)
    allindexes.extend(pathIndexes)
    slen.append(pathLen)

    G.remove_nodes_from(pathNodes)


a= strips
b = allindexes
c = slen
