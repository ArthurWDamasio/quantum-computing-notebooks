# Quantum Information Theory

This repository contains annotations, notes, and small projects developed during my studies in **Quantum Information Theory** and **Quantum Computing**.  
The material combines theoretical foundations with practical implementations, primarily using **Python** and **Qiskit**.

## Contents

- **Notes & Annotations**
  - Core concepts in quantum information theory
  - Mathematical foundations (states, measurements, entanglement, circuits)
  - Explanatory notebooks and derivations

- **Jupyter Notebooks**
  - `notebooks/basics/qiskit-lesson1.ipynb` — Introductory Qiskit concepts and basic quantum circuits
  - `notebooks/arithmetic/somador10qbits.ipynb` — 3-qubit register adder
  - `notebooks/arithmetic/ripple_carry_adder.ipynb` — n-qubit ripple-carry adder (VBE)
  - `notebooks/arithmetic/qft-intro.ipynb` — QFT and approximate QFT (AQFT)
  - `notebooks/arithmetic/qadders-study.ipynb` — Comparison of quantum adders (RCA, QFT, AQFT, carry-lookahead): circuit metrics, routing depth and noisy success rates

- **Arithmetic module** — `notebooks/arithmetic/qadders.py` holds all reusable gates (RCA, QFT/AQFT, Draper adders, carry-lookahead adder).

- **Small Projects**
  - Quantum algorithms and subroutines
  - Circuit constructions and simulations
  - Exploratory implementations related to quantum arithmetic and information processing

## Setup

```bash
pip install -r requirements.txt
```

## Tools & Technologies

- Python
- Jupyter Notebook
- Qiskit
- Linear Algebra & Quantum Mechanics formalism

## Purpose

The goal of this repository is to:
- Serve as a structured study log
- Consolidate theoretical understanding with hands-on experimentation
- Provide reproducible examples for learning and reference

## Disclaimer

This repository is intended for **educational and research purposes**.  
Implementations may prioritize clarity and learning over performance or optimization.

## License

MIT License.