---
title: "Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra"
date: 2026-09-20T09:00:00-04:00
draft: false
author: "Amey Thakur"
summary: "Naming the Galois group of a degree-24 integer polynomial ordinarily demands resolvent computations inside a computer algebra system. This paper presents a statistical alternative that needs only polynomial factorisation modulo small primes, and evaluates it against 576,682 polynomials whose groups the SAIR IGP24 evaluation server computed independently in Magma. The method reads the multiset of Frobenius cycle types at 60 primes as a sample from the group's own cycle-type distribution, which the Chebotarev density theorem licenses, then scores that sample against empirical profiles of candidate groups drawn by product-replacement sampling. Within its domain the classifier reaches 69.0% top-1 and 88.7% top-3 accuracy at 53 ms per polynomial."
tags: ["Mathematics", "Number Theory", "Galois Theory", "Chebotarev Density", "Inverse Galois Problem", "Transitive Groups", "Statistical Classification", "Computational Mathematics", "LMFDB", "SAIR Foundation", "Research", "Python", "Machine Learning"]
ShowToc: true
TocOpen: false
---

<style>
/* Make images transparent on light backgrounds */
.post-content img {
    mix-blend-mode: multiply;
}

/* Dark mode: show original images with transparent backgrounds */
[data-theme="dark"] .post-content img {
    filter: none;
    mix-blend-mode: normal;
    border-radius: 8px;
    opacity: 0.95;
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

/* Dark mode hover effect (same colour) */
[data-theme="dark"] .post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Reference list */
.reference-container {
    margin-top: 1rem;
}
.reference-item {
    display: flex;
    gap: 0.6rem;
    margin-bottom: 0.7rem;
    line-height: 1.55;
}
.reference-num {
    flex-shrink: 0;
    color: inherit;
}
.reference-text {
    flex: 1;
}
</style>

{{< Academic_Figure src="card.gif" alt="Title card: Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra, by Amey Thakur." align="center" >}}

<div align="center">

**[Code and data](https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24)** &nbsp;·&nbsp;
**[Competition](https://competition.sair.foundation/competitions/igp24/overview)** &nbsp;·&nbsp;
**[SAIR Foundation index](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH)**

</div>

## Abstract

Naming the Galois group of a degree-24 integer polynomial ordinarily demands
resolvent computations inside a computer algebra system. This paper presents a
statistical alternative that needs only polynomial factorisation modulo small
primes, and evaluates it against 576,682 polynomials whose groups the SAIR
IGP24 evaluation server computed independently in Magma. The method reads the
multiset of Frobenius cycle types at 60 primes as a sample from the group's own
cycle-type distribution, which the Chebotarev density theorem licenses, then
scores that sample against empirical profiles of candidate groups drawn by
product-replacement sampling. Within its domain the classifier reaches 69.0%
top-1 and 88.7% top-3 accuracy at 53 ms per polynomial. Its practical value rests on a calibrated
abstention rule: required to beat the runner-up by a log-likelihood margin of
8, the classifier commits on 12.7% of inputs and answers correctly on 76 of
76 commitments, a 95% Wilson lower bound of 95.2% on precision. A
separability bound explains these figures instead of merely reporting them.
The Bhattacharyya coefficient between the cycle-type distributions of two
groups caps the accuracy of every possible method at a given number of primes,
and group theory alone computes it, before any polynomial is factored. It
predicts two things and measurement confirms both: accuracy falls from 100%
to 23.5% as a group's nearest competitor closes in, respecting that cap in
every band, and 60 primes is too few, since accuracy is still climbing there.
Two further limitations get the same treatment. Profiles cover 24<i>T</i><sub>1</sub> through
24<i>T</i><sub>8000</sub>, and only 9.4% of the labelled corpus falls in that range, so
coverage rather than accuracy binds deployment. Novelty counted in fingerprints
overstates novelty in groups by more than an order of magnitude. All code and
data are public.

## Introduction
Let <i>f</i> &isin; &#8484;[<i>x</i>] be monic and irreducible of degree <i>n</i>. Its Galois
group is the automorphism group of the splitting field of <i>f</i> over &#8474;,
which acts faithfully and transitively on the <i>n</i> roots and therefore embeds as
a transitive subgroup of <i>S</i><sub><i>n</i></sub>. Identifying that subgroup among the transitive
groups of degree <i>n</i>, up to conjugacy, is a basic computational question in
algebraic number theory. Degree 24 admits exactly 25,000 such groups, labelled
24<i>T</i><sub>1</sub> through 24<i>T</i><sub>25000</sub>; 24,193 of them are solvable and 807 are not.

The standard approach computes resolvent polynomials and inspects how they
factor, descending the lattice of transitive groups. Magma, PARI/GP and Sage all
implement this family of algorithms [[2]](#ref-2)[[3]](#ref-3)[[13]](#ref-13)[[9]](#ref-9).
The approach returns an exact answer, and it costs accordingly. It also presumes
that one of those systems is available.

This paper asks a narrower question. Suppose no computer algebra system is at
hand, and the only available primitive is factorisation of <i>f</i> modulo small
primes, which any integer-arithmetic library supplies. How much of the group can
one recover, and how reliably? Figure 1 states the answer this
paper develops as six steps and no symbols; the rest of the paper makes each
step precise and measures how well it works.

The question arose in practice. Preparing submissions for the SAIR Inverse
Galois Problem competition at degree 24 required deciding, before spending a
submission, which group a candidate polynomial would realise, so that search
effort could go toward groups no other participant had claimed. The evaluation
server computes the label in Magma and returns it, but only after a submission
is spent. Locally, no computer algebra system was installed. A predictor was
therefore not a convenience but a precondition for directing the search at all.
{{< Academic_Figure src="fig-1-method-without-notation.png" alt="The method without notation. Factoring a polynomial modulo a prime is elementary arithmetic that any integer library per" align="center" >}}

<p class="equation-note"><b>Figure 1.</b> The method without notation. Factoring a polynomial modulo a prime is elementary arithmetic that any integer library performs, and steps 2 and 3 need nothing more. What makes the pattern informative is the Chebotarev density theorem (Section 2.2): the patterns a polynomial produces are not arbitrary but are drawn, at random, from a distribution fixed by its Galois group. Reading the observed patterns as a sample from that distribution turns identification into a statistical question. Figure 2 gives the same pipeline in the notation used throughout.</p>

### Contributions

1. **A classifier** that names the Galois group of a degree-24
 polynomial from factorisation data alone, with no resolvent computation
 and no computer algebra system (Section 4).
2. **An evaluation against independent ground truth.** The SAIR
 evaluation server labelled 576,682 polynomials in Magma over the
 campaign. Section 7 measures the classifier against that
 corpus and reports 69.0% top-1 and 88.7% top-3 accuracy, each with a
 95% interval.
3. **A calibrated abstention rule** under which the classifier answers
 correctly on 76 of 76 commitments while covering 12.7% of inputs
 (Section 4.4). For directing a search, precision without
 recall is the useful trade, and this rule is what made the method usable.
4. **A separability bound** that decides, before any polynomial is
 factored, which groups the method can name at all
 (Proposition 1). The bound predicts accuracy from the
 geometry of the candidate set, and Section 8 confirms
 the prediction: accuracy falls from 100% to 23.5% across four bands of
 increasing crowding, and stays under the information-theoretic ceiling
 in every band.
5. **Two quantified negative results** (Section 9).
 Profile coverage rather than classifier accuracy binds deployment: only
 9.4% of the labelled corpus carries a true label inside the profiled
 range (Section 6). Separately, fingerprint novelty
 overstates group novelty by more than a factor of ten, which misleads
 any pipeline that counts its own discoveries by the statistic it uses
 to predict them.

### Hypotheses
Four claims organise the experiments. Each one admits a measurement that
could contradict it, and Section 8.4 returns to each with
the evidence that bears on it.
- **H1 (sufficiency).** Cycle types at a few dozen primes identify a degree-24
 group more often than not, within the range for which profiles exist.
- **H2 (crowding binds, not evidence).** The distance from a group to its
 nearest competitor in cycle-type distribution governs accuracy, and that
 distance is fixed before any polynomial is seen. Errors therefore
 concentrate on crowded groups rather than falling uniformly.
- **H3 (calibration).** The log-likelihood margin measures reliability, so
 thresholding it exchanges coverage for precision at a predictable rate.
- **H4 (saturation).** Accuracy levels off in the number of primes, so the
 prime budget can be fixed by measurement rather than guessed.
The evidence supports H1, H2 and H3. It contradicts H4, and the contradiction
is useful: the operating point this work deployed spent too few primes, and
Section 8.1 measures what that cost.
## Background

### Frobenius elements and cycle types
Let <i>f</i> be as above, with splitting field <i>K</i> and Galois group
<i>G</i> = Gal(<i>K</i>/&#8474;). Let <i>p</i> be a prime not dividing
disc(<i>f</i>). Reducing modulo <i>p</i> factors <i>f</i> into distinct
irreducibles over &#120125;<sub><i>p</i></sub>,
<p class="equation"><i>f</i> &equiv; <i>f</i><sub>1</sub> <i>f</i><sub>2</sub> &hellip; <i>f</i><sub><i>m</i></sub>  (mod <i>p</i>),
 &nbsp;&nbsp; 
deg <i>f</i><sub><i>i</i></sub> = <i>d</i><sub><i>i</i></sub>,
 &nbsp;&nbsp; 
&Sigma;<sub><i>i</i>=1</sub><sup><i>m</i></sup> <i>d</i><sub><i>i</i></sub> = <i>n</i> .</p>
Dedekind's theorem states that the Frobenius automorphism at <i>p</i> permutes the
roots of <i>f</i> with cycle type exactly
&lambda;(<i>f</i>,<i>p</i>) = (<i>d</i><sub>1</sub>, <i>d</i><sub>2</sub>, &hellip;, <i>d</i><sub><i>m</i></sub>), the partition of <i>n</i> recording those
factor degrees. The theorem converts a question about a Galois group into a
question about factorisation, which is the pivot the whole method turns on.
### The Chebotarev density theorem
Chebotarev's theorem [[1]](#ref-1) states that Frobenius elements
equidistribute across conjugacy classes: a conjugacy class <i>C</i> &sube; <i>G</i>
receives the primes whose Frobenius class is <i>C</i> with natural density
|<i>C</i>|/|<i>G</i>|. Fix a set <i>P</i> of primes avoiding disc(<i>f</i>) and collect
the observed multiset
<p class="equation">&Lambda;(<i>f</i>, <i>P</i>)  =  {&thinsp; &lambda;(<i>f</i>, <i>p</i>)  :  <i>p</i> &isin; <i>P</i> &thinsp;} .</p>
Chebotarev licenses reading &Lambda;(<i>f</i>,<i>P</i>) as a sample from the cycle-type
distribution of <i>G</i> on <i>n</i> points,
<p class="equation">&pi;<sub><i>G</i></sub>(&lambda;)  = 
(|{&thinsp; <i>g</i> &isin; <i>G</i> : type(<i>g</i>) = &lambda; &thinsp;}|)&#8260;(|<i>G</i>|) ,</p>
a probability distribution over partitions of <i>n</i>.

That statement carries the entire theoretical content of the method, and it also
fixes the method's ceiling. Groups with different cycle-type distributions
produce different fingerprints and separate cleanly. Groups sharing a
distribution do not separate at all, however many primes one observes.
Section 9 measures how often that happens.
### Discriminants and signatures
The polynomial discriminant &Delta;(<i>f</i>) and the discriminant <i>d</i><sub><i>K</i></sub> of the field
<i>K</i> = &#8474;[<i>x</i>]/(<i>f</i>) satisfy
<p class="equation">&Delta;(<i>f</i>)  =  <i>d</i><sub><i>K</i></sub> &middot; <i>i</i><sup>2</sup> ,</p>
where <i>i</i> is the index of &#8484;[<i>x</i>]/(<i>f</i>) in the ring of integers of <i>K</i>.
The competition scores |<i>d</i><sub><i>K</i></sub>|, which PARI/GP computes through `nfdisc`
[[9]](#ref-9), so a large index costs nothing provided the field discriminant
stays small. The signature reduces to <i>r</i>, the number of real roots, which is
even in even degree, so <i>r</i> &isin; {0, 2, &hellip;, 24}.
### The competition and its scoring rule
The Inverse Galois Problem competition at degree 24 ran from 16 June to
15 August 2026 under the SAIR Foundation, which runs open competitions on
unsolved problems in mathematics and computation. John Jones, Jen Paulhus,
David Roe, Andrew Sutherland and Terence Tao co-organised it in
collaboration with the LMFDB [[6]](#ref-6)[[7]](#ref-7). The arrangement matters for
this paper beyond provenance: the same project that supplies the baseline
of Section 2.4 and the generators of
Section 4.2 also defines the target the classifier is
measured against, so the labels, the candidate set and the notion of
novelty all come from one consistent source.

The competition [[6]](#ref-6) scores each distinct pair (24<i>T</i><sub><i>t</i></sub>, <i>r</i>).
Writing <i>k</i> for the
number of teams holding a pair, <i>D</i> for the submitter's best absolute field
discriminant and <i>D</i><sub>0</sub> for the smallest any team achieved,
<p class="equation">points  =  2<sup>&thinsp;1-<i>k</i></sup> &middot; (log <i>D</i><sub>0</sub>)&#8260;(log <i>D</i>) .</p>
<p class="equation-note">(1)</p>
The exponential factor dominates. Ten teams holding a pair reduce its value to
2<sup>-9</sup> of a pair held alone, so whether anyone else found the same group
governs the value of a submission, while the quality of the discriminant
contributes only logarithmically. Of the 165,836 possible (24<i>T</i><sub><i>t</i></sub>, <i>r</i>) pairs,
the frozen LMFDB baseline [[7]](#ref-7) covered 286 labels and 622 pairs, under
half of one percent. That sparsity is what made the space worth searching. It is
also what made blind search unrewarding, because dense random polynomials fall
into 24<i>T</i><sub>25000</sub> = <i>S</i><sub>24</sub> and into <i>A</i><sub>24</sub>, which every participant already
holds.

Equation (1) explains why this work needed a predictor rather than
merely benefiting from one. Without one, a search yields polynomials whose value
stays unknown until a submission has already been spent on them.
## Related work

**Exact determination of Galois groups.**Stauduhar [[2]](#ref-2) introduced the relative resolvent method, which
descends the lattice of transitive groups and tests resolvents for rational
roots. Fieker and Kl&uuml;ners [[3]](#ref-3) extended the approach to
higher degrees with practical algorithms that underpin current computer algebra
implementations. These methods return certainties. The present method returns
evidence, and the two therefore answer different questions: a resolvent
computation proves a group, whereas a fingerprint ranks candidates cheaply
enough to steer a search of hundreds of thousands of polynomials.
**Factorisation patterns as group evidence.**Constraining a Galois group by its factorisation pattern is standard for small
degrees, where a handful of primes often eliminates all but one candidate.
Degree 24 changes the character of the problem. With 25,000 candidate groups,
elimination fails and the task becomes statistical discrimination among
thousands of similar distributions. This paper treats it explicitly as
maximum-likelihood classification over sampled distributions, and measures it
with the vocabulary of classification: accuracy, precision, coverage and
abstention.
**The Inverse Galois Problem.**Whether every finite group arises as a Galois group over &#8474; remains
open. Malle and Matzat [[4]](#ref-4) and Serre [[5]](#ref-5) collect the
rigidity, specialisation and embedding-problem techniques that settle large
families. The competition inverts the usual emphasis. Rather than realising one
prescribed group, participants search broadly and must then identify what they
have produced, which moves identification, not construction, into the critical
path.
**Sampling finite groups.**Celler et al. [[8]](#ref-8) introduced product replacement,
a random walk that generates near-uniform elements of a finite group from a
generating set. Section 4.2 uses it to estimate &pi;<sub><i>G</i></sub> for
candidate groups, taking generators from the LMFDB [[7]](#ref-7).
**Positioning within the author's prior work.**Three strands of the author's earlier work bear directly on the design adopted
here. The accident-detection pipeline of Thakur and Talele [[15]](#ref-15)
assigns labels zero-shot, without training on examples of the target classes.
The classifier below does the same: its profiles come from group theory and
never from labelled polynomials, so no polynomial in Table 4
could have leaked into training. The gesture detector of Thakur [[16]](#ref-16)
identifies a class from a deterministic structural signature, the projected
winding order, rather than from a learned representation; Section 4
follows that pattern and substitutes the cycle-type multiset as the signature.
The treatment of graded confidence in Thakur et al. [[17]](#ref-17) motivates the decision rule of Section 4.4,
which acts above a confidence threshold and withholds judgement below it, the
trade Table 4 quantifies. The maximum-likelihood framing and the
vocabulary of decision rules follow the classification treatment in
Thakur and Konde [[18]](#ref-18).
**Crowding rules in open scientific competitions.**The exponential factor of Equation (1) recurs across SAIR
competitions. A companion study of the Andrews-Curtis Challenge under the same
2<sup>1-<i>k</i></sup> rule [[19]](#ref-19) finds that solver competence and point value are
anti-correlated by construction, because a target is widely shared precisely
when it is easy to reach. Section 10 reports the same mechanism
operating here, which suggests the effect belongs to the scoring rule rather
than to either problem.
## Method
Figure 2 shows the pipeline. A polynomial enters, factorisation
modulo a fixed prime set produces its fingerprint, and the fingerprint is scored
against precomputed group profiles to yield either a committed label or an
abstention.
{{< Academic_Figure src="fig-2-classifier-pipeline.png" alt="The classifier. Factorisation supplies the only evidence; the profiles depend on group-theoretic data alone and never on" align="center" >}}

<p class="equation-note"><b>Figure 2.</b> The classifier. Factorisation supplies the only evidence; the profiles depend on group-theoretic data alone and never on the polynomial under test.</p>

### Fingerprints

> **Definition 1 (Fingerprint).** Fix a set <i>P</i> of primes. The *fingerprint* of <i>f</i> is the multiset
> &Lambda;(<i>f</i>, <i>P</i>) of cycle types &lambda;(<i>f</i>,<i>p</i>) taken over those <i>p</i> &isin; <i>P</i> at
> which <i>f</i> stays squarefree modulo <i>p</i>.
The implementation uses two prime sets, listed in Table 1.
Clustering needs only to decide whether two polynomials plausibly share a group,
and 24 primes suffice. Classification must name one group among thousands, which
demands more resolution, so it uses 60. Both remain inexpensive: factoring a
degree-24 polynomial modulo a small prime costs on the order of a millisecond
through python-flint.
| Purpose | Primes | Count |
|---|---|---:|
| Clustering, deduplication | 101, 103, &hellip;, 227 | 24 |
| Classification | 101, 103, &hellip;, 439 | 60 |

<p class="equation-note"><b>Table 1.</b> Prime sets. All lie above the coefficient range of the generated families, which keeps ramified primes rare.</p>

### Group profiles
For each candidate group <i>G</i> the pipeline estimates a profile &pi;&#770;<sub><i>G</i></sub> by
walking the group with product replacement [[8]](#ref-8) from
generators supplied by the LMFDB [[7]](#ref-7), recording the cycle type of each
sampled element and normalising the counts. Profiles exist for 24<i>T</i><sub>1</sub> through
24<i>T</i><sub>8000</sub>, which Section 9.1 identifies as the binding
constraint on the method as deployed.
### The classifier
Given an observation &Lambda;(<i>f</i>,<i>P</i>) and the profiles, the classifier assigns
each group the log-likelihood
<p class="equation"><i>&#8467;</i>(<i>G</i>)  =  &Sigma;<sub>&lambda; &isin; &Lambda;(<i>f</i>,<i>P</i>)</sub>
log max(&pi;&#770;<sub><i>G</i></sub>(&lambda;),&thinsp; &epsilon;),
 &nbsp;&nbsp;  &epsilon; = 10<sup>-4</sup>,</p>
<p class="equation-note">(2)</p>
and predicts argmax<sub><i>G</i></sub> <i>&#8467;</i>(<i>G</i>).

The floor &epsilon; does real work. A profile is a finite sample, so a cycle
type genuinely attainable in <i>G</i> can be missing from &pi;&#770;<sub><i>G</i></sub> by chance.
Scoring that absence as log 0 = -&infin; would eliminate the true group on a
single unlucky observation. Replacing it with a large finite penalty preserves
the ranking while keeping the true group recoverable, which turns a brittle rule
into a usable one.
| Prime <i>p</i> | Cycle type of <i>f</i> mod <i>p</i> |
|---:|---|
| 101 | 1<sup>4</sup>2<sup>2</sup>4<sup>4</sup> |
| 103 | 2<sup>4</sup>4<sup>4</sup> |
| 107 | 1<sup>4</sup>2<sup>10</sup> |
| 109 | 2<sup>4</sup>4<sup>4</sup> |
| 113 | 6<sup>4</sup> |
| 127 | 6<sup>4</sup> |
| &hellip; and 54 more primes |  |

| Rank | Candidate | <i>&#8467;</i>(<i>G</i>) |
|---:|---|---:|
| 1 | 24<i>T</i><sub>7142</sub> **(true group)** | -124.8 |
| 2 | 24<i>T</i><sub>4860</sub> | -135.2 |
| 3 | 24<i>T</i><sub>4806</sub> | -136.1 |

<p class="equation-note"><b>Table 2.</b> The method on one polynomial. Each prime contributes the cycle type of its factorisation, shown left as a partition of 24 in exponent notation, so 1<sup>4</sup>2<sup>2</sup>4<sup>4</sup> means four linear factors, two quadratic and four quartic. Summing Equation (2) over all 60 observations ranks the candidates, shown right. The leader beats the runner-up by 10.4, above the margin of 8, so the classifier commits, and it is correct. The gap is the whole decision: the ranking alone would be the same whether the evidence were decisive or not.</p>

### Abstention
A confident error costs more than silence. It sends search effort toward a group
the polynomial will not realise, and that effort is unrecoverable. The
classifier therefore commits only when the evidence separates the leader
decisively.
> **Definition 2 (Confident prediction).** Let <i>&#8467;</i><sub>(1)</sub> &ge; <i>&#8467;</i><sub>(2)</sub> denote the two largest log-likelihoods and let
> &tau; &gt; 0 be a margin. The classifier commits to the leading label when
> <i>&#8467;</i><sub>(1)</sub> - <i>&#8467;</i><sub>(2)</sub> &ge; &tau;, and abstains otherwise.
Table 2 follows one polynomial through the whole procedure, from
its factorisations to the ranked candidates and the margin that decides whether
the classifier speaks.

A margin in log-likelihood is a likelihood ratio. Setting &tau; = 8 requires the
leading group to explain the observed factorisation data at least
<i>e</i><sup>8</sup> &asymp; 2981 times better than its nearest rival. Every result below
uses &tau; = 8.
## Separability: what the evidence can decide
Accuracy is usually treated as a property of a classifier. Much of it here is a
property of the problem. Two groups whose elements have the same distribution of
cycle types cannot be told apart by factorisation at any number of primes, and
two groups whose distributions are merely close need proportionally more primes
to separate. This section makes that quantitative, which gives the experiments
something to predict rather than merely describe.
### A coefficient that bounds every decision rule
Write &#119983; for the set of cycle types available in degree 24; 231 of
them occur across the 8,000 profiles. This is the alphabet the observations
are drawn from, not the multiset &Lambda;(<i>f</i>,<i>P</i>) observed for a particular
polynomial. For a transitive <i>G</i> &le; <i>S</i><sub>24</sub> let &pi;<sub><i>G</i></sub>
be its cycle-type distribution, so &pi;<sub><i>G</i></sub>(&lambda;) is the proportion of
elements of <i>G</i> with cycle type &lambda;. For two groups define the
*Bhattacharyya coefficient*
<p class="equation">&rho;(<i>G</i>,<i>H</i>)  =  &Sigma;<sub>&lambda; &isin; &#119983;</sub> &radic;<span style="text-decoration:overline">&pi;<sub><i>G</i></sub>(&lambda;)&thinsp;&pi;<sub><i>H</i></sub>(&lambda;)</span>
   &isin;  [0,1].</p>
It equals 1 exactly when &pi;<sub><i>G</i></sub> = &pi;<sub><i>H</i></sub> and 0 when the two groups share no
cycle type. Table 3 shows a pair at &rho; = 0.99, which
makes the abstraction concrete: two groups placing almost the same mass on the
same handful of cycle types. Bhattacharyya [[10]](#ref-10) introduced it as a measure of divergence between
populations; it is the Hellinger affinity of the two distributions
[[12]](#ref-12), and it multiplies over independent observations, which is what
makes it the right currency for counting primes.
| Cycle type &lambda; | &pi;<sub><i>G</i></sub>(&lambda;) | &pi;<sub><i>H</i></sub>(&lambda;) | &radic;<span style="text-decoration:overline">&pi;<sub><i>G</i></sub> &pi;<sub><i>H</i></sub></span> |
|---|---:|---:|---:|
| 6<sup>4</sup> | 0.2433 | 0.2447 | 0.2440 |
| 12<sup>2</sup> | 0.1747 | 0.1693 | 0.1720 |
| 3<sup>4</sup>6<sup>2</sup> | 0.1557 | 0.1717 | 0.1635 |
| 3<sup>8</sup> | 0.0857 | 0.0793 | 0.0824 |
| 1<sup>4</sup>2<sup>6</sup>4<sup>2</sup> | 0.0837 | 0.0623 | 0.0722 |
| 2<sup>4</sup>4<sup>4</sup> | 0.0670 | 0.0763 | 0.0715 |
| all 16 types with mass | &rho; = 0.9900 |  |  |

<p class="equation-note"><b>Table 3.</b> Why a coefficient near 1 is fatal. <i>G</i> = 24<i>T</i><sub>3860</sub> and <i>H</i> = 24<i>T</i><sub>3789</sub> place almost the same mass on the same cycle types, so a factorisation drawn from either looks the same. The right-hand column sums to &rho; = 0.9900, and Proposition 1(ii) then forbids any method from separating them at 60 primes with error below 8%. No amount of classifier design recovers this; only more primes do.</p>

> **Proposition 1.** Let <i>G</i> and <i>H</i> be equally likely a priori, and let &lambda;<sub>1</sub>,&hellip;,&lambda;<sub><i>m</i></sub>
> be the cycle types of <i>f</i> at <i>m</i> primes unramified in both, modelled as
> independent draws from &pi;<sub><i>G</i></sub> or from &pi;<sub><i>H</i></sub>. Write &rho; = &rho;(<i>G</i>,<i>H</i>). Then
>
> 1. the likelihood-ratio test decides wrongly with probability at most
>  1&#8260;2&rho;<sup><i>m</i></sup>, and
>
> 2. every rule that sees only &lambda;<sub>1</sub>,&hellip;,&lambda;<sub><i>m</i></sub> decides wrongly
>  with probability at least
>  1&#8260;2(1 - &radic;<span style="text-decoration:overline">1 - &rho;<sup>2<i>m</i></sup></span>).

*Proof.* Under the model the two hypotheses are the product measures
<i>p</i> = &pi;<sub><i>G</i></sub><sup>&otimes; <i>m</i></sup> and <i>q</i> = &pi;<sub><i>H</i></sub><sup>&otimes; <i>m</i></sup>. The coefficient multiplies
over products, so &rho;(<i>p</i>,<i>q</i>) = &rho;<sup><i>m</i></sup>.

Under a uniform prior the least error any rule attains is the Bayes error
1&#8260;2&Sigma;<sub><i>x</i></sub> min(<i>p</i>(<i>x</i>),<i>q</i>(<i>x</i>)), achieved by the
likelihood-ratio test. For (i), min(<i>a</i>,<i>b</i>) &le; &radic;<span style="text-decoration:overline"><i>ab</i></span> for non-negative
<i>a</i> and <i>b</i>, so the Bayes error is at most
1&#8260;2&Sigma;<sub><i>x</i></sub> &radic;<span style="text-decoration:overline"><i>p</i>(<i>x</i>)<i>q</i>(<i>x</i>)</span> = 1&#8260;2&rho;<sup><i>m</i></sup>.

For (ii), the Bayes error equals
1&#8260;2(1 - &#8214; <i>p</i> - <i>q</i> &#8214;<sub>TV</sub>). Let
<i>h</i><sup>2</sup>(<i>p</i>,<i>q</i>) = &Sigma;<sub><i>x</i></sub> (&radic;<span style="text-decoration:overline"><i>p</i>(<i>x</i>)</span> - &radic;<span style="text-decoration:overline"><i>q</i>(<i>x</i>)</span>)<sup>2</sup> = 2(1 - &rho;(<i>p</i>,<i>q</i>))
be the squared Hellinger distance, written <i>h</i> rather than <i>H</i> because <i>H</i>
already denotes a group here. The standard comparison
&#8214; <i>p</i> - <i>q</i> &#8214;<sub>TV</sub> &le; <i>h</i>&radic;<span style="text-decoration:overline">1 - <i>h</i><sup>2</sup>/4</span> [[12]](#ref-12)
becomes, after substituting <i>h</i><sup>2</sup> = 2(1-&rho;(<i>p</i>,<i>q</i>)),

<p class="equation">&#8214; <i>p</i> - <i>q</i> &#8214;<sub>TV</sub> &le; &radic;<span style="text-decoration:overline">1 - &rho;(<i>p</i>,<i>q</i>)<sup>2</sup></span>
 = &radic;<span style="text-decoration:overline">1 - &rho;<sup>2<i>m</i></sup></span> .</p>

Since no rule beats the Bayes error, every rule errs with probability at least
1&#8260;2(1 - &radic;<span style="text-decoration:overline">1-&rho;<sup>2<i>m</i></sup></span>). &#9633;
The two halves do different work, and conflating them is the easiest mistake to
make with a bound of this kind. Part (i) states when success is guaranteed and
says nothing otherwise, so a pair it fails to cover may still be classified
correctly. Part (ii) forbids: a group whose nearest competitor sits at &rho;
cannot be named more reliably than the stated figure, whatever classifier is
used and however the evidence is weighed. The negative result in
Section 8 rests on (ii) alone.
> **Corollary 2.** To hold the pairwise error below &delta; &lt; 1&#8260;2 it suffices to use
>
> <p class="equation"><i>m</i> &ge; (log(1/2&delta;))&#8260;(log(1/&rho;))</p>
>
> primes. Against <i>N</i> candidate groups rather than two, a union bound over the
> <i>N</i>-1 competitors replaces &delta; by &delta;/(<i>N</i>-1), so the requirement grows
> only as log <i>N</i>: multiplying the size of the candidate set by ten costs a fixed
> number of additional primes, not a fixed factor.

{{< Academic_Figure src="fig-3-separability-bound.png" alt="The bound of Proposition 1(ii): the smallest error any method can achieve when a group's nearest competitor sits at coef" align="center" >}}

<p class="equation-note"><b>Figure 3.</b> The bound of Proposition 1(ii): the smallest error any method can achieve when a group's nearest competitor sits at coefficient &rho;. The vertical line marks the 60 primes this work spent. At &rho;=0.95 that budget is ample, at the measured median of 0.98 it is adequate, and beyond 0.995 it leaves an error floor no classifier can remove. Section 5.2 gives the measured distribution of &rho;, and Table 6 the accuracy that results.</p>

### What the bound predicts here
For a group <i>G</i> the binding quantity is its nearest competitor anywhere in the
profile set,
<p class="equation">&rho;<sup>*</sup>(<i>G</i>)  =  max<sub><i>H</i> &ne; <i>G</i></sub> &rho;(<i>G</i>,<i>H</i>),</p>
computed once from the profiles alone and independent of any polynomial.
Across the 8,000 profiles, &rho;<sup>*</sup> has median 0.9805, ninetieth percentile
0.9984 and maximum 0.9999. Figure 4 gives the whole
distribution. The candidate set is crowded: for a typical group some other group
produces almost the same factorisation statistics, and only 4.9% of groups have
a competitor further away than &rho; = 0.9.

Corollary 2 converts this into a prime count. Driving the
pairwise error below 5% against the nearest competitor takes a median of 117
primes, so the 60 the classifier uses guarantee that error rate for only 31.0%
of groups. Applying the union bound over all 7,999 competitors raises the
median requirement to 573 primes. Two predictions follow, and
Section 8 tests both.
1. Accuracy should fall as &rho;<sup>*</sup> rises, and should stay below the
 ceiling 1 - 1&#8260;2(1-&radic;<span style="text-decoration:overline">1-&rho;<sup>*2<i>m</i></sup></span>) that part
 (ii) imposes at <i>m</i> = 60.
2. Accuracy should not yet have saturated at 60 primes, since the budget
 falls well short of what the sufficiency direction asks for.

{{< Academic_Figure src="fig-4-crowding-distribution.png" alt="Nearest-competitor distance across the 8,000 profiled groups, by lower edge of each band. Only 394 groups, 4.9% of the s" align="center" >}}

<p class="equation-note"><b>Figure 4.</b> Nearest-competitor distance across the 8,000 profiled groups, by lower edge of each band. Only 394 groups, 4.9% of the set, have a competitor further than &rho; = 0.9; most sit above 0.95. The candidate set is crowded almost everywhere, which is what Figure 3 converts into an error floor.</p>

### What the model idealises
Two idealisations enter, and both work against the bound's reliability rather
than for it.

Chebotarev is an asymptotic statement. It gives the density of primes whose
Frobenius class lies in a given conjugacy class, not independence across a
fixed finite set of 60 small primes. Treating the observations as independent
draws is an approximation, and Proposition 1 inherits it.
Effective forms of the theorem exist [[11]](#ref-11), but their error
terms are governed by the discriminant of the splitting field, which for a
degree-24 field is far too large for a bound at 60 primes near 100 to say
anything useful. The approximation is therefore not one this paper can
discharge by citing a sharper theorem, which is why it is tested empirically
instead. The
approximation is the same one the classifier itself makes, so the bound and the
method stand or fall together, which is why the empirical test in
Section 8 carries the weight.

Second, &pi;<sub><i>G</i></sub> is not known exactly. The profiles estimate it from 3,000
product-replacement samples for each group, so &rho; is itself an estimate.
Sampling noise biases that estimate downward where two distributions are
genuinely close, because two finite samples drawn from one distribution do not
give &rho; = 1. The separability figures above are therefore optimistic at the
hard end, and the true crowding is at least as severe as reported.
## Experimental setup

**Ground truth.**The SAIR evaluation server computes the 24<i>T</i><sub><i>t</i></sub> label of each submitted
polynomial in Magma [[13]](#ref-13) and returns it with the verification response.
The campaign accumulated 576,682 labelled polynomials spanning 3,995
distinct labels. This ground truth is unusually strong for a study of this
kind. The labels come from a different method, resolvent computation rather
than statistics; from a different implementation, which the author never
ran and could not inspect; and from a party with no stake in the
classifier's performance, namely the competition organisers [[6]](#ref-6). Nothing in the evaluation depends on the
author's own judgement of what a polynomial's group is, which is the usual
weak point in a study that proposes a classifier and then measures it.
**Domain of evaluation.**The classifier can name only a group it holds a profile for. Among the labelled
polynomials, 54,350, or 9.4%, carry a true label inside the profiled range.
Drawing an evaluation sample uniformly from the corpus would therefore cap
measured accuracy near 9.4% however well the method discriminates, reporting
profile coverage under the name of predictive power. This paper separates the
two: Section 7 measures accuracy inside the domain, and
Section 9.1 reports coverage as the distinct limitation it is.
**Protocol.**From the in-domain polynomials the evaluation drew 600 uniformly at random under
a fixed seed. No evaluation polynomial influenced any profile, since profiles
derive from group-theoretic data alone.
## Results

| Measure | Value | 95% interval |
|---|---:|---:|
| Top-1 accuracy | 414 / 600 = 69.0% | [65.2%, 72.6%] |
| Top-3 accuracy | 532 / 600 = 88.7% | [85.9%, 91.0%] |
| Confident commitments | 76 / 600 = 12.7% |  |
| Confident precision | 76 / 76 = 100% | &ge; 95.2% |
| Abstentions | 524 / 600 = 87.3% |  |
| Time per polynomial, reference | 409 ms |  |
| Time per polynomial, vectorised | 53 ms |  |

<p class="equation-note"><b>Table 4.</b> Classifier performance on 600 polynomials drawn from the in-domain portion of the server-labelled corpus, at margin &tau; = 8. Intervals are Wilson score intervals [[14]](#ref-14). The two timings run the same classifier and return the same rankings; the campaign used the reference implementation, and Section 8.3 explains the difference.</p>
Table 4 reports the measurement, and three points follow from
it.
**The classifier ranks well even when it does not lead correctly.**Top-1 accuracy reaches 69.0% and top-3 reaches 88.7%. The gap shows that
failures are usually failures of separation rather than of candidacy: the true
group sits among the leaders but does not pull clear of them. Groups with
similar cycle-type distributions produce exactly this signature, which is what
Section 7.1 predicts and what motivates abstention.
**Confident mode made no errors on this sample.**The classifier committed 76 times and was right 76 times. A point estimate of 1
says little on its own, so the honest summary is an interval. For <i>x</i> = <i>n</i>
successes in <i>n</i> trials the Wilson score lower bound [[14]](#ref-14) collapses to
<p class="equation">(<i>n</i>)&#8260;(<i>n</i> + <i>z</i><sup>2</sup>)
 =  (76)&#8260;(76 + 1.96<sup>2</sup>)
 =  (76)&#8260;(79.84)
 =  0.952 ,</p>
<p class="equation-note">(3)</p>
so the data support precision of at least 95.2% at the 95% level. The claim
this paper makes is "no errors in 76 commitments, precision at least 95.2%",
not an unqualified 100%.
**The method trades recall for precision by design.**The classifier abstains on 87.3% of inputs. A general-purpose identification
tool operating there would be close to useless. A targeting tool operating there
is well placed, because an abstention costs only that the pipeline treats the
polynomial as unknown and explores it anyway, while a confident error costs
search effort spent against a group that will never appear.
### Why similar groups bound the method
The ceiling is structural, not an artefact of sample size. Two groups sharing a
cycle-type distribution are indistinguishable to any amount of factorisation
evidence, because Equation (2) reads only that distribution. More
primes sharpen the estimate of which distribution generated the data; they
cannot separate two groups that induce the same one. Raising top-1 accuracy
beyond a certain point therefore requires evidence outside factorisation
patterns, such as a resolvent, and not merely a longer prime list.
### Choice of margin
The margin &tau; slides the operating point along a precision-recall curve
without altering the classifier. Lowering &tau; buys coverage and admits
errors; raising it does the reverse. This work fixed &tau; = 8 during the
campaign, on a different
sample, and reports it here unchanged rather than tuning it to the evaluation.
## Analysis
Section 7 reports what the classifier does. This section asks
why, along the three axes the hypotheses of Section 1.2 name:
how much evidence the method needs, where its mistakes fall
(Section 8.2), and whether the separability bound of
Section 5 describes the behaviour observed. All three experiments run on the same 600 in-domain
polynomials at the same margin, and the script that produces them,
`scripts/analysis.py`, is in the repository.

Scoring 8,000 candidate groups for every prefix of the prime list would be
prohibitive one group at a time, so the analysis scores all groups at once as a
matrix product. That reimplementation earns its place only if it agrees with
the released predictor, and it does: on 25 polynomials the two rank candidates
identically, and at 60 primes the matrix scorer reproduces the accuracy, top-3
rate and coverage of Table 4 exactly. The experiments below
therefore measure the classifier this paper reports, not a variant of it.
### How many primes the classifier needs
Factorisation dominates the cost, so the prime count is the parameter worth
tuning. Because the log-likelihood is a sum over observations, scores at <i>m</i>
primes are a prefix of the scores at 60, and a single factorisation pass yields
every row of Table 5.
| Primes | Top-1 | Top-3 | Coverage | Confident precision |
|---:|---:|---:|---:|---:|
| 5 | 7.0% | 14.8% | 0.0% | no commitments |
| 10 | 19.8% | 32.7% | 0.3% | 2 of 2 |
| 15 | 29.7% | 48.0% | 0.7% | 4 of 4 |
| 20 | 39.5% | 58.2% | 1.5% | 9 of 9 |
| 30 | 50.0% | 72.7% | 3.7% | 22 of 22 |
| 40 | 61.5% | 82.0% | 6.8% | 41 of 41 |
| 50 | 64.0% | 84.5% | 9.0% | 54 of 54 |
| 60 | 69.0% | 88.7% | 12.7% | 76 of 76 |

<p class="equation-note"><b>Table 5.</b> Accuracy against the number of primes, on the same 600 in-domain polynomials. The final row is the operating point of Table 4. Accuracy is still climbing at the right-hand edge, and confident precision holds at every budget.</p>

{{< Academic_Figure src="fig-5-accuracy-vs-primes.png" alt="Accuracy against prime count. Neither curve has flattened at 60 primes, the budget this work deployed, so the operating " align="center" >}}

<p class="equation-note"><b>Figure 5.</b> Accuracy against prime count. Neither curve has flattened at 60 primes, the budget this work deployed, so the operating point sits on the rising part of the curve rather than at a saturation point.</p>
Two findings follow. First, accuracy has not saturated. The last ten primes add
5.0 points of top-1 accuracy and 4.2 of top-3, and raise confident coverage from
9.0% to 12.7%. Figure 5 shows both curves still rising at the
right-hand edge. H4 is therefore false as stated: 60 primes was a budget, not a
measured optimum, and the measurement says the budget was set too low. This
matches the second prediction of Section 5.2, which put the
median requirement near 117 primes. The cost of correcting it is mild, since
factorisation at one more prime costs under a millisecond, and
Section 8.3 gives the arithmetic.

Second, confident precision holds at 100% at every budget, across commitments
ranging from 2 to 76. The margin rule is not tuned to the operating point; it
survives a twelvefold change in the evidence available to it. This is the
clearest support for H3, and it is stronger evidence than the single
operating-point figure in Table 4, which a favourable sample
could produce by chance.
### Where the mistakes fall
Section 5.2 predicts that accuracy tracks &rho;<sup>*</sup>, the
coefficient between a group and its nearest competitor. Because &rho;<sup>*</sup>
depends only on the profiles, it is fixed before any polynomial is examined,
so grouping the test set by it tests a prediction rather than describing an
outcome.
| Nearest competitor &rho;<sup>*</sup> | Polynomials | Top-1 accuracy | Ceiling |
|---|---:|---:|---:|
| below 0.95 | 75 | 100.0% (95.1&ndash;100.0) | 100.0% |
| 0.95 to 0.99 | 335 | 81.2% (76.7&ndash;85.0) | 99.3% |
| 0.99 to 0.999 | 156 | 37.8% (30.6&ndash;45.6) | 84.8% |
| 0.999 and above | 34 | 23.5% (12.4&ndash;40.0) | 62.1% |

<p class="equation-note"><b>Table 6.</b> Accuracy against the crowding of the true group's neighbourhood, with 95% Wilson intervals. The ceiling is the largest accuracy Proposition 1(ii) permits any method at 60 primes, evaluated at the midpoint of each band. Accuracy falls monotonically as crowding rises and respects the ceiling in every band.</p>
Table 6 confirms the prediction. Accuracy falls from
100.0% to 23.5% across the four bands, monotonically, and in no band does it
exceed the ceiling that Proposition 1(ii) allows. Where the theory
says the problem is easy, in the 75 polynomials whose groups have a distant
nearest competitor, the classifier makes no mistakes at all. Where the theory
says the problem is nearly undecidable at 60 primes, accuracy collapses. The
evidence supports H2.

The gap between the measured accuracy and the ceiling widens as crowding
increases, from nothing in the first band to 47 points in the third. Two
readings are available and the data here does not separate them. The bound may
be loose, since the Bhattacharyya inequality is not tight; or the classifier may
lose ground to the true optimum exactly where discrimination is hardest. The
ceiling is also a pairwise quantity applied to an 8,000-way problem, which
makes it conservative as an upper bound on accuracy. What the table establishes
is the direction and the ordering, not the size of the gap.

A second, weaker comparison points the same way. Taking each polynomial's
strongest rival, the highest-ranked group other than the true one, the median
coefficient between truth and rival is 0.9684 when the classifier is right and
0.9867 when it is wrong. Comparing the true group with the *predicted*
group instead would be vacuous, since a correct prediction names the true group
and scores 1 by construction. This comparison carries a confound the bands in
Table 6 do not: the rival is the runner-up when the
classifier is right and the leader when it is wrong, so the two cases sit at
different ranks. This comparison corroborates Table 6; it
does not carry the argument.

When the classifier is wrong it is rarely far wrong. The true label has median
rank 3 among 8,000 candidates and lies within the top ten for 91.4% of
errors. The failure is one of discrimination among near-identical candidates,
not of misdirection, which is what Table 6 would lead one
to expect and what makes the top-3 figure and the abstention rule useful.
### Cost
The reference implementation scores one candidate group at a time and runs at
409 ms per polynomial. Scoring all 8,000 groups as a single matrix product
leaves every ranking unchanged and brings this to roughly 53 ms, of which
35 ms is factorisation and 17 ms scoring. That 17 ms covers the eight
prefixes of Table 5 rather than a single prediction, so it
overstates the cost of one call.

The consequence matters more than the speedup. Once the scorer handles all
groups at once, factorisation dominates, and factorisation costs roughly
0.6 ms per prime, linear in the budget. Buying the 57 extra primes that Section 5.2
asks for would cost about 35 ms per polynomial, less than the saving just
described. The budget that Table 5 shows to be too low can be
corrected without exceeding the cost of the implementation this work actually
deployed.
### The hypotheses
H1 holds: 69.0% top-1 accuracy inside the profiled range, against a candidate
set of 8,000 and with no computer algebra system, exceeds the more-often-than-not
threshold with a 95% interval of 65.2% to 72.6%.

H2 holds. Accuracy falls monotonically across four bands of increasing
crowding, a quantity fixed before any polynomial is seen, and respects the
information-theoretic ceiling in each band.

H3 holds, and more strongly than the operating point alone shows. Confident
precision is 100% at every one of eight prime budgets, across 2 to 76
commitments.

H4 fails. Accuracy is still rising at 60 primes, so the deployed budget was too
small. The separability analysis predicted this before the ablation was run,
and Section 8.3 shows the correction is affordable. Reporting the
prediction and the refutation together is the point: the bound earns confidence
by forecasting a result that contradicted the design in use.
## Limitations
Three limitations bound what the method can claim, and
Section 9.4 collects the threats to the validity of the
measurements themselves.
### Coverage binds before accuracy does
The dominant practical constraint is silence, not error. Profiles cover 8,000
of the 25,000 groups, and the labelled corpus concentrates outside that range:
90.6% of labelled polynomials realise a group the classifier holds no profile
for. Table 7 sets the two limits side by side. Extending
coverage is a matter of computation rather than research, and it is the single
highest-value improvement available to this method.
|  | Count | Share |
|---|---:|---:|
| Transitive groups of degree 24 | 25,000 |  |
| &nbsp;&nbsp; with a sampled profile | 8,000 | 32.0% |
| Server-labelled polynomials | 576,682 |  |
| &nbsp;&nbsp; whose true label has a profile | 54,350 | 9.4% |
| &nbsp;&nbsp; outside the profiled range | 522,332 | 90.6% |
| Distinct labels observed in the corpus | 3,995 |  |

<p class="equation-note"><b>Table 7.</b> Coverage, which bounds deployment more tightly than accuracy does. A uniform sample of the corpus would cap measured top-1 accuracy at 9.4%.</p>

### Fingerprint novelty overstates group novelty
A fingerprint is a statistic, not a separating invariant. Distinct groups can
share a cycle-type distribution, and in this data many do, so the map from
fingerprints to labels is many-to-one in the direction that matters. Joining the
campaign ledger to the server's labels shows the consequence: roughly 10,000
fingerprint clusters that the pipeline judged novel collapsed to roughly 771
genuinely new (24<i>T</i><sub><i>t</i></sub>, <i>r</i>) pairs, an overstatement exceeding an order of
magnitude.

The methodological lesson generalises beyond this competition. A search pipeline
that counts distinct fingerprints as distinct discoveries will report progress
it has not made. Novelty has to be measured against labels, never against the
statistic used to predict them.
### Evidence, not proof
A confident prediction is evidence. Chebotarev guarantees equidistribution in
the limit, 60 primes form a finite sample, and the floor &epsilon; in
Equation (2) softens the likelihood further. The method suits
search direction and does not suit any setting that requires a certificate.
Where certainty matters, a resolvent computation remains necessary.
### Threats to validity
Four threats bear on the conclusions above.

*Sample size.* Every accuracy figure rests on 600 in-domain polynomials.
The Wilson intervals quantify this, and the narrowest conclusions, such as the
ordering in Table 6, survive comfortably. The 34
polynomials in the most crowded band give an interval from 12.4% to 40.0%,
wide enough that the value of that band should be read as an order of
magnitude.

*Corpus composition.* The evaluation corpus is what the campaign submitted,
not a uniform sample of degree-24 polynomials. Submissions favoured groups the
search targeted, so the distribution of true labels is not the natural one. The
in-domain restriction removes the largest distortion but not this one, and the
accuracy reported here describes performance on polynomials of the kind this
campaign generated.

*Profile estimation.* Profiles rest on 3,000 product-replacement samples
per group. Product-replacement approximates uniform sampling without
guaranteeing it at a fixed number of steps, so a systematic bias in the sampler
would propagate to every profile. Section 5.3 notes the
direction of the resulting error in &rho;.

*Independence.* Proposition 1 and the classifier both treat
cycle types at distinct primes as independent draws. Chebotarev licenses this
asymptotically, not at 60 fixed small primes. The empirical agreement in
Table 6 is evidence that the approximation holds well
enough to be useful here; it is not a proof that it holds, a distinction
Section 9.3 draws out.
## Application and outcome
The campaign used the classifier to steer submission batches toward groups that
the competition's intelligence endpoints reported as unclaimed or weakly held,
following Equation (1). Fingerprint-based deduplication kept
batches distinct, and the ledger recorded 610,718 clusters across the
campaign.

The final standing was rank 54 of 256 teams, scoring 2.3559 across 10,180
scoreable pairs. The distance between a five-figure count of scoreable pairs and
a score near two is entirely the exponential factor of
Equation (1): the pairs obtained were, in the main, pairs other
teams also held. This is the empirical shape of the same effect the companion
Andrews-Curtis study reports under the identical rule [[19]](#ref-19). Volume proved
achievable and rarity did not, and only rarity pays.
## Conclusion
Factorisation data alone identifies the Galois group of a degree-24 polynomial
often enough to be useful, and under a calibrated abstention rule reliably
enough to act on. The measured operating point is 69.0% top-1 accuracy, 88.7%
top-3, and no errors across 76 confident commitments, a precision of at least
95.2% at 95% confidence, obtained in 53 ms per polynomial without a computer
algebra system.

What distinguishes this account from a report of measurements is that the
measurements were predicted. Proposition 1 turns the geometry of
the candidate set into a ceiling on the accuracy of any method whatsoever, and
that ceiling is computable from group theory before a single polynomial is
factored. It called both results correctly: accuracy tracks the crowding of a
group's neighbourhood, falling from 100% to 23.5% across four bands while
staying under the ceiling in each, and the 60-prime budget this work deployed
is too small, a verdict the ablation then confirmed. A bound that contradicts
the design in use, and turns out to be right, has earned more trust than one
that ratifies it.

The limitations carry as much information as the result. Coverage, not accuracy,
prevents deployment at scale, and computation alone would remedy it. Fingerprint
novelty overstates group novelty by more than an order of magnitude, which traps
any search pipeline that measures its own progress by the statistic it uses to
predict labels rather than by the labels themselves. The honest summary is that
the method works where the mathematics says it can, fails where the mathematics
says it must, and now carries the means to tell the two cases apart in advance.
Section 11 lists the scripts that regenerate every table above.
## Data and code availability
All code and data live at
<https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24>
[[20]](#ref-20). The classifier is `scripts/predict_label.py` and the
fingerprint routine is `scripts/fingerprint.py`. Two scripts regenerate
the tables: `scripts/evaluate_predictor.py` reproduces
Table 4, and `scripts/analysis.py` reproduces
Tables 5 and 6 together with the
separability figures of Section 5.2, writing its output as JSON.
The directory `data/` holds the group profiles, the server-labelled
corpus and the submission ledger.

The evaluation sample is drawn under a fixed seed, so the 600 polynomials
behind every table are the same 600 on any machine. Reproducing the paper needs
Python 3.10 or later, `python-flint` for factorisation and NumPy. It
needs no computer algebra system, which is the point of the method.

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra" (Sep 2026). https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2026chebotarev,
  title   = "Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra",
  author  = "Thakur, Amey",
  year    = "2026",
  month   = "Sep",
  url     = "https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24"
}
```

---

## References

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">[1]</span>
    <span class="reference-text"><a id="ref-1"></a><b>N. Chebotarev</b>, "Die Bestimmung der Dichtigkeit einer Menge von Primzahlen, welche zu
einer gegebenen Substitutionsklasse geh&ouml;ren," <i>Mathematische Annalen, 95:191&ndash;228, 1926</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>R. P. Stauduhar</b>, "The determination of Galois groups," <i>Mathematics of Computation, 27(124):981&ndash;996, 1973</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>C. Fieker and J. Kl&uuml;ners</b>, "Computation of Galois groups of rational polynomials," <i>LMS Journal of Computation and Mathematics, 17(1):141&ndash;158, 2014</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>G. Malle and B. H. Matzat</b>, "*Inverse Galois Theory*," <i>Springer Monographs in Mathematics. Springer, 2nd edition, 2018</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>J.-P. Serre</b>, "*Topics in Galois Theory*," <i>Research Notes in Mathematics. Jones and Bartlett, 1992</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>J. Jones, J. Paulhus, D. Roe, A. Sutherland, and T. Tao</b>, "SAIR Inverse Galois Problem Challenge at degree 24," <i>SAIR Foundation, in collaboration with the LMFDB, 16 June to 15 August 2026</i>, <a href="https://competition.sair.foundation/competitions/igp24/overview">https://competition.sair.foundation/competitions/igp24/overview</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>The LMFDB Collaboration</b>, "The L-functions and Modular Forms Database," <i>, 2026</i>, <a href="https://www.lmfdb.org">https://www.lmfdb.org</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>F. Celler, C. R. Leedham-Green, S. H. Murray, A. C. Niemeyer, and E. A. O'Brien</b>, "Generating random elements of a finite group," <i>Communications in Algebra, 23(13):4931&ndash;4948, 1995</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>The PARI Group</b>, "PARI/GP, version 2.15," <i>Universit&eacute; de Bordeaux, 2026</i>, <a href="https://pari.math.u-bordeaux.fr">https://pari.math.u-bordeaux.fr</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>A. Bhattacharyya</b>, "On a measure of divergence between two statistical populations defined
by their probability distributions," <i>Bulletin of the Calcutta Mathematical Society, 35:99&ndash;109, 1943</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>J. C. Lagarias and A. M. Odlyzko</b>, "Effective versions of the Chebotarev density theorem," <i>In Algebraic Number Fields, pages 409&ndash;464. Academic Press, 1977</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>L. Le Cam</b>, "*Asymptotic Methods in Statistical Decision Theory*," <i>Springer, New York, 1986</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[13]</span>
    <span class="reference-text"><a id="ref-13"></a><b>W. Bosma, J. Cannon, and C. Playoust</b>, "The Magma algebra system I: the user language," <i>Journal of Symbolic Computation, 24(3&ndash;4):235&ndash;265, 1997</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[14]</span>
    <span class="reference-text"><a id="ref-14"></a><b>E. B. Wilson</b>, "Probable inference, the law of succession, and statistical inference," <i>Journal of the American Statistical Association, 22(158):209&ndash;212, 1927</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[15]</span>
    <span class="reference-text"><a id="ref-15"></a><b>A. Thakur and S. Talele</b>, "A modular zero-shot pipeline for accident detection, localization, and
classification in traffic surveillance video," <i>arXiv:2604.09685, 2026</i>, <a href="https://arxiv.org/abs/2604.09685">https://arxiv.org/abs/2604.09685</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[16]</span>
    <span class="reference-text"><a id="ref-16"></a><b>A. Thakur</b>, "Frame-synchronous hand gesture detection by projected winding order," <i>arXiv:2609.13269, 2026a</i>, <a href="https://arxiv.org/abs/2609.13269">https://arxiv.org/abs/2609.13269</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[17]</span>
    <span class="reference-text"><a id="ref-17"></a><b>A. Thakur, K. Dhiman, and M. Phansikar</b>, "Neuro-fuzzy: artificial neural networks and fuzzy logic," <i>International Journal for Research in Applied Science and Engineering Technology, 9(9):128&ndash;135, 2021. `10.22214/ijraset.2021.37930`</i>, <a href="https://doi.org/10.22214/ijraset.2021.37930">https://doi.org/10.22214/ijraset.2021.37930</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[18]</span>
    <span class="reference-text"><a id="ref-18"></a><b>A. Thakur and A. Konde</b>, "Fundamentals of neural networks," <i>International Journal for Research in Applied Science and Engineering Technology, 9(VIII):407&ndash;426, 2021. `10.22214/ijraset.2021.37362`</i>, <a href="https://doi.org/10.22214/ijraset.2021.37362">https://doi.org/10.22214/ijraset.2021.37362</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[19]</span>
    <span class="reference-text"><a id="ref-19"></a><b>A. Thakur</b>, "Length as priority, not constraint: search geometry of the
Andrews-Curtis Challenge pool," <i>SAIR Andrews-Curtis Challenge, Proof Track, 2026</i>, <a href="https://github.com/Amey-Thakur/SAIR-ANDREWS-CURTIS-CHALLENGE">https://github.com/Amey-Thakur/SAIR-ANDREWS-CURTIS-CHALLENGE</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[20]</span>
    <span class="reference-text"><a id="ref-20"></a><b>A. Thakur</b>, "SAIR Inverse Galois Problem IGP24: search pipeline, classifier and
campaign data," <i>Software and dataset, 2026</i>, <a href="https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24">https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24</a> [Accessed: Sep. 20, 2026].</span>
</div>

</div>