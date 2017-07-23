---
layout: post
title: "Simulating physics with computers Part 1: Universal Quantum Simulator"
date: 2017-06-16
---



These blog series is inspired by Richard Feynman's 1982 paper: Simulating Physics with computers." This paper can found [here]

The paper is divided into 3 parts: Simulating time, Simulating Probability, Universal Quantum Simulators, and Two-State Quantum Systems. Let us study the ideas in this paper using the Python Programming Language.

Simulating Time: Simulating Time with a computer is ussually straigt forward. You just use the computer's internal clock to keep track of the time.


Simulating Probabilities: Simulating probabilities can just be done using a random number generator, so this part if also not that interesting at all. You actually can't simulate quantum mecanics with the comoputer that you are using. because of the hidden variable problem.


Universal Quantum Simulators: The universal simulator is made out of pauli matrices. These matrices are the pauli X, pauli Y, and Pauli , and the Identity matrix.These matrices are enough to describe a general quantum mechanical simulator, If there was one more matrice, the CNOT matrix. This Quantum simulator will trully be universal.



Two-State Quantum System: A two state quantum system is called a qubit. You cannot arrange in a classical experiemnt a method tha the probability of agreement at 30 degrees will be bigger than 2/3 but in quantum mechanics this is possible.


You can find all of the code and the documentation on my github [repo]



[here]:https://people.eecs.berkeley.edu/~christos/classics/Feynman.pdf
[repo]:https://github.com/vtomole/simulating-physics-with-computers