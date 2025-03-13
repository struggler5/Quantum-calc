from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(1)
qc.cx(1,0)
qc.x(1)
qc.draw()
print(qc)
print(Statevector(qc))
