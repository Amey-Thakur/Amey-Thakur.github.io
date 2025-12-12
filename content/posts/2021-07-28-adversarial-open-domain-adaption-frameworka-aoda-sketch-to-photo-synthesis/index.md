---
title: "Adversarial Open Domain Adaption Framework (AODA): Sketch-to-Photo Synthesis"
date: 2021-07-28T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["AI", "AI Art", "AODA", "Artificial Intelligence", "Computer Vision", "Conditional GANs", "Deep Learning", "Domain Adaptation", "GANs", "Generative Adversarial Networks", "Generative AI", "Image Synthesis", "Machine Learning", "Neural Networks", "Sketch to Image", "Sketch to Photo", "Transfer Learning", "Unsupervised Domain Adaptation"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Mega Satish for her meaningful contributions, support, and wisdom that helped shape this work. This paper aims to demonstrate the efficiency of the Adversarial Open Domain Adaption framework for sketch-to-photo synthesis. The unsupervised open domain adaption for generating realistic photos from a hand-drawn sketch is challenging as there is no such sketch of that class for training data."
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

<style>
.special-thanks {
    font-size: 0.9rem;
    color: #1a73e8; /* Standard Blue for Light Mode */
    margin-bottom: 1.5rem;
}

.special-thanks a {
    color: #1a73e8;
    text-decoration: underline;
    border: none;
    background-image: none;
    box-shadow: none;
    text-underline-offset: 3px;
    transition: all 0.3s ease;
}

.special-thanks a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676; /* Subtle glow/bolding effect without lift */
}

[data-theme="dark"] .special-thanks {
    color: #64b5f6; /* Lighter Blue for Dark Mode readability */
}

[data-theme="dark"] .special-thanks a {
    color: #64b5f6;
}

[data-theme="dark"] .special-thanks a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}
</style>

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=7Ajrr6EAAAAJ&hl=en">Mega Satish</a> for her meaningful contributions, support, and wisdom that helped shape this work.
</p>

This paper aims to demonstrate the efficiency of the Adversarial Open Domain Adaption framework for sketch-to-photo synthesis. The unsupervised open domain adaption for generating realistic photos from a hand-drawn sketch is challenging as there is no such sketch of that class for training data. The absence of learning supervision and the huge domain gap between both the freehand drawing and picture domains make it hard. We present an approach that learns both sketch-to-photo and photo-to-sketch generation to synthesise the missing freehand drawings from pictures. Due to the domain gap between synthetic sketches and genuine ones, the generator trained on false drawings may produce unsatisfactory results when dealing with drawings of lacking classes. To address this problem, we offer a simple but effective open-domain sampling and optimization method that “tricks” the generator into considering false drawings as genuine. Our approach generalises the learnt sketch-to-photo and photo-to-sketch mappings from in-domain input to open-domain categories. On the Scribble and SketchyCOCO datasets, we compared our technique to the most current competing methods. For many types of open-domain drawings, our model outperforms impressive results in synthesising accurate colour, substance, and retaining the structural layout.



---

## Introduction

Generative Adversarial Networks [[1]](#ref-1) have been a recent breakthrough in the field of machine learning. When it comes to the generation of images from various inputs, GANs have been widely used for the desired outcome. Lately, new research regarding GANs allowed the generation of cartoon images from real high-quality pictures. The generator outputs cartoonized images and tries to fool the discriminator whereas the latter one tries to distinguish the real images from fake ones. The results of White Box Cartoonization using an extended GAN framework [[2]](#ref-2)[[3]](#ref-3) were similar to the real photo yet it had characteristics of a cartoon image. The synthesis of cartoon images from real ones is a real challenge but a GAN framework was able to do it with real precision in less time.

Sketches are drawn by anyone and they can be anything. Sketches can describe ideas of any product or artwork. It might be used to depict people, landscapes, or create art. The popularity of artwork created by computers has risen in recent years. Artists, as well as Social Media Users, can interact with visual media and communicate their goals via a freehand sketch. Given the limitation of a sketched object, the purpose of sketch-based image synthesis is to construct some image, photorealistic or non-photorealistic. This enables non-artists to transform simple black-and-white sketches into more abstract, intricate paintings. Also, with the widespread use of touch screens, new scenarios for sketch-based applications are emerging, such as sketch-based photo editing [[4]](#ref-4), sketch-based image retrieval for 2D [[5]](#ref-5) and 3D shapes [[6]](#ref-6), and 3D modelling from sketches.

The aim of the sketch to image translation is to convert a sketch of source domain S to destination photo domain P. Generative Adversarial Networks are used for the sketch-to-photo synthesis [[7]](#ref-7) and use paired data for learning purposes. But there are some limitations to the open domain adaption [[8]](#ref-8): the source domain and the target domain both have images that are not labelled or paired [[9]](#ref-9). Moreover, images in the target domain are unrelated to images in the source domain, and vice versa. As a result, the data is essentially unlabeled and unpaired. Also, the freehand sketches represent a minority of the categories of photos as they need to be annotated. So some systems [[10]](#ref-10) change the sketches with extracted edges from the target photo. However edges and freehand still remain two distinct sketches as freehand sketches are more deformed. Because of this domain difference, Models trained on edge inputs frequently fail to generalise to freehand sketches. A decent sketch-based picture generator should adjust the object structure depending on the input composition as well as fill the right textures within the lines.

Paired and labelled data could help with the synthesis of the sketch to photo. Recent adversarial networks have learned from unpaired sketches and pictures that were gathered separately. But this still doesn't cover all types of pictures in the open domain as many datasets don't have enough freehand drawings for the training of sketch-to-photo synthesis.

To address this difficult problem, we present an Adversarial Open Domain Adaption (AODA) [[11]](#ref-11). This framework will, firstly, train to reconstruct missing freehand drawings and enable unsupervised open-domain adaptation. We are proposing a concurrent framework: a generating sketch-to-photo translation network and a photo-to-sketch translation network for translating open-domain pictures into drawings. We may extend the learnt correlation between in-domain hand-drawn designs and photographs to open-domain classes using the photo-to-sketch synthesis link. Yet, there is a significant domain gap between created drawings and genuine sketches, which prohibits the generalisation of the learnt correlation to real sketches as well as the synthesis of realistic pictures for open-domain classes. To reduce this gap which affects the generator and exploits the results, we propose a random-mixed sampling algorithm that takes a number of false drawings as real ones arbitrarily for all categories. With this learning strategy, our model is capable of generating a realistic photo for unlabeled sketches. The suggested AODA [[11]](#ref-11), [[12]](#ref-12) is compared to existing unpaired sketch-to-image generating methods. Both qualitative and quantitative findings demonstrate that our suggested technique outperforms the competition on both seen and unseen data.

---

## Related Work

### Pix2Pix

Conditional Generative Adversarial Network (cGAN) [[13]](#ref-13) are a branch of GANs and are widely used for image-to-image translation. They have two components: a generator and a discriminator. CGANs learn the mapping from the source image to the output image, with the help of a loss function. We can apply the same basic method to others examples that would need different loss formulae. The framework has been tested on a variety of image-to-image translation [[14]](#ref-14) tasks, including translating maps to satellite pictures, black-and-white photographs to class label graphs, and product drawings to product photographs.

### Sketch to image generation with limited data

The generation of the sketch to photo synthesis has gone through a few phases. The first phase is to turn edges into images like pix2pix i.e. Image-to-image translation with a conditional GAN. The second phase is to turn the freehand sketches into images compared to edge to image freehand sketches that have more deformation and the connections between input and output can be loose. Some freehand sketches can be really ambiguous. Some works take class labels as inputs to specify the output still it takes a lot of human labour to draw the freehand sketches that is why we always lack nicely labelled and pure sketches data. Here we introduce a surface open-domain freehand sketch to image synthesis. We want to learn a multi-class generation with one generation and even generate output from unseen sketches in the training phase.

### Challenges

We might encounter several obstacles in order to tackle this problem. The first is Freehand sketches. Most of them don't look like their target photo. Also, the sketches and target photos are unpaired. The sketch data is also limited for some classes; there are only a few or no sketches. Besides, we aim to generate multiple classes of photos with only one model.
In the training phase, sketches of some categories are missing and in the inference stage, input sketches are not only from known classes but also from the classes that were missing during the training.

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(1)%20Training%20Stage%20and%20Inference%20Stage.png" caption="Training Stage and Inference Stage" align="center" >}}

### Previous Solutions

It allows a network to learn to synthesise pictures from both in-domain and open-domain classes. The difficulties in the preceding techniques can be solved in two ways. The first is to train a model using extracted edges maps, while the second is to supplement open domain classes with synthesised drawings generated by a pre-trained picture to sketch extractor.

#### Edge Maps

An edge map is a graphic that shows where the image's edges are. With an edge detection algorithm, the edges of the image are filtered and a map is created. The edge map indicates the sharpness of the edges as well as other metrics. The picture may already have been quantized with the edge() method to produce a binary image. An efficient hashing approach associated with the internal sequencing of the edges is used to create edge maps. The anticipated time for an access operation is O(1).

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(2)%20(a)%20Edge%20-%20Output%20(b)%20Real%20Sketch%20-%20Output.png" caption="(a) Edge -> Output (b) Real Sketch -> Output" align="center" >}}

XDoG-extracted edges were used to train a model. The model can't fix the deformed forms of freehand doodles because it's only trained with edges. The result from drawings isn't as realistic as the pictures created by edge mapping, which are relatively realistic.

#### Synthesized Sketches

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(3)%20(a)%20Fake%20Sketch%20-%20Output%20(b)%20Real%20Sketch%20-%20Output.png" caption="(a) Fake Sketch -> Output (b) Real Sketch -> Output" align="center" >}}

Pre-extracted drawings were used to train a model. On genuine sketches, the model was unable to generalise. From the synthesised drawings, the model may create ever more realistic approaches.

---

## Framework

### Network Structure

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(4)%20Network%20Structure.png" caption="Network Structure" align="center" >}}

Our framework is made up of the following components, as illustrated in the Figure. Two generators and two discriminators. The first generator is a Photo-to-Sketch generator i.e. <i>G<sub>A</sub></i> and the second generator is a multi-class Sketch-to-photo generator i.e. <i>G<sub>B</sub></i> which take inputs sketch and class label <i>&eta;<sub>s</sub></i>. The first discriminator is <i>D<sub>A</sub></i> which is a sketch discriminator and the second discriminator is <i>D<sub>B</sub></i> which is a Photo discriminator. Unpaired drawing and picture data are used to train the AODA framework.
Generator <i>G<sub>B</sub></i> derives the drawing <i>G<sub>A</sub></i>(<i>p</i>) from the provided picture <i>p</i> throughout the training phase. By passing the synthesised drawing <i>G<sub>A</sub></i>(<i>p</i>) and the original sketch <i>s</i> to <i>G<sub>B</sub></i>, the photo that has been rebuilt <i>G<sub>B</sub></i>(<i>G<sub>A</sub></i>(<i>p</i>), <i>&eta;<sub>p</sub></i>) and the synthesised photo <i>G<sub>B</sub></i>(<i>s</i>, <i>&eta;<sub>s</sub></i>) are formed accompanied by the labels <i>p</i> and <i>s</i>. To verify that <i>G<sub>B</sub></i> acquires the proper form of rectification from sketch to picture domain for each class, we only transmit the drawing with its actual label. A pixel-wise consistency loss imposes a similarity requirement on the rebuilt photo. We don't impose a consistency restriction on the sketch domain since we want the synthesised sketches to be as varied as possible. The generated photo is sent to discriminator <i>D<sub>B</sub></i> as inputs to check if it's real or fake and the classifier <i>R</i> confirms that it shares the target class's perceptual properties.

### Training

Four elements make up the generator loss:
*   The adversarial loss of photo generation to sketch generation. I.e. <i>L<sub>G<sub>A</sub></sub></i>
*   The adversarial loss of sketch translation to photo translation. I.e. <i>L<sub>G<sub>B</sub></sub></i>
*   The pixel consistency of photo reconstruction. I.e. <i>L<sub>pix</sub></i>
*   The classification loss for synthesizing to photos. I.e. <i>L<sub>&eta;</sub></i>

### Generator Loss

<div style="font-family: 'Times New Roman', Times, serif; font-style: italic; font-size: 1.2rem; text-align: center; background: rgba(128, 128, 128, 0.1); padding: 20px; border-radius: 8px; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); line-height: 2;">
    <i>L<sub>GAN</sub></i> = <i>&lambda;<sub>A</sub> L<sub>G<sub>A</sub></sub></i>(<i>G<sub>A</sub></i>, <i>D<sub>A</sub></i>, <i>p</i>) + <i>&lambda;<sub>B</sub> L<sub>G<sub>B</sub></sub></i>(<i>G<sub>B</sub></i>, <i>D<sub>B</sub></i>, <i>s</i>, <i>&eta;<sub>s</sub></i>) + <i>&lambda;<sub>pix</sub> L<sub>pix</sub></i>(<i>G<sub>A</sub></i>, <i>G<sub>B</sub></i>, <i>p</i>, <i>&eta;<sub>p</sub></i>) + <i>&lambda;<sub>&eta;</sub> L<sub>&eta;</sub></i>(<i>R</i>, <i>G<sub>B</sub></i>, <i>s</i>, <i>&eta;<sub>s</sub></i>)
</div>

<div style="display: flex; flex-direction: column; align-items: center; margin: 1rem 0;">

<p style="font-size: 0.9em; margin-bottom: 10px; text-align: center;">
    <span style="user-select: none;">Table 1: </span>
    Breakdown of Terms
</p>

<table style="width: auto; min-width: 200px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid #ccc;">
      <th style="text-align: center; padding: 8px;">Symbol</th>
      <th style="text-align: center; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sub>GAN</sub></i></td>
      <td style="padding: 8px;">The total GAN loss function.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>&lambda;<sub>A</sub></i>, <i>&lambda;<sub>B</sub></i>, <i>&lambda;<sub>pix</sub></i>, <i>&lambda;<sub>&eta;</sub></i></td>
      <td style="padding: 8px;">Weighting coefficients (hyperparameters) for the different loss components.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sub>G<sub>A</sub></sub></i>, <i>L<sub>G<sub>B</sub></sub></i></td>
      <td style="padding: 8px;">Loss functions for Generators A and B respectively.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sub>pix</sub></i></td>
      <td style="padding: 8px;">Pixel-level loss.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sub>&eta;</sub></i></td>
      <td style="padding: 8px;">Noise/Latent vector loss.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>G<sub>A</sub></i>, <i>G<sub>B</sub></i></td>
      <td style="padding: 8px;">Generator networks.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>D<sub>A</sub></i>, <i>D<sub>B</sub></i></td>
      <td style="padding: 8px;">Discriminator networks.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>p</i>, <i>s</i></td>
      <td style="padding: 8px;">Input variables (picture and sketch).</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>&eta;<sub>s</sub></i>, <i>&eta;<sub>p</sub></i></td>
      <td style="padding: 8px;">Noise vectors or latent variables.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><i>R</i></td>
      <td style="padding: 8px;">Classifier/Regularization term.</td>
    </tr>
  </tbody>
</table>

</div>

Due to the missing sketches <i>s</i>, the training objectives for open-domain classes <i>M</i> take the following form if we simply train the multi-class generator with the aforementioned loss:

<div style="font-family: 'Times New Roman', Times, serif; font-style: italic; font-size: 1.2rem; text-align: center; background: rgba(128, 128, 128, 0.1); padding: 20px; border-radius: 8px; margin: 2rem 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); line-height: 2;">
    <i>L<sup>M</sup><sub>GAN</sub></i> = <i>&lambda;<sub>A</sub> L<sub>G<sub>A</sub></sub></i>(<i>G<sub>A</sub></i>, <i>D<sub>A</sub></i>, <i>p</i>) + <i>&lambda;<sub>pix</sub> L<sub>pix</sub></i>(<i>G<sub>A</sub></i>, <i>G<sub>B</sub></i>, <i>p</i>, <i>&eta;<sub>p</sub></i>)
</div>

Where <i>&eta;<sub>p</sub></i> &in; <i>M</i>.

<div style="display: flex; flex-direction: column; align-items: center; margin: 1rem 0;">

<p style="font-size: 0.9em; margin-bottom: 10px; text-align: center;">
    <span style="user-select: none;">Table 2: </span>
    Breakdown of Terms
</p>

<table style="width: auto; min-width: 200px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid #ccc;">
      <th style="text-align: center; padding: 8px;">Symbol</th>
      <th style="text-align: center; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sup>M</sup><sub>GAN</sub></i></td>
      <td style="padding: 8px;">Specialized GAN loss for open-domain classes (where <i>&eta;<sub>p</sub></i> &in; <i>M</i>).</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>&lambda;<sub>A</sub></i>, <i>&lambda;<sub>pix</sub></i></td>
      <td style="padding: 8px;">Weighting hyperparameters for adversarial and pixel-wise loss.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sub>G<sub>A</sub></sub></i></td>
      <td style="padding: 8px;">Loss function for Generator A.</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px;"><i>L<sub>pix</sub></i></td>
      <td style="padding: 8px;">Pixel consistency loss function.</td>
    </tr>
    <tr>
      <td style="padding: 8px;"><i>&eta;<sub>p</sub></i> &in; <i>M</i></td>
      <td style="padding: 8px;">Condition specifying the noise variable <i>&eta;<sub>p</sub></i> is drawn from set <i>M</i>.</td>
    </tr>
  </tbody>
</table>

</div>

As a result, the open-domain classes get pixelated images from the drawing to photo generator <i>G<sub>B</sub></i> since <i>L<sub>1</sub></i> and <i>L<sub>2</sub></i> loss leads to the median and mean of pixels, respectively.

### Training strategy for limited data: zero-shot/open-domain

For example,

<div style="display: flex; flex-direction: column; align-items: center; margin: 1rem 0;">

<p style="font-size: 0.9em; margin-bottom: 10px; text-align: center;">
    <span style="user-select: none;">Table 3: </span>
    Example
</p>

<table style="width: auto; min-width: 200px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid #ccc;">
      <th style="text-align: center; padding: 8px;">Index</th>
      <th style="text-align: center; padding: 8px;">Category</th>
      <th style="text-align: center; padding: 8px;">Sketch Number</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">0</td>
      <td style="padding: 8px; text-align: center;">Pineapple</td>
      <td style="padding: 8px; text-align: center;">151</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">1</td>
      <td style="padding: 8px; text-align: center;">Strawberry</td>
      <td style="padding: 8px; text-align: center;">0</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">2</td>
      <td style="padding: 8px; text-align: center;">Basketball</td>
      <td style="padding: 8px; text-align: center;">147</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">3</td>
      <td style="padding: 8px; text-align: center;">Chicken</td>
      <td style="padding: 8px; text-align: center;">0</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">4</td>
      <td style="padding: 8px; text-align: center;">Cookie</td>
      <td style="padding: 8px; text-align: center;">146</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">5</td>
      <td style="padding: 8px; text-align: center;">Cupcake</td>
      <td style="padding: 8px; text-align: center;">0</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">6</td>
      <td style="padding: 8px; text-align: center;">Moon</td>
      <td style="padding: 8px; text-align: center;">0</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">7</td>
      <td style="padding: 8px; text-align: center;">Orange</td>
      <td style="padding: 8px; text-align: center;">146</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">8</td>
      <td style="padding: 8px; text-align: center;">Soccer</td>
      <td style="padding: 8px; text-align: center;">0</td>
    </tr>
    <tr>
      <td style="padding: 8px; text-align: center;">9</td>
      <td style="padding: 8px; text-align: center;">Watermelon</td>
      <td style="padding: 8px; text-align: center;">146</td>
    </tr>
  </tbody>
</table>

</div>

To address this issue, we suggest a random-mixed sampling method to reduce the impact of the domain gap between real and false sketch inputs on the generator. This approach mainly consists of generating fake drawings from pictures and mixing them randomly with the actual ones in the pre-built batch. Consequently, it will enhance the quality of the output with open-domain categories. All in-domain and open-domain classes are invisible to the random mixing procedure. As a direct consequence, the batch pool gets enhanced with both genuine and fake produced drawings and related tags from various epochs during the learning process.

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(5)%20Proposed%20Solution%20-%20Mixed%20Sampling%20with%20Batchwise%20Substitution.jpg" caption="Proposed Solution: Mixed Sampling with Batchwise Substitution" align="center" >}}

### Random Mixed Strategy

The goal of this method is to deceive the generator into thinking bogus sketches are real.

#### Algorithm: Minibatch Random-Mixed Sampling and Updating

<div style="font-family: 'Times New Roman', serif; font-size: 1.1em; background: rgba(128, 128, 128, 0.05); padding: 20px; border-radius: 8px; margin: 1.5rem 0; text-align: left;">
<p><b>Input:</b> In training set <i>D</i>, each minibatch contains photo set <i>p</i>, freehand sketch set <i>s</i>, the class label of photo <i>&eta;<sub>p</sub></i>, and the class label of sketch <i>&eta;<sub>s</sub></i>;</p>
<p><b>for</b> number of training iterations <b>do</b></p>
<div style="margin-left: 20px;">
    <p><i>s<sub>fake</sub></i> &larr; <i>G<sub>A</sub></i>(<i>p</i>);</p>
    <p><i>s<sub>c</sub></i> &larr; <i>s</i>;</p>
    <p><i>&eta;<sub>c</sub></i> &larr; <i>&eta;<sub>s</sub></i>;</p>
    <p><b>if</b> <i>t</i> &lt; <i>u</i> ~ <i>U</i>(0, 1) <b>then</b></p>
    <div style="margin-left: 20px;">
        <p>&mid; <i>s<sub>c</sub></i>, <i>&eta;<sub>c</sub></i> &larr; <i>pool.query</i>(<i>s<sub>fake</sub></i>, <i>&eta;<sub>p</sub></i>);</p>
    </div>
    <p><b>end</b></p>
    <p><i>p<sub>rec</sub></i> &larr; <i>G<sub>B</sub></i>(<i>s<sub>fake</sub></i>, <i>&eta;<sub>p</sub></i>);</p>
    <p><i>p<sub>fake</sub></i> &larr; <i>G<sub>B</sub></i>(<i>s</i>, <i>&eta;<sub>s</sub></i>);</p>
    <p>Calculate <i>L<sub>GAN</sub></i> with (<i>p</i>, <i>s<sub>c</sub></i>, <i>p<sub>rec</sub></i>, <i>&eta;<sub>c</sub></i>) and update <i>G<sub>A</sub></i> and <i>G<sub>B</sub></i>;</p>
    <p>Calculate <i>L<sub>D<sub>A</sub></sub></i>(<i>s</i>, <i>s<sub>fake</sub></i>) and <i>L<sub>D<sub>A</sub></sub></i>(<i>p</i>, <i>p<sub>fake</sub></i>), update <i>D<sub>A</sub></i> and <i>D<sub>B</sub></i>;</p>
    <p>Calculate <i>L<sub>R</sub></i>(<i>p</i>, <i>p<sub>fake</sub></i>, <i>&eta;<sub>p</sub></i>, <i>&eta;<sub>s</sub></i>) and update the classifier</p>
</div>
<p><b>end</b></p>
</div>

<div style="display: flex; flex-direction: column; align-items: center; margin: 1rem 0;">

<p style="font-size: 0.9em; margin-bottom: 10px; text-align: center;">
    <span style="user-select: none;">Table 4: </span>
    Breakdown of Steps
</p>

<table style="width: auto; min-width: 200px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid #ccc;">
      <th style="text-align: center; padding: 8px;">Step</th>
      <th style="text-align: center; padding: 8px;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; font-weight: bold;">Initialization</td>
      <td style="padding: 8px;">The algorithm iterates through a training set <i>D</i> using minibatches of photos (<i>p</i>), sketches (<i>s</i>), and their respective class labels (<i>&eta;<sub>p</sub></i>, <i>&eta;<sub>s</sub></i>).</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; font-weight: bold;">Sketch Generation (<i>G<sub>A</sub></i>)</td>
      <td style="padding: 8px;">The network uses Generator A to create a fake sketch (<i>s<sub>fake</sub></i>) based on the input photo (<i>p</i>).</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; font-weight: bold;">Pool Mechanism</td>
      <td style="padding: 8px;">A decision block uses a random variable <i>u</i> and a threshold <i>t</i>. If the condition is met, the "current" sketch (<i>s<sub>c</sub></i>) and label (<i>&eta;<sub>c</sub></i>) are updated by querying a pool using the fake sketch and photo label. Otherwise, they remain as the real sketch (<i>s</i>) and its label (<i>&eta;<sub>s</sub></i>).</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; font-weight: bold;">Reconstruction and Fake Photo Generation (<i>G<sub>B</sub></i>)</td>
      <td style="padding: 8px;">
        <i>p<sub>rec</sub></i>: Generator B attempts to reconstruct the photo from the fake sketch and the photo label.<br>
        <i>p<sub>fake</sub></i>: Generator B generates a fake photo from the real sketch and the sketch label.
      </td>
    </tr>
    <tr>
      <td style="padding: 8px; font-weight: bold;">Loss Calculation and Parameter Updates</td>
      <td style="padding: 8px;">
        <b>Generators:</b> The total GAN loss (<i>L<sub>GAN</sub></i>) is calculated using the photos, current sketches, reconstructed photos, and current labels, followed by updates to <i>G<sub>A</sub></i> and <i>G<sub>B</sub></i>.<br>
        <b>Discriminators:</b> The discriminator losses are calculated comparing real vs. fake sketches and real vs. fake photos, followed by updates to <i>D<sub>A</sub></i> and <i>D<sub>B</sub></i>.<br>
        <b>Classifier:</b> A regularization or recognition loss (<i>L<sub>R</sub></i>) is calculated, and the classifier is updated accordingly.
      </td>
    </tr>
  </tbody>
</table>

</div> 

---

## Network Architecture

We show how our framework's architecture works, including generators, discriminators, and a classifier. Note that our proposed method is not tied to a certain network design; we chose the CycleGAN as a baseline to demonstrate its effectiveness. As a result, we merely alter the <i>G<sub>B</sub></i> to a multi-class generator and leave the rest of the structures alone, as seen below.

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(6)%20Multi-Class%20Sketch-to-Photo%20Generator%20Architecture.png" caption="Multi-Class Sketch-to-Photo Generator Architecture" align="center" >}}

---

## Sketch-To-Photo Synthesis

To show the efficacy of our method, we use CycleGAN [[14]](#ref-14) as the basis for creating our network. We converted the sketch-to-photo translator into a conditional generator so that it could receive sketch class labels. We compared a recent EdgeGAN [[15]](#ref-15) study on each dataset with different other models. On all datasets, we can state that our model is chosen by more people than other approaches and delivers greater performance in terms of FID [[16]](#ref-16) rating and classification accuracy. We also put our produced robustness to the test against the input. Our approach works well for drawings that have been altered by deleting and introducing strokes.

---

## Photo-To-Sketch Synthesis

For a given photo, our network can also generate a high-quality freehand sketch generator <i>G<sub>A</sub></i>. Beyond the edge map of a photo, our model can create numerous types of freehand drawings like human drawers, even for invisible things. The weights of the generator are continually updated as the training advances, which is characterised by joint training. As a byproduct, the drawings produced by <i>G<sub>A</sub></i> evolve epoch by epoch. The changing drawings broaden the sketch's diversity, which can help the sketch-to-photo generator generalise to a wider range of hand-drawn sketch sources.

---

## Experiments

### Implementation

PyTorch was used for the implementation of the model and training was done with the Adam algorithm [[17]](#ref-17), an optimiser for deep learning. We trained using 1 NVIDIA V100 GPU. The loss function to train the generator contains four elements: the adversarial loss of photo-to-sketch generation <i>L<sub>G<sub>A</sub></sub></i>, the adversarial loss of sketch-to-photo translation <i>L<sub>G<sub>B</sub></sub></i>, the pixel-wise consistency of photo reconstruction <i>L<sub>pix</sub></i>, and the classification loss for synthesised photo <i>L<sub>&eta;</sub></i>. For the discriminator’s <i>D<sub>A</sub></i> and <i>D<sub>B</sub></i>, two-loss functions are used.

For all datasets, the batch size is set at 1 and the initial learning rate is set at 2e - 4.

The epoch numbers for the Scribble [[18]](#ref-18), QMUL-Sketch [[19]](#ref-19), and SketchyCOCO [[15]](#ref-15) are 200, 400, and 100, respectively. In the second half of the epochs, the learning rates are multiplied by 0.5.

### Dataset

The model was trained using three sets of data: Scribble which contained 10 classes, SketchyCOCO which contained 14 classes of objects, and open domain setting. To satisfy the open-domain conditions, the drawings of some classes are eliminated during the training stage.

### Results

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(7)%20Results%20on%20Scribble%20Dataset.png" caption="Results on Scribble Dataset" align="center" >}}

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(8)%20Results%20on%20SketchCOCO%20Dataset.png" caption="Results on SketchCOCO Dataset" align="center" >}}

{{< figure src="Adversarial%20Open%20Domain%20Adaption%20Framework%20(AODA)%20Sketch-To-Photo%20Synthesis/Figures/Figure%20(9)%20Results%20on%20%20QMUL-Sketch%20Dataset.png" caption="Results on QMUL-Sketch Dataset" align="center" >}}

As we can see, the output photos are very similar to the open domain inputs. Based on the shape of the input image, the framework can synthesise the output as well as colouring the photo.

### Evaluation Metrics

Quantitative evaluation was done with three distinct metrics. The Frechet Inception Distance (FID) analyses the feature similarity of generated and actual image collections. A low FID score indicates that the produced pictures are less dissimilar to the genuine ones and hence have good integrity. Classification Accuracy of produced pictures. Having higher accuracy implies realistic images. And finally, User Preference Study in which we display the users a provided drawing and the class label, and ask them to choose one photo from the produced results that has the highest quality and authenticity.

### Comparison with Other Methods

To demonstrate the efficiency of our model, we have compared it with several other solutions like CycleGAN, conditional CycleGAN, Classifier and CycleGAN, EdgeGAN. We have used two datasets for this comparison: Scribble and SketchyCOCO. For some, we have given as input open domain sketches.

**Scribble:** The initial CycleGAN displays mode collapse and synthesises similar textures for all categories, most likely because the sketches in the Scribble dataset hardly suggest their class names. This issue is resolved with the conditional CycleGAN but it still fails to generate real pictures for some classes. For the classifier and conditional CycleGAN, the gap between the open domain and in-domain data is even bigger, because the classifier widens current differences. The EdgeGAN is closer to the input shape but still doesn't entirely translate the sketch. The consistency of the model is shown in our results where the mapping of the images is done with accuracy.

**SketchyCOCO:** CycleGAN's outputs struggle from mode collapse whereas conditional CycleGAN cannot create rich textures for open-domain categories. In comparison to EdgeGAN, the postures in our produced photographs are more accurate than the original drawings.

Our model is favoured by more participants than the other techniques evaluated, and that it produces the best results in terms of FID score and classification accuracy across all datasets. And we can see from our comparison that our random mixed sampling algorithm improves both the in the domain and open domain results.

---

## Effectiveness of AODA

### Open-domain classes

1.  Baseline without classifier or strategy.
2.  AODA framework without the strategy.
3.  Trained with pre-extracted open-domain and real in-domain sketches.
4.  Random Mixed sampling strategy.

### Observation

1.  Turn everything to the in-domain category.
2.  Generates texture-less images.
3.  Fails on open-domain category.
4.  AODA strategy can alleviate the above issues and brings superior performance for a multi-class generation.

---

## Conclusion

Synthesis of sketch-to-photo is a challenging task, especially for freehand sketches The open set domain, where the source domain has labelled categories and the target domain has undefined categories, raises an issue as the data is unpaired. To solve this problem, we are proposing an adversarial open domain adaption that can learn how to develop the missing hand-drawn sketches. The framework enables the unsupervised open domain adaption by learning sketch-to-image translation and vice versa. Also, the random mixing sampling method reduces the domain gap’s effect on the generator, thus generating accurate images. Additional testing and user assessments on a variety of samples show that our model can properly synthesize real images for many types of open-domain hand-drawn sketches. Further work in this model can lead to the generation of high-quality photos by improving the design and accuracy.

---

## Additional Resources

### Research Paper

Explore the published research paper and preprint:

<div style="display: flex; flex-direction: column; gap: 8px;">

  <div>
    <!-- arXiv Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;"><path d="M3.8423 0a1.0037 1.0037 0 0 0-.922.6078c-.1536.3687-.0438.6275.2938 1.1113l6.9185 8.3597-1.0223 1.1058a1.0393 1.0393 0 0 0 .003 1.4229l1.2292 1.3135-5.4391 6.4444c-.2803.299-.4538.823-.2971 1.1986a1.0253 1.0253 0 0 0 .9585.635.9133.9133 0 0 0 .6891-.3405l5.783-6.126 7.4902 8.0051a.8527.8527 0 0 0 .6835.2597.9575.9575 0 0 0 .8777-.6138c.1577-.377-.017-.7502-.306-1.1407l-7.0518-8.3418 1.0632-1.13a.9626.9626 0 0 0 .0089-1.3165L4.6336.4639s-.3733-.4535-.768-.463zm0 .272h.0166c.2179.0052.4874.2715.5644.3639l.005.006.0052.0055 10.169 10.9905a.6915.6915 0 0 1-.0072.945l-1.0666 1.133-1.4982-1.7724-8.5994-10.39c-.3286-.472-.352-.6183-.2592-.841a.7307.7307 0 0 1 .6704-.4401Zm14.341 1.5701a.877.877 0 0 0-.6554.2418l-5.6962 6.1584 1.6944 1.8319 5.3089-6.5138c.3251-.4335.479-.6603.3247-1.0292a1.1205 1.1205 0 0 0-.9763-.689zm-7.6557 12.2823 1.3186 1.4135-5.7864 6.1295a.6494.6494 0 0 1-.4959.26.7516.7516 0 0 1-.706-.4669c-.1119-.2682.0359-.6864.2442-.9083l.0051-.0055.0047-.0055z"></path></svg>
    <a href="https://arxiv.org/abs/2108.04351" target="_blank">arXiv Preprint</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://www.ijeast.com/papers/251-257,Tesma602,IJEAST.pdf" target="_blank">Full Paper (IJEAST)</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Adversarial Open Domain Adaption Framework (AODA): Sketch-to-Photo Synthesis". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-28-adversarial-open-domain-adaption-frameworka-aoda-sketch-to-photo-synthesis/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2021aoda,
  title   = "Adversarial Open Domain Adaption Framework (AODA): Sketch-to-Photo Synthesis",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-28-adversarial-open-domain-adaption-frameworka-aoda-sketch-to-photo-synthesis/"
}
```

---

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
    <span class="reference-text"><a id="ref-1"></a><b>I. Goodfellow et al.</b>, "Generative adversarial networks," <i>Communications of the ACM</i>, vol. 63, no. 11, pp. 139-144, 2020, DOI: <a href="https://doi.org/10.1145/3422622">10.1145/3422622</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>X. Wang and J. Yu</b>, "Learning to cartoonize using white-box cartoon representations," in <i>Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition</i>, pp. 8090-8099, 2020, DOI: <a href="https://doi.org/10.1109/CVPR42600.2020.00811">10.1109/CVPR42600.2020.00811</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>A. Thakur, H. Rizvi, and M. Satish</b>, "White-Box Cartoonization Using An Extended GAN Framework," <i>arXiv preprint arXiv:2107.04551</i>, 2021, DOI: <a href="https://doi.org/10.48550/arXiv.2107.04551">10.48550/arXiv.2107.04551</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>T. Dekel, C. Gan, D. Krishnan, C. Liu, and W. T. Freeman</b>, "Sparse, smart contours to represent and edit images," in <i>Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition</i>, pp. 3511-3520, 2018, DOI: <a href="https://doi.org/10.1109/CVPR.2018.00370">10.1109/CVPR.2018.00370</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>A. K. Bhunia, Y. Yang, T. M. Hospedales, T. Xiang, and Y.-Z. Song</b>, "Sketch less for more: On-the-fly fine-grained sketch-based image retrieval," in <i>Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition</i>, pp. 9779-9788, 2020, DOI: <a href="https://doi.org/10.1109/CVPR42600.2020.00980">10.1109/CVPR42600.2020.00980</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>X. Han, C. Gao, and Y. Yu</b>, "Deepsketch2face: A deep learning based sketching system for 3d face and caricature modeling," <i>ACM Transactions on graphics (TOG)</i>, vol. 36, no. 4, pp. 1-12, 2017, DOI: <a href="https://doi.org/10.1145/3072959.3073629">10.1145/3072959.3073629</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>W. Chen and J. Hays</b>, "Sketchygan: Towards diverse and realistic sketch to image synthesis," in <i>Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition</i>, pp. 9416-9425, 2018, DOI: <a href="https://doi.org/10.1109/CVPR.2018.00981">10.1109/CVPR.2018.00981</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>Z. Fang, J. Lu, F. Liu, J. Xuan, and G. Zhang</b>, "Open set domain adaptation: Theoretical bound and algorithm," <i>IEEE Transactions on Neural Networks and Learning Systems</i>, 2020, DOI: <a href="https://doi.org/10.48550/arXiv.1907.08375">10.48550/arXiv.1907.08375</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>D. Li, Y. Yang, Y.-Z. Song, and T. M. Hospedales</b>, "Deeper, broader and artier domain generalization," in <i>Proceedings of the IEEE international conference on computer vision</i>, pp. 5542-5550, 2017, DOI: <a href="https://doi.org/10.1109/ICCV.2017.591">10.1109/ICCV.2017.591</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>P. Isola, J.-Y. Zhu, T. Zhou, and A. A. Efros</b>, "Image-to-image translation with conditional adversarial networks," in <i>Proceedings of the IEEE conference on computer vision and pattern recognition</i>, pp. 1125-1134, 2017, DOI: <a href="https://doi.org/10.1109/CVPR.2017.632">10.1109/CVPR.2017.632</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>X. Xiang, D. Liu, X. Yang, Y. Zhu, X. Shen, and J. P. Allebach</b>, "Adversarial Open Domain Adaption for Sketch-to-Photo Synthesis," <i>arXiv preprint arXiv:2104.05703</i>, 2021, DOI: <a href="https://doi.org/10.48550/arXiv.2104.05703">10.48550/arXiv.2104.05703</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>T. Shermin, G. Lu, S. W. Teng, M. Murshed, and F. Sohel</b>, "Adversarial Network with Multiple Classifiers for Open Set Domain Adaptation," <i>arXiv preprint arXiv:2007.00384</i>, 2020, DOI: <a href="https://doi.org/10.48550/arXiv.2007.00384">10.48550/arXiv.2007.00384</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[13]</span>
    <span class="reference-text"><a id="ref-13"></a><b>M. Mirza and S. Osindero</b>, "Conditional generative adversarial nets," <i>arXiv preprint arXiv:1411.1784</i>, 2014, DOI: <a href="https://doi.org/10.48550/arXiv.1411.1784">10.48550/arXiv.1411.1784</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[14]</span>
    <span class="reference-text"><a id="ref-14"></a><b>M.-Y. Liu, T. Breuel, and J. Kautz</b>, "Unsupervised image-to-image translation networks," <i>arXiv preprint arXiv:1703.00848</i>, 2017, DOI: <a href="https://doi.org/10.48550/arXiv.1703.00848">10.48550/arXiv.1703.00848</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[15]</span>
    <span class="reference-text"><a id="ref-15"></a><b>C. Gao, Q. Liu, Q. Xu, L. Wang, J. Liu, and C. Zou</b>, "SketchyCOCO: Image Generation from Freehand Scene Sketches," <i>arXiv preprint arXiv:2003.02683</i>, 2020, DOI: <a href="https://doi.org/10.48550/arXiv.2003.02683">10.48550/arXiv.2003.02683</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[16]</span>
    <span class="reference-text"><a id="ref-16"></a><b>A. Obukhov and M. Krasnyanskiy</b>, "Quality Assessment Method for GAN Based on Modified Metrics Inception Score and Fréchet Inception Distance," in <i>Proceedings of the Computational Methods in Systems and Software</i>, pp. 102-114, Springer, Cham, 2020, DOI: <a href="https://doi.org/10.1007/978-3-030-63322-6_8">10.1007/978-3-030-63322-6_8</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[17]</span>
    <span class="reference-text"><a id="ref-17"></a><b>D. P. Kingma and J. Ba</b>, "Adam: A method for stochastic optimization," <i>arXiv preprint arXiv:1412.6980</i>, 2014, DOI: <a href="https://doi.org/10.48550/arXiv.1412.6980">10.48550/arXiv.1412.6980</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[18]</span>
    <span class="reference-text"><a id="ref-18"></a><b>A. Ghosh, R. Zhang, P. K. Dokania, O. Wang, A. A. Efros, P. H. Torr, and E. Shechtman</b>, "Interactive sketch & fill: Multiclass sketch-to-image translation," in <i>Proceedings of the IEEE/CVF International Conference on Computer Vision</i>, pp. 1171-1180, 2019, DOI: <a href="https://doi.org/10.48550/arXiv.1909.11081">10.48550/arXiv.1909.11081</a> [Accessed: Jul. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[19]</span>
    <span class="reference-text"><a id="ref-19"></a><b>R. Liu, Q. Yu, and S. Yu</b>, "Unsupervised Sketch to Photo Synthesis," <i>arXiv preprint arXiv:1909.08313</i>, 2019, DOI: <a href="https://doi.org/10.48550/arXiv.1909.08313">10.48550/arXiv.1909.08313</a> [Accessed: Jul. 28, 2021].</span>
</div>

</div>
