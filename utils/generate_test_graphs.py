from structure import BokehStructureGraph
import json
from bokeh.plotting import figure
import networkx as nx


F=figure()
F.line(x=[1,2,3],y=[1,2,3])
K = BokehStructureGraph(F)
with open('graph_data.txt','w') as f:
    f.write(json.dumps(nx.node_link_data(K.graph)))
KK = BokehStructureGraph(K.model)
with open('graph_data_2.txt','w') as f:
    f.write(json.dumps(nx.node_link_data(KK.graph)))

