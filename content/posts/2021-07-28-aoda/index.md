---
title: "AODA: Adversarial Open Domain Adaptation for Sketch-to-Photo Synthesis"
date: 2021-07-28T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Generative Adversarial Networks", "Deep Learning", "Domain Adaptation", "Image Synthesis", "AODA", "Computer Vision"]
ShowToc: true
TocOpen: false
description: "A novel framework for synthesizing realistic photos from freehand sketches, overcoming the domain gap between sparse sketches and rich photorealistic images."
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




Synthesizing realistic photos from freehand sketches is a "Cross-Domain" challenge. Sketches are sparse and abstract, while photos are dense and detailed. We propose an **Adversarial Open Domain Adaptation (AODA)** framework that bridges this gap. By utilizing a **Mixed-Sampling Strategy** and separating the high-level semantic features from low-level stylistic features, our model generates photorealistic outputs even from rough, amateur sketches [[1]](#ref-1).

---

## From Scribble to Masterpiece

How does an AI turn a stick figure into a photograph?

### The Analogy: The Police Sketch Artist
*   **The Witness (The Sketch)**: Provides a rough idea. "He had a round nose and big eyes." It's incomplete.
*   **The Artist (The Generator)**: Must fill in the gaps. They know what *human skin* looks like (Domain Knowledge). They take the rough shape and apply the texture of reality.
*   **The Detective (The Discriminator)**: Looks at the drawing and says, "That nose looks fake." The Artist tries again until the Detective is fooled.

AODA is a training regimen that makes the Artist (Generator) much better at guessing the missing textures.

---

## Framework Overview

The AODA architecture employs a multi-stage training process to align the sketch and photo domains.

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(1)%20Training%20Stage%20and%20Inference%20Stage.png" caption="Training vs. Inference Workflow" align="center" >}}

### Key Innovations
1.  **Open Domain Adaptation**: Unlike typical models trained on paired data (photo + perfect edge map), we train on *unpaired* data, allowing the model to generalize to real-world, messy sketches.
2.  **Mixed Sampling**: We randomly mix sketches with edge maps during training to prevent the model from overfitting to "perfect" lines.

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(5)%20Proposed%20Solution%20-%20Mixed%20Sampling%20with%20Batchwise%20Substitution.jpg" caption="Mixed Sampling Strategy" align="center" >}}

---

## Experimental Results

The model demonstrates superior performance in generating textures from sparse inputs compared to baseline CycleGAN methods.

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(7)%20Results%20on%20Scribble%20Dataset.png" caption="Results on Scribble Dataset" align="center" >}}

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/(A)%20Generator%20Loss.png" caption="Generator Loss Convergence" align="center" >}}

---

## Publication Details

This research was published in the **International Journal of Engineering Applied Sciences and Technology (IJEAST)**.

### Additional Resources
*   [Full Paper (PDF)](Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/IJEAST-V6I2%20-%20Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis.pdf)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "AODA: Adversarial Open Domain Adaptation for Sketch-to-Photo Synthesis". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-28-aoda/.</code></pre>

**Or use the BibTex citation:**

**BibTeX:**

```
@article{thakur2021aoda,
  title   = "AODA: Adversarial Open Domain Adaptation for Sketch-to-Photo Synthesis",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-28-aoda/"
}
```

## References

1. <a id="ref-1"></a> **Thakur, A.** (2021). Adversarial Open Domain Adaptation Framework (AODA) Sketch-To-Photo Synthesis. *International Journal of Engineering Applied Sciences and Technology (IJEAST)*, 6(2).

---
*Authored by Amey Thakur.*
