# Urban Innovation Network Analysis

Network analysis of urban innovation systems using Python and NetworkX. 
This repository contains tools developed for my master's thesis research 
analyzing patent co-application networks across 282 Chinese cities (2011-2023).

## Research Context

This project investigates how urban innovation networks affect industrial 
chain resilience through spatial spillover effects. The work bridges 
economics and computer science, applying network science methods to 
economic geography questions.

**Key Finding**: Network centrality exerts heterogeneous impacts on 
industrial chain resilience—degree centrality promotes resilience while 
betweenness centrality shows inhibitory effects.

## Repository Structure

- `network_construction.py` - Build temporal networks from patent data
- `centrality_analysis.py` - Calculate network metrics (degree, betweenness, eigenvector)
- `spatial_visualization.py` - Geographic visualization and ArcGIS integration

## Technical Stack

- **Language**: Python 3.8+
- **Core Libraries**: 
  - NetworkX (complex network analysis)
  - pandas (data manipulation)
  - NumPy (numerical computing)
  - matplotlib (visualization)
  - statsmodels (statistical modeling)
- **GIS Tools**: ArcGIS (spatial analysis)

## Data Scale

- **282 Chinese cities** (2011-2023)
- **50,000+ patent co-application records**
- **Temporal network construction** with yearly snapshots

## Usage Example

```python
from network_construction import build_city_network, calculate_centrality_metrics

# Load your data
G = build_city_network('data/patent_coapplications.csv')

# Calculate metrics
metrics = calculate_centrality_metrics(G)

# Analyze results
print(f"Network density: {nx.density(G)}")
print(f"Average clustering: {nx.average_clustering(G)}")

## Research Output

- **Conference**: 8th Annual Conference on Energy and Resource Systems 
  Engineering (Wuhan, Nov 2024) - Excellent Paper Award
- **Thesis**: "Spatial Spillover Effects of Urban Technological Innovation 
  Networks on Industrial Chain Resilience" (Expected June 2026)

## Author

**Mengjiao Song**  
Master's Candidate in Economics, Xinjiang University  
Email: 17863778569@163.com  
Research Interests: Network Science, Data Mining, Computational Social Science

## License

MIT License - See LICENSE file for details

## Quick Start

```bash
# Clone the repository
git clone https://github.com/SONGMENGJIAO/urban-innovation-network-analysis.git

# Install dependencies
pip install networkx pandas numpy matplotlib

# Run example
python network_construction.py
