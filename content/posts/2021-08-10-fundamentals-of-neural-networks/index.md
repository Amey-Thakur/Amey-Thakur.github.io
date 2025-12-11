---
title: "Fundamentals of Neural Networks: From Neurons to Deep Learning"
date: 2021-08-10T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Neural Networks", "Deep Learning", "Perceptrons", "Backpropagation", "AI Fundamentals", "Machine Learning"]
ShowToc: true
TocOpen: false
description: "A foundational guide to the architecture, mathematics, and evolution of Artificial Neural Networks."
---

<style>
/* Make images transparent on light backgrounds */
.post-content img {
    mix-blend-mode: multiply;
}

/* Dark mode: Show original images with transparent backgrounds */
[data-theme="dark"] .post-content img {
    filter: none;
    mix-blend-mode: normal;
    border-radius: 8px;
    opacity: 0.95; /* Slightly reduce glare while maintaining contrast */
}

/* General hover effect for all links in post content */
.post-content a {
    transition: all 0.3s ease;
}
.post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Dark mode hover effect (same color) */
[data-theme="dark"] .post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}
</style>




Artificial Neural Networks (ANNs) are the engines powering the modern AI revolution. Inspired by the biological brain, these computational systems learn to perform tasks by considering examples, generally without being programmed with task-specific rules. This article explores the progression from the humble **Perceptron** to complex **Multi-Layer Perceptrons (MLP)**. We break down the mathematics of forward propagation, activation functions (Sigmoid, ReLU), and the crucial backpropagation algorithm that allows these networks to learn from their mistakes [[1]](#ref-1).

---

## The Silicon Brain

How do we teach a pile of math to think? The concept of the ANN is deeply rooted in biology.

{{< figure src="figures/Figure-1-Biological-Neuron.png" caption="Structure of a Biological Neuron" align="center" >}}

### The Analogy: The Committee Decision
Think of a neural network as a massive committee making a decision (e.g., "Is this a picture of a cat?").
*   **Input Layer (The Eyes)**: Pixels 1 through 100 shout "I see black!", "I see white!"
*   **Hidden Layers (The Middle Managers)**: They take these shouts and weigh them.
    *   Manager A: "If pixels 1 and 2 are black, that might be an ear."
    *   Manager B: "If pixels 50 and 51 are round, that might be an eye."
*   **Activation Function (The Voting Threshold)**: A manager only shouts to their boss if they are confident (e.g., "I am 90% sure this is an ear!"). If they are unsure, they stay silent (ReLU activation).
*   **Output Layer (The Boss)**: Listens to the managers. If the "Ear" manager and "Eye" manager both shout, the Boss says: "It's a cat!" [[2]](#ref-2).

---

## The Mathematical Unit: Perceptron

The perceptron is the simplest form of a neural network, modeling a single neuron.

{{< figure src="figures/Figure-2-Perceptron.png" caption="The Mathematical Perceptron" align="center" >}}

It takes inputs ($x$), multiplies them by weights ($w$), adds a bias ($b$), and passes the result through an activation function:
$$ y = f(\sum (w_i x_i) + b) $$

---

## Architectures and Deep Learning

As we stack these neurons, we create Deep Neural Networks. The depth of the network allows it to learn hierarchical features—edges become shapes, shapes become objects.

{{< figure src="figures/Figure-7-Deep-Neural-Network.png" caption="Deep Neural Network Architecture" align="center" >}}

### Types of Architectures
We explore several specialized architectures developed for specific tasks:
*   **Feedforward Networks**: The standard architecture where information flows in one direction [[3]](#ref-3).
*   **Convolutional Neural Networks (CNN)**: Specialized for image processing, using sliding filters to detect spatial patterns.
*   **Recurrent Neural Networks (RNN)**: Designed for sequence data (like text or time series), maintaining an internal memory state.

{{< figure src="figures/Figure-9-Convolutional-Neural-Network.png" caption="Convolutional Neural Network (CNN)" align="center" >}}

---

## Biology vs. Technology

How does our artificial model compare to the real thing?

{{< figure src="figures/TABLE-1---An-Analogy-of-BNN-and-ANN.jpg" caption="Analogy between Biological and Artificial Neural Networks" align="center" >}}

---

## Publication Details

This research was published in the **International Journal of Research in Applied Science and Engineering Technology (IJRASET)**.

### Additional Resources
*   [Full Paper (PDF)](IJRASET-V9I8%20-%20Fundamentals%20of%20Neural%20Networks.pdf)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Fundamentals of Neural Networks: From Neurons to Deep Learning". AmeyArc (Aug 2021). https://amey-thakur.github.io/posts/2021-08-10-fundamentals-of-neural-networks/.</code></pre>

**Or use the BibTex citation:**

**BibTeX:**

```
@article{thakur2021neuralnetworks,
  title   = "Fundamentals of Neural Networks: From Neurons to Deep Learning",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Aug",
  url     = "https://amey-thakur.github.io/posts/2021-08-10-fundamentals-of-neural-networks/"
}
```

---

## References

1. <a id="ref-1"></a> **Thakur, A.** (2021). Fundamentals of Neural Networks. *International Journal of Research in Applied Science and Engineering Technology (IJRASET)*, 9(8).

1. <a id="ref-2"></a> **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press.

1. <a id="ref-3"></a> **Rosenblatt, F.** (1958). The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain. *Psychological Review*.

---
*Authored by Amey Thakur.*
