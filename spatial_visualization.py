"""
Spatial Visualization Tools
Author: Mengjiao Song
Description: Integrate network analysis with geographic visualization
"""

import matplotlib.pyplot as plt
import networkx as nx

def plot_network_with_metrics(G, centrality_metric, title):
    """
    Create network visualization with node size based on centrality
    """
    plt.figure(figsize=(12, 8))
    
    # 节点大小根据中心性调整
    node_sizes = [v * 1000 for v in centrality_metric.values()]
    
    # 绘制网络
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, 
            node_size=node_sizes,
            node_color=list(centrality_metric.values()),
            cmap=plt.cm.viridis,
            with_labels=True,
            font_size=8,
            edge_color='gray',
            alpha=0.7)
    
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.viridis), 
                 label='Centrality Score')
    plt.title(title)
    plt.tight_layout()
    return plt

def export_for_arcgis(node_data, edge_data, output_path):
    """
    Export network data for ArcGIS visualization
    """
    # 节点数据
    node_data.to_csv(f"{output_path}/nodes_for_arcgis.csv", index=False)
    # 边数据  
    edge_data.to_csv(f"{output_path}/edges_for_arcgis.csv", index=False)
    print(f"Data exported to {output_path} for ArcGIS mapping")
