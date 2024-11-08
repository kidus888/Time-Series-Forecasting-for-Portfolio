
import numpy as np

def calculate_var(df, confidence=0.05):
    """Calculate Value at Risk (VaR) at the specified confidence level."""
    return np.percentile(df['Daily Return'].dropna(), confidence * 100)

def calculate_sharpe_ratio(df, risk_free_rate=0.01):
    """Calculate the Sharpe Ratio."""
    return (df['Daily Return'].mean() - risk_free_rate) / df['Daily Return'].std()
