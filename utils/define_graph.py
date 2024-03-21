#imports and load datas

import json
import networkx as nx
import matplotlib.pyplot as plt


def create_graphs(paths = ['../db/starwars-full-interactions.json',
        '../db/starwars-full-mentions.json']):

    #load data
    for path in paths:
        with open(path, 'r') as f:
            if 'interactions' in path:
                full_interactions = json.load(f)
            else:
                full_mentions = json.load(f)

    #initialize graphs
    G_interactions = nx.Graph()
    G_mentions = nx.Graph()

    #add nodes
    for node in full_interactions['nodes']:
        G_interactions.add_node(node['name'], value=node['value'], colour=node['colour'])

    for node in full_mentions['nodes']:
        G_mentions.add_node(node['name'], value=node['value'], colour=node['colour'])


    #add links
    for link in full_interactions['links']:
        G_interactions.add_edge(full_interactions['nodes'][link['source']]['name'],
                                full_interactions['nodes'][link['target']]['name'],
                                weight=link['value'])

    for link in full_mentions['links']:
        G_mentions.add_edge(full_mentions['nodes'][link['source']]['name'],
                            full_mentions['nodes'][link['target']]['name'],
                            weight=link['value'])
        
    #check if connected
    if not nx.is_connected(G_interactions):
        S = [G_interactions.subgraph(c).copy() for c in nx.connected_components(G_interactions)]
        G_interactions = S[0]
    if not nx.is_connected(G_mentions):
        S = [G_mentions.subgraph(c).copy() for c in nx.connected_components(G_mentions)]
        G_mentions = S[0]   


    return G_interactions, G_mentions