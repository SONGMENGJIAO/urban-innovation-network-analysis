"""
Centrality Analysis and Statistical Modeling
Author: Mengjiao Song
Description: Analyze network centrality effects on industrial resilience
"""

import pandas as pd
import statsmodels.api as sm
from scipy import stats

def merge_centrality_with_outcomes(centrality_df, outcome_df):
    """
    Merge network centrality data with economic outcome data
    for regression analysis
    """
    merged = pd.merge(centrality_df, outcome_df, on='city_id', how='inner')
    return merged

def run_spatial_regression(data, dependent_var, independent_vars):
    """
    Run spatial econometric model (simplified version)
    In actual research, used Stata for spatial lag models
    """
    X = data[independent_vars]
    y = data[dependent_var]
    X = sm.add_constant(X)
    
    model = sm.OLS(y, X).fit()
    return model.summary()

def identify_key_hubs(centrality_dict, threshold=0.8):
    """
    Identify network hubs based on centrality threshold
    """
    max_cent = max(centrality_dict.values())
    hubs = {k: v for k, v in centrality_dict.items() 
            if v >= threshold * max_cent}
    return hubs
