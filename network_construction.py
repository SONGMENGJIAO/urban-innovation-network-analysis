"""
Network Construction for Urban Innovation Analysis
Author: Mengjiao Song
Date: 2024
Description: Build patent co-application networks from city-level data
"""

import networkx as nx
import pandas as pd
import numpy as np

def build_city_network(data_path):
    """
    Construct temporal network from patent co-application data
    Input: CSV file with columns [city_A, city_B, year, patent_count]
    Output: NetworkX Graph object
    """
    # 读取数据
    df = pd.read_csv(data_path)
    
    # 创建空图
    G = nx.Graph()
    
    # 添加边（城市之间的专利合作）
    for _, row in df.iterrows():
        city_a = row['city_A']
        city_b = row['city_B']
        weight = row['patent_count']
        year = row['year']
        
        # 添加带权重的边
        if G.has_edge(city_a, city_b):
            G[city_a][city_b]['weight'] += weight
        else:
            G.add_edge(city_a, city_b, weight=weight, year=year)
    
    return G

def calculate_centrality_metrics(G):
    """
    Calculate multiple centrality measures for network analysis
    """
    metrics = {
        'degree': nx.degree_centrality(G),
        'betweenness': nx.betweenness_centrality(G, weight='weight'),
        'eigenvector': nx.eigenvector_centrality(G, weight='weight', max_iter=1000)
    }
    return metrics

# 示例用法（实际使用时替换为真实数据路径）
if __name__ == "__main__":
    # 示例：创建一个小型测试网络
    G_test = nx.karate_club_graph()
    metrics = calculate_centrality_metrics(G_test)
    print(f"Network has {G_test.number_of_nodes()} nodes and {G_test.number_of_edges()} edges")
    print("Top 3 nodes by degree centrality:", 
          sorted(metrics['degree'].items(), key=lambda x: x[1], reverse=True)[:3])
