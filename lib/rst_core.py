import numpy as np
from scipy.linalg import eigvalsh

class RSTEngine:
    """
    RST v6.1 Core Engineering Module.
    Calculates topological stability and predicted latency.
    """
    def __init__(self, adjacency_matrix, friction_coeff=0.9):
        self.A = adjacency_matrix
        self.zeta = friction_coeff
        self.N = adjacency_matrix.shape[0]

    def calculate_metrics(self):
        # Calculate Laplacian L = D - A
        D = np.diag(np.sum(self.A, axis=1))
        L = D - self.A
        
        # Extract Lambda_2
        eigenvalues = eigvalsh(L)
        lambda_2 = eigenvalues[1]
        
        # Calculate Predicted Bottleneck (τ)
        # Using the RST Limit Formula
        latency = (self.zeta * np.log(self.N)) / (lambda_2 + 1e-9)
        
        return {
            "lambda_2": lambda_2,
            "latency_sec": min(latency, 6.18), # Caps at the physical bottleneck
            "state": "STABLE" if lambda_2 > 1.0 else "CRITICAL"
        }
