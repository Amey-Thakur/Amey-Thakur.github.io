---
title: "White-Box Cartoonization: An Extended GAN Framework"
date: 2021-07-09T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["AI", "Artificial Intelligence", "Cartoonization", "Computer Vision", "CV", "Deep Learning", "GAN", "Generative Adversarial Networks", "Image Processing", "Image-to-Image Translation", "Machine Learning", "ML", "Neural Networks", "Python", "Style Transfer", "TensorFlow", "White-Box Cartoonization"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Mega Satish and Hasan Rizvi for their meaningful contributions, support, and wisdom that helped shape this work. In the present study, we propose to implement a new framework for estimating generative models via an adversarial process to extend an existing GAN framework and develop a white-box controllable image cartoonization, which can generate high-quality cartooned images/videos from real-world photos and videos."
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

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=7Ajrr6EAAAAJ&hl=en">Mega Satish</a> and <a href="https://scholar.google.com/citations?user=OJuGq08AAAAJ&hl=en">Hasan Rizvi</a> for their meaningful contributions, support, and wisdom that helped shape this work.
</p>

In the present study, we propose to implement a new framework for estimating generative models via an adversarial process to extend an existing GAN framework and develop a white-box controllable image cartoonization, which can generate high-quality cartooned images/videos from real-world photos and videos. The learning purposes of our system are based on three distinct representations: surface representation, structure representation, and texture representation. The surface representation refers to the smooth surface of the images. The structure representation relates to the sparse colour blocks and compresses generic content. The texture representation shows the texture, curves, and features in cartoon images. Generative Adversarial Network (GAN) framework decomposes the images into different representations and learns from them to generate cartoon images. This decomposition makes the framework more controllable and flexible which allows users to make changes based on the required output. This approach overcomes any previous system in terms of maintaining clarity, colours, textures, shapes of images yet showing the characteristics of cartoon images.

---

## Introduction

Cartoons are a highly popular art style that has been extensively used in a variety of contexts, from print media to children's narrative. Some cartoon artwork was created based on real-world scenes. However, manually re-creating situations from real life may be very time consuming and needs specialised abilities. Machine Learning advancements have increased the possibilities for producing visual artworks. A cartoon is a popular style of art that has been adapted for usage in a wide range of contexts. By turning real-world photos into usable cartoon scene components, the method of image cartoonization has resulted in the development of many well-known products. White box cartoonization is a method that reconstructs high-quality real-life pictures into exceptional cartoon images using the GAN framework.

The motivation of this paper is to build sophisticated cartoon animation processes that enable artists to generate material from a range of sources. Artists often use filters supplied by various software to cartoonize images/videos, however, the industry-standard software degrades the quality during translation. Additionally, meticulously recreating real-world events in cartoon styles involves a great deal of time and work, as well as a great deal of creative ability. Manually cartoonizing pictures frame by frame and producing high-quality cartoons is a time-consuming process. Existing software fails to produce the required outputs due to issues such as generator-discriminator stability. As a consequence, specially developed techniques for automatically converting real-world photos into high-quality cartoon-style images are very beneficial, as they enable artists to finish their work with more precision and in less time.

Many models have been developed to generate cartoon images from pictures, but have many drawbacks. CartoonGAN [[1]](#ref-1) is one of the technologies to generate cartoonized images but it adds noise and reduces the quality of an image. On the other hand, White Box Cartoonization [[2]](#ref-2) overcomes these problems and results in more precise and sharp images.

The challenges in CartoonGAN are the stability between generator and discriminator, the inaccurate positioning of the object,  and understanding the perspective of images i.e. 2D or 3D as well as global objects i.e. trees, flowers, etc.

White Box Cartoonization is a variant of Black Box Cartoonization that addresses the latter's shortcomings. For example, in some cartoon workflows, by analysing the processed dataset, global palette themes are prioritised over line sharpness as a secondary concern. For others, the sharpness of objects and persons hold a great value. Black box cartoonization algorithms fail to deal with such various workflow requirements and applying a black-box model to directly fit the training data might have a severe impact on generality and stylization quality, resulting in low-quality outputs.

To get a better idea of Cartoonization, researchers consulted artists and observed cartoon painting behaviour to identify three separate cartoon image representations: a surface representation that contains smooth surfaces, a structure representation that refers to sparse colour-blocks and flattens global content in the workflow, and a texture representation that reflects high-frequency texture, contours, and details in cartoon images.

Each representation is retrieved using image processing modules, and the extracted representations are then learned and cartoonized using a generative adversarial network (GAN) architecture [[3]](#ref-3). Tuning the value of each representation in the loss function may be used to alter the output style.

In a user survey with ten respondents and thirty pictures, the suggested technique beat three current techniques in terms of cartoon quality (similarity between the input and cartoon pictures) and quality of the product (identifying undesirable colour shifts, texture distortions, high-frequency noise or other artefacts in the images).

---

## Related Work

### Preprocessing

Preprocessing, in addition to the proposed three-step method, is a key component of our model. It aids in the smoothing of images, the filtering of features, the conversion of images to sketches, and the translation of output from one domain to another. Following the completion of these associated tasks, we can be confident that the output provided by our model will be of the highest quality.

### Image to Image Translation

For image cartoonization, we use an unpaired image-to-image [[4]](#ref-4) translation system in this article. The disadvantage of GAN is that it only works with given training data, and paired training data is not always accessible. To overcome this limitation, we use cycleGAN [[5]](#ref-5), which aims to translate a picture from a source domain X to a target domain Y even in the absence of paired training data. In terms of loss, we deconstruct images into many representations, forcing the network to learn various aspects with distinct goals, making the learning process more manageable and adaptable.

### Generative Adversarial Network

White Box Cartoonization uses an unsupervised learning approach. Hence we use generative modelling. In the generative model, there are samples and data i.e. x (input variable) and y (It does not have an output variable). Deep learning-based generative models are used for unsupervised learning. In short,  it's a system where two networks compete with each other to create or generate variation in the data. In 2014 a framework for estimating generative networks was introduced and further many algorithms were used to enhance the adversarial process.

### GAN Architecture

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Fig.%20(1)%20Architecture%20of%20GAN.jpg" caption="Architecture of GAN" align="center" >}}

GAN is made up of two models [[6]](#ref-6), namely generative and discriminative. The generator (G) is a network that processes input and generates sample data. The discriminator (D) determines whether the data is produced or taken from the original sample by using binary classification problems and a sigmoid function that returns values between 0 and 1.

In machine learning, there are two major techniques for developing predictive models. The discriminative model is the most well-known. In this scenario, the model learns the target variable's conditional probability given the input variable, i.e. <i>P</i>(<i>Y</i>|<i>X</i>=<i>x</i>). Examples include logistic regression, linear regression, and so on.

The generative model, on the other hand, learns the joint probability distribution of the input variable and the output variable, i.e. <i>P</i>(<i>X</i>, <i>Y</i>) = <i>P</i>(<i>X</i>|<i>Y</i>)<i>P</i>(<i>Y</i>) = <i>P</i>(<i>Y</i>|<i>X</i>)<i>P</i>(<i>X</i>). If the model wishes to predict something, it employs the Bayes theorem to calculate the conditional probability of the target variable given the input variable, i.e. <i>P</i>(<i>Y</i>|<i>X</i>) = <i>P</i>(<i>X</i>, <i>Y</i>)/<i>P</i>(<i>X</i>).

A prominent example of generative models is Naive Bayes. The most significant advantage of the generative model over the discriminative model is that we can use it to create new instances of data because we are learning the distribution function of the data itself, which a discriminator cannot do. To generate fresh data points in GANs, we employ a generative model.

We implement the discriminator to determine whether a given data point is original or generated by our generator. Now, these two models operate in an adversarial environment, which means they compete with each other and eventually both of them improve.

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Fig.%20(2)%20High-level%20structure%20of%20GAN.jpg" caption="High-level structure of GAN" align="center" >}}

G and D are multi-layered neural networks, θg and θd are the respective weights. We are using neural networks because they can approximate any function we know from the universal approximation theorem. The distribution function of the original data is shown above. In reality, we cannot really draw or mathematically compute the distribution function of original data because we input images, voices, videos and they are higher dimensional complex data so graphs are shown for mathematical analysis.

In noise distribution, we show the normal distribution because we sample randomly some data from the distribution and we feed that to our generator. <i>z</i> contains no information, we input it to the generator and it will produce <i>G</i>(<i>z</i>). The domain of the original data is the same as the range of <i>G</i>(<i>z</i>). It is necessary as we are trying to replicate original data. <i>p</i><sub>data</sub> represents the probability distribution of original data. <i>p</i><sub>z</sub> represents the distribution of noise and <i>p</i><sub>g</sub> represents the distribution function of the output of the generator. We are passing original data and reconstructed data to the discriminator which will provide us with a single number that will tell the probability of the input belonging to the original data. As we can see, the discriminator is just a simple binary classifier. For training purposes, when we input original data to the discriminator we take <i>Y</i>=1. For reconstructed data we take <i>Y</i>=0. <i>D</i> will try to maximise the chances of predicting correct classes but <i>G</i> will try to fool <i>D</i>.

#### Value function for GAN:

The Objective Function

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
    <i>min</i><sub><i>G</i></sub> <i>max</i><sub><i>D</i></sub> <i>V</i>(<i>G</i>,<i>D</i>) = <i>E</i><sub><i>x</i>~<i>p</i><sub>data</sub></sub>[ln <i>D</i>(<i>x</i>)] + <i>E</i><sub><i>z</i>~<i>p</i><sub>z</sub></sub>[ln(1 − <i>D</i>(<i>G</i>(<i>z</i>)))]
</div>

#### Interpretation

This equation defines a minimax game between two models: a Generator <i>G</i> and a Discriminator <i>D</i>.

*   **Generator (<i>G</i>)** aims to minimize the objective by producing samples that are indistinguishable from real data.
*   **Discriminator (<i>D</i>)** aims to maximize the objective by correctly separating real samples from generated ones.

#### Term-by-Term Breakdown

**Real data term**

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2rem; text-align: center; background: rgba(128, 128, 128, 0.05); padding: 15px; border-radius: 8px; margin: 1rem 0;">
    <i>E</i><sub><i>x</i>~<i>p</i><sub>data</sub></sub>[ln <i>D</i>(<i>x</i>)]
</div>

Encourages the discriminator to assign high probability to real data samples.

**Generated data term**

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2rem; text-align: center; background: rgba(128, 128, 128, 0.05); padding: 15px; border-radius: 8px; margin: 1rem 0;">
    <i>E</i><sub><i>z</i>~<i>p</i><sub>z</sub></sub>[ln(1 − <i>D</i>(<i>G</i>(<i>z</i>)))]
</div>

Captures how well the generator can fool the discriminator using samples generated from noise <i>z</i>.

#### Key Idea

Training proceeds as an adversarial process: the discriminator learns to distinguish real from fake, while the generator learns to produce increasingly realistic samples. This objective forms the foundation of Generative Adversarial Networks (GANs).

---

## Model Architecture

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Fig.%20(3)%20Representation%20Techniques.png" caption="Representation Techniques" align="center" >}}

### Surface Representation

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Fig.%20(4)%208-step%20edge-preserving%20filtering%20with%20(a)-(d)%20flat%20and%20(e)%20flexible%20intensity%20models.png" caption="8-step edge-preserving filtering with (a)-(d) flat and (e) flexible intensity models" align="center" >}}

Surface representation is similar to cartoon painting in which painters draw early sketches with rough strokes and possess smooth surfaces comparable to cartoon imagery. For edge-preserving filtering [[7]](#ref-7), a differentiable guided filter is used to smooth images while keeping the global semantic structure. Guided filters [[8]](#ref-8) are a more advanced variant of bilateral filters that perform better towards the edge. In simple terms, this filter preserves the edges and its information while blurring an image Examples are the median, bilateral, guided, and anisotropic diffusion filters. As compared to CartoonGAN, White box cartoonization reduces artefacts at significant levels.

### Structure Representation

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Fig.%20(5)%20(a)%20Input%20(b)%20Visualisation%20(c)%20Output.png" caption="(a) Input (b) Visualisation (c) Output" align="center" >}}

Structure representation is used to segment images into separate regions. The segmentation is done using the Felzenszwalb algorithm [[9]](#ref-9). This algorithm also assists us in capturing generic content information and producing outputs that are practically suitable for celluloid-style animation procedures. The pixel value average is used to colour each segmented region in standard superpixel [[10]](#ref-10) algorithms. However, they only evaluate pixel similarity and disregard semantic information; we use selective search to combine segmented regions and produce a sparse segmentation map. We discovered that this reduces global contrast, darkens images, and generates hazing effects in the final results by studying the processed dataset. To overcome these constraints, we propose an adaptive colouring algorithm. SLIC (Simple Linear Iterative Clustering) [[11]](#ref-11) algorithm is used for superpixel generation. It generates superpixels by clustering pixels on the basis of colour similarity and proximity in the image plane.

### Texture Representation

The high-frequency elements of cartoon images are important learning objectives, but brightness and colour information help differentiate cartoon images from real-world photography. As a result, we suggest a random colour shift algorithm. The random colour shift can provide random intensity maps that are devoid of luminance and colour information. <i>F</i><sub>rcs</sub> extracts single-channel texture representation from colour images, which retains high-frequency textures and decreases the influence of colour and luminance.

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.2rem; text-align: center; background: rgba(128, 128, 128, 0.05); padding: 15px; border-radius: 8px; margin: 1rem 0;">
    <i>F</i><sub>rcs</sub>(<i>I</i><sub>rgb</sub>) = (1 − <i>&alpha;</i>)(<i>&beta;</i><sub>1</sub> ∗ <i>I</i><sub>r</sub> + <i>&beta;</i><sub>2</sub> ∗ <i>I</i><sub>g</sub> + <i>&beta;</i><sub>3</sub> ∗ <i>I</i><sub>b</sub>) + <i>&alpha;</i> ∗ <i>Y</i>
</div>

Where, <i>I</i><sub>rgb</sub> represents 3-channel RGB colour images, <i>I</i><sub>r</sub>, <i>I</i><sub>g</sub> and <i>I</i><sub>b</sub> represent three colour channels, and <i>Y</i> represents standard grayscale image converted from RGB colour image. Note: We set <i>&alpha;</i> = 0.8, <i>&beta;</i><sub>1</sub>, <i>&beta;</i><sub>2</sub> and <i>&beta;</i><sub>3</sub> ∼ <i>U</i>(−1, 1).

---

## Experimental Setup

### Implementation

TensorFlow is used to deploy our GAN methodology. [[12]](#ref-12) A discriminator is suggested to check whether the result and associated cartoon pictures have comparable surfaces and to control the generator to learn the information encoded in the extracted surface representation. To separate the regions, we use the Felzenszwalb method. We employ a pretrained VGGNetwork [[13]](#ref-13) to enforce a spatial limitation on content between outputs and given matching cartoons.

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Web_UI_Implementation.png" caption="Web UI Implementation" align="center" >}}

### Dataset

Data on human faces and landscapes are collected for standardization across different situations. The data contains both real-world and cartoon pictures, but the test data only comprises real-world photographs. All of the photos have been scaled and cropped to 256*256 pixels. Photos are obtained from the Internet and used for testing.

### Learning Rate

When fine-tuning our model's hyperparameters, we initially used a grid search to obtain an ideal learning rate of 0.001. Our mini-batch size was restricted to two because we were testing locally due to GCloud resource limitations.

### Experimental Result

As we can see in the cartoonized pictures below, they are very similar when it comes to the sharpness of the object and the presence of different colours in the pictures. Additionally, elements like reflection, shadows are depicted with precision.

<video width="100%" autoplay loop muted playsinline>
  <source src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/JOEY%20DOESN'T%20SHARE%20FOOD!!%20[Original%20vs%20Cartoonized].mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<p style="text-align: center; font-size: 14px; margin-top: 10px;"><em>Video 1: Real-time Cartoonization (Original vs Processed)</em></p>

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Result_1.png" caption="(a) Original image (b) Processed image" align="center" >}}

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Result_2.png" caption="(a) Original image (b) Processed image" align="center" >}}

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Result_3.png" caption="(a) Original image (b) Processed image" align="center" >}}

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Result_4.png" caption="(a) Original image (b) Processed image" align="center" >}}

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Result_Balcony.png" caption="(a) Original image (b) Processed image" align="center" >}}

{{< figure src="White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/Figures/Result_5.png" caption="(a) Original image (b) Processed image" align="center" >}}

### Qualitative Evaluation

We offer findings from qualitative tests with information from four distinct methodologies and original photos, as well as qualitative analysis. We use Frechet Inception Distance (FID) [[14]](#ref-14) to evaluate performance in quantitative studies by measuring the distance between the source and target image distributions. Candidates in the user study are asked to rate the cartoon quality and overall quality of various techniques on a scale of 1 to 5. Higher scores indicate higher quality.

### Performance Analysis

Our model is the quickest of the four techniques on all devices and resolutions, and it has the shortest model size. Our model, in particular, can process a 720*1280 picture on GPU in only 17.23ms, allowing it to do real-time High-Resolution video processing workloads. Generality to a wide range of use cases: we test our model on a variety of real-world situations, such as natural landscapes, city vistas, people, and animals.

---

## Conclusion

In this paper, we proposed a deployed white-box controllable image cartoonization framework based on GAN, which can generate high-quality cartoonized images from real-world photos. Images are decomposed into three cartoon representations: the surface representation, the structure representation, and the texture representation. Corresponding image processing modules are used to extract three representations for network training. Extensive quantitative and qualitative experiments have been conducted to validate the performance of our method.

---

## Future Work

Meanwhile, existing systems cannot produce satisfactory results in terms of cartoonization. But further research in this field can lead to various applications in other domains. The model could help generate quick prototypes or sprites for anime, cartoons and games. Games can import shortcut scenes very easily without using motion capture. Also, since it subdues facial features and information in general, it can be used to generate minimal art. It can be modelled as an assistant to graphic designers or animators so the artists can use it to design and produce unique artworks.

---

## YouTube Demonstration

{{< youtube 8VNc8p6AKmw >}}

---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="/posts/2021-07-09-whitebox-cartoonization-an-extended-gan-framework/White-Box%20Cartoonization%20-%20An%20Extended%20GAN%20Framework/MINI-PROJECT_TE-COMPS_B-50,51,58.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

### Project Resources & Research Materials
Explore the full implementation details, local & live demonstrations, source code repositories, and research publications associated with this project:
<div style="display: flex; flex-direction: column; gap: 10px;">
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/8VNc8p6AKmw" target="_blank">YouTube Demonstration</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/WHITE-BOX-CARTOONIZATION" target="_blank">Whitebox Cartoonization Repository (Amey Thakur)</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/msatmod/WhiteBox-Cartoonization-WebApp" target="_blank">Whitebox Cartoonization Repository (Mega Satish)</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/rizvihasan/whitebox_cartoonisation-webapp" target="_blank">Whitebox Cartoonization Repository (Hasan Rizvi)</a>
  </div>
  <div>
    <!-- Web/Globe Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
    <a href="https://amey-thakur.github.io/WHITE-BOX-CARTOONIZATION/" target="_blank">Whitebox Cartoonization Web App</a>
  </div>
  <div>
    <!-- ResearchGate Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;">
        <path d="M19.586 0c-.818 0-1.508.19-2.073.565-.563.377-.97.936-1.213 1.68a3.193 3.193 0 0 0-.112.437 8.365 8.365 0 0 0-.078.53 9 9 0 0 0-.05.727c-.01.282-.013.621-.013 1.016a31.121 31.123 0 0 0 .014 1.017 9 9 0 0 0 .05.727 7.946 7.946 0 0 0 .077.53h-.005a3.334 3.334 0 0 0 .113.438c.245.743.65 1.303 1.214 1.68.565.376 1.256.564 2.075.564.8 0 1.536-.213 2.105-.603.57-.39.94-.916 1.175-1.65.076-.235.135-.558.177-.93a10.9 10.9 0 0 0 .043-1.207v-.82c0-.095-.047-.142-.14-.142h-3.064c-.094 0-.14.047-.14.141v.956c0 .094.046.14.14.14h1.666c.056 0 .084.03.084.086 0 .36 0 .62-.036.865-.038.244-.1.447-.147.606-.108.385-.348.664-.638.876-.29.212-.738.35-1.227.35-.545 0-.901-.15-1.21-.353-.306-.203-.517-.454-.67-.915a3.136 3.136 0 0 1-.147-.762 17.366 17.367 0 0 1-.034-.656c-.01-.26-.014-.572-.014-.939a26.401 26.403 0 0 1 .014-.938 15.821 15.822 0 0 1 .035-.656 3.19 3.19 0 0 1 .148-.76 1.89 1.89 0 0 1 .742-1.01c.344-.244.593-.352 1.137-.352.508 0 .815.096 1.144.303.33.207.528.492.764.925.047.094.111.118.198.07l1.044-.43c.075-.048.09-.115.042-.199a3.549 3.549 0 0 0-.466-.742 3 3 0 0 0-.679-.607 3.313 3.313 0 0 0-.903-.41A4.068 4.068 0 0 0 19.586 0zM8.217 5.836c-1.69 0-3.036.086-4.297.086-1.146 0-2.291 0-3.007-.029v.831l1.088.2c.744.144 1.174.488 1.174 2.264v11.288c0 1.777-.43 2.12-1.174 2.263l-1.088.2v.832c.773-.029 2.12-.086 3.465-.086 1.29 0 2.951.057 3.667.086v-.831l-1.49-.2c-.773-.115-1.174-.487-1.174-2.264v-4.784c.688.057 1.29.057 2.206.057 1.748 3.123 3.41 5.472 4.355 6.56.86 1.032 2.177 1.691 3.839 1.691.487 0 1.003-.086 1.318-.23v-.744c-1.031 0-2.063-.716-2.808-1.518-1.26-1.376-2.95-3.582-4.355-6.074 2.32-.545 4.04-2.722 4.04-4.9 0-3.208-2.492-4.698-5.758-4.698zm-.515 1.29c2.406 0 3.839 1.26 3.839 3.552 0 2.263-1.547 3.782-4.097 3.782-.974 0-1.404-.03-2.063-.086v-7.19c.66-.059 1.547-.059 2.32-.059z"/>
    </svg>
    <a href="https://doi.org/10.13140/RG.2.2.22496.40964" target="_blank">Presentation (ResearchGate)</a>
  </div>
  <div>
    <!-- Project Report - File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://github.com/Amey-Thakur/WHITE-BOX-CARTOONIZATION/blob/main/Mini-Project/Files/MINI-PROJECT_TE-COMPS_B-50%2C51%2C58.pdf" target="_blank">Project Report</a>
  </div>
  <div>
    <!-- arXiv Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;"><path d="M3.8423 0a1.0037 1.0037 0 0 0-.922.6078c-.1536.3687-.0438.6275.2938 1.1113l6.9185 8.3597-1.0223 1.1058a1.0393 1.0393 0 0 0 .003 1.4229l1.2292 1.3135-5.4391 6.4444c-.2803.299-.4538.823-.2971 1.1986a1.0253 1.0253 0 0 0 .9585.635.9133.9133 0 0 0 .6891-.3405l5.783-6.126 7.4902 8.0051a.8527.8527 0 0 0 .6835.2597.9575.9575 0 0 0 .8777-.6138c.1577-.377-.017-.7502-.306-1.1407l-7.0518-8.3418 1.0632-1.13a.9626.9626 0 0 0 .0089-1.3165L4.6336.4639s-.3733-.4535-.768-.463zm0 .272h.0166c.2179.0052.4874.2715.5644.3639l.005.006.0052.0055 10.169 10.9905a.6915.6915 0 0 1-.0072.945l-1.0666 1.133-1.4982-1.7724-8.5994-10.39c-.3286-.472-.352-.6183-.2592-.841a.7307.7307 0 0 1 .6704-.4401Zm14.341 1.5701a.877.877 0 0 0-.6554.2418l-5.6962 6.1584 1.6944 1.8319 5.3089-6.5138c.3251-.4335.479-.6603.3247-1.0292a1.1205 1.1205 0 0 0-.9763-.689zm-7.6557 12.2823 1.3186 1.4135-5.7864 6.1295a.6494.6494 0 0 1-.4959.26.7516.7516 0 0 1-.706-.4669c-.1119-.2682.0359-.6864.2442-.9083l.0051-.0055.0047-.0055z"></path></svg>
    <a href="https://arxiv.org/abs/2107.04551" target="_blank">arXiv Preprint</a>
  </div>
  <div>
    <!-- Full Paper (IJEAST) - File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="http://dx.doi.org/10.33564/IJEAST.2021.v05i12.049" target="_blank">Full Paper (IJEAST)</a>
  </div>
  <div>
    <!-- Graduation Cap Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    <a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING" target="_blank">Computer Engineering Resources</a>
  </div>
</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "White-Box Cartoonization: An Extended GAN Framework". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-09-whitebox-cartoonization-an-extended-gan-framework/.</code></pre>

**Or use the BibTex citation:**


```
@article{thakur2021cartoonization,
  title   = "White-Box Cartoonization: An Extended GAN Framework",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-09-whitebox-cartoonization-an-extended-gan-framework/"
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
    <span class="reference-text"><a id="ref-1"></a><b>B. Corona, M. Nakano, and H. Pérez</b>, "Adaptive Watermarking Algorithm for Binary Image Watermarks," in <i>Lecture Notes in Computer Science</i>, Vol. 3034, Springer, pp. 207–215, 2004, DOI: <a href="https://doi.org/10.1007/978-3-540-24681-7_23">10.1007/978-3-540-24681-7_23</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>A. A. Reddy and B. N. Chatterji</b>, "A new wavelet based logo-watermarking scheme," <i>Pattern Recognition Letters</i>, vol. 26, pp. 1019–1027, 2005, DOI: <a href="https://doi.org/10.1016/j.patrec.2004.09.047">10.1016/j.patrec.2004.09.047</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>P. S. Huang, C. S. Chiang, C. P. Chang, and T. M. Tu</b>, "Robust spatial watermarking technique for colour images via direct saturation adjustment," <i>IEE Proceedings - Vision, Image and Signal Processing</i>, vol. 152, pp. 561-574, 2005, <a href="https://digital-library.theiet.org/doi/abs/10.1049/ip-vis%3A20041081">https://digital-library.theiet.org/doi/abs/10.1049/ip-vis%3A20041081</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>F. Gonzalez and J. Hernandez</b>, "A tutorial on Digital Watermarking," in <i>IEEE Annual Carnahan Conference on Security Technology</i>, Spain, 1999, DOI: <a href="https://doi.org/10.1109/CCST.1999.797926">10.1109/CCST.1999.797926</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>D. Kunder</b>, "Multi-resolution Digital Watermarking Algorithms and Implications for Multimedia Signals," Ph.D. thesis, University of Toronto, Canada, 2001, DOI: <a href="https://dl.acm.org/doi/book/10.5555/930897">10.5555/930897</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>J. Eggers, J. Su, and B. Girod</b>, "Robustness of a Blind Image Watermarking Scheme," in <i>Proc. IEEE Int. Conf. on Image Proc.</i>, Vancouver, 2000, DOI: <a href="https://doi.org/10.1109/ICIP.2000.899269">10.1109/ICIP.2000.899269</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>M. Barni, F. Bartolini, and A. Piva</b>, "Multichannel watermarking of color images," <i>IEEE Transaction on Circuits and Systems for Video Technology</i>, vol. 12, no. 3, pp. 142-156, 2002, DOI: <a href="https://doi.org/10.1109/76.993436">10.1109/76.993436</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>D. Kundur and D. Hatzinakos</b>, "Towards robust logo watermarking using multiresolution image fusion," <i>IEEE Transactions on Multimedia</i>, vol. 6, pp. 185-197, 2004, DOI: <a href="https://doi.org/10.1109/TMM.2003.819747">10.1109/TMM.2003.819747</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>C.S. Lu and H.Y.M. Liao</b>, "Multipurpose watermarking for image authentication and protection," <i>IEEE Transaction on Image Processing</i>, vol. 10, pp. 1579-1599, 2001, DOI: <a href="https://doi.org/10.1109/83.951542">10.1109/83.951542</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>L. Ghouti, A. Bouridane, M.K. Ibrahim, and S. Boussakta</b>, "Digital image watermarking using balanced multiwavelets," <i>IEEE Trans. Signal Process.</i>, vol. 54, no. 4, pp. 1519-1536, 2006, DOI: <a href="https://doi.org/10.1109/TSP.2006.870624">10.1109/TSP.2006.870624</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>P. Tay and J. Havlicek</b>, "Image Watermarking Using Wavelets," in <i>Proceedings of the 2002 IEEE</i>, pp. II.258 – II.261, 2002, DOI: <a href="https://doi.org/10.1109/MWSCAS.2002.1187021">10.1109/MWSCAS.2002.1187021</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>P. Kumswat, K. Attakitmongcol, and A. Srikaew</b>, "A New Approach for Optimization in Image Watermarking by Using Genetic Algorithms," <i>IEEE Transactions on Signal Processing</i>, vol. 53, no. 12, pp. 4707-4719, 2005, DOI: <a href="https://doi.org/10.1109/TSP.2005.859323">10.1109/TSP.2005.859323</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[13]</span>
    <span class="reference-text"><a id="ref-13"></a><b>H. Daren, L. Jifuen, H. Jiwu, and L. Hongmei</b>, "A DWT-Based Image Watermarking Algorithm," in <i>Proceedings of the IEEE International Conference on Multimedia and Expo</i>, pp. 429-432, 2001, DOI: <a href="https://doi.org/10.1109/ICME.2001.1237719">10.1109/ICME.2001.1237719</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[14]</span>
    <span class="reference-text"><a id="ref-14"></a><b>C. Hsu and J. Wu</b>, "Multi-resolution Watermarking for Digital Images," <i>IEEE Transactions on Circuits and Systems- II</i>, vol. 45, no. 8, pp. 1097-1101, 1998, DOI: <a href="https://doi.org/10.1109/82.718818">10.1109/82.718818</a> [Accessed: Jul. 09, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[15]</span>
    <span class="reference-text"><a id="ref-15"></a><b>R. Mehul</b>, "Discrete Wavelet Transform Based Multiple Watermarking Scheme," in <i>Proceedings, IEEE TENCON</i>, pp. 935-938, 2003, DOI: <a href="https://doi.org/10.1109/TENCON.2003.1273384">10.1109/TENCON.2003.1273384</a> [Accessed: Jul. 09, 2021].</span>
</div>

</div>
