import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

#draw heatmap
def draw(G, pos, measures, measure_name = ''):
    
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma, 
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
    
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()

#define heatmap plot
def heatmap(Graph, cent):
    plt.figure(figsize=(12,12))
    pos = nx.spring_layout(Graph)
    draw(Graph, pos, cent)

#histogram plot
def histogram(cent):
    sns.set_style("darkgrid")
    sns.displot(list(cent.values()),stat='density',kde=True)
    # plt.xlim(0, 0.23)

#make degree centrality
def make_dc(Graph):
    dc = nx.degree_centrality(Graph)
    sorted_dc= sorted(dc.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Degree Centrality per le interazioni:")
    for node, centrality in sorted_dc:
        print(f"{node} : {centrality}")

    histogram(dc)
    heatmap(Graph, dc)

    
#make closeness centrality
def make_cc(Graph):
    cc = nx.closeness_centrality(Graph)
    sorted_cc= sorted(cc.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Closeness Centrality per le interazioni:")
    for node, centrality in sorted_cc:
        print(f"{node} : {centrality}")

    histogram(cc)
    heatmap(Graph, cc)


#make betweenness centrality
def make_bc(Graph):
    bc = nx.betweenness_centrality(Graph)
    sorted_bc= sorted(bc.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Betwenness Centrality per le interazioni:")
    for node, centrality in sorted_bc:
        print(f"{node} : {centrality}")

    histogram(bc)
    heatmap(Graph, bc)


#make eigenvector centrality
def make_ec(Graph):
    ec = nx.eigenvector_centrality(Graph)
    sorted_ec= sorted(ec.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Betwenness Centrality per le interazioni:")
    for node, centrality in sorted_ec:
        print(f"{node} : {centrality}")

    histogram(ec)
    heatmap(Graph, ec)