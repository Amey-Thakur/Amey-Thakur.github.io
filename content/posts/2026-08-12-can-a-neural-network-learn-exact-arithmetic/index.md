---
title: "Can a Neural Network Learn Exact Arithmetic?"
date: 2026-08-12T19:59:59-04:00
draft: false
author: "Amey Thakur"
summary: "A calculator multiplies two thousand-digit numbers and takes the remainder without thinking about it. Ask a neural network to do the same thing and it becomes an open research question, one that Terence Tao helped set as a competition. The answer has to be exact, because a remainder that is off by one is simply wrong. This is what I submitted to the SAIR Foundation's Modular Arithmetic Challenge, why the obvious approach cannot work, and the one idea that made the difference."
tags: ["Machine Learning", "Deep Learning", "Transformers", "Mathematics", "Modular Arithmetic", "Neural Networks", "PyTorch", "Competitions", "SAIR Foundation", "Grokking", "Length Generalisation", "Research"]
ShowToc: true
TocOpen: false
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

.equation {
    text-align: center;
    margin: 1.4rem 0;
    font-size: 1.05rem;
}

.equation-note {
    text-align: center;
    font-size: 0.85rem;
    color: #6c6c6c;
    margin-top: -0.9rem;
    margin-bottom: 1.4rem;
}

[data-theme="dark"] .equation-note {
    color: #9b9c9d;
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

{{< Academic_Figure src="card.gif" alt="Two operands and a prime entering a small network, and the exact residue leaving it, in the SAIR Foundation card style." caption="Two numbers and a prime go in. One exact remainder comes out, and nothing in the submitted code is allowed to calculate it." align="center" >}}

## The question a calculator makes look silly

Take two whole numbers, multiply them, divide by a prime, and keep the
remainder. Your phone does this in less time than it takes to lift your finger.

Now make the numbers about **1,233 digits long**, make the prime up to **617
digits**, and ask a neural network to do it instead. Not approximately.
Exactly, digit for digit, because a remainder that is off by one is not close,
it is wrong.

That is the [Modular Arithmetic Challenge](https://competition.sair.foundation/competitions/modular-arithmetic-challenge/overview),
run by the SAIR Foundation from 8 June to 12 August 2026, and organised by a
group that includes **Terence Tao**. One hundred and thirty people entered.
Submissions closed today.

The reason a competition exists at all is that nobody is sure it can be done.

## Why it is hard, in one paragraph you do not need mathematics for

A network that recognises a cat does not have to be exactly right. It has to be
mostly right, and being mostly right about a cat is still useful. Arithmetic
does not work like that. There is no partial credit for a remainder. So the
network has to find an actual procedure, not a good approximation, and it has to
find it on its own from examples.

Then it has to run that procedure over a thousand digits without losing its
place.

| What makes it bite | Why |
| :--- | :--- |
| **Carrying** | A digit at one end of the number changes a digit at the far end |
| **Coordination** | That has to hold across every digit, at every scale, at once |
| **Growing output** | The answer's length follows the input's, so nothing is fixed width |
| **Reduction** | And then the remainder sits on top of all of it |

Small transformers can already learn modular *addition* for small primes, and
when you look inside them the representations resemble Fourier analysis on a
cyclic group, which is a lovely result. Multiplication is a different animal.

## The obstacle that has nothing to do with arithmetic

This is the part I would keep if I could keep only one paragraph.

A transformer does not know where anything is unless you tell it. The standard
way to tell it is by position: this digit is the first, this one is the second,
this one is the seventh.

Now pad the number. Every digit moves. A model trained on short operands has
never in its life encountered index 7, so when a longer number arrives, every
digit it can see is at a coordinate it has no experience of.

Describe the digit by **what it is worth** instead, its place value, and the
problem dissolves. Significance 3 is significance 3 whether the number is twelve
digits long or twelve hundred. The model has seen it on every example it was
ever given.

> Place value is not a trick for this task. It is the only description of a digit
> that survives what the task does to its inputs.

That is not a machine learning insight. It is the same insight that made the
abacus work, and the reason we teach children columns before we teach them
carrying.

{{< Academic_Figure src="scale.gif" alt="Two sixty-digit integers and a prime streaming into a small network, with the exact product modulo p resolving digit by digit." caption="The task at the scale it is actually set: operands far longer than anything the model was trained on." align="center" >}}

## The rule that makes it a real problem

Here is the part I found genuinely elegant, and it is a design lesson rather
than a mathematical one.

The obvious way to win a competition like this is to cheat: call a library, look
the answer up, hard-code something. So the organisers built an interface where
cheating is not forbidden so much as **structurally impossible**.

Your submission provides three separate preprocessing hooks, one for each input.
Each hook sees **only its own argument**. No single point in the code you submit
ever holds the two operands and the prime at the same time. The decoder that
turns the model's output back into a number belongs to the competition
pipeline, not to you.

You cannot compute the answer because you are never given the question.

The explicit ban list covers the rest: no `sympy`, `gmpy2`, `mpmath` or Python
big integers on the original arguments at inference, no lookup tables keyed on
the inputs, no `eval`, no network access, no subprocesses, no leakage between
the three hooks. What remains allowed is telling: base conversion inside a
single hook, any internal representation you like, and feeding the model its
own output one token at a time.

The principle fits in a sentence. **The model must learn to compute the answer,
and may not delegate, look up, or hard-code it.**

I have started designing my own evaluation harnesses this way. It is far easier
to make the wrong answer impossible to express than to write a rule that
forbids it.

## What I submitted, and the four bets in it

**Place-value embeddings.** Drop absolute position and inject significance, for
the reason above. A 1,024-bit prime then travels the same path as a 16-bit one.

**Algorithmic scratchpads.** Force the model to write out its intermediate
working. This turns a fixed-depth network into something closer to a recurrent
state machine, and it lets the model spend computation in proportion to the size
of the number rather than in proportion to its own depth. A network that must
show its working can afford a longer calculation.

**Grokking.** Train far past the point where the validation loss has flattened,
with heavy weight decay, and wait. There is a transition, well documented in the
literature, where memorised circuits collapse into the sparse algorithm
underneath them. The published weights were taken after that transition rather
than before it, which is a decision about patience more than about architecture.

**Routing.** Small and large moduli want different amounts of computation, so a
light router reads the width of the prime and dispatches to a direct model or a
scratchpad model accordingly.

The result is a public model on the Hugging Face Hub, identified by an immutable
commit hash, which the organisers evaluate against a secret seed:
[ameythakur/SAIR-Modular-Arithmetic-Challenge](https://huggingface.co/ameythakur/SAIR-Modular-Arithmetic-Challenge).

## What I would tell someone entering the next one

**Read the interface before the problem.** The three-hook design told me more
about what the organisers considered a real solution than the problem statement
did. An hour spent understanding how a competition prevents cheating is an hour
spent understanding what it actually wants.

**Build the judge before the model.** The repository has a sandbox with an AST
validator and a simulator of the official judge, so a submission is checked
against the rules before it is packaged. Every hour that went into it was
returned. Discovering a rule violation at submission time is not a bug, it is a
lost competition.

**Take the representation seriously first.** Everything else in this project was
ordinary engineering. The one decision that changed what was possible was
describing a digit by its worth rather than its position, and it was available
on day one.

## Where the work is

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">Code</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/SAIR-MODULAR-ARITHMETIC-CHALLENGE">Amey-Thakur/SAIR-MODULAR-ARITHMETIC-CHALLENGE</a>, the laboratory, the datasets, the sandbox and the export</span>
</div>

<div class="reference-item">
    <span class="reference-num">Model</span>
    <span class="reference-text"><a href="https://huggingface.co/ameythakur/SAIR-Modular-Arithmetic-Challenge">ameythakur/SAIR-Modular-Arithmetic-Challenge</a> on the Hugging Face Hub</span>
</div>

<div class="reference-item">
    <span class="reference-num">Competition</span>
    <span class="reference-text"><a href="https://competition.sair.foundation/competitions/modular-arithmetic-challenge/overview">SAIR Foundation, Modular Arithmetic Challenge</a>, 130 participants, closed 12 August 2026</span>
</div>

</div>

<style>
.reference-container {
    padding-left: 0;
}
.reference-item {
    display: flex;
    margin-bottom: 0.8rem;
}
.reference-num {
    flex: 0 0 110px; /* Fixed width for the label column */
    font-weight: bold;
    color: inherit;
}
.reference-text {
    flex: 1; /* Takes remaining space */
}
</style>

## How to cite this

```text
Thakur, A. (2026). Can a Neural Network Learn Exact Arithmetic?
Amey's Arc. https://amey-thakur.github.io/posts/
2026-08-12-can-a-neural-network-learn-exact-arithmetic/
```

```bibtex
@misc{thakur2026modulararithmetic,
  author       = {Thakur, Amey},
  title        = {Can a Neural Network Learn Exact Arithmetic?},
  year         = {2026},
  month        = {August},
  howpublished = {Amey's Arc},
  note         = {Written for the SAIR Foundation Modular Arithmetic Challenge, submissions closed 12 August 2026},
  url          = {https://amey-thakur.github.io/posts/2026-08-12-can-a-neural-network-learn-exact-arithmetic/}
}
```

---

<div align="center">

<i>There is no partial credit for a remainder, which is exactly what makes it worth asking.</i>

</div>
