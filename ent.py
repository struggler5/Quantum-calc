from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2

q = QuantumCircuit(2,2)
q.h(0)
q.cx(0,1)
q.measure(0,0)
q.measure(1,1)
q.draw()
print(q)



sim_a = AerSimulator()

samp_aer = SamplerV2(mode=sim_a)
result = samp_aer.run([q ],shots=100).result()
count_samp = result[0].data.c.get_counts()

print(count_samp)
