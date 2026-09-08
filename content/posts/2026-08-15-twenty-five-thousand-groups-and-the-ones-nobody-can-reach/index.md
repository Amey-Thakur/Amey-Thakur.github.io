---
title: "Twenty-Five Thousand Groups, and the Ones Nobody Can Reach"
date: 2026-08-15T19:59:59-04:00
draft: false
author: "Amey Thakur"
summary: "There is a question in mathematics that has been open since the 1800s, and for one slice of it you can now attack it by search. I built a factory that produced degree-24 polynomials, submitted ten thousand scoreable pairs to a competition organised with the LMFDB and Terence Tao, and finished 54th of 256 with a score of 2.36. The interesting part is not the rank. It is that I can prove, with numbers, exactly why the score was small, and the answer says something about how these searches should be run."
tags: ["Mathematics", "Number Theory", "Galois Theory", "Computational Mathematics", "Search", "LMFDB", "PARI/GP", "Competitions", "SAIR Foundation", "Research", "Python"]
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

{{< Academic_Figure src="card.gif" alt="A degree 24 polynomial over the rationals, its Galois group, and the ladder of 25,000 transitive groups of degree 24, in the SAIR Foundation card style." caption="Twenty-five thousand groups. The competition asks for a polynomial that realises each one." align="center" >}}

## An open problem you can attack with a laptop

Most famous unsolved problems in mathematics cannot be attacked by anyone
without a decade of specialist training. The inverse Galois problem is unusual,
because one slice of it turns into something a search can bite on.

The problem asks whether every finite group is the symmetry group of some
number field. Nobody knows. But you can ask it one degree at a time, and then it
becomes concrete:

> For every transitive permutation group on 24 letters, find an irreducible
> integer polynomial of degree 24 whose Galois group is that group.

There are **25,000** such groups, labelled `24T1` through `24T25000`. Each one
can appear with several signatures, counting how many of its roots are real, and
across all of them that gives **165,836** possible targets.

Everything below degree 24 is essentially finished. Every transitive group of
degree 22 or less has a known realisation, and degree 23 has exactly one holdout,
the Mathieu group `M23`. Degree 24 is wide open. The frozen baseline this
competition started from, drawn from the [LMFDB](https://www.lmfdb.org/), covered
**286 labels and 622 pairs**, which is under half a per cent of the surface.

The competition was [IGP24](https://competition.sair.foundation/competitions/igp24/overview),
run by the SAIR Foundation in collaboration with the LMFDB, co-organised by John
Jones, Jen Paulhus, David Roe, Andrew Sutherland and Terence Tao. Two hundred
and fifty-six teams entered. Submissions closed today.

There is a theorem in the background that makes the gap sharper. Shafarevich
proved that every finite solvable group does occur as a Galois group over the
rationals, and 24,193 of these 25,000 groups are solvable. So the existence
question is largely settled. What nobody has is the polynomials. The theorem
does not hand them over, and that is exactly the gap the competition exists to
close.

## The scoring rule, which is the whole strategy

A submission is a plain text file. Each line is 25 integers, the coefficients of
a monic degree-24 polynomial. At most 1,000 per submission, 200 submissions a
day. An official verifier computes the real answer.

You might reasonably assume the goal is volume. It is not, and the scoring makes
that mathematically precise. For a pair held by `k` teams, your score is
proportional to `2^(1 − k)`.

| Who holds the pair | What it is worth |
| :--- | ---: |
| Only you | 1 point |
| Two teams | about 0.5 each |
| Ten teams | about 0.002 each |

A pair held by ten teams is worth roughly one five-hundredth of a pair held
alone. Discriminant size applies a mild adjustment on top, and ties pay nothing.

**Rarity is the entire game.** Volume without rarity is worth almost nothing,
and I want to be honest that I understood this rule before I started and still
built a machine that produced volume.

## The factory, and the trick inside it

I had no Magma licence, which is the standard tool for computing a Galois group
label. The whole pipeline was designed around not having it: construct
structured candidates, guess their group cheaply, avoid re-sending anything
already held, and let the official verifier settle the label.

The cheap guess is the piece worth taking away.

Factor the polynomial modulo a fixed set of primes and collect the cycle types
you see. By Chebotarev's density theorem, that set of shapes is close to a
signature for the Galois group. It costs about a millisecond, against a Magma
computation I could not run at all. Joined back against the labels the server
returned, it matched **10,750 entries with 7 conflicts**, so as a predictor it
is very nearly exact.

It is also exactly the kind of tool that will lie to you if you let it.

> Many distinct fingerprints collapse onto the same label, so novelty in
> fingerprint space badly overstates novelty in pair space. In one wave, 10,000
> apparently novel clusters yielded about 771 genuinely new pairs.

A pipeline that counts clusters as discoveries will report progress it has not
made. I know because mine did, until I checked it against what the server
actually credited.

{{< Academic_Figure src="run.gif" alt="Degree 24 polynomials searched against 25,000 transitive groups, ending at rank 54 with a score of 2.3559 across 10,180 scoreable pairs." caption="The run itself: what the factory searched, and where it finished." align="center" >}}

## The result, and it is not a good one

| | |
| :--- | :--- |
| Team | AVATAR, `IGP24-T00178` |
| Rank | **54 of 256** |
| Score | **2.3559** |
| Scoreable pairs | **10,180** |

Ten thousand pairs and two and a third points. That ratio is the whole story,
and it is not bad luck. It is the arithmetic of arriving late to a space that
had already been swept.

## Why, measured rather than guessed

This is the part I would keep. The most useful thing I have from three months of
this is a negative result with numbers attached.

**Everything reachable was already taken.** As of 1 August, of the 165,836
possible pairs, **155,366 already had at least one team on them**. The typical
pair carried two teams. The most crowded carried 75. Every pair my factory
produced landed somewhere in that mass.

**The gap is constructive, not computational.** About 97 per cent of my labelled
output landed on high-index generic groups, which every team reaches without
trying. The pairs still unclaimed sit on groups my engines simply never produce.
Reaching them needs constructive Galois theory of the kind Magma provides, and
no amount of additional compute substitutes for it. I was not short of cycles. I
was short of constructions.

**The class field theory campaign proved it exactly.** Ray class field sweeps
over quartic, sextic and octic bases produced about 48,000 polynomials and 1,410
pairs. Twelve of those were nearly uncrowded, which was the first encouraging
thing in weeks. All twelve were inside the frozen baseline, and on nine of them
the discriminant came out **exactly equal** to the baseline minimum rather than
below it.

Sit with that for a second. The method had independently re-derived LMFDB's own
minimal fields, to the digit. It is the most satisfying failure I have had.
Unlocking a baseline pair requires strictly smaller, so all of it paid nothing.

The honest shape of the finding is this: the small-conductor class field zone
**is** the LMFDB baseline. Tooling that reaches it arrives precisely where the
ground is already occupied, and it arrives there by rediscovering what is
already known.

## What I would tell the next person

**Grade your engines early, and drop the ones that make generic groups.** This
is measurable within a day. Compositum constructions put **57 per cent** of
their output into the useful middle band. Tower constructions managed **1.6 per
cent**. That difference decides the entire outcome, and I spent real time on
towers before I measured it.

**Distrust a cheap proxy that has never been checked against ground truth.** The
fingerprint was excellent and it still inflated my sense of progress by more
than an order of magnitude, because it was measuring the wrong space. A proxy
tells you about the thing you can compute, not the thing you are scored on.

**When the scoring is exponential, read it as a constraint on the method, not on
the effort.** I read the rule correctly and drew the wrong conclusion from it. I
optimised throughput inside a construction family that could only ever reach
crowded ground. The rule was not asking me to work harder. It was telling me
which mathematics I needed and did not have.

## Where the work is

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">Code</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24">Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24</a>, the construction engines, the fingerprinting, the ledger and the crowding intelligence</span>
</div>

<div class="reference-item">
    <span class="reference-num">Competition</span>
    <span class="reference-text"><a href="https://competition.sair.foundation/competitions/igp24/overview">SAIR Foundation, IGP24</a>, 256 teams, closed 15 August 2026</span>
</div>

<div class="reference-item">
    <span class="reference-num">Database</span>
    <span class="reference-text"><a href="https://www.lmfdb.org/">The LMFDB</a>, which supplied the frozen baseline and, as it turned out, the ceiling</span>
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

## How to cite this

```text
Thakur, A. (2026). Twenty-Five Thousand Groups, and the Ones Nobody Can Reach.
Amey's Arc. https://amey-thakur.github.io/posts/
2026-08-15-twenty-five-thousand-groups-and-the-ones-nobody-can-reach/
```

```bibtex
@misc{thakur2026igp24,
  author       = {Thakur, Amey},
  title        = {Twenty-Five Thousand Groups, and the Ones Nobody Can Reach},
  year         = {2026},
  month        = {August},
  howpublished = {Amey's Arc},
  note         = {Written for the SAIR Foundation IGP24 competition, submissions closed 15 August 2026; final standing 54 of 256},
  url          = {https://amey-thakur.github.io/posts/2026-08-15-twenty-five-thousand-groups-and-the-ones-nobody-can-reach/}
}
```

---

<div align="center">

<i>The method rediscovered what was already known, to the digit, and was paid nothing for it. That is still a result.</i>

</div>
