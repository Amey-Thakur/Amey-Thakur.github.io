---
title: "Attention Is All You Need"
description: "Understanding the Mathematics of the Transformer"
date: 2026-03-16T15:05:09-04:00
draft: false
author: "Amey Thakur"
tags: ["AI", "Artificial Intelligence", "Transformers", "NLP", "Machine Learning", "Mathematics"]
math: true
ShowToc: true
TocOpen: false
---

![Cover graphic titled Attention Is All You Need — Understanding the Mathematics of the Transformer. It shows the scaled dot-product attention equation with labeled Query, Key, and Value blocks, plus references to self-attention, multi-head attention, and positional encoding.](attention-fig-1.png)

A visual cover introducing the mathematical foundations of the Transformer architecture from the paper Attention Is All You Need. The graphic highlights the core scaled dot-product attention equation alongside the key components of the architecture: self-attention, multi-head attention, and positional encoding.

![Simplified transformer architecture showing input embeddings and positional encoding followed by repeated blocks of multi-head attention, feed-forward networks, and layer normalization, producing output probabilities through a linear layer and softmax.](attention-fig-2.png)

*Architecture of the Transformer model introduced in* Attention Is All You Need *(Vaswani et al., 2017). The model processes input embeddings with positional encodings through stacked layers of multi-head self-attention and feed-forward networks, followed by a linear projection and Softmax to produce output probabilities.*

## Introduction

In 2017, researchers at Google introduced the paper *Attention Is All You Need* by [Ashish Vaswani](https://scholar.google.com/citations?user=oR9sCGYAAAAJ&hl=en) and colleagues. The paper proposed a new neural architecture for sequence modelling known as the **Transformer**.

Earlier neural architectures for language processing relied primarily on recurrence or convolution. The Transformer instead introduced a mechanism called **self-attention**, which allows every token in a sequence to interact directly with every other token.

This architectural change significantly improved the efficiency and scalability of neural language models. According to [Google Scholar (2026)](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=oR9sCGYAAAAJ&citation_for_view=oR9sCGYAAAAJ%3AzYLM7Y9cAGgC), the paper has accumulated **over 240,000 citations**, making it one of the most influential works in modern machine learning.

The goal of this article is to explain the **mathematical foundations of the Transformer architecture** in a clear and accessible way.

## Overview

I originally summarized the central idea of the paper in the following X thread.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">1/8<br><br>A paper that shaped modern natural language processing.<br><br>"Attention Is All You Need" (Vaswani et al., 2017)<br><br>It introduced the Transformer architecture used by many modern language models.<br><br>A short explanation of the central idea.</p>&mdash; Amey Thakur (@iameythakur) <a href="https://x.com/iameythakur/status/2033045678423683185?ref_src=twsrc%5Etfw">March 15, 2026</a></blockquote> <script async src="https://platform.x.com/widgets.js" charset="utf-8"></script>

The thread provides a concise overview of the paper.
The following sections expand on the **mathematical structure of the Transformer architecture**.

## Sequence Modelling Before Transformers

Before the introduction of the Transformer architecture, most neural language models relied on **recurrent neural networks (RNNs)** or **long short-term memory networks (LSTMs)**.

In these architectures, a sequence of tokens \\(x_1, x_2, x_3, \dots, x_n\\) is processed sequentially.

At each step, the model computes a hidden representation

$$h_t = f(x_t, h_{t-1})$$

where

* \\(x_t\\) represents the current token
* \\(h_{t-1}\\) represents the hidden state from the previous step

This formulation introduces two important limitations.

First, sequential computation prevents efficient parallelization during training.

Second, modelling **long-range dependencies** becomes difficult because information must propagate through many intermediate steps.

The Transformer architecture addresses these limitations by allowing **direct interactions between all tokens in the sequence**.

## Self-Attention

Self-attention enables each token in a sentence to determine which other tokens are most relevant when constructing its representation.

Consider a sequence of token embeddings:

$$x_1, x_2, \dots, x_n$$

Each token embedding is transformed into three vectors using learned linear projections:

$$q_i = x_i W^Q$$

$$k_i = x_i W^K$$

$$v_i = x_i W^V$$

* \\(q_i\\) is the **query vector**
* \\(k_i\\) is the **key vector**
* \\(v_i\\) is the **value vector**

The matrices \\(W^Q\\), \\(W^K\\), and \\(W^V\\) are learned parameters.

Conceptually:

* queries represent **what a token is searching for**
* keys represent **what information a token contains**
* values represent **the information shared with other tokens**

The model determines how strongly token \\(i\\) should attend to token \\(j\\) by comparing their query and key vectors.

## Computing Attention Scores

The similarity between tokens is measured using the **dot product** between query and key vectors.

$$\text{score}(i, j) = q_i \cdot k_j$$

If the vectors point in similar directions in the representation space, the dot product becomes large. This indicates that token \\(i\\) should attend strongly to token \\(j\\).

These similarity scores are computed for every pair of tokens in the sequence.

## Scaled Dot-Product Attention

The Transformer computes attention using the following formulation:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

This equation can be understood step by step.

### Query–Key Similarity

The matrix multiplication \\(QK^T\\) computes similarity scores between all query vectors and key vectors.

Each element of this matrix represents how strongly one token attends to another.

### Scaling

The scores are divided by \\(\sqrt{d_k}\\), where \\(d_k\\) is the dimensionality of the key vectors.

This scaling prevents the dot products from becoming too large when the vector dimension increases, which would otherwise destabilize the softmax computation.

### Softmax Normalization

The **softmax** function converts similarity scores into probabilities.

Each row of the resulting matrix represents a probability distribution indicating how much attention a token assigns to every other token in the sequence.

### Weighted Combination of Values

Finally, these probabilities are multiplied by the value vectors \\(V\\).

The resulting vector for each token becomes a **weighted combination of information from the entire sequence**.

This mechanism allows the model to integrate contextual information from all tokens simultaneously.

## Example of Self-Attention

![Self-attention example illustrating coreference resolution in a Transformer model. The token it assigns strong attention to animal in the sentence The animal did not cross the street because it was tired, demonstrating how self-attention captures long-range dependencies within a sequence.](attention-fig-3.png)

*Self-attention visualization showing how the token "it" attends strongly to "animal" in the sentence "The animal did not cross the street because it was tired."*

Consider the sentence

> The animal did not cross the street because it was tired.

A language model must determine what the word **"it"** refers to.

Through self-attention, the query vector associated with **"it"** aligns strongly with the key vector associated with **"animal."**

As a result, the representation of the word **"it"** incorporates contextual information from **"animal."**

This mechanism allows the model to resolve pronoun references and other contextual relationships.

## Minimal Demonstration of Self-Attention

The following minimal implementation demonstrates scaled dot-product attention using the same sentence example.

*Reference implementation of scaled dot-product self-attention based on the formulation in* Attention Is All You Need *(Vaswani et al., 2017). The example demonstrates how attention weights enable a Transformer model to resolve pronoun reference by assigning higher importance to semantically related tokens.*

```python
"""
File: transformer_self_attention_demo.py

Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
X: https://x.com/iameythakur

Tech Stack: Python 3, NumPy

Release Date: March 16, 2026

Description
A minimal demonstration of scaled dot-product attention
as defined in "Attention Is All You Need" (Vaswani et al., 2017).

The example shows how the token "it" attends strongly to
the token "animal", illustrating long-range dependency capture.
"""

import numpy as np

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.shape[-1]

    scores = np.dot(Q, K.T) / np.sqrt(d_k)

    exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)

    output = np.dot(attention_weights, V)

    return attention_weights, output

tokens = [
    "The","animal","did","not","cross",
    "the","street","because","it","was","tired."
]

np.random.seed(42)

embedding_dim = 4
embeddings = np.random.randn(len(tokens), embedding_dim) * 0.1

embeddings[1] = np.array([2.0,1.0,0.0,0.0])
embeddings[8] = np.array([1.9,1.1,0.1,0.0])

Q = embeddings
K = embeddings
V = embeddings

attention_weights,_ = scaled_dot_product_attention(Q,K,V)

it_index = tokens.index("it")

print("Tokens:", " | ".join(tokens))
print("\nSelf-Attention Distribution for token 'it'\n")

print("Token        | Weight   | Visual")
print("-"*45)

for i,token in enumerate(tokens):
    weight = attention_weights[it_index,i]
    bar = "█"*int(weight*50) if weight>0.01 else "·"
    print(f"{token:<12} | {weight:.4f} | {bar}")
```

### Example output:

```
Tokens: The | animal | did | not | cross | the | street | because | it | was | tired.

Self-Attention Distribution for token 'it'

Token        | Weight   | Visual
---------------------------------------------
The          | 0.0356   | █
animal       | 0.3625   | ██████████████████
did          | 0.0310   | █
not          | 0.0302   | █
cross        | 0.0288   | █
the          | 0.0296   | █
street       | 0.0297   | █
because      | 0.0288   | █
it           | 0.3500   | █████████████████
was          | 0.0402   | ██
tired.       | 0.0337   | █
```

The token **"it"** assigns its highest attention weight to **"animal."**

This demonstrates how self-attention captures long-range relationships through a single parallel computation.

## Multi-Head Attention

A single attention operation captures only one type of relationship between tokens.

The Transformer therefore computes multiple attention functions in parallel:

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)W^O$$

Each head computes attention independently:

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

Different attention heads can learn different linguistic patterns, including syntactic structure and semantic relationships.

## Positional Encoding

Because the Transformer processes tokens simultaneously, it must explicitly encode token positions.

The original paper proposes sinusoidal positional encodings:

$$PE(pos, 2i) = \sin\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$

$$PE(pos, 2i+1) = \cos\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)$$

These functions generate continuous patterns that represent token positions while preserving useful mathematical properties.

## Impact on Modern Machine Learning

The Transformer architecture has become the dominant framework for language modelling.

Models such as **BERT** and **GPT** are direct descendants of the Transformer architecture.

Beyond natural language processing, Transformer-based architectures are now widely applied in:

* computer vision
* multimodal learning
* speech processing

Understanding the mathematical structure of the Transformer therefore provides an essential foundation for studying modern machine learning systems.

## Reference

Vaswani, A. et al. (2017)
*Attention Is All You Need*
<https://arxiv.org/abs/1706.03762>
