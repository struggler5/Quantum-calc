import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.providers.basic_provider import BasicSimulator
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import SamplerV2
import sympy as sp

q = QuantumRegister(6)
c = ClassicalRegister(2)
qc = QuantumCircuit(q,c)

qc.ccx(q[0],q[1],q[4])
qc.cx(q[0],q[1])
qc.ccx(q[1],q[2],q[3])
qc.cx(q[1],q[2])
qc.x(q[3])
qc.x(q[4])
qc.ccx(q[3],q[4],q[5])

qc.x(q[5])


qc.measure(q[2],c[0])

qc.measure(q[5],c[1])
qc.draw(output='mpl')
print(qc)

#    sim_b = BasicSimulator()

sim_a = AerSimulator()
#
 #   res_b = sim_b.run(qc,shots=100).result().get_counts()
#
 #   res_a = sim_a.run(qc,shots=100).result().get_counts()

#print(res_b)
#print(res_a)


samp_aer = SamplerV2(mode=sim_a)
result = samp_aer.run([qc],shots=100).result()
count_samp = result[0].data.c0.get_counts()

print(count_samp)
