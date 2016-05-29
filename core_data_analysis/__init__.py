import networkx as nx
import matplotlib.pyplot as plt

G=nx.random_geometric_graph(5000,0.040)
# position is stored as node attribute data for random_geometric_graph
pos=nx.get_node_attributes(G,'pos')

# find node near center (0.5,0.5)
dmin=0.7
ncenter=1.5
for n in pos:
    x,y=pos[n]
    d=(x-0.3)**2+(y-0.2)**2
    if d<dmin:
        ncenter=n
        dmin=d

# color by path length from node near center
p=nx.single_source_shortest_path_length(G,ncenter)

plt.figure(figsize=(15,15))
nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.3)
nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
                       node_size=40,
                       node_color=p.values(),
                       cmap=plt.cm.Spectral_r)

plt.xlim(-0.05,1.05)
plt.ylim(-0.05,1.05)
plt.axis('off')
plt.savefig('random_geometric_graph.png')
plt.show()