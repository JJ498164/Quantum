# RST v6.1: Spectral Engineering for Neural Topology

## Overview
RST v6.1 is a mathematical framework for analyzing and mitigating information bottlenecks in damaged neural graphs. It utilizes **Spectral Graph Theory** to quantify the relationship between structural connectivity ($\lambda_2$) and the temporal limits of state transitions.

## Key Mathematical Constants
* **$\tau_{limit}$ (6.18s):** The critical relaxation time of a human-scale neural graph as $\lambda_2 \to 0.1$.
* **$f_{res}$ (39 Hz):** The resonance frequency that minimizes Effective Resistance ($R_{eff}$) in the Fiedler Vector.

## Repository Structure
- `/lib`: Core Python implementations using NumPy and NetworkX.
- `/docs`: Analytical derivations and proofs.
- `/benchmarks`: Performance comparisons against GNW and IIT models.
