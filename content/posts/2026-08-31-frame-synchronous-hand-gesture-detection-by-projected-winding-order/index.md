---
title: "Frame-Synchronous Hand Gesture Detection by Projected Winding Order"
date: 2026-08-31T21:40:12-04:00
draft: false
author: "Amey Thakur"
summary: "Gesture recognition on video is normally posed as classification: assign a label to each frame, then act on the label. That formulation is adequate for control, where a command may be obeyed several frames late without a user noticing, and inadequate for *synchronisation*, where an output must be aligned to the frame on which the gesture physically occurred. We take the synchronisation problem for a specific and common movement, the rotation of an open hand about its own long axis, and show that it admits an exact solution requiring no classifier, no training data and no calibration. Let s denote the normalised two-dimensional cross product of the two palm edges, taken at the wrist and the two outer knuckles, under the projection the camera already performs."
tags: ["Computer Vision", "Gesture Recognition", "Hand Tracking", "Real-Time Systems", "WebGL", "Browser", "Non-Photorealistic Rendering", "Projective Geometry", "MediaPipe", "Human-Computer Interaction", "TypeScript", "On-Device Inference", "Signal Processing"]
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

{{< Academic_Figure src="social_preview.png" alt="Title card: Frame-Synchronous Hand Gesture Detection by Projected Winding Order, by Amey Thakur." align="center" >}}

<div align="center">

**[arXiv:2609.13269](https://arxiv.org/abs/2609.13269)** &nbsp;·&nbsp;
**[Code](https://github.com/Amey-Thakur/GESTURE-FX)** &nbsp;·&nbsp;
**[Live demo](https://amey-thakur.github.io/GESTURE-FX/)**

</div>

> This is the paper in full, as announced on arXiv as **[arXiv:2609.13269](https://arxiv.org/abs/2609.13269)**. The code that produced every figure, and a demo that runs in the browser, are at **[Amey-Thakur/GESTURE-FX](https://github.com/Amey-Thakur/GESTURE-FX)**.

## Abstract

Gesture recognition on video is normally posed as classification: assign a label
to each frame, then act on the label. That formulation is adequate for control,
where a command may be obeyed several frames late without a user noticing, and
inadequate for *synchronisation*, where an output must be aligned to the
frame on which the gesture physically occurred. We take the synchronisation
problem for a specific and common movement, the rotation of an open hand about
its own long axis, and show that it admits an exact solution requiring no
classifier, no training data and no calibration.

Let <i>s</i> denote the normalised two-dimensional cross product of the two palm
edges, taken at the wrist and the two outer knuckles, under the projection the
camera already performs. We prove that <i>s</i> factorises as <i>k</i>(&theta;)cos&theta;
with |<i>k</i>(&theta;)| &gt; 0 everywhere, so that <i>s</i> vanishes if and only if the palm
is edge-on and its sign tracks the face presented to the camera. Detecting the
gesture therefore reduces to locating a zero crossing of a single scalar, which
yields an instant rather than an interval. We further prove that the criterion
is invariant to image mirroring, to hand scale and to handedness, and that these
follow from the algebraic form rather than from any property of the estimator
supplying the landmarks.

A second, two-handed interaction uses four fingertips as the corners of a
window onto a restyled version of the same scene. We give the coverage predicate
this requires, showing that the triangulation ordinarily used is unsound the
moment the hands cross and that an even-odd test is both correct there and
cheaper, and we derive the three operators that fill the window: an iterated
edge-preserving filter whose range width must vary across iterations for a reason
we quantify, a quantiser whose amplification of residual noise we bound, and a
difference of Gaussians whose noise response we compute in closed form and use to
fix its one free mixing parameter.

We embed both in a browser system in which landmark inference is rate limited
well below the display rate and each recognised gesture carries the timestamp of
its cause, so that presentation quality is independent of inference throughput.
The system composites effects onto the recorded surface rather than the camera
stream, so no editing stage is required. In its default configuration it runs
entirely on the client, with no server, no key and no per-use cost; two optional
paths depart from this, are disabled until enabled by the user, and are accounted
for rather than elided.

Against a corpus with exact ground truth the criterion detects 95% of flips
with no false positive in 240 near-miss sequences, and places each detection
within 6.7 ms on average of the instant it occurred: a sixth of the interval
at which the hand is observed. Reporting an event more finely than one samples is
the practical consequence of treating a gesture as the zero of a continuous
quantity rather than as a label attached to a frame, and it is unavailable to a
classifier operating on the same stream. We state plainly what remains
unverified.
**Keywords.** Gesture Recognition &middot; Hand Tracking &middot; Projective Geometry &middot;
Real-Time Video &middot; Human Computer Interaction &middot; On-Device Inference
## Introduction
A gesture recogniser that drives an interface is judged by whether it eventually
fires. A gesture recogniser that drives a *visual effect inside a recording*
is judged by *when* it fires, because the viewer sees the gesture and its
consequence in the same footage and will attribute one to the other only if they
coincide. An effect placed two hundred milliseconds after a hand movement does
not read as caused by it; it reads as a coincidence.

This distinction is not usually drawn. The dominant formulation labels frames and
acts on labels, which returns an interval during which a gesture was judged to be
in progress. Recovering a single instant from such an interval is not well posed:
the interval's boundaries are artefacts of the classifier's confidence profile,
and that profile is at its worst exactly where the instant lies. During the fast
middle of a hand rotation the hand is motion blurred and self-occluding, so a
classifier is least certain precisely when certainty is required.

We show that for one important gesture the instant can be obtained directly, and
exactly, from projective geometry.
**Contributions.**
1. A criterion for detecting the rotation of an open hand about its long
 axis as the zero crossing of a single scalar computed from three
 landmarks, with a proof that the crossing coincides exactly with the
 edge-on configuration (Theorem 1).
2. Proofs that the criterion is invariant under image mirroring, under
 uniform scaling of the hand, and under exchange of handedness
 (Propositions 1&ndash;3), all following
 from its algebraic form rather than from the landmark estimator.
3. A coverage predicate for the two-hand window that remains correct when
 the quadrilateral self-intersects, with the exact area by which the
 triangulation it replaces overdraws in that case
 (Proposition 6, Corollary 2).
4. An analytic realisation of the three-representation cartoon
 decomposition, in which each of the three free parameters is fixed by a
 derived quantity rather than by inspection: the range schedule by the
 expected attenuation under sensor noise
 (Proposition 7), the band-selection neighbourhood by the
 quantiser's slope (13), and the contour operator's mixing
 fraction by its closed-form noise response
 (Proposition 8).
5. Sub-frame localisation of the event by interpolating the zero between
 the two samples that bracket it, with a proof that the error is second
 order in the sampling interval where reporting either sample is first
 order (Proposition 5), and a measurement showing
 the mean absolute error falling from 23.0 ms to 6.7 ms.
6. A generated corpus with exact ground truth, and the argument for
 generating rather than filming it, which is that the crossing frame is
 not observable in video to a precision finer than the quantity being
 measured (Section 6).
7. A rate-decoupled compositing architecture in which a trigger carries the
 timestamp of its cause, making the smoothness of the response
 independent of inference throughput (Section 4.6).
8. A bounded temporal buffer permitting retrospective compositing, which
 obtains an effect otherwise requiring generative synthesis from
 information the stream has already delivered
 (Section 4.7).
9. A statement of the condition under which a window tracked in one clip
 may be composited over a generatively restyled version of it, and of why
 that condition can be requested but not enforced
 (Proposition 10).
10. A complete client-side implementation, released under the MIT licence,
 with the components that were verified and those that were not reported
 separately (Sections 5&ndash;7).

## Related Work

### Hand pose estimation
Recovering hand keypoints from a single view was for a long time limited by the
cost of annotation, since a hand is small, frequently self-occluded, and tedious
to label. Simon et al. [[1]](#ref-1) broke the dependency by bootstrapping
annotations across a multi-camera rig, using detections that succeed in one view
to supervise the views in which they fail. The resulting detectors were
integrated into the multi-person pose framework of Cao et al. [[2]](#ref-2),
which established the part-affinity formulation for associating keypoints into
skeletons.

Those systems target accuracy on server hardware. The mobile line of work
instead fixes a latency budget and designs within it. Bazarevsky et al. [[3]](#ref-3)
introduced a detector architecture tuned for mobile GPUs, extended to the body
in Bazarevsky et al. [[4]](#ref-4) and to the hand in
Zhang et al. [[5]](#ref-5), the last of which supplies the two-stage design
we build on: a palm detector run intermittently, followed by a landmark
regressor confined to the detected region, assembled in the pipeline framework
of Lugaresi et al. [[6]](#ref-6).

We take such an estimator as given and contribute downstream of it. This matters
for the scope of our results: the invariances in Section 4.3
are properties of the projection, not of any network, and therefore hold for any
estimator whose output is a projection of the hand.
### Classical hand analysis
Before learned estimators, hand gestures were recognised by pipelines assembled
from the primitives collected in OpenCV [[7]](#ref-7): skin-tone
segmentation, contour extraction, convex hulls, and convexity defects to count
extended fingers. These are sensitive to illumination, background and skin tone,
which is precisely what learned landmark estimation removed.

It is worth being clear that the quantity we use is of the same kind as the ones
those pipelines computed. A signed area over three points is a classical
primitive, and had reliable landmark correspondences been available it could
have been evaluated then. The contribution here is not the primitive but the
observation that this particular one resolves the synchronisation problem
exactly. The containment test of Section 4.9 belongs to the same
family as the one a quadtree applies at every node, deciding which axis-aligned
region a point falls in; Thakur et al. [[8]](#ref-8) builds that index for the
interactive display of large point sets, where the cost of repeating the test is
what bounds the frame rate. The problem here is the same in kind and smaller by
orders of magnitude: four edges, once per fragment.
### Gesture recognition from landmarks
Given landmarks, two families dominate. Learned classifiers map the landmark
vector, or a window of them, to a gesture label; the real-time architecture of
K{&ouml;}p{&uuml;}kl{&uuml;} et al. [[9]](#ref-9) is representative, pairing a lightweight detector
with a deeper classifier so that the expensive model runs only when a gesture is
plausibly in progress. Rule-based recognisers instead threshold derived
quantities such as joint angles and finger extension.
The two are ends of a spectrum rather than alternatives: a neuro-fuzzy system
keeps the rules and learns their parameters instead of fixing them by hand, which
is the middle ground surveyed by Thakur et al.(2021{})Thakur, Dhiman, and
 Phansikar [[10]](#ref-10). The learned end
produces its per-frame label from a parameterised network trained by gradient
descent, and the models and learning rules that make one, from the limitations of
the perceptron to the rectified unit that answers them, are set out in
Thakur and Konde [[11]](#ref-11).

Both families return a per-frame decision, and therefore an interval once
aggregated over time. Our criterion is rule-based in implementation but is not a
tuned rule: it is a closed-form consequence of the projection, and the
thresholds around it gate evidence quality rather than define the gesture. That
distinction is what allows a claim of exactness in
Theorem 1 that a tuned rule could not support.
### Locating a gesture in time
Two literatures address directly the question of where a gesture sits in a
stream. Gesture spotting separates gestures from the movements between them in a
continuous signal; the threshold model of Lee and Kim [[12]](#ref-12) is the
canonical treatment, adding a garbage state against which candidate gestures
compete so that a segmentation falls out of the recognition rather than being
imposed before it. Temporal action localisation asks the same question of
untrimmed video and answers it with proposals scored and refined by a network, in
the multi-stage form of Shou et al. [[13]](#ref-13).

Both return a segment. That is the right output for their purposes, and it is one
step short of what synchronisation needs: a segment has two boundaries and the
instant we require is interior to it, so recovering the instant means positing a
further rule over the segment. The boundaries are also where these methods are
least certain, since they are defined by the decay of a score rather than by any
event. The criterion here differs in kind rather than in accuracy. It does not
locate a segment and then reduce it; the quantity it evaluates has a zero, the
zero is the event, and there is nothing left to reduce.
### Optical flow as a temporal cue
When the question is when something moved rather than what shape it took, dense
optical flow is the usual instrument, most often in the polynomial-expansion
formulation of Farneb{&auml;}ck [[14]](#ref-14). It is the cue used for temporal
localisation in the modular surveillance pipeline of
Thakur and Talele [[15]](#ref-15), where the event to be located is a collision and
flow magnitude peaks sharply at it.

Flow is poorly matched to the present problem. The gesture here is a rigid
rotation passing through a particular orientation, and flow magnitude is
elevated across the whole fast portion of that rotation rather than at its
midpoint. Using it would reproduce the interval problem rather than resolve it.
The distinction is between locating motion and locating a configuration, and
only the latter admits the exact treatment of Section 4.3.
### Filtering noisy interactive input
Landmark estimates jitter by a small but visible fraction of the frame even when
the hand is stationary, and any geometry built from them inherits that jitter. A
fixed low-pass filter trades jitter against lag and cannot serve both a
stationary and a moving hand. Casiez et al. [[16]](#ref-16) resolve this with a filter
whose cutoff rises with the estimated speed of the signal, so that a slow signal
is smoothed heavily and a fast one is followed closely.

The corner filter in Section 4.8 is of this family. We depart from
the original in one respect that matters for our architecture: because inference
runs at a rate well below the display rate and that rate varies with load, we
rescale the smoothing coefficient to the elapsed interval, so the filter's
behaviour in wall-clock time is invariant to the inference rate.
### Appearance transformation of video
Restyling a subject is well studied as a learned image-to-image problem. The
adversarial formulation it usually takes, a generator trained against a
discriminator until its output is not separable from the target distribution,
and the variants that formulation has since acquired, are surveyed by
Thakur and Satish(2021{}) [[17]](#ref-17). Two instances of it matter here. White-box
cartoonisation [[18]](#ref-18) learns an explicitly decomposed
representation, a surface carrying flat regions, a structure carrying segmented
colour and a texture carrying contours, rather than an opaque mapping; it is that
decomposition, and not its training, that Section 4.10 reproduces
analytically. Open-domain sketch-to-photo synthesis [[19]](#ref-19) must
produce photographic content for sketch classes absent from its training set,
which is the sharpest case of the property at issue. Such methods synthesise
content absent from the input, which is exactly what allows them to replace a
subject and exactly what makes them unsuitable under a constraint of zero
marginal cost and bounded latency: a generative model of useful quality is either
hosted, and therefore metered, or too slow for interactive compositing.

We use an analytic shader instead, and are explicit in
Section 7 that this restyles the subject present in the
frame rather than replacing it. The distinction is stated because it is the one
a reader is most likely to assume away.
### Browser implementations
Several browser demonstrations composite effects over hand-tracked geometry, and
the two-hand framing gesture in particular has an established following. In the
survey we conducted before implementation, every such system terminated at a
live preview: none encoded the composited output, and none stated a detection
criterion that could be evaluated or reproduced. Where the interior of such a
frame is restyled, video is routed to a hosted generative model, which
reintroduces a server, a key and a per-use cost, and shifts the latency from
frames to seconds or minutes.
## Problem Formulation
Let V = (<i>I</i><sub>1</sub>, <i>I</i><sub>2</sub>, &hellip;) be a video stream with frame <i>I</i><sub><i>t</i></sub>
observed at time <i>t</i>. Let &Lambda; be a landmark estimator producing, for each
observed frame, a set of hand landmark configurations in normalised image
coordinates.
> **Definition 1 (Synchronisation problem).** Given a gesture <i>G</i> occurring physically over the interval [<i>t</i><sub><i>a</i></sub>, <i>t</i><sub><i>b</i></sub>] with a
> distinguished instant <i>t</i><sup>&#8902;</sup> &isin; [<i>t</i><sub><i>a</i></sub>, <i>t</i><sub><i>b</i></sub>], produce an estimate
> <i>t</i>&#770;<sup>&#8902;</sup> and a composited stream V' in which a designated
> transformation is applied from <i>t</i>&#770;<sup>&#8902;</sup> onward, such that
> |<i>t</i>&#770;<sup>&#8902;</sup> - <i>t</i><sup>&#8902;</sup>| is below perceptual tolerance and V' is
> encoded without a subsequent editing stage.
Three constraints distinguish this from classification.

**The instant is the deliverable.** A classifier estimates the support
[<i>t</i><sub><i>a</i></sub>, <i>t</i><sub><i>b</i></sub>]. Reducing that support to a point requires a rule that the
classifier does not supply, and any such rule is sensitive to the confidence
profile at the boundaries.

**Evidence is worst where it is needed.** <i>t</i><sup>&#8902;</sup> lies in the interior of
the movement, where angular velocity is highest, where motion blur is greatest,
and where self-occlusion is most severe. Landmark confidence is therefore
minimised at the instant to be recovered.

**Inference and presentation compete.** Let <i>C</i><sub>&Lambda;</sub> be the per-frame
cost of landmark estimation and <i>C</i><sub><i>R</i></sub> that of rendering. Naively evaluating both
at the display rate <i>f</i><sub><i>d</i></sub> requires <i>f</i><sub><i>d</i></sub>(<i>C</i><sub>&Lambda;</sub> + <i>C</i><sub><i>R</i></sub>), and since
<i>C</i><sub>&Lambda;</sub> &Gt; <i>C</i><sub><i>R</i></sub> on commodity mobile hardware this caps the system at the
inference rate. Section 4.6 removes the coupling.
## Method

### The projected palm winding
Let <i>P</i><sub>0</sub>, <i>P</i><sub>5</sub>, <i>P</i><sub>17</sub> &isin; &#8477;<sup>3</sup> denote the wrist, the index knuckle and
the little finger knuckle in a hand-fixed frame, with the <i>y</i> axis along the
hand's long axis and the <i>z</i> axis out of the palm. These three points span the
palm plane and are, among the 21 landmarks, the three least affected by finger
articulation.

Let <i>R</i><sub>&theta;</sub> be rotation about the long axis by &theta; and let
&pi;(<i>x</i>, <i>y</i>, <i>z</i>) = (<i>x</i>, <i>y</i>) be orthographic projection. Write the projected edges as
<p class="equation"><i>v</i><sub>1</sub>(&theta;) = &pi;(<i>R</i><sub>&theta;</sub> <i>P</i><sub>5</sub>) - &pi;(<i>R</i><sub>&theta;</sub> <i>P</i><sub>0</sub>),
   &nbsp;&nbsp; 
  <i>v</i><sub>2</sub>(&theta;) = &pi;(<i>R</i><sub>&theta;</sub> <i>P</i><sub>17</sub>) - &pi;(<i>R</i><sub>&theta;</sub> <i>P</i><sub>0</sub>).</p>
<p class="equation-note">(1)</p>

> **Definition 2 (Projected palm winding).** <p class="equation"><i>s</i>(&theta;) = (<i>v</i><sub>1</sub>(&theta;) &times; <i>v</i><sub>2</sub>(&theta;))&#8260; &#8214; <i>v</i><sub>1</sub>(&theta;) &#8214; &thinsp; &#8214; <i>v</i><sub>2</sub>(&theta;) &#8214;,
>  &nbsp;&nbsp; 
>  <i>a</i> &times; <i>b</i> = <i>a</i><sub><i>x</i></sub> <i>b</i><sub><i>y</i></sub> - <i>a</i><sub><i>y</i></sub> <i>b</i><sub><i>x</i></sub> .</p>
> <p class="equation-note">(2)</p>
The numerator is twice the signed area of the projected triangle
<i>P</i><sub>0</sub> <i>P</i><sub>5</sub> <i>P</i><sub>17</sub>; dividing by the edge lengths gives the sine of the angle
between them, so <i>s</i> &isin; [-1, 1]. Its sign is the winding order of that triangle
under projection.
### The crossing theorem

> **Theorem 1 (Exact crossing).** Write the unrotated projected edges as <i>v</i><sub>1</sub>(0) = (<i>a</i>, <i>b</i>) and <i>v</i><sub>2</sub>(0) = (<i>c</i>, <i>d</i>),
> and let &kappa; = <i>ad</i> - <i>bc</i>. If &kappa; &ne; 0 then for all &theta;
>
> <p class="equation"><i>s</i>(&theta;) = <i>k</i>(&theta;)cos&theta;,
>  &nbsp;&nbsp; 
>  <i>k</i>(&theta;) = &kappa;&#8260;(&#8214; <i>v</i><sub>1</sub>(&theta;) &#8214; &thinsp; &#8214; <i>v</i><sub>2</sub>(&theta;) &#8214;),</p>
> <p class="equation-note">(3)</p>
>
> with |<i>k</i>(&theta;)| &gt; 0 for every &theta;. Consequently
>
> <p class="equation">sign <i>s</i>(&theta;) = sign(&kappa;)sign(cos&theta;),
>  &nbsp;&nbsp; and &nbsp;&nbsp; 
>  <i>s</i>(&theta;) = 0 &hArr; &theta; &equiv; &pi;&#8260;2 (mod &pi;).</p>
> <p class="equation-note">(4)</p>

*Proof.* Rotation about the <i>y</i> axis maps (<i>x</i>, <i>y</i>, <i>z</i>) to
(<i>x</i>cos&theta; + <i>z</i>sin&theta;, <i>y</i>, -<i>x</i>sin&theta; + <i>z</i>cos&theta;). The three
landmarks lie in the palm plane <i>z</i> = 0, so after projection the <i>x</i> components
are scaled by cos&theta; and the <i>y</i> components are unchanged:
<i>v</i><sub>1</sub>(&theta;) = (<i>a</i>cos&theta;,&thinsp; <i>b</i>) and <i>v</i><sub>2</sub>(&theta;) = (<i>c</i>cos&theta;,&thinsp; <i>d</i>). Hence

<p class="equation"><i>v</i><sub>1</sub>(&theta;) &times; <i>v</i><sub>2</sub>(&theta;)
 = (<i>a</i>cos&theta;)<i>d</i> - <i>b</i>(<i>c</i>cos&theta;)
 = (<i>ad</i> - <i>bc</i>)cos&theta;
 = &kappa;cos&theta; ,</p>
<p class="equation-note">(5)</p>

which gives (3) on dividing by the norms. Both norms are
bounded below by min(|<i>b</i>|, |<i>d</i>|) &gt; 0, since <i>b</i> and <i>d</i> are the components along
the axis of rotation and are unaffected by &theta;; the knuckles are displaced
from the wrist along the hand, so neither vanishes. Therefore |<i>k</i>(&theta;)| &gt; 0.
Because <i>k</i> never changes sign, the sign of <i>s</i> is that of &kappa;cos&theta;,
and <i>s</i> vanishes exactly where cos&theta; does. &#9633;

> **Corollary 2 (Instant recovery).** A change of sign of <i>s</i> observed between two sampled frames localises
> &theta; = &pi;/2 to the interval between them. The estimate <i>t</i>&#770;<sup>&#8902;</sup> is
> therefore accurate to the sampling interval of the estimator, independently of
> any confidence the estimator reports.
This is the property the formulation was chosen for. The sampling interval, not
the classifier's certainty during the fastest part of the movement, bounds the
error.
{{< Academic_Figure src="geometry.png" alt="The projected palm triangle at three rotations, computed rather than drawn. Left: palm toward the camera, positive windi" align="center" >}}

<p class="equation-note"><b>Figure 1.</b> The projected palm triangle at three rotations, computed rather than drawn. Left: palm toward the camera, positive winding. Centre: edge-on, the projected triangle has no area and <i>s</i> = 0, which is the trigger. Right: back toward the camera, winding reversed. The printed values are those the implementation reads for the model hand used in the figure.</p>
Figure 1 shows the configuration at
&theta; &isin; {0, &pi;/2, &pi;}. Note that |<i>s</i>(0)| = 0.647 &ne; 1: the magnitude
depends on the angle subtended at the wrist and hence on the individual hand.
Only the sign and the zero are exact, and Theorem 1 claims only
those.
### Invariance
The following hold for the criterion itself, and therefore for any landmark
estimator whose output is a projection of the hand.
> **Proposition 3 (Mirror invariance).** Let <i>M</i>(<i>x</i>, <i>y</i>) = (-<i>x</i>, <i>y</i>) be reflection about the vertical axis, as applied to a
> front-facing camera preview. Then <i>s</i> &compfn; <i>M</i> = -<i>s</i>, and the zero set is
> unchanged.

*Proof.* Reflection is linear, so the reflected edges are <i>Mv</i><sub>1</sub>(&theta;) and
<i>Mv</i><sub>2</sub>(&theta;). Using <i>v</i><sub>1</sub>(&theta;) = (<i>a</i>cos&theta;, <i>b</i>) and
<i>v</i><sub>2</sub>(&theta;) = (<i>c</i>cos&theta;, <i>d</i>) from the proof of Theorem 1,

<p class="equation"><i>Mv</i><sub>1</sub>(&theta;) &times; <i>Mv</i><sub>2</sub>(&theta;)
 = (-<i>a</i>cos&theta;)<i>d</i> - <i>b</i>(-<i>c</i>cos&theta;)
 = -(<i>ad</i> - <i>bc</i>)cos&theta;
 = -&thinsp;<i>v</i><sub>1</sub>(&theta;) &times; <i>v</i><sub>2</sub>(&theta;),</p>
<p class="equation-note">(6)</p>

while &#8214; <i>Mv</i> &#8214; = &#8214; <i>v</i> &#8214; since <i>M</i> is an isometry. Hence
<i>s</i> &#8614; -<i>s</i> for every &theta;. The zero set of -<i>s</i> equals that of <i>s</i>, so a
crossing at a given instant remains a crossing at that instant. &#9633;
Mirroring is thus a global sign convention. A detector keyed on a *change*
of sign is unaffected, whereas one keyed on an absolute sign, such as a
palm-versus-back classifier, requires the convention to be tracked.
> **Proposition 4 (Scale invariance).** For any &lambda; &gt; 0, <i>s</i> is unchanged under (<i>v</i><sub>1</sub>, <i>v</i><sub>2</sub>) &#8614; (&lambda; <i>v</i><sub>1</sub>, &lambda; <i>v</i><sub>2</sub>).

*Proof.* The numerator is bilinear and so scales by &lambda;<sup>2</sup>; the denominator is a
product of two norms and so scales by &lambda;<sup>2</sup>. The quotient is homogeneous of
degree zero. &#9633;
Hand size and distance from the lens act as such a &lambda; under orthographic
projection, so neither enters the criterion. No per-user calibration exists in
the implementation.
> **Proposition 5 (Chirality).** A left and a right hand differ in the sign of &kappa;. The detection criterion
> is unaffected.

*Proof.* The two hands are related by reflection, which by the argument of
Proposition 1 negates &kappa;. By
Theorem 1 the zero set of <i>s</i> is independent of
sign&kappa;, and the detector is defined by a sign change of <i>s</i>,
which is likewise independent of it. &#9633;

> **Proposition 6 (Degeneracy).** &kappa; = 0 if and only if the wrist and the two knuckles are collinear in the
> palm plane.

*Proof.* Immediate: &kappa; is twice the signed area of the triangle they span. &#9633;
This configuration does not occur in a hand, so the hypothesis of
Theorem 1 is satisfied in practice. It is nonetheless the
correct failure mode to state, since a landmark estimator that collapses the
three points would produce <i>s</i> &equiv; 0 and no crossing.
### From a crossing to a decision
Theorem 1 localises the instant but does not by itself
distinguish a deliberate flip from any other rotation. The implementation gates
the crossing with four conditions, each removing a failure observed during
development:
1. |<i>s</i>| &ge; &tau;<sub>arm</sub> sustained for 120 ms before the
 crossing, rejecting a hand that enters the field already rotating;
2. at least three fingers extended, rejecting a rotating fist and a
 conversational wrist turn;
3. the transit from |<i>s</i>| &le; &tau;<sub>cross</sub> to the opposite face
 completing within [20, 600] ms. The lower bound excludes a crossing
 that begins and ends inside one sample, which is what a single inverted
 landmark frame produces, and is far below the duration of a turn because
 it times the passage through edge-on rather than the turn: a hand that
 takes 300 ms to turn over is edge-on for some 40 ms of it, and a
 guard set at the duration of a turn rejects most real flips. The upper
 bound excludes a hand brought to edge-on and held there, not a hand
 turned over slowly, which passes through edge-on quickly whatever its
 overall pace and is the same gesture at a different speed;
4. the opposite face reaching |<i>s</i>| &ge; &tau;<sub>confirm</sub>, rejecting
 a wobble toward edge-on that returns.
Thresholds gate evidence quality; they do not define the gesture, which is
defined by the crossing. The asymmetry of the design is deliberate: a missed
gesture costs one repetition, whereas a spurious one corrupts a recording that
cannot be repeated, so every default is biased toward the former.
### Recovering the instant between samples
Theorem 1 places the gesture at the zero of <i>s</i>. A detector
observes <i>s</i> only at the sampling instants, and the zero almost never coincides
with one, so reporting the sample at which <i>s</i> was first observed inside a band
about zero places the gesture early by about half the time the signal spends
inside that band. At the rate this system tracks at, that error is tens of
milliseconds and is visible: the effect begins before the hand has finished
turning.

The zero is recoverable between samples. Let <i>t</i><sub><i>a</i></sub> be the last sampling instant
carrying the sign presented before the rotation and <i>t</i><sub><i>b</i></sub> the first carrying the
opposite sign. The reported instant is the linear interpolant,
<p class="equation"><i>t</i>&#770;<sup>&#8902;</sup> = <i>t</i><sub><i>a</i></sub> + (<i>t</i><sub><i>b</i></sub> - <i>t</i><sub><i>a</i></sub>)&thinsp;(|<i>s</i>(<i>t</i><sub><i>a</i></sub>)|)&#8260;(|<i>s</i>(<i>t</i><sub><i>a</i></sub>)| + |<i>s</i>(<i>t</i><sub><i>b</i></sub>)|).</p>
<p class="equation-note">(7)</p>

> **Proposition 7 (Second-order localisation).** If the rotation rate is constant over [<i>t</i><sub><i>a</i></sub>, <i>t</i><sub><i>b</i></sub>], the error of
> (7) is <i>O</i>(&Delta; <i>t</i><sup>2</sup>) in the sampling interval, whereas
> reporting either bracketing sample is <i>O</i>(&Delta; <i>t</i>).

*Proof.* By Theorem 1, <i>s</i>(<i>t</i>) = <i>k</i>(&theta;(<i>t</i>))cos&theta;(<i>t</i>) with <i>k</i>
smooth and non-vanishing. Writing &theta;(<i>t</i>) = &pi;/2 + &omega;(<i>t</i> - <i>t</i><sup>&#8902;</sup>) for a
constant rate &omega; gives cos&theta;(<i>t</i>) = -sin(&omega;(<i>t</i> - <i>t</i><sup>&#8902;</sup>)), whose
Taylor expansion about <i>t</i><sup>&#8902;</sup> is -&omega;(<i>t</i> - <i>t</i><sup>&#8902;</sup>) + <i>O</i>((<i>t</i>-<i>t</i><sup>&#8902;</sup>)<sup>3</sup>).
Hence <i>s</i> is linear in <i>t</i> about the zero up to a cubic remainder, and <i>k</i>
contributes a smooth factor whose variation over an interval of length &Delta; <i>t</i>
is <i>O</i>(&Delta; <i>t</i>) relative. Linear interpolation of a function that is linear to
that order recovers its zero with an error of the order of the neglected terms,
which is <i>O</i>(&Delta; <i>t</i><sup>2</sup>). Reporting <i>t</i><sub><i>a</i></sub> or <i>t</i><sub><i>b</i></sub> instead incurs the full
distance to the zero, which is <i>O</i>(&Delta; <i>t</i>). &#9633;
Section 6 measures this: the interpolant reduces the mean
absolute localisation error from 23.0 ms to 6.7 ms and removes a
22.1 ms bias, at the cost of one division and two stored samples.
### Rate-decoupled compositing
Let <i>f</i><sub>&Lambda;</sub> be the rate at which the estimator is evaluated and <i>f</i><sub><i>d</i></sub> the
display rate, with <i>f</i><sub>&Lambda;</sub> &Lt; <i>f</i><sub><i>d</i></sub>. Let a recognised gesture emit a trigger
(<i>t</i>&#770;<sup>&#8902;</sup>, <i>e</i>) carrying the estimated causal instant and an effect
identifier, and let the effect be a function <i>E</i>(<i>u</i>) of normalised progress
<i>u</i> &isin; [0, 1] over duration <i>D</i>. We render at <i>f</i><sub><i>d</i></sub> with
<p class="equation"><i>u</i>(<i>t</i>) = (<i>t</i> - <i>t</i><sub>0</sub>)&#8260;(<i>D</i>),
   &nbsp;&nbsp; 
  <i>t</i><sub>0</sub> = max(<i>t</i>&#770;<sup>&#8902;</sup>,  <i>t</i><sub><i>c</i></sub> - &Delta;),</p>
<p class="equation-note">(8)</p>
where <i>t</i><sub><i>c</i></sub> is the confirmation time and &Delta; a bound on backdating.

Two consequences follow. Effect playback is sampled at <i>f</i><sub><i>d</i></sub> regardless of
<i>f</i><sub>&Lambda;</sub>, so reducing the inference rate degrades recognition latency and not
smoothness. And because <i>t</i><sub>0</sub> is anchored to the cause rather than to the
detection, the effect occupies the correct position in the encoded output even
though it was decided later. The clamp by &Delta; ensures the onset is not
skipped when confirmation is slow, at the cost of a bounded misalignment; we use
&Delta; = 120 ms.

The distinction is the one a distributed system draws between when an event
happened and when a process learned of it. Ordering by a clock read at the
observer orders by arrival, which is a property of the network rather than of the
events; Lamport's happened-before relation orders by cause instead, and the
physical algorithms that narrow the gap sit alongside the logical and vector
clocks that sidestep it in Thakur and Satish [[20]](#ref-20). Anchoring the timeline on
<i>t</i>&#770;<sup>&#8902;</sup> rather than on <i>t</i><sub><i>c</i></sub> is the same choice made for the same reason:
the confirmation time is a property of the rate at which the hand is sampled, not
of the gesture.
### Retrospective compositing
Some desired effects require content absent from the current frame. Substituting
the subject requires synthesis. Substituting the *moment*, however, requires
only memory.

We retain a circular buffer of <i>N</i> frames at reduced resolution, captured at
<i>f</i><sub><i>b</i></sub> &Lt; <i>f</i><sub><i>d</i></sub>, holding <i>N</i> / <i>f</i><sub><i>b</i></sub> seconds of history. On a trigger the compositor
selects
<p class="equation"><i>F</i><sup>&#8902;</sup> = argmin<sub><i>i</i></sub> | &tau;<sub><i>i</i></sub> - (<i>t</i> - <i>D</i><sub><i>r</i></sub>) |</p>
<p class="equation-note">(9)</p>
for a requested delay <i>D</i><sub><i>r</i></sub>, where &tau;<sub><i>i</i></sub> is the capture time of buffered frame
<i>i</i>. Nearest-in-time rather than oldest is used so the effective delay remains
meaningful while the buffer is filling and does not jump when it wraps. With
<i>N</i> = 24, <i>f</i><sub><i>b</i></sub> = 8 Hz and quarter resolution the cost is approximately
5.5 MB of texture memory for three seconds of history.
### The two-hand frame
A second interaction uses both hands. Four fingertips, two per hand, define a
quadrilateral used as a window onto a restyled version of the same scene. Corners
are held in anatomical order, so a corner corresponds to a fixed fingertip for
the lifetime of the gesture and smoothing requires no correspondence search;
crossing the hands yields a self-intersecting quadrilateral that recovers when
they uncross, since the ordering is stateless.

Landmark noise is the dominant difficulty: fingertip estimates move by a
noticeable fraction of the frame while the hands are still, and a window whose
boundary shimmers is unusable regardless of its contents. We smooth each corner
with a velocity-adaptive exponential filter in the manner of
Casiez et al. [[16]](#ref-16), whose coefficient is rescaled to the elapsed interval,
<p class="equation">&alpha;<sub>&Delta; <i>t</i></sub> = 1 - (1 - &alpha;<sub>60</sub>)<sup>&Delta; <i>t</i> / &Delta; <i>t</i><sub>60</sub></sup>,</p>
<p class="equation-note">(10)</p>
so that the filter behaves identically at any inference rate, and we apply
hysteresis to both gates, since a hand rotating toward the camera foreshortens
and would otherwise cross a fixed threshold downward.
### Coverage of the window
The window is a region a fragment shader must fill, so the quadrilateral has to
become a predicate. The obvious construction, and the one we adopted first,
splits it into the triangle fan <i>F</i>(<i>Q</i>) = <i>T</i>(<i>c</i><sub>0</sub>,<i>c</i><sub>1</sub>,<i>c</i><sub>2</sub>)&cup; <i>T</i>(<i>c</i><sub>0</sub>,<i>c</i><sub>2</sub>,<i>c</i><sub>3</sub>) and
tests membership of either. That is sound only while the quadrilateral is
convex, and the anatomical ordering above guarantees that it is not always:
crossing the hands exchanges one hand's two corners and yields a
self-intersecting boundary. In that state the fan does not degrade gracefully.
It covers most of the bounding rectangle, which is visible as the stylised
region abruptly leaving the hands.

We use the even-odd rule instead: a point lies inside when a ray cast from it
meets the closed boundary an odd number of times [[21]](#ref-21). Write
<i>E</i>(<i>Q</i>) for that region.
> **Proposition 8 (Coverage).** Let <i>Q</i> be the closed polyline <i>c</i><sub>0</sub><i>c</i><sub>1</sub><i>c</i><sub>2</sub><i>c</i><sub>3</sub><i>c</i><sub>0</sub> in general position.
>
> 1. If <i>Q</i> is simple and the diagonal <i>c</i><sub>0</sub><i>c</i><sub>2</sub> lies in its interior, then
>  <i>F</i>(<i>Q</i>) = <i>E</i>(<i>Q</i>).
>
> 2. If the edges <i>c</i><sub>0</sub><i>c</i><sub>1</sub> and <i>c</i><sub>2</sub><i>c</i><sub>3</sub> meet at a point <i>x</i> interior to both,
>  then
>
> <p class="equation"><i>E</i>(<i>Q</i>) = <i>T</i>(<i>c</i><sub>0</sub>,<i>x</i>,<i>c</i><sub>3</sub>)&thinsp;&cup;&thinsp;<i>T</i>(<i>c</i><sub>1</sub>,<i>c</i><sub>2</sub>,<i>x</i>) &sube; <i>F</i>(<i>Q</i>),</p>
>
> and the inclusion is strict.

*Proof.* For (i), an interior diagonal partitions a simple quadrilateral into exactly the
two triangles of the fan, and the even-odd region of a simple closed curve is its
interior. For (ii), cutting <i>Q</i> at <i>x</i> decomposes the boundary into two closed
simple loops, <i>c</i><sub>0</sub> &rarr; <i>x</i> &rarr; <i>c</i><sub>3</sub> &rarr; <i>c</i><sub>0</sub> and <i>x</i> &rarr; <i>c</i><sub>1</sub> &rarr; <i>c</i><sub>2</sub> &rarr; <i>x</i>, meeting
only at <i>x</i> and each traversed once. A ray from a point interior to either loop
meets the boundary an odd number of times and a ray from a point exterior to both
meets it an even number, which is the stated union. Containment in <i>F</i>(<i>Q</i>) is
immediate because each lobe has its three vertices in one triangle of the fan,
and both triangles are convex. Strictness holds because <i>x</i> is interior to
<i>c</i><sub>0</sub><i>c</i><sub>1</sub>, so the triangle <i>T</i>(<i>c</i><sub>0</sub>,<i>c</i><sub>1</sub>,<i>c</i><sub>2</sub>) of the fan contains a neighbourhood of
points on the far side of <i>c</i><sub>0</sub><i>x</i> from <i>c</i><sub>3</sub>; such points lie in no lobe, since
each lobe is bounded by <i>c</i><sub>0</sub><i>x</i> and <i>xc</i><sub>1</sub> respectively. The corollary below
measures the excess in one symmetric case. &#9633;

> **Corollary 9.** For the crossed unit square <i>c</i><sub>0</sub>=(0,1), <i>c</i><sub>1</sub>=(1,0), <i>c</i><sub>2</sub>=(1,1), <i>c</i><sub>3</sub>=(0,0),
> the edges <i>c</i><sub>0</sub><i>c</i><sub>1</sub> and <i>c</i><sub>2</sub><i>c</i><sub>3</sub> meet at (1&#8260;2,1&#8260;2) and
>
> <p class="equation">|<i>E</i>(<i>Q</i>)| = 1&#8260;2, &nbsp;&nbsp; |<i>F</i>(<i>Q</i>)| = 3&#8260;4 .</p>
>
> The fan therefore covers half as much area again as the window, and one third of
> what it draws lies outside it.
The predicate costs four half-open vertical comparisons and at most four
divisions. The fan it replaces costs a signed area for each of the five distinct
edges of its two triangles, ten multiplications, so correctness here is obtained
at a lower price than the failure it replaces.
### Stylising the interior
The window shows the same scene in another medium. We compute the three
representations of the white-box formulation [[18]](#ref-18)
analytically rather than learning them, which removes the model but keeps the
decomposition: a surface carrying flat interiors, a structure carrying quantised
colour, and a texture carrying contours.
**Surface.**An iterated bilateral filter [[22]](#ref-22), in the manner
established for real-time abstraction by Winnem{&ouml;}ller et al. [[23]](#ref-23),
<p class="equation"><i>I</i><sup>(<i>m</i>+1)</sup>(<i>x</i>) = 1&#8260;(<i>Z</i>(<i>x</i>)) &Sigma;<sub><i>y</i> &isin; N(<i>x</i>)</sub> <i>I</i><sup>(<i>m</i>)</sup>(<i>y</i>)&thinsp;
    exp(-(&#8214;<i>y</i>-<i>x</i>&#8214;<sup>2</sup>)&#8260;(2&sigma;<sub><i>s</i></sub><sup>2</sup>))
    exp(-(&#8214;<i>I</i><sup>(<i>m</i>)</sup>(<i>y</i>)-<i>I</i><sup>(<i>m</i>)</sup>(<i>x</i>)&#8214;<sup>2</sup>)&#8260;(2&sigma;<sub><i>r</i></sub><sup>(<i>m</i>)2</sup>)),</p>
<p class="equation-note">(11)</p>
with <i>Z</i> the sum of the weights. One pass suppresses noise; a short sequence
collapses each region onto its own colour while leaving boundaries in place, and
it is that flatness rather than any outline that makes the result read as drawn.

The range width &sigma;<sub><i>r</i></sub><sup>(<i>m</i>)</sup> is not held constant across the sequence, and
the reason is quantitative rather than aesthetic.
> **Proposition 10 (Range attenuation under sensor noise).** Let two pixels of one surface differ only by independent sensor noise, each of
> <i>C</i> channels distributed N(0,&sigma;<sub><i>n</i></sub><sup>2</sup>). The expected range weight
> in (11) is
>
> <p class="equation">E[exp(-(&#8214;&Delta; <i>I</i>&#8214;<sup>2</sup>)&#8260;(2&sigma;<sub><i>r</i></sub><sup>2</sup>))]
>  = (1 + (2&sigma;<sub><i>n</i></sub><sup>2</sup>)&#8260;(&sigma;<sub><i>r</i></sub><sup>2</sup>))<sup>-<i>C</i>/2</sup>.</p>

*Proof.* &Delta; <i>I</i> has independent N(0,2&sigma;<sub><i>n</i></sub><sup>2</sup>) components, so
&#8214;&Delta; <i>I</i>&#8214;<sup>2</sup>/(2&sigma;<sub><i>n</i></sub><sup>2</sup>) &sim; &chi;<sup>2</sup><sub><i>C</i></sub>. Writing <i>t</i>=&sigma;<sub><i>n</i></sub><sup>2</sup>/&sigma;<sub><i>r</i></sub><sup>2</sup>,
the expectation is the moment generating function of &chi;<sup>2</sup><sub><i>C</i></sub> evaluated at
-<i>t</i>, which is (1+2<i>t</i>)<sup>-<i>C</i>/2</sup>. &#9633;
For <i>C</i>=3 the consequence is direct. A filter with &sigma;<sub><i>r</i></sub>=0.09 retains a
weight of 0.74 between two samples of a surface carrying &sigma;<sub><i>n</i></sub>=0.03, and
averages the noise away; against &sigma;<sub><i>n</i></sub>=0.06, which is an ordinary amount in
a dim room, the weight falls to 0.39 and the filter defends each grain as
though it were an edge. Widening to &sigma;<sub><i>r</i></sub>=0.24 restores 0.84. The schedule
is therefore coarse to fine, &sigma;<sub><i>r</i></sub> = (0.24,&thinsp;0.14,&thinsp;0.09): the first pass
averages, and the passes after it restore the boundaries the first softened.
**Structure.**Tone is quantised in luminance with a controlled edge,
<p class="equation"><i>Q</i>(<i>L</i>) = <i>q</i> + (&Delta; <i>q</i>)&#8260;2tanh(&phi;&thinsp;(<i>L</i>-<i>q</i>)&#8260;(&Delta; <i>q</i>)),
   &nbsp;&nbsp;  <i>q</i> = &Delta; <i>q</i> round(<i>L</i>/&Delta; <i>q</i>),</p>
<p class="equation-note">(12)</p>
and the colour is rescaled by <i>Q</i>(<i>L</i>)/<i>L</i>, which flattens the shading and holds the
hue. Rounding the three channels independently, which is what a posterisation
does, moves a colour toward a vertex of the unit cube and turns skin green.

Differentiating (12),
<p class="equation"><i>Q</i>'(<i>L</i>) = &phi;&#8260;2sech<sup>2</sup>(&phi;(<i>L</i>-<i>q</i>)&#8260;(&Delta; <i>q</i>))
   &le;  &phi;&#8260;2,</p>
<p class="equation-note">(13)</p>
with equality at a band centre. The quantiser is thus an amplifier of whatever
variation reaches it, by a factor of &phi;/2 = 3.5 at the setting we use.
Variation the surface has reduced below visibility is returned above it, and a
large flat region whose tone sits near a band boundary flickers between two
levels. We therefore select the band from a five-tap mean of the surface
luminance with weights (2,1,1,1,1)/6, whose variance factor is
&Sigma; <i>w</i><sub><i>i</i></sub><sup>2</sup> / (&Sigma; <i>w</i><sub><i>i</i></sub>)<sup>2</sup> = 8/36 = 2/9; the input standard deviation falls by
&radic;<span style="text-decoration:overline">2/9</span> = 0.471 and the effective amplification with it, to 1.65. Only the
choice of band is made from a neighbourhood: the colour is still read per pixel,
so no edge is softened.
**Texture.**Line work is a difference of Gaussians [[24]](#ref-24),
<p class="equation"><i>D</i><sub>&sigma;</sub> = <i>G</i><sub>&sigma;</sub> * <i>L</i> - <i>G</i><sub><i>k</i>&sigma;</sub> * <i>L</i>,  &nbsp;&nbsp;  <i>k</i> = 1.6,</p>
<p class="equation-note">(14)</p>
thresholded in the manner of the extended operator of
Winnem{&ouml;}ller et al. [[25]](#ref-25), though through a ramp rather than through that
operator's hyperbolic tangent. A tangent approaches its limits without reaching
them, so it returns a small nonzero coverage at zero difference and lays a faint
wash of ink over every flat region in the frame; in a style that adds its line to
a dark ground rather than mixing it in, the wash becomes the picture. A ramp is
exactly zero above its bias. The two kernels are given equal weight, which is
what makes that possible: both integrate to unity, so <i>D</i><sub>&sigma;</sub> vanishes
identically on any region of constant <i>L</i>, whatever that constant is.
The weighted form <i>G</i><sub>&sigma;</sub> - &tau; <i>G</i><sub><i>k</i>&sigma;</sub> with &tau;&lt;1 instead leaves a
residue (1-&tau;)<i>L</i> proportional to brightness, and no single threshold then
draws the same line on a lit face and on a dark coat.

What the operator does respond to, besides contours, is noise.
> **Proposition 11 (Noise response).** For per-pixel luminance noise of variance &sigma;<sub><i>L</i></sub><sup>2</sup>, independent across
> pixels,
>
> <p class="equation">Var <i>D</i><sub>&sigma;</sub> = &sigma;<sub><i>L</i></sub><sup>2</sup> &#8214;<i>G</i><sub>&sigma;</sub> - <i>G</i><sub><i>k</i>&sigma;</sub>&#8214;<sub>2</sub><sup>2</sup>
>  = (&sigma;<sub><i>L</i></sub><sup>2</sup>)&#8260;(4&pi;&sigma;<sup>2</sup>)(1 - 4&#8260;(1+<i>k</i><sup>2</sup>) + 1&#8260;(<i>k</i><sup>2</sup>)),</p>
>
> which for <i>k</i> = 1.6 equals 0.0212&thinsp;&sigma;<sub><i>L</i></sub><sup>2</sup>/&sigma;<sup>2</sup>.

*Proof.* Convolution with a fixed kernel scales an independent noise field's variance by
the squared <i>L</i><sup>2</sup> norm of that kernel. Expanding,
&#8214;<i>G</i><sub>&sigma;</sub> - <i>G</i><sub><i>k</i>&sigma;</sub>&#8214;<sub>2</sub><sup>2</sup> = &#8214;<i>G</i><sub>&sigma;</sub>&#8214;<sub>2</sub><sup>2</sup> - 2&lang; <i>G</i><sub>&sigma;</sub>,<i>G</i><sub><i>k</i>&sigma;</sub>&rang; + &#8214;<i>G</i><sub><i>k</i>&sigma;</sub>&#8214;<sub>2</sub><sup>2</sup>.
In two dimensions &#8214;<i>G</i><sub><i>a</i></sub>&#8214;<sub>2</sub><sup>2</sup> = 1/(4&pi; <i>a</i><sup>2</sup>) and
&lang; <i>G</i><sub><i>a</i></sub>, <i>G</i><sub><i>b</i></sub>&rang; = 1/(2&pi;(<i>a</i><sup>2</sup>+<i>b</i><sup>2</sup>)), since the integral of a product of
Gaussians is a Gaussian of the combined width evaluated at the origin.
Substituting <i>a</i>=&sigma;, <i>b</i>=<i>k</i>&sigma; gives the stated form, and <i>k</i>=1.6 gives
1 - 4/3.56 + 1/2.56 = 0.267, hence the coefficient 0.267/4&pi; = 0.0212. &#9633;
The consequence settles a design choice. A camera frame with per-channel noise
&sigma;<sub><i>n</i></sub> = 0.03 carries luminance noise
&sigma;<sub><i>L</i></sub> = &sigma;<sub><i>n</i></sub>&radic;<span style="text-decoration:overline">0.2126<sup>2</sup>+0.7152<sup>2</sup>+0.0722<sup>2</sup></span> = 0.750&thinsp;&sigma;<sub><i>n</i></sub> = 0.0225,
so at &sigma; = 1.4 pixels Proposition 8 gives a response of
standard deviation 2.3&times;10<sup>-3</sup>. The operator does not threshold at a point
but over a ramp: ink begins at <i>D</i><sub>&sigma;</sub> = -1.6&times;10<sup>-3</sup> and is laid in full
at -4.8&times;10<sup>-3</sup>, so the contrast at which a line is half drawn is
&epsilon; = -3.2&times;10<sup>-3</sup>. Grain therefore reaches two thirds of the
contrast the operator asks of a contour, and exceeds outright the contrast at
which it begins to draw, which is precisely the field of short marks we observed
across flat walls. We read it instead from
a mixture
<p class="equation"><i>L</i> = (1-&lambda;)&thinsp;<i>L</i><sub>surface</sub> + &lambda;&thinsp;<i>L</i><sub>raw</sub>,  &nbsp;&nbsp;  &lambda; = 0.16,</p>
<p class="equation-note">(15)</p>
where <i>L</i><sub>surface</sub> is the output of (11). The surface
has already had the grain averaged out of it, so what reaches the operator is the
raw share of the noise and its response scales with &lambda;. Requiring the
half-drawn contrast to stand at least eight standard deviations clear of that
response bounds &lambda; &le; 0.17; we use 0.16, which places it at 8.6 and
leaves the fine detail the half-resolution surface cannot carry. The value is
fixed by the ratio the operator must achieve, not by inspection.
### Following the subject
The gesture of Section 4.8 occupies both hands, so the device is
propped rather than held and is not aimed accurately. The output frame is
already a crop of a wider sensor, so the crop can follow a detected face
[[3]](#ref-3) at no cost beyond the detection. Two properties
are required of the update: that it not answer detection jitter, and that it not
jump when it stops ignoring it. Writing <i>p</i><sub><i>t</i></sub> for the measured face centre and
<i>c</i><sub><i>t</i></sub> for the framing,
<p class="equation"><i>c</i><sub><i>t</i>+1</sub> = <i>c</i><sub><i>t</i></sub> + &alpha;&thinsp;(max(0, &#8214;<i>e</i><sub><i>t</i></sub>&#8214; - &delta;))&#8260;(&#8214;<i>e</i><sub><i>t</i></sub>&#8214;)&thinsp;<i>e</i><sub><i>t</i></sub>,
   &nbsp;&nbsp;  <i>e</i><sub><i>t</i></sub> = <i>p</i><sub><i>t</i></sub> - <i>c</i><sub><i>t</i></sub> .</p>
<p class="equation-note">(16)</p>

> **Proposition 12 (Soft dead zone).** The map (16) is continuous in <i>e</i><sub><i>t</i></sub>; its fixed set is the closed
> ball {<i>c</i> : &#8214;<i>p</i>-<i>c</i>&#8214; &le; &delta;}; and for a stationary target the excess over
> the dead zone contracts geometrically,
>
> <p class="equation">&#8214;<i>e</i><sub><i>t</i>+1</sub>&#8214; - &delta; = (1-&alpha;)(&#8214;<i>e</i><sub><i>t</i></sub>&#8214; - &delta;).</p>

*Proof.* The coefficient max(0,&#8214;<i>e</i>&#8214;-&delta;)/&#8214;<i>e</i>&#8214; tends to 0 as &#8214;<i>e</i>&#8214;&rarr;&delta;
from either side, so the displacement is continuous across the boundary. Inside
the ball the coefficient is identically zero and every point is fixed; outside it
the displacement has magnitude &alpha;(&#8214;<i>e</i>&#8214;-&delta;) &gt; 0, so no point there is
fixed. For &#8214;<i>e</i><sub><i>t</i></sub>&#8214; &gt; &delta; the displacement
is parallel to <i>e</i><sub><i>t</i></sub> with magnitude &alpha;(&#8214;<i>e</i><sub><i>t</i></sub>&#8214;-&delta;), so
&#8214;<i>e</i><sub><i>t</i>+1</sub>&#8214; = &#8214;<i>e</i><sub><i>t</i></sub>&#8214; - &alpha;(&#8214;<i>e</i><sub><i>t</i></sub>&#8214;-&delta;); subtracting &delta; gives the
stated recurrence. &#9633;
A hard dead zone, which ignores motion below &delta; and follows it in full
above, is discontinuous at the boundary and produces a visible jump each time the
subject drifts across it. The form above never moves the framing by more than the
excess, so a subject who crosses the frame slowly is followed the whole way,
trailing by exactly &delta;. As in Section 4.8, &alpha; is rescaled
to the elapsed interval, so the behaviour does not depend on the frame rate.
### Delegated restyling
Section 4.10 restyles the subject that is present. Replacing it
requires a generative model, and the constraint of zero marginal cost forbids
hosting one. The remaining option is to let the user supply their own key, which
moves the cost to them and keeps the deployment static. We implement that path
and state exactly what it requires.

The model is asked to redraw the whole take, not the interior of the window. The
window is then a reveal: the generated clip inside, the original outside. This is
the only order that can work, because the boundary moves every frame and a model
cannot be given a per-frame region to respect.

The correctness condition is a statement about the model's output. Let <i>R</i> be the
raw take and let the returned clip be
<p class="equation"><i>G</i>(<i>x</i>,<i>t</i>) = <i>S</i>(<i>R</i>(<i>W</i><sub><i>t</i></sub>(<i>x</i>)),&thinsp;<i>t</i>)</p>
<p class="equation-note">(17)</p>
for some appearance map <i>S</i> and per-frame spatial warp <i>W</i><sub><i>t</i></sub>.
> **Proposition 13 (Alignment).** The composite that shows <i>G</i> inside the tracked window and <i>R</i> outside is
> geometrically consistent if and only if <i>W</i><sub><i>t</i></sub> = id for every <i>t</i>.

*Proof.* The window is positioned from landmarks measured in <i>R</i>. A point <i>x</i> inside it
displays <i>G</i>(<i>x</i>,<i>t</i>) = <i>S</i>(<i>R</i>(<i>W</i><sub><i>t</i></sub>(<i>x</i>)),<i>t</i>), whose content is that of <i>R</i> at <i>W</i><sub><i>t</i></sub>(<i>x</i>).
Consistency requires the content shown at <i>x</i> to be the content of <i>R</i> at <i>x</i>,
that is <i>W</i><sub><i>t</i></sub>(<i>x</i>) = <i>x</i> for all <i>x</i> in the window and all <i>t</i>; extending to the
whole frame by continuity of the constraint across the boundary gives
<i>W</i><sub><i>t</i></sub>=id. &#9633;
We cannot enforce Proposition 10; we can only request it. Every
prompt therefore carries a fixed constraint forbidding the reframing a generative
video model applies by default, and the style instruction is the only part the
user edits. A residual warp is reported as a limitation rather than corrected,
because correcting it means estimating <i>W</i><sub><i>t</i></sub> from the pair, which is a
registration problem of the same order as the one avoided by asking the model not
to introduce it.
## Implementation
The system is a static web application. In its default configuration it
contacts no server, holds no key and has no per-use cost; the one path that
departs from this is Section 4.12, which is disabled until a user
supplies their own credential. Hand landmarks come from a WebAssembly build of an
on-device estimator [[5]](#ref-5), and face detection, when
framing is enabled, from a second on-device model [[3]](#ref-3)
built on the same runtime so the runtime is downloaded once. Compositing is
WebGL 2 [[26]](#ref-26); capture and encoding use the platform's own
interfaces [[27]](#ref-27)[[28]](#ref-28).

Rendering is four passes rather than two. A first pass applies the persistent
colour treatment together with the aspect crop, the mirror and the framing offset
of Section 4.11. A second evaluates (11) at half
resolution, ping-ponged between two targets so that no pass samples the texture
it writes, and runs only while the window is open. A third composites the window,
evaluating the style of Section 4.10 for the fragments inside it and
no others. A fourth applies the transient effect. Separating the persistent
treatment from the transient one is what allows any of the six filters to combine
with any of the seven effects without a shader for each pairing.

The half resolution of the second pass is chosen for reach rather than for cost.
A kernel of fixed tap count spans twice as much of the full frame there, which is
what collapses skin and clothing into single regions instead of merely reducing
their grain; the softness introduced at a boundary is removed again by
(12), since quantising a ramp between two levels restores a step at
the crossing.
{{< Academic_Figure src="fig-2-pipeline.png" alt="The pipeline. Inference (cyan) is rate limited and feeds a timeline anchored to the causal instant; rendering runs at th" align="center" >}}

<p class="equation-note"><b>Figure 2.</b> The pipeline. Inference (cyan) is rate limited and feeds a timeline anchored to the causal instant; rendering runs at the display rate. The encoder reads the composited surface (magenta), so the effect is present in the output as pixels and no editing stage exists.</p>
The decision with the largest consequence is that the encoder captures the
composited surface rather than the camera stream (Figure 2).
The alternative, recording the camera and reapplying effects afterwards, would
require storing trigger times, decoding, compositing offline and re-encoding, and
each stage is an opportunity for drift.
{{< Academic_Figure src="rewind_cut.jpg" alt="Verification of the temporal buffer. The synthetic subject renders the elapsed time at which each frame was drawn, and m" align="center" >}}

<p class="equation-note"><b>Figure 3.</b> Verification of the temporal buffer. The synthetic subject renders the elapsed time at which each frame was drawn, and moves, so a recalled frame is distinguishable from a recoloured current one. The strip runs left to right: one live frame at 4.3 s, three recalled frames reading 2.5, 2.8 and 2.9 s, and one live frame after the effect at 5.6 s. The live clock at each recalled frame is not printed on it, but lies between those two bounds and advances with the strip, so each recalled frame is about the requested 2.2 s behind the moment it was shown.</p>

## Evaluation
We report what was measured and separate it from what was not, since the value of
a systems claim lies in that distinction.
**Frame budget.**At 60 Hz the budget is 16.7 ms. Landmark inference measured 6&ndash;11 ms
per evaluation on desktop integrated graphics, texture upload 1&ndash;2 ms, and
an effect shader 0.5&ndash;2 ms. Inference dominates, which is what motivates
Section 4.6. Feature extraction and detector evaluation for two
hands and five detectors measured below 0.1 ms combined, consistent with the
criterion requiring one cross product per hand.
**Window coverage.**The predicate of Section 4.9 was checked against the failure it
replaces. With one hand's corners exchanged, so that the boundary self-intersects,
the even-odd predicate renders two lobes and leaves the region between them
untouched; sampling on the axis through the crossing confirms the interior of each
lobe is filled and the two points where the shape pinches are not. The fan
predicate fills both, which is Corollary 2 at work: for the
symmetric configuration it draws half as much area again as the window, a third of
it outside.
**Abstraction.**A flat field was given independent per-channel grain drawn uniformly on
&plusmn; 15 of 255, a standard deviation of 8.7, and delivered to the renderer
through the same capture path a camera uses. The mean absolute difference between
horizontally adjacent output samples, measured well inside the window and clear
of its border, was 4.5 of 255 without the window and 0.2 with it. The grain
is drawn from a seeded stream, so the two figures are reproducible rather than
merely reported. What the schedule of Section 4.10 leaves is
therefore below the amplification of (13), which is what
(15) and the five-tap band selection were sized to achieve.
**Separation of the styles.**The seven media are intended to be nameable from a still. We rendered one frame
through each and measured the mean absolute channel difference over the interior
of the window for all twenty-one pairs. The widest, neon against ink, differed by
122.7 of 255; the closest, cartoon against paint, by 7.6, against a floor of
6 set before the measurement. Those two share a flattened surface and differ
mainly in saturation and in the direction of their strokes, so they are the pair
a reader should expect to find closest, and 7.6 is a thinner margin than the
rest of the set enjoys. The measurement is reported, and its weakest pair named,
because ``they look different'' is otherwise an assertion by the author about
their own work.
**Behavioural coverage.**Four suites run against the shipped modules. Ninety assertions cover the
render passes, the coverage predicate under crossing, the framing clamp, the
noise reduction, the tracker's hysteresis and dropout behaviour, the spoken
command matcher, the credential store, the prompt constraint, the geometry track
and the exchange of Section 4.12 against a stubbed transport.
Forty-two further assertions drive the application through its own document with
a synthetic camera and microphone, from the first-visit guide to a downloaded
file, and confirm among other things that audio is present in the encoded output
by decoding it rather than by trusting the container's declaration.

That distinction earned its cost. It caught a defect no weaker check could see:
the container was selected once at startup, before it was known whether a take
would carry sound, and the preferred string named a video codec alone. A recorder
given an explicit codec list encodes those codecs and no others, so an attached
audio track was accepted and then discarded without error. The track was present
in the stream, the file was well formed, its declared type named the container
correctly, and every recording was mute. Only decoding the output distinguishes
that state from a working one. The correction is to choose the container per
take, once the track set is known, rather than once at startup.

A third suite of twenty-two puts synthetic landmark poses through the
recording-cue detector at the rate the render loop actually calls it, which is
where a detector that treats a throttled frame as an absent hand is caught. A
fourth of ten stubs the speech interface and pushes transcripts through the
shipped matcher. The four suites total one hundred and sixty-four assertions.
**Temporal buffer.**The buffer was verified by rendering a subject that states its own draw time and
moves between draws (Figure 3). With a requested delay of
2.2 s, the strip runs from a live frame at 4.3 s, through three recalled
frames reading 2.5, 2.8 and 2.9 s, to a live frame at 5.6 s, with the
subject visibly displaced between them. Each recalled frame therefore sits about
2.2 s behind the live clock at the moment it was shown, which advances across
the strip. The buffer returns genuine earlier frames at approximately the
requested delay, the residual being the 125 ms capture granularity at
<i>f</i><sub><i>b</i></sub> = 8 Hz.
**Two-hand frame.**The tracker was exercised with synthetic landmark configurations. It correctly
returned no window with no hands, opened to full presence on a framing
configuration, produced corners matching the constructed rectangle to two decimal
places, held the window through a 133 ms tracking dropout, closed after the
hands left, and rejected a configuration whose area fell below the opening gate.
**End-to-end.**The second suite covers acquisition, recording, review, export, output presets,
filters, effect rebinding, settings persistence, theme selection, focus
containment and keyboard dismissal, and passes against both the development
server and the deployed build. The distinction matters: the bundler moves
stylesheet links in the built page, and an override that wins by source order in
development can lose in the build.
**Detector accuracy against known ground truth.**The quantity that matters for a frame-synchronous detector is the error between
the instant the gesture occurred and the instant reported. That quantity cannot
be obtained from recorded video: an annotator watching a hand rotate can identify
the edge-on frame only to within the several frames over which the hand appears
edge-on, which is the same order as the error to be measured. Any figure derived
that way would report the annotator rather than the detector.

We therefore generate the corpus. A rigid twenty-one point hand is rotated about
its long axis through &pi; radians on a known schedule, projected
orthographically, and perturbed by independent Gaussian landmark noise of
standard deviation 0.004 frame widths. The instant &theta; = &pi;/2 is then
known exactly. Sequences are drawn from a seeded stream, so the figures below
are reproducible rather than merely reported, and the evaluation runs the shipped
detector modules rather than a reimplementation of them
[[29]](#ref-29).

Four near-miss classes are included, each sharing part of a flip's signature. A
detector that fires on everything scores perfectly on the flip class alone, so
the near misses are what make the positive result meaningful.
| Class | Requirement | Fired | Correct |
|---|---|---:|---:|
| Palm flip, quick, 180&ndash;520 ms | must fire | 54/60 | 90.0% |
| Palm flip, deliberate, 0.9&ndash;1.6 s | must fire | 60/60 | 100.0% |
| Held edge-on, 0.8&ndash;1.4 s | must not fire | 0/60 | 100.0% |
| Wobble to 54&ndash;79 degrees | must not fire | 0/60 | 100.0% |
| Rotating closed hand | must not fire | 0/60 | 100.0% |
| Entering frame mid-rotation | must not fire | 0/60 | 100.0% |
| **Total** |  | 95.0% detected, 0 false positives in 240 near misses |  |

<p class="equation-note"><b>Table 1.</b> Classification over 60 generated sequences per class, at <i>f</i><sub>&Lambda;</sub> = 24 Hz with the shipped thresholds. The two flip classes differ only in how quickly the hand is turned.</p>

|  | Reported at <i>t</i><sub><i>a</i></sub> | Interpolated |  |  |
|---|---:|---:|---:|---:|
|  | ms | frames | ms | frames |
| Mean absolute error | 23.0 | 0.55 | 6.7 | 0.16 |
| Median absolute error | 22.2 | 0.53 | 4.0 | 0.10 |
| Ninetieth percentile | 41.7 | 1.00 | 18.1 | 0.43 |
| Worst case | 66.3 | 1.59 | 26.7 | 0.64 |
| Mean signed error | -22.1 | &mdash; | +0.8 | &mdash; |

<p class="equation-note"><b>Table 2.</b> Localisation error on the 114 detected flips, reported at the bracketing sample and after the interpolation of Section 4.5. The sampling interval is 41.7 ms. Both columns are computed by the published evaluation.</p>
Three things in Tables 1 and 2 are
worth stating plainly.

The detector localises the gesture to a sixth of the interval at which it
observes, and to a tenth of it in the median case, against the 0.55 frames that
reporting the bracketing sample costs. That is the practical content of
Proposition 5: a zero crossing carries information between
samples that a per-frame label does not. A classifier operating on the same
stream cannot report an instant finer than the frame it labels.

The mean signed error after interpolation is under one millisecond, so what
remains is scatter rather than bias, and its source is the landmark noise
entering through the two bracketing magnitudes.

The six missed flips are the fastest in the class. A hand turned over in
180 ms is edge-on for roughly 25 ms, which is shorter than the sampling
interval, so no sample falls inside the band and no bracket exists. This is a
limit of the observation rate rather than of the criterion, and only a higher
tracking rate moves it.
**An incidental finding.**A canvas capture stream emits frames only while the canvas is *painted*, and
a browser may cease painting a surface it considers not visible while still
reporting the document as visible. The recording then encodes nothing and the
failure surfaces only at the end. We detect the condition with a timer rather
than within the render loop, since the condition is the loop not running, and
abandon the recording after 2.5 s with an explanation. We record this because
it is a property of the platform that any comparable system will meet.
## Limitations
**Restyling is not substitution.** The shader restyles the subject present
in the frame. It cannot replace that subject, which would require synthesis of
content the stream never carried. Systems that do so route video to a hosted
generative model, reintroducing a server, a key and a per-use cost, and operate
either offline or at a latency set by the service.

**Orthography.** Theorem 1 assumes orthographic
projection, and the factorisation (3) does not hold verbatim
under perspective. The qualitative conclusion does. Three points project to
collinear image points under a pinhole camera exactly when they are coplanar with
the centre of projection, so the projected triangle still degenerates once per
half turn and <i>s</i> still changes sign there. The degeneracy occurs when the palm
plane contains the centre of projection rather than at &theta; = &pi;/2
precisely; the discrepancy is set by the angle the hand subtends from the optical
axis and vanishes as the hand approaches it. The crossing therefore remains
exact as an event, with a small bias in the associated angle, and only the
magnitude thresholds, which are gates rather than definitions, are affected.

**Rotation axis.** The analysis assumes rotation about the hand's long
axis. A rotation with a component about the optical axis leaves <i>s</i> unchanged, so
it is correctly ignored; a rotation about the remaining axis is not modelled and
is excluded in practice by the finger-extension condition.

**Unverified surfaces.** No test was performed with a physical camera, with
real hands, or on Apple platforms. The gesture thresholds are derived rather than
fitted, but no threshold has met a human hand. Recording on iOS is the least
certain component: the interfaces are supported and four documented defects are
mitigated, but none of this was confirmed on a device.

**The corpus is generated, not filmed.** Table 1
measures the criterion and its gating; it does not measure the landmark
estimator, which appears in the corpus as unbiased noise of constant variance and
is in reality neither. A hand also deforms as it turns, and a rigid model does
not. The figures are therefore a floor on the error attributable to the detector,
not a prediction of field performance, and the gap between the two is the
estimator's contribution. We consider this the honest form of the measurement
rather than a substitute for one: the alternative, annotating filmed rotations,
would report the annotator's uncertainty about the edge-on frame, which is of the
same order as the quantity being measured.
**The delegated path is verified as far as the free tier reaches.**Section 4.12 is implemented against a preview interface whose
response shape has more than one documented form and whose model name has changed
between revisions, so its transport was exercised against the live service rather
than only against a stub. Four properties were confirmed. The endpoint accepts
the request the implementation constructs, returning an interaction bearing the
identifier and status field the client polls on, and reporting the terminal state
that ends the loop. The call succeeds from a page rather than from a server: the
service sends permissive cross-origin headers, so the browser-only architecture
of Section 5 needs no proxy, and a proxy would have
reintroduced the server the design exists to avoid. A take produced by the
recorder, in the container of Section 5, is accepted and
decoded: the service billed 539 video tokens for a four-second clip and
returned a description naming frame content that was present only in the video,
which establishes that frames survive capture, encoding and transport intact.
Finally, the media type must be sent without its codec parameters, and the
payload must be separated from the data URL header at the `;base64,`
marker rather than at the first comma, because a container that names two codecs
contains a comma of its own; both were found by this exercise and both are
defects the stub could not have exposed.

What remains open is the generation itself. The editing model carries a free-tier
quota of exactly zero and answers with a quota refusal rather than a result, so
the alignment of a real generation was not measured.
Proposition 10 states the condition the composite requires;
whether a given model satisfies it is an empirical question that a metered key
would settle and this work does not, and the interface reports a mismatch rather
than concealing it.
**Two paths are not local, and both are opt-in.**Spoken command recognition uses the browser's own speech interface, which in the
two most common engines transmits audio to the vendor; the restyle transmits one
recording to a hosted model. Both are disabled by default, both state what they
do at the point of enabling, and both display an indicator while active. We
record this here rather than only in the interface because a paper that claimed a
wholly local system while shipping two exceptions would be making a false claim,
and because the design question of how such an exception should be surfaced is
not incidental to a privacy-preserving system.
**A key held in a page is exposed to that page.**The delegated path requires a credential in the browser, which no client-side
design can protect from the page that uses it. We reduce the surface by loading
no third-party script at runtime, by keeping the credential out of storage unless
asked, and by transmitting it in a header rather than a query string, but the
residual risk is real and is stated to the user in those terms.
## Conclusion
Posing hand-gesture detection as synchronisation rather than classification
changes what counts as a solution. For rotation of an open hand about its long
axis, the change admits an exact answer: the projected palm winding factorises as
<i>k</i>(&theta;)cos&theta; with <i>k</i> non-vanishing, so the gesture is a zero crossing of
one scalar and the crossing is the instant. The criterion needs no training data,
no calibration and one cross product per hand, and is provably invariant to
mirroring, to scale and to handedness.

Measured against a corpus with exact ground truth, the criterion detects
95% of flips with no false positive in 240 near-miss sequences, and places
each one within 6.7 ms on average of the instant it occurred, which is a sixth
of the interval at which the hand is observed. That a detector can report an
event more finely than it samples is the practical consequence of treating the
gesture as a zero of a continuous quantity rather than as a label attached to a
frame, and it is the result we would ask a reader to take from this work.

The implementation, the derivation, the figure-generating code and the evaluation
itself are released under the MIT licence, and the evaluation runs in a browser
against the shipped modules, so every figure above can be reproduced by opening a
page rather than by rebuilding a toolchain [[29]](#ref-29).
## Availability
Source code, documentation and the scripts that generate every figure in this
paper: <https://github.com/Amey-Thakur/GESTURE-FX>. A live deployment:
<https://amey-thakur.github.io/GESTURE-FX/>. Released under the MIT licence.

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Frame-Synchronous Hand Gesture Detection by Projected Winding Order." arXiv:2609.13269 (Sep 2026). https://arxiv.org/abs/2609.13269.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2026winding,
  title         = "Frame-Synchronous Hand Gesture Detection by Projected Winding Order",
  author        = "Thakur, Amey",
  journal       = "arXiv preprint arXiv:2609.13269",
  year          = "2026",
  month         = "Sep",
  eprint        = "2609.13269",
  archivePrefix = "arXiv",
  url           = "https://arxiv.org/abs/2609.13269"
}
```

---

## References

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">[1]</span>
    <span class="reference-text"><a id="ref-1"></a><b>Tomas Simon, Hanbyul Joo, Iain Matthews, and Yaser Sheikh</b>, "Hand keypoint detection in single images using multiview
 bootstrapping," <i>arXiv preprint arXiv:1704.07809, 2017</i>, <a href="https://arxiv.org/abs/1704.07809">https://arxiv.org/abs/1704.07809</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>Zhe Cao, Gines Hidalgo, Tomas Simon, Shih-En Wei, and Yaser Sheikh</b>, "{OpenPose}: Realtime multi-person {2D} pose estimation using part
 affinity fields," <i>IEEE Transactions on Pattern Analysis and Machine Intelligence, 43 (1): 172&ndash;186, 2021</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>Valentin Bazarevsky, Yury Kartynnik, Andrey Vakunov, Karthik Raveendran, and
 Matthias Grundmann</b>, "{BlazeFace}: Sub-millisecond neural face detection on mobile {GPU}s," <i>arXiv preprint arXiv:1907.05047, 2019</i>, <a href="https://arxiv.org/abs/1907.05047">https://arxiv.org/abs/1907.05047</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>Valentin Bazarevsky, Ivan Grishchenko, Karthik Raveendran, Tyler Zhu, Fan
 Zhang, and Matthias Grundmann</b>, "{BlazePose}: On-device real-time body pose tracking," <i>arXiv preprint arXiv:2006.10204, 2020</i>, <a href="https://arxiv.org/abs/2006.10204">https://arxiv.org/abs/2006.10204</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>Fan Zhang, Valentin Bazarevsky, Andrey Vakunov, Andrei Tkachenka, George Sung,
 Chuo-Ling Chang, and Matthias Grundmann</b>, "{MediaPipe Hands}: On-device real-time hand tracking," <i>arXiv preprint arXiv:2006.10214, 2020</i>, <a href="https://arxiv.org/abs/2006.10214">https://arxiv.org/abs/2006.10214</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>Camillo Lugaresi, Jiuqiang Tang, Hadon Nash, Chris McClanahan, Esha Uboweja,
 Michael Hays, Fan Zhang, Chuo-Ling Chang, Ming Guang Yong, Juhyun Lee,
 Wan-Teh Chang, Wei Hua, Manfred Georg, and Matthias Grundmann</b>, "{MediaPipe}: A framework for building perception pipelines," <i>arXiv preprint arXiv:1906.08172, 2019</i>, <a href="https://arxiv.org/abs/1906.08172">https://arxiv.org/abs/1906.08172</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>Gary Bradski</b>, "The {OpenCV} library," <i>Dr. Dobb's Journal of Software Tools, 25 (11): 120&ndash;125, 2000</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>Amey Thakur, Mega Satish, Randeep Kaur Kahlon, Hasan Rizvi, and Ajay Davare</b>, "{QuadTree} visualizer," <i>International Journal of Engineering Research and Technology (IJERT), 11 (4), 2022. {10.5281/zenodo.18447415}</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>Okan K{&ouml;}p{&uuml;}kl{&uuml;}, Ahmet Gunduz, Neslihan Kose, and Gerhard Rigoll</b>, "Real-time hand gesture detection and classification using
 convolutional neural networks," <i>arXiv preprint arXiv:1901.10323, 2019. {10.48550/arXiv.1901.10323}</i>, <a href="https://arxiv.org/abs/1901.10323">https://arxiv.org/abs/1901.10323</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>Amey Thakur, Karan Dhiman, and Mayuresh Phansikar</b>, "Neuro-fuzzy: Artificial neural networks and fuzzy logic," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET), 9 (9): 128&ndash;135, 2021{}</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>Amey Thakur and Archit Konde</b>, "Fundamentals of neural networks," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET), 9 (8): 407&ndash;426, 2021</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>Hyeon-Kyu Lee and Jin H. Kim</b>, "An {HMM}-based threshold model approach for gesture recognition," <i>IEEE Transactions on Pattern Analysis and Machine Intelligence, 21 (10): 961&ndash;973, 1999</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[13]</span>
    <span class="reference-text"><a id="ref-13"></a><b>Zheng Shou, Dongang Wang, and Shih-Fu Chang</b>, "Temporal action localization in untrimmed videos via multi-stage
 {CNN}s," <i>In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 1049&ndash;1058, 2016</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[14]</span>
    <span class="reference-text"><a id="ref-14"></a><b>Gunnar Farneb{&auml;}ck</b>, "Two-frame motion estimation based on polynomial expansion," <i>In Image Analysis (SCIA 2003), volume 2749 of Lecture Notes in Computer Science, pages 363&ndash;370. Springer, 2003</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[15]</span>
    <span class="reference-text"><a id="ref-15"></a><b>Amey Thakur and Sarvesh Talele</b>, "A modular zero-shot pipeline for accident detection, localization,
 and classification in traffic surveillance video," <i>arXiv preprint arXiv:2604.09685, 2026</i>, <a href="https://arxiv.org/abs/2604.09685">https://arxiv.org/abs/2604.09685</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[16]</span>
    <span class="reference-text"><a id="ref-16"></a><b>G{&eacute;}ry Casiez, Nicolas Roussel, and Daniel Vogel</b>, "{One Euro} filter: A simple speed-based low-pass filter for noisy
 input in interactive systems," <i>In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '12), pages 2527&ndash;2530. ACM, 2012</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[17]</span>
    <span class="reference-text"><a id="ref-17"></a><b>Amey Thakur and Mega Satish</b>, "Generative adversarial networks," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET), 9 (8): 2307&ndash;2325, 2021{}</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[18]</span>
    <span class="reference-text"><a id="ref-18"></a><b>Amey Thakur, Hasan Rizvi, and Mega Satish</b>, "White-box cartoonization using an extended {GAN} framework," <i>International Journal of Engineering Applied Sciences and Technology (IJEAST), 5 (12), 2021{}. {10.33564/IJEAST.2021.v05i12.049}</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[19]</span>
    <span class="reference-text"><a id="ref-19"></a><b>Amey Thakur and Mega Satish</b>, "Adversarial open domain adaption framework ({AODA}): Sketch-to-photo
 synthesis," <i>International Journal of Engineering Applied Sciences and Technology (IJEAST), 6 (2), 2021{}. {10.33564/IJEAST.2021.v06i02.037}</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[20]</span>
    <span class="reference-text"><a id="ref-20"></a><b>Amey Thakur and Mega Satish</b>, "Clock synchronization in distributed systems," <i>International Research Journal of Engineering and Technology (IRJET), 9 (3), 2022</i>, <a href="https://www.irjet.net/archives/V9/i3/IRJET-V9I3350.pdf">https://www.irjet.net/archives/V9/i3/IRJET-V9I3350.pdf</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[21]</span>
    <span class="reference-text"><a id="ref-21"></a><b>Eric Haines</b>, "Point in polygon strategies," <i>In Paul S. Heckbert, editor, Graphics Gems IV, pages 24&ndash;46. Academic Press, 1994</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[22]</span>
    <span class="reference-text"><a id="ref-22"></a><b>Carlo Tomasi and Roberto Manduchi</b>, "Bilateral filtering for gray and color images," <i>In Proceedings of the Sixth International Conference on Computer Vision (ICCV), pages 839&ndash;846, 1998</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[23]</span>
    <span class="reference-text"><a id="ref-23"></a><b>Holger Winnem{&ouml;}ller, Sven C. Olsen, and Bruce Gooch</b>, "Real-time video abstraction," <i>ACM Transactions on Graphics, 25 (3): 1221&ndash;1226, 2006</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[24]</span>
    <span class="reference-text"><a id="ref-24"></a><b>David Marr and Ellen Hildreth</b>, "Theory of edge detection," <i>Proceedings of the Royal Society of London. Series B, Biological Sciences, 207 (1167): 187&ndash;217, 1980</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[25]</span>
    <span class="reference-text"><a id="ref-25"></a><b>Holger Winnem{&ouml;}ller, Jan Eric Kyprianidis, and Sven C. Olsen</b>, "{XDoG}: An extended difference-of-gaussians compendium including
 advanced image stylization," <i>Computers & Graphics, 36 (6): 740&ndash;753, 2012</i> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[26]</span>
    <span class="reference-text"><a id="ref-26"></a><b>{Khronos Group}</b>, "{WebGL} 2.0 specification," <i>Technical report, The Khronos Group, 2022</i>, <a href="https://registry.khronos.org/webgl/specs/latest/2.0/">https://registry.khronos.org/webgl/specs/latest/2.0/</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[27]</span>
    <span class="reference-text"><a id="ref-27"></a><b>{World Wide Web Consortium}</b>, "Media capture and streams," <i>W3c recommendation, W3C, 2025{}</i>, <a href="https://www.w3.org/TR/mediacapture-streams/">https://www.w3.org/TR/mediacapture-streams/</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[28]</span>
    <span class="reference-text"><a id="ref-28"></a><b>{World Wide Web Consortium}</b>, "{MediaStream} recording," <i>W3c working draft, W3C, 2025{}</i>, <a href="https://www.w3.org/TR/mediastream-recording/">https://www.w3.org/TR/mediastream-recording/</a> [Accessed: Sep. 20, 2026].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[29]</span>
    <span class="reference-text"><a id="ref-29"></a><b>Amey Thakur</b>, "{GESTURE-FX}: Gesture-triggered camera effects in the browser," <i>, 2026</i>, <a href="https://github.com/Amey-Thakur/GESTURE-FX">https://github.com/Amey-Thakur/GESTURE-FX</a> [Accessed: Sep. 20, 2026].</span>
</div>

</div>