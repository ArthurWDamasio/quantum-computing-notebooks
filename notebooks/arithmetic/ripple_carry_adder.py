import numpy as np
from qiskit.circuit.quantumcircuit import QuantumCircuit
from qiskit.circuit import Gate
from qiskit.circuit.library import CXGate, CCXGate


class Carry(Gate):
    def __init__(self):
        super().__init__(name="Carry", num_qubits=4, params=[])
        qc = QuantumCircuit(4, name=self.name)
        c_in, a, b, c_out = 0, 1, 2, 3
        qc.append(CCXGate(), [a, b, c_out])
        qc.append(CXGate(),  [a, b])
        qc.append(CCXGate(), [c_in, b, c_out])
        self.definition = qc


class Sum(Gate):
    def __init__(self):
        super().__init__(name="Sum", num_qubits=3, params=[])
        qc = QuantumCircuit(3, name=self.name)
        c_in, a, b = 0, 1, 2
        qc.cx(a, b)
        qc.cx(c_in, b)
        self.definition = qc


class RippleCarryAdder(Gate):
    def __init__(self, n: int):
        num_q = 3 * n + 1
        super().__init__(name="RCA", num_qubits=num_q, params=[])
        
        carry    = Carry()
        sum_gate = Sum()
        i_carry  = carry.inverse()
        
        qc = QuantumCircuit(num_q, name=self.name)

        # Fase 1 — propagação: aplica Carry em cada bit
        for i in range(0, num_q - 3, 3):
            qc.append(carry, [i, i + 1, i + 2, i + 3])

        # Fase 2 — bit mais significativo:
        qc.cx(num_q - 3, num_q - 2)
        qc.append(sum_gate, [num_q - 4, num_q - 3, num_q - 2])

        # Fase 3 — desfaz cada Carry e calcula os bits de soma restantes
        for j in range(num_q - 4, 0, -3):
            qc.append(i_carry,  [j - 3, j - 2, j - 1, j])
            qc.append(sum_gate, [j - 3, j - 2, j - 1])

        self.definition = qc