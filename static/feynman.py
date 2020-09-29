import numpy as np

import itertools
X = np.matrix([[0, 1], [1, 0]])


Z = np.matrix([[1, 0], [0, -1]])

H = (X + Z)/np.sqrt(2)




class Gates:
    I = np.matrix([[1, 0], [0, 1]])
    X = np.matrix([[0, 1], [1, 0]])
    Y = np.matrix([[0, 0 - 1j], [0 + 1j, 0]])
    Z = np.matrix([[1, 0], [0, -1]])

    # universal gates
    H = (X + Z)/np.sqrt(2)
    T = np.matrix([[1, 0], [0, np.exp(1j * np.pi / 4)]])
    S = np.matrix([[1.0, 0.0], [0.0, 1.0j]])
    CNOT = np.matrix([[1, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]])


def H(qubit):
    return {'gate' :'H', 'qubit': str(qubit)}


def QREG(num_qubits):
    return {'QUBITS': num_qubits}


def X(qubit):
    return {'gate': 'X', 'qubit': str(qubit)}

def I(qubit):
    return {'gate': 'I', 'qubit': str(qubit)}


def CNOT(qubit, qubit1):
    return {'CNOT' : [str(qubit), str(qubit1)]}


class Program:
    "Consists of a list of instructions"

    def __init__(self, *instructions):    
        self.instructions = list(instructions)

    def get_instructions(self):
        return self.instructions

    # def run(self):
    #     return API.cli_api(self.instructions)



gates_set = {
        "X": Gates().X,
        "I": Gates().I,
        "Z": Z,
        "H": H,
}


def amplitude(xm, C, x0):
    xm = np.asmatrix(xm)
    x0 = np.asmatrix(x0)
    res = C * x0
    return xm.getH() * res


g = np.matrix([[1], [0]]) 
f = np.matrix([[1], [0]])


def get_kron(gate, num_qubits):
    

    gate_main = gates_set[gate['gate']]
    if num_qubits == 1:
        return gate_main
    else:
        final_gate = np.kron(gate_main,  gates_set['I'])
        for i in range(num_qubits-2):
             final_gate = np.kron(final_gate,  gates_set['I'])
            
    return final_gate 



def multiply(num_gates, y, num_qubits, instructions):
    res = 1

  
    print(y)

    for i in range(num_gates):
    
       

        # g = get_kron(instructions[i], num_qubits)
        
        # print("Call this once")
        g =  gates_set['X']
        j = i + 1
        res = res * amplitude(create_ket(y[j], num_qubits), g, create_ket(y[j-1], num_qubits))

    return res


def create_ket(binary, num_qubits):
    a = np.zeros((2**num_qubits,1))
    a[int(binary, 2)] = 1
    return a


def path_integral(program):
    instructions = program.get_instructions()

    num_qubits = int(instructions[0]['QUBITS'])
    instructions.pop(0)
    sum = 0
    num_gates = len(instructions)
    res = ["".join(seq) for seq in itertools.product("01", repeat=num_qubits * (num_gates-1))]
    a_k_0 =  '0' * num_qubits
    x = '00'

    for j in res:
        a_k = ([j[i:i+num_qubits] for i in range(0, len(j), num_qubits)])
        a_k.insert(0, a_k_0) 
        a_k.append(x)
        sum = sum + multiply(num_gates, a_k, num_qubits, instructions)

    


    return sum







x_prog = Program(
    QREG(2),
    X(0),)



sum = path_integral(x_prog)

print(sum)

