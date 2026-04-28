import numpy as np
from qiskit.circuit.quantumcircuit import QuantumCircuit
from qiskit.circuit import Gate


class QFT(Gate):
    def __init__(self, n, do_swaps=True):
        self.do_swaps = do_swaps
        super().__init__(name="QFT", num_qubits=n, params=[])

    def _define(self):
        n = self.num_qubits
        qc = QuantumCircuit(n, name="QFT")

        for j in range(n - 1, -1, -1):
            qc.h(j)
            for k in range(j - 1, -1, -1):
                lam = np.pi / (2.0 ** (j - k))
                qc.cp(lam, k, j)

        if self.do_swaps:
            for i in range(n // 2):
                qc.swap(i, n - i - 1)

        self.definition = qc


class AQFT(Gate):
    def __init__(self, n, do_swap=True):
        self.do_swap = do_swap
        super().__init__(name="AQFT", num_qubits=n, params=[])
        

    def _define(self):
        """
        Approximate QFT: same convention fixes as QFT, but controlled-phase gates
        are truncated to only the m = ceil(log2(n)) nearest neighbours, reducing
        circuit depth at the cost of a small approximation error.
        """
        n = self.num_qubits
        qc = QuantumCircuit(n, name="AQFT")

        m = int(np.ceil(np.log2(n)))  # truncation parameter

        for j in range(n - 1, -1, -1):
            qc.h(j)
            # Only apply phases for the m nearest lower-index qubits
            for k in range(j - 1, max(j - m, -1), -1):
                lam = np.pi / (2.0 ** (j - k))
                qc.cp(lam, k, j)
        if self.do_swap:
            for i in range(n // 2):
                qc.swap(i, n - i - 1)

        self.definition = qc