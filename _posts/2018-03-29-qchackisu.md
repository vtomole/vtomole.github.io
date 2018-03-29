---
layout: post
title: "Quantum programming at HackISU"
date: 2018-03-29
---

**Introduction**

Qchackers built an [SDK for quantum computers] at Hack ISU last weekend. Evan Anderson,  Dylan Sharp and I created a compiler and quantum virtual machine (QVM); which we used to demonstrated quantum teleportation between two QVMs.  This project was good enough to get us the [AWS Education prize]. 

**Compiler and QVM**

The compiler was written in Common Lisp.  I first tried to write the compiler in Python, but it did not have all the features I needed; like generating and executing code on the fly. Even though Common Lisp made it harder to deploy our SDK on the cloud, It was a good trade off because a Common Lisp implementation of the compiler is easier to extend than a Python implementation.

The QVM was implemented in Python with Numpy. Implementing the virtual machine was straightforward. The most difficult part was debugging. Our virtual machine executes basic single and two qubit gates.  It also performs measurements on the qubits. Measurement results can be stored in a classical register via a classical instruction.

**Quantum teleportation**

Hack ISU was the first time Dylan studied quantum computation. His task was to grok quantum teleportation and figure out how to implement it across two QVMs. Dylan went through all the highs and lows of studying quantum computation in 24 hours. He went from reviewing linear algebra to understanding quantum teleportation in a day. Dylan corresponded with Evan in implementing quantum teleportation on the QVMs.

**Conclusion**

Hack ISU Spring 2018 was my most productive hackathon. I was lucky to work with someone who knew quantum computing, and another who was eager learn. Without Dylan’s newfound knowledge of quantum teleportation and Evan’s expertise in Python programming and web development, we wouldn’t have accomplished as much as we did. I would definitely hack with this group of Qchackers again!


[SDK for quantum computers]: http://qchackers.com
[AWS Education prize]: https://twitter.com/MLHacks/status/977959734467858433	

