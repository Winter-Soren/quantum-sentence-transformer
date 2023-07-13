# Quantum-Sentence-Transformer
Quantum-Enhanced Transfer Learning for Natural Language Processing

This is based on the research paper. [1] https://arxiv.org/abs/1912.08278

The approach taken here is to start with a traditional pre-trained model for capturing text semantics, then freeze its initial layers and stack at the end of the net a predetermined number of Quantum Variational Circuits (QVC) that can be trained using PennyLane's interface. The universality of the Fourier series demonstrates that Quantum Neural Nets (given sufficiently wide and deep circuits) are universal function approximators! More information can be found in [2].


What's intriguing about this concept? The input to the QVC is the output of the classical net (that is, a real-valued vector). So, this information is being mapped into Hilbert Space! An intriguing question that naturally arises is whether, aside from the potential speedup, Quantum Models can possibly generalise better than classical ones, and if so, in which regime. This is an active area of research, and in [3,] it is demonstrated that Quantum Nets have greater expressivity than classical ones. First, a new measure of expressivity based on Effective Dimension is proposed, and then it is demonstrated that, when comparing a classical net to a quantum net (both with the same number of parameters), as the labels become corrupted, the quantum model activates more of its total capacity!

Another paper published by Google demonstrates that there is a regime in which the topology of the data mapped into the Hilbert space provides better learning generalisation than the Real space [4].


References:

[1] Mari, Andrea, et al. "Transfer learning in hybrid classical-quantum neural networks." Quantum 4 (2020): 340.

[2] Schuld, Maria, and Francesco Petruccione. Supervised learning with quantum computers. Vol. 17. Berlin: Springer, 2018.

[3] Abbas, Amira, et al. "The power of quantum neural networks." Nature Computational Science 1.6 (2021): 403-409.

[4] Huang, Hsin-Yuan, et al. "Power of data in quantum machine learning." Nature communications 12.1 (2021): 1-9.
