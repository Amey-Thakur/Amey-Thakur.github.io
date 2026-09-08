---
title: "When an Answer Stops Being Enough"
date: 2026-08-31T19:59:59-04:00
draft: false
author: "Amey Thakur"
summary: "A competition organised by Terence Tao and Damek Davis asked whether mathematical reasoning can be compressed into a page a language model reads before answering. Then its second stage removed the thing that made the first stage easy to fake: an answer was no longer worth anything unless it arrived with a proof a machine would check. This is what I built for both stages, and the moment that convinced me a confident answer and a correct one are completely different products."
tags: ["Mathematics", "Formal Methods", "Lean 4", "Language Models", "Automated Theorem Proving", "Prompt Engineering", "Competitions", "SAIR Foundation", "Research", "Python", "Evaluation"]
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

{{< Academic_Figure src="stage1.gif" alt="Stage 1: a 2.81 KB cheatsheet within a 10 KB cap, read by a language model at temperature zero returning true or false." caption="Stage 1. One page of distilled mathematics, a model, and a yes or no." align="center" >}}

## A model that scored fifty per cent and knew nothing

Start with the detail that reorganised how I think about evaluation.

Stage 1 of this competition asked a language model a series of true-or-false
questions about algebra, and the evaluation set was deliberately balanced, half
true and half false. One of the three models scored close to **fifty per cent
accuracy**. It parsed every prompt correctly. It answered in the right format
every time.

Its F1 score was near zero, because it had answered the same way on every
single question.

Fifty per cent looks like a model that half understands. It was a model that
understood nothing and had found the one strategy a balanced set rewards for
free. Accuracy alone cannot tell a reasoner from a coin, and I have never seen
that demonstrated so cleanly.

## The problem underneath

A **magma** is the least structured object in algebra: a set with one operation
and no rules at all. No associativity, no identity, no inverses. Because so
little is assumed, a law like `x = x ◇ y` constrains it only lightly, and
working out what else that law forces is genuinely hard.

The [Equational Theories Project](https://github.com/teorth/equational_theories)
[[1]](#ref-1) took the 4,694 simplest such laws and asked, for every ordered pair, whether the
first implies the second. That is **22,033,636 questions**, settled in Lean 4
through a mix of automated search and human proof.

This competition asked something different about the same material:

> Can strong mathematical reasoning be distilled into a compact artefact that
> makes a language model better at a formal task?

It was organised by **Damek Davis**, Associate Professor of Statistics and Data
Science at the University of Pennsylvania, and **Terence Tao**, with the SAIR
Foundation [[2]](#ref-2). The setup follows the cheat-sheet distillation of
Honda, Murakami and Zhang [[3]](#ref-3), with the artefact discovered by open
competition rather than produced by a single model query. Two hundred and ninety-four people took part.

Stage 1 launched on 14 March 2026 at 15:09:26 in UTC+14, the earliest place on
Earth to reach the time 3.1415926. I mention it because a competition that goes
to that trouble is telling you something about the people running it.

## Stage 1, and why it could be gamed

You submit a complete prompt: the template and a cheatsheet, together at most
**10 KB**, exactly as it will be sent. The model answers true or false. Only
correctness is scored. No browser, no search, no retrieval.

Ten kilobytes is not much. It is roughly this article, up to here, and into it
has to go whatever a model needs to reason about laws it has never seen.

But re-read that scoring rule. **Only correctness is scored.** A model that is
fluent and wrong scores exactly what a model that is careful and wrong scores,
and the constant-answer strategy above shows how far that can be pushed without
any reasoning at all.

## Stage 2, which closes the door

{{< Academic_Figure src="stage2.gif" alt="Stage 2: a 500 KB deterministic-first solver emitting a Lean 4 certificate for each goal, accepted or rejected by a deterministic judge." caption="Stage 2. The answer is worth nothing without a certificate a machine will check." align="center" >}}

Stage 2 replaces the answer with a **certificate**.

You submit one `solver.py`, at most 500 KB. For every pair of equations it must
produce something a Lean 4 [[4]](#ref-4) judge will verify:

| Verdict | What you must actually produce |
| :--- | :--- |
| **True** | A Lean 4 proof that the hypothesis forces the goal in every magma |
| **False** | A concrete magma where the hypothesis holds and the goal fails |

The judge is deterministic. There is no partial credit. A confident wrong answer
now scores exactly zero, and so does a correct answer you cannot prove.

This is the same design idea as the Modular Arithmetic Challenge I wrote about
earlier this month: rather than forbidding the shortcut, build an interface where
the shortcut cannot be expressed. There, no part of your code ever saw the whole
question. Here, no claim counts until a machine has checked it.

## What I built, and why it runs backwards

The obvious solver asks a model to write the Lean proof and hopes the judge
agrees. Model-written Lean is wrong often enough that a large share come back
rejected, and every rejection has already been paid for in tokens.

Mine inverts the order. It proves what it can **without** the model, and every
deterministic answer is verified locally before it is ever sent.

**Counterexamples are cheap and certain.** Orders 2 and 3 exhaustively, affine
magmas to order 8, order 4 by constrained backtracking, filtered random tables at
5 and 6. Every witness is checked in Python first, so the judge only confirms
something already established.

**Some true implications need no model either.** If the hypothesis forces every
element to be equal, one line closes any goal. Beyond that, a rewrite prover
simulates Lean's `rw` exactly and searches short chains in both directions, and a
saturation pass derives helper lemmas and proves them before using them.

**The verdict is known before the search begins.** The Equational Theories
outcome matrix is embedded in the solver, compressed to about 32 KB by collapsing
4,694 equations into **1,415 classes** with identical implication behaviour.

**The model is the last resort**, called only for true implications that survived
every deterministic stage.

On the official 20-problem sample, the deterministic stages alone answer **15**,
with no tokens spent and no incorrect certificate produced.

The property I am most pleased with is that the embedded verdict table steers the
budget and nothing else. If it is wrong, or misses, it cannot produce a wrong
answer, because every certificate is still verified locally before it is sent. A
lookup table that can only waste time and never mislead you is a safe thing to
carry.

## The failure mode that would have cost everything

The evaluation sandbox is `python:3.12-slim`, with **no third-party packages and
no network**.

A solver that imports `numpy` does not run slowly. It does not answer badly. It
dies on import, before the first problem, and every answer in the run is lost.

Nothing in local testing reveals this, because locally the packages are
installed. So it is enforced in continuous integration instead: a check that
holds the solver to the sandbox rules and the size cap, and a second that
re-parses every emitted certificate from its Lean source and re-verifies it,
both running with no Lean toolchain at all.

If you take one practical thing from this post, take that. **The environment your
code will die in should be a test, not a hope.**

## What the two stages taught me together

Stage 1 asks whether reasoning can be compressed. Stage 2 asks whether the thing
that came out the other end was reasoning at all.

Between them they draw a line I now use elsewhere. A system that produces answers
can be evaluated only statistically, and statistics can be gamed by a constant
function. A system that produces **checkable artefacts** can be evaluated one
item at a time, by a machine, with no benefit of the doubt available anywhere.

Certificates are more work. They are also the only version of this where being
confidently wrong costs you exactly what it should.

## Where the work is

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">Code</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE">Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE</a>, both stages, the three solvers, and the sandbox gate [[5]](#ref-5)</span>
</div>

<div class="reference-item">
    <span class="reference-num">Competition</span>
    <span class="reference-text"><a href="https://competition.sair.foundation/competitions/mathematics-distillation-challenge-equational-theories-stage2/overview">SAIR Foundation, Mathematics Distillation Challenge, Stage 2</a>, 294 participants, closed 31 August 2026</span>
</div>

<div class="reference-item">
    <span class="reference-num">Source</span>
    <span class="reference-text"><a href="https://github.com/teorth/equational_theories">The Equational Theories Project</a>, the 4,694 laws and the 22 million implications behind the problem</span>
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
    flex: 0 0 120px; /* Fixed width for the label column */
    font-weight: bold;
    color: inherit;
}
.reference-text {
    flex: 1; /* Takes remaining space */
}
</style>

## References


<style>
.reference-container {
    padding-left: 0;
}
.reference-item {
    display: flex;
    margin-bottom: 0.8rem;
}
.reference-num {
    flex: 0 0 45px; /* Fixed width for the number column */
    font-weight: bold;
    color: inherit;
}
.reference-text {
    flex: 1; /* Takes remaining space */
}
</style>

<div class="reference-container">
<div class="reference-item">
    <span class="reference-num">[1]</span>
    <span class="reference-text"><a id="ref-1"></a><b>T. Tao et al.</b>, "The Equational Theories Project," Software and formalisation, 2025, <a href="https://github.com/teorth/equational_theories">https://github.com/teorth/equational_theories</a> [Accessed: Aug. 31, 2026].</span>
</div>
<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>SAIR Foundation</b>, "Mathematics Distillation Challenge, Equational Theories, Stage 2," <i>SAIR Foundation Competitions</i>, 2026, <a href="https://competition.sair.foundation/competitions/mathematics-distillation-challenge-equational-theories-stage2/overview">https://competition.sair.foundation/competitions/mathematics-distillation-challenge-equational-theories-stage2/overview</a> [Accessed: Aug. 31, 2026].</span>
</div>
<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>Honda, Murakami, and Zhang</b>, "Distilling Many-Shot In-Context Learning into a Cheat Sheet," 2025. Cited as the setup the competition follows.</span>
</div>
<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>L. de Moura and S. Ullrich</b>, "The Lean 4 Theorem Prover and Programming Language," in <i>Automated Deduction (CADE 28)</i>, Lecture Notes in Computer Science, vol. 12699, Springer, 2021, <a href="https://doi.org/10.1007/978-3-030-79876-5_37">https://doi.org/10.1007/978-3-030-79876-5_37</a> [Accessed: Aug. 31, 2026].</span>
</div>
<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>A. Thakur</b>, "SAIR Mathematics Distillation Challenge," Software, CC BY 4.0, 2026, <a href="https://github.com/Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE">https://github.com/Amey-Thakur/SAIR-MATHEMATICS-DISTILLATION-CHALLENGE</a> [Accessed: Aug. 31, 2026].</span>
</div>

</div>

## How to cite this

```text
Thakur, A. (2026). When an Answer Stops Being Enough.
Amey's Arc. https://amey-thakur.github.io/posts/
2026-08-31-when-an-answer-stops-being-enough/
```

```bibtex
@misc{thakur2026distillation,
  author       = {Thakur, Amey},
  title        = {When an Answer Stops Being Enough},
  year         = {2026},
  month        = {August},
  howpublished = {Amey's Arc},
  note         = {Written for the SAIR Foundation Mathematics Distillation Challenge, Equational Theories, Stage 2, submissions closed 31 August 2026},
  url          = {https://amey-thakur.github.io/posts/2026-08-31-when-an-answer-stops-being-enough/}
}
```

---

<div align="center">

<i>A confident answer and a correct one are different products. Only one of them can be checked.</i>

</div>
