from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2

q = QuantumCircuit(3,1)

q.ccx(0,1, 2)
q.measure(2,0)
q.draw()
print(q)

