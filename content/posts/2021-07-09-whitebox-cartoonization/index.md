---
title: "White-Box Cartoonization: An Extended GAN Framework"
date: 2021-07-09T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Generative Adversarial Networks", "Computer Vision", "Deep Learning", "Image Processing", "GANs", "Python"]
ShowToc: true
TocOpen: false
description: "A novel GAN framework that decomposes cartoonization into surface, structure, and texture representations for high-quality image synthesis."
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




Black-box models often produce unpredictable artifacts when transforming real-world images into cartoons. This project implements a **White-Box Cartoonization** framework using Generative Adversarial Networks (GANs). By decomposing the image into three controllable representations—**Surface** (smoothness), **Structure** (sparse details), and **Texture** (high-frequency details)—we achieve artistically consistent results without the common "checkerboard" artifacts found in traditional CycleGAN approaches [[1]](#ref-1).

---

## Deconstructing the Art Style

How does an AI learn to paint like an animator?

### The Analogy: The Tracing Paper Method
*   **Black-Box GAN**: Like a student trying to copy a painting by just looking at it and guessing. Sometimes the face looks like a potato.
*   **White-Box GAN**: Like a professional artist who breaks the process down:
    1.  **Drafting (Structure)**: Outline the edges.
    2.  **Smoothing (Surface)**: Apply base colors, removing noise.
    3.  **Detailing (Texture)**: Add the specific brush strokes.
    
    Our model forces the generator to perfect each of these layers independently before combining them, ensuring the final image looks intentional, not accidental.

---

## Methodology & Architecture

The core innovation is the decomposition of the image into three separate representations, each handled by a specific loss function.

{{< figure src="Figures/Fig.%20(1)%20Architecture%20of%20GAN.jpg" caption="Overall Architecture of the White-Box GAN" align="center" >}}

1.  **Surface Representation**: We use a guided filter to smooth out the image, preserving the global structure while removing high-frequency noise. This mimics the flat shading of cartoons.
2.  **Structure Representation**: A superpixel grid is used to group uniform regions, helping the model identify and strengthen semantic edges.
3.  **Texture Representation**: A random color shift algorithm prevents the model from overfitting to specific colors, forcing it to learn the *pattern* of the cartoon texture instead.

{{< figure src="Figures/Fig.%20(2)%20High-level%20structure%20of%20GAN.jpg" caption="High-Level Decomposition Strategy" align="center" >}}
{{< figure src="Figures/Fig.%20(3)%20Representation%20Techniques.png" caption="Surface, Structure, and Texture Visualized" align="center" >}}

---

## Live Demonstration

The framework can process video streams in real-time, applying the cartoonization effect frame-by-frame.

<video width="100%" controls>
  <source src="JOEY%20DOESN'T%20SHARE%20FOOD!!%20[Original%20vs%20Cartoonized].mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<p style="text-align: center; font-size: 14px; margin-top: 10px;"><em>Video 1: Real-time Cartoonization (Original vs Processed)</em></p>

---

## Results

The model successfully simplifies complex real-world scenes into clean, aesthetic cartoon visuals.

{{< figure src="Figures/Fig.%20(6)%20(a)%20Original%20image%20(b)%20Processed%20image.png" caption="Before and After Transformation" align="center" >}}

---

## Publication Details

This research was published in the **International Journal of Engineering Applied Sciences and Technology (IJEAST)**.

### Additional Resources
*   [Full Paper (PDF)](IJEAST-V5I12%20-%20White-Box%20Cartoonization%20Using%20An%20Extended%20GAN%20Framework.pdf)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "White-Box Cartoonization: An Extended GAN Framework". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-09-whitebox-cartoonization/.</code></pre>

**Or use the BibTex citation:**

**BibTeX:**

```
@article{thakur2021cartoonization,
  title   = "White-Box Cartoonization: An Extended GAN Framework",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-09-whitebox-cartoonization/"
}
```

## References

1. <a id="ref-1"></a> **Thakur, A.** (2021). White-Box Cartoonization Using An Extended GAN Framework. *International Journal of Engineering Applied Sciences and Technology (IJEAST)*, 5(12).

---
*Authored by Amey Thakur.*
