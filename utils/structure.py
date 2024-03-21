import networkx as nx
import matplotlib.pyplot as plt

def find_best_triads(triads, graph):
    triad_weights = {}

    for triad in triads:
        weight = 0
        # print(triad)
        data = graph.nodes(data=True)
        weight += data[triad[0]]['value']
        weight += data[triad[1]]['value']
        weight += data[triad[2]]['value']
        triad = tuple(triad)
        triad_weights[triad] = weight
    #sort triads by weight
    triad_sorted = sorted(triad_weights.items(), key=lambda x: x[1], reverse=True)

    #take first ten values
    first_ten = triad_sorted[:10]

    for k, v in first_ten:
        print(f"{k} : {v}")


#find cliques
def find_cliques(graph):
    cliques=nx.find_cliques(graph)
    count = 0
    max = 0
    for clique in cliques:
        count +=1
        if len(clique) > max:
            max = len(clique)
    print(f'Totale Clique: {count}, max length: {max}')
    return max


#plot max clique
def plot_max_clique(graph, max_clique):
    max_clique_g = graph.subgraph(max_clique[0])

    plt.figure(figsize = (12,12))
    pos = nx.spring_layout(max_clique_g)
    nx.draw(max_clique_g, pos, node_color=[max_clique_g.nodes(data=True)[n]['colour'] for n in max_clique_g.nodes])
    nx.draw_networkx_labels(max_clique_g, pos,font_size=12, font_color="black")

    plt.show()

#find main k_core and print
def make_k_core(graph):
    main_k_core = nx.k_core(graph)
    print('Nodi nel main k-core:', main_k_core.nodes(), len(main_k_core), main_k_core.degree)

    # Visualizzazione del main k-core
    plt.figure(figsize=(12,12))
    nx.draw(main_k_core, node_color=[main_k_core.nodes(data=True)[n]['colour'] for n in main_k_core.nodes],
             with_labels=True)
    plt.show()


#find and plot egos
def make_ego(graph, roles = ['OBI-WAN', 'ANAKIN']):
    for role in roles:
        ego = nx.ego_graph(graph, role, radius=1)
        plt.figure(figsize=(25,20))
        d = dict(ego.degree)
        nx.draw(ego, with_labels=True,node_color=[ego.nodes(data=True)[n]['colour'] for n in ego.nodes],
                 node_size=[v * 180 for v in d.values()])
        plt.show()