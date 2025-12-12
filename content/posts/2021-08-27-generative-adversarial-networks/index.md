---
title: "Generative Adversarial Networks"
date: 2021-08-27T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["AI", "AI Art", "AI Research", "Artificial Intelligence", "BigGAN", "CNN", "Computer Vision", "Conditional GAN", "Convolutional Neural Networks", "CycleGAN", "Data Augmentation", "DCGAN", "Deep Convolutional GAN", "Deep Learning", "Discriminator", "GAN Architectures", "GAN Applications", "GAN Training", "GANs", "Generator", "Generative Adversarial Networks", "Generative AI", "Generative Models", "Image Generation", "Image Synthesis", "Image-to-Image Translation", "InfoGAN", "Loss Functions", "Machine Learning", "Minimax Loss", "Nash Equilibrium", "Neural Networks", "Pix2Pix", "ProGAN", "PyTorch", "SRGAN", "StackGAN", "StyleGAN", "TensorFlow", "Unsupervised Learning", "Wasserstein GAN"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Mega Satish for her meaningful contributions, support, and wisdom that helped shape this work. Deep learning's breakthrough in the field of artificial intelligence has resulted in the creation of a slew of deep learning models. One of these is the Generative Adversarial Network, which has only recently emerged. The goal of GAN is to use unsupervised learning to analyse the distribution of data and create more accurate results."
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

Deep learning's breakthrough in the field of artificial intelligence has resulted in the creation of a slew of deep learning models. One of these is the Generative Adversarial Network, which has only recently emerged. The goal of GAN is to use unsupervised learning to analyse the distribution of data and create more accurate results. The GAN allows the learning of deep representations in the absence of substantial labelled training information. Computer vision, language and video processing, and image synthesis are just a few of the applications that might benefit from these representations. The purpose of this research is to get the reader conversant with the GAN framework as well as to provide the background information on Generative Adversarial Networks, including the structure of both the generator and discriminator, as well as the various GAN variants along with their respective architectures. Applications of GANs are also discussed with examples.

---

## Introduction

In the last decade, the rise of machine learning and later deep learning has taken an essential role in the field of computer science. With this breakthrough, our ability to solve complex problems continues to increase significantly. Deep learning has the potential of discovering comprehensive multilayer models [[1]](#ref-1) capable of describing probabilities for data used in artificial intelligence applications. Generative Adversarial Networks [[2]](#ref-2)[[3]](#ref-3) are a type of generative modelling that employs deep learning techniques such as convolutional neural networks. GANs are a revolutionary innovation for both kinds of learning, supervised and unsupervised. GANs [[4]](#ref-4) are a creative approach to train a generative model by defining it as a supervised learning technique with two sub-models: the generator model, which we train to create new instances, and the discriminator model, which attempts to categorise examples as real or fake i.e. generated. The two models are trained until the discriminator model is tricked approximately half of the time, indicating that the generator model is producing convincing instances.

In machine learning, generative modelling is an unsupervised learning problem that entails automatically identifying and trying to learn patterns or similarities in the dataset so that the model may be used to create or produce new instances that might have been drawn from the original dataset. In Generative Adversarial Networks, the generator creates a new sample from input data and the discriminator tries to distinguish whether the generated sample is real or fake. Both networks are in competition with one another and are being trained at the same time. The generator doesn't know how to generate the sample; it learns by interacting with the discriminator. The discriminator basically tries to distinguish between the sample generated by the generator model and the actual data as it has access to both real data and synthesized data. If the output of the generator is considered fake, an error signal is sent to the generator to improve the quality of the results. The discriminator is then modified in the following round to improve its ability to distinguish between real and false data, and the generator is changed depending on how successfully or poorly the produced samples deceived the discriminator.

With this paper, we are proposing an explanation of Generative Adversarial Networks background as well as generative modelling and discriminative modelling. We intend to describe the architecture of the Generative Adversarial Network including its working and the data used for this system. We aim to provide an elucidation of the variations of GANs along with their applications in the real world.

### Supervised and Unsupervised Learning

Predictive modelling, for example, is a common machine learning issue that includes utilising a model to generate a forecast. This necessitates a training dataset, which consists of numerous instances, referred to as samples, each having input variables (X) and output class labels (y). A model is trained by displaying patterns of inputs, having it predict outputs, and then correcting the model so that the outputs are more similar to the predicted outputs [[5]](#ref-5). A supervised type of learning, or supervised learning [[6]](#ref-6), refers to the process of correcting the model. Classification and regression are examples of supervised learning tasks, whereas logistic regression and random forest are examples of supervised learning algorithms.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(1)%20Example%20of%20Supervised%20Learning.jpg" caption="Example of Supervised Learning" align="center" >}}

Another learning approach is one in which the model is provided with only the input variables (X) and the challenge has no output variables (y). The patterns in the dataset are extracted or summarised to create a model. Because the model isn't forecasting anything, there isn't any need for it to be corrected.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(2)%20Example%20of%20Unsupervised%20Learning.jpg" caption="Example of Unsupervised Learning" align="center" >}}

The unsupervised learning technique [[7]](#ref-7) is the second primary form of machine learning. The aim is to discover "meaningful findings" in the data, and we are only provided inputs. Because we are not informed what sorts of patterns to look for and there is no clear error measure to utilize, this is a far less well-defined problem unlike supervised learning, where we can compare our predicted y for a given x to the observed value, unsupervised learning does not allow us to compare our predictions to the observed value. Unsupervised learning is the term used to describe this lack of correction. Clustering and generative modelling are examples of unsupervised learning problems, whereas K-means and Generative Adversarial Networks are examples of unsupervised learning algorithms.

### Discriminative and Generative Modelling

We could be interested in creating a model that predicts a class label given a sample of input variables in supervised learning. This process of predictive modelling is known as classification.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(3)%20Example%20of%20Discriminative%20Modelling.jpg" caption="Example of Discriminative Modelling" align="center" >}}

Discriminative modelling and classification are two terms that have been used interchangeably in the past. We combine the inference and evaluation stages into a single learning problem by using the training data to develop a discriminant function f(x) that maps each x directly onto a class label. This is because a model must distinguish between instances of input variables belonging to different classes; it must pick or decide which class a given example belongs to. A discriminative model overlooks the question of whether or not a particular event is likely, instead of focusing on the likelihood of a label being applied to it.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(4)%20Example%20of%20Generative%20Modelling.jpg" caption="Example of Generative Modelling" align="center" >}}

Unsupervised models that summarise the distribution of input variables, on the other hand, could be able to produce or generate new examples in the distribution. As a result, generative models are used to describe various sorts of models. A single variable, for example, could have a well-known data distribution, such as a Gaussian distribution or a bell curve. A generative model may be able to adequately describe this data distribution and then be used to create new variables that fit within the input variable's distribution.

Generative models are approaches that explicitly or implicitly describe the distribution of inputs and outputs, allowing synthetic data points to be generated in the input space by sampling from them. A competent generative model may be able to produce new instances that are not just reasonable, but also indistinguishable from real-world examples.

A generative model takes into account the data's distribution and informs how likely a specific occurrence is. Because they can assign a probability to a succession of words, models that predict the next word in a sequence are often generative.

### Generative models Examples

Naive Bayes [[8]](#ref-8) is a generative model that is frequently used as a discriminative model. Naive Bayes sums together the probability distributions of each input variable and the output class. When making a prediction, the chance of each potential outcome for each variable is computed, the independent probabilities are added, and the most likely outcome is predicted. Using the probability distributions for each variable in reverse, new reasonable (independent) feature values may be generated. Latent Dirichlet Allocation [[9]](#ref-9) (LDA) and the Gaussian Mixture Model [[10]](#ref-10) (GMM) are two more examples of generative models.

As generative models, deep learning approaches can be employed. The Restricted Boltzmann Machine [[11]](#ref-11) (RBM) and the Deep Belief Network [[12]](#ref-12) (DBN) are two prominent examples. The Variational Autoencoder [[13]](#ref-13) (VAE) and the Generative Adversarial Network (GAN) are two examples of deep learning generative modelling techniques that are currently in use.

---

## Overview of GAN Structure

There are two elements to a generative adversarial network (GAN):

1. The generator improves its ability to create credible data over time. The discriminator uses the produced instances as negative training examples.
2. The discriminator learns to tell the difference between false and real data generated by the generator. The generator is penalised by the discriminator if it produces improbable results.

When training begins, the generator generates false data, which the discriminator soon recognises:

The generator comes closer to creating output that can deceive the discriminator as training progresses:

Finally, assuming generator training goes well, the discriminator becomes less capable of distinguishing between genuine and fake objects. It begins to mistakenly identify false data as real, and its accuracy suffers as a result.

The following is a diagram of the entire system:

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(5)%20Structure%20of%20GANs.jpg" caption="Structure of GANs" align="center" >}}

---

## The Generator

By integrating input from the discriminator, the generator portion of a GAN learns to produce false data. It learns how to convince the discriminator that its output is real.

Generator training necessitates a greater degree of integration between the generator and the discriminator than discriminator training. The component of the GAN that trains the generator consists of the following:

1. random input
2. The random input is transformed into a data instance via the generator network.
3. The produced data is classified using a discriminator network.
4. discriminator output
5. Generator loss is a penalty imposed on the generator when it fails to mislead the discriminator.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(6)%20Backpropagation%20in%20generator%20training.jpg" caption="Backpropagation in generator training" align="center" >}}

### Random Input

In order to function, neural networks require some type of input. We usually enter data that we wish to do something with, such as a case that we want to categorise or forecast. What, on the other hand, do we feed into a network that generates whole new data instances?

A GAN uses random noise as its input in its most basic form. The generator then converts the noise into something useful. We can get the GAN to create a broad range of data by adding noise and sampling from different points in the target distribution.

Experiments show that the noise distribution is unimportant, therefore we may select a distribution that is simple to sample from, such as a uniform distribution. The space from which the noise is sampled is generally less in size than the dimensionality of the output space for practical reasons.

### Training the Generator with the Discriminator

We change the weights of a neural net to decrease the inaccuracy or loss of its output when training it. The generator in our GAN, on the other hand, is not directly related to the loss we are attempting to reduce. The generator feeds into the discriminator net, which generates the output we are seeking to influence. The generator is penalised by the generator loss if the discriminator network classifies a sample as fraudulent.

Backpropagation [[14]](#ref-14) must incorporate this additional network segment. Backpropagation corrects each weight by estimating the weight's influence on the output, or how the output would change if the weight were altered. The impact of a generator weight, on the other hand, is determined by the impact of the discriminator weights into which it feeds. As a result, backpropagation begins at the output and flows back into the generator through the discriminator.

During generator training, however, we do not want the discriminator to alter. Attempting to strike a moving target would make an already difficult task considerably more difficult for the generator.

As a result, we use the technique below to train the generator:

1. Sample random noise.
2. Using sampled random noise, generate generator output.
3. For generator output, use the discriminator to classify it as "Real" or "Fake".
4. Calculate the loss incurred as a result of discriminator classification.
5. Gradients may be obtained by backpropagation through the discriminator and generator.
6. To just modify the generator weights, use gradients.

This is one iteration of generator training.

---

## The Discriminator

In a GAN, the discriminator is essentially a classifier. It tries to tell the difference between actual data and data generated by the generator. Any network architecture suited to the sort of data it's categorising might be used.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(7)%20Backpropagation%20in%20discriminator%20training.jpg" caption="Backpropagation in discriminator training" align="center" >}}

### Discriminator Training Data

The training data for the discriminator originates from two places:

1. Real-world data examples, such as real-world portraits of people. During training, the discriminator utilises these examples as positive examples.
2. The generator generates fake data objects. During training, the discriminator utilises these events as negative examples.

The generator does not train during discriminator training. It keeps its weights constant while creating samples for the discriminator to learn from.

### Training the Discriminator

Two loss functions are connected to the discriminator. The discriminator ignores the generator loss and only utilises the discriminator loss during training. During generator training, we utilise the generator loss.

During discriminator training, the discriminator sorts the generator's actual and false data. The discriminator suffers a loss if it incorrectly classifies a genuine instance as fake or a fake instance as real. Backpropagation from the discriminator loss across the discriminator network updates the weights of the discriminator.

---

## Training of GAN

The GAN training technique comprises concurrent training of both the discriminator and generator models. The algorithm is summarised in the image below, which is borrowed from Ian Goodfellow and his colleagues 2014 publication titled "Generative Adversarial Networks."

A summary of the Generative Adversarial Network Training Algorithm.

#### Algorithm: Minibatch Stochastic Gradient Descent Training of Generative Adversarial Nets

<div style="font-family: 'Times New Roman', serif; font-size: 1.1em; background: rgba(128, 128, 128, 0.05); padding: 20px; border-radius: 8px; margin: 1.5rem 0; text-align: left;">
<p>The number of steps to apply to the discriminator, <i>k</i>, is a hyperparameter. We used <i>k</i> = 1, the least expensive option, in our experiments.</p>
<p><b>for</b> number of training iterations <b>do</b></p>
<div style="margin-left: 20px;">
    <p><b>for</b> <i>k</i> steps <b>do</b></p>
    <div style="margin-left: 20px;">
        <p>Sample minibatch of <i>m</i> noise samples {<i>z</i><sup>(1)</sup>, ..., <i>z</i><sup>(<i>m</i>)</sup>} from noise prior <i>p<sub>g</sub></i>(<i>z</i>).</p>
        <p>Sample minibatch of <i>m</i> examples {<i>x</i><sup>(1)</sup>, ..., <i>x</i><sup>(<i>m</i>)</sup>} from data generating distribution <i>p<sub>data</sub></i>(<i>x</i>).</p>
        <p>Update the discriminator by ascending its stochastic gradient:</p>
        <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
            <span style="font-size: 1.1em;">∇</span><sub style="font-size: 0.7em;">θ<sub style="font-size: 0.9em;">d</sub></sub>
            <span style="display: inline-block; margin: 0 0.3em;">
                <div style="display: inline-block; text-align: center; vertical-align: middle;">
                    <div style="font-size: 0.8em; border-bottom: 1px solid currentColor; padding-bottom: 2px;">1</div>
                    <div style="font-size: 0.8em; font-style: italic; padding-top: 2px;">m</div>
                </div>
            </span>
            <span style="font-size: 2em; vertical-align: middle; margin: 0 0.2em;">∑</span><sup style="font-size: 0.65em; margin-left: -0.3em;"><i>m</i></sup><sub style="font-size: 0.65em; margin-left: -0.5em;"><i>i</i>=1</sub>
            <span style="margin: 0 0.3em;">[</span><span style="font-style: normal;">log</span> <i>D</i>
            <span style="margin: 0 0.1em;">(</span><b><i>x</i></b><sup style="font-size: 0.7em;">(<i>i</i>)</sup><span style="margin: 0 0.1em;">)</span>
            <span style="margin: 0 0.4em;">+</span>
            <span style="font-style: normal;">log</span>
            <span style="margin: 0 0.1em;">(</span>1 − <i>D</i>
            <span style="margin: 0 0.1em;">(</span><i>G</i>
            <span style="margin: 0 0.1em;">(</span><b><i>z</i></b><sup style="font-size: 0.7em;">(<i>i</i>)</sup><span style="margin: 0 0.1em;">)</span><span style="margin: 0 0.1em;">)</span><span style="margin: 0 0.1em;">)</span><span style="margin: 0 0.3em;">]</span>
        </div>
    </div>
    <p><b>end for</b></p>
    <p>Sample minibatch of <i>m</i> noise samples {<i>z</i><sup>(1)</sup>, ..., <i>z</i><sup>(<i>m</i>)</sup>} from noise prior <i>p<sub>g</sub></i>(<i>z</i>).</p>
    <p>Update the generator by descending its stochastic gradient:</p>
    <div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
        <span style="font-size: 1.1em;">∇</span><sub style="font-size: 0.7em;">θ<sub style="font-size: 0.9em;">g</sub></sub>
        <span style="display: inline-block; margin: 0 0.3em;">
            <div style="display: inline-block; text-align: center; vertical-align: middle;">
                <div style="font-size: 0.8em; border-bottom: 1px solid currentColor; padding-bottom: 2px;">1</div>
                <div style="font-size: 0.8em; font-style: italic; padding-top: 2px;">m</div>
            </div>
        </span>
        <span style="font-size: 2em; vertical-align: middle; margin: 0 0.2em;">∑</span><sup style="font-size: 0.65em; margin-left: -0.3em;"><i>m</i></sup><sub style="font-size: 0.65em; margin-left: -0.5em;"><i>i</i>=1</sub>
        <span style="font-style: normal; margin: 0 0.2em;">log</span>
        <span style="margin: 0 0.1em;">(</span>1 − <i>D</i>
        <span style="margin: 0 0.1em;">(</span><i>G</i>
        <span style="margin: 0 0.1em;">(</span><b><i>z</i></b><sup style="font-size: 0.7em;">(<i>i</i>)</sup><span style="margin: 0 0.1em;">)</span><span style="margin: 0 0.1em;">)</span><span style="margin: 0 0.1em;">)</span>
    </div>
</div>
<p><b>end for</b></p>
</div>

The gradient-based updates can use any standard gradient-based learning rule. We used momentum in our experiments.

The algorithm's outer loop iterates over steps to train the models in the architecture. One cycle through this loop is not an epoch; rather, it is a single update consisting of particular batch modifications to the discriminator and generator models. An epoch is defined as one cycle through a training dataset in which the samples are utilised to update the model weights in mini-batches. A training dataset of 100 samples used to train a model with a mini-batch size of 10 samples, for example, would result in 10 mini-batch updates for each epoch. The model would be appropriate for a specific number of epochs, such as 500. This is frequently concealed from you by automating model training by calling the fit() method and setting the number of epochs and the size of each mini-batch.

### Convergence

Because the discriminator can't detect the difference between genuine and false, as the generator improves with training, the discriminator's performance deteriorates. The discriminator has a 50% accuracy if the generator succeeds flawlessly. To make its forecast, the discriminator essentially flips a coin. This development causes difficulty for the GAN's overall convergence: the discriminator feedback becomes less useful over time. If the GAN continues to train after the discriminator has given totally random feedback, the generator will begin to train on garbage feedback, and its own quality will deteriorate. Convergence is generally a transitory rather than a permanent condition for a GAN.

---

## GAN Loss Functions

The discriminator has been trained to distinguish between authentic and false pictures. This is accomplished by averaging over each mini-batch of samples the log of the anticipated probability of actual pictures and the log of the inverted probability of false images. Remember that adding log probabilities is the same as multiplying probabilities, but without the possibility of disappearing into small values. As a result, we may interpret this loss function as seeking probability near 1.0 for actual pictures and probabilities near 0.0 for false images, inverted to produce bigger numbers. The combination of these numbers indicates that lower average values of this loss function result in higher discriminator performance.

The loss of the generator model is defined by the GAN method as reducing the log of the inverted probability of the discriminator's prediction of false pictures over a mini-batch. This is simple, but the authors claim that it is ineffective in practice when the generator is weak and the discriminator is skilled at rejecting false pictures with high confidence. The loss function saturates rather than providing appropriate gradient information for the generator to change weights.

Instead, the authors suggest increasing the log of the discriminator's anticipated likelihood of detecting false pictures. The transformation is slight. In the first example, the generator is taught to reduce the likelihood that the discriminator would be right. With this modification to the loss function, the generator is trained to maximise the likelihood that the discriminator will be wrong. This loss function's sign may then be reversed to provide a familiar minimising loss function for training the generator. As a result, this is also known as the -log D technique for training GANs.

### Loss Functions

GANs are algorithms that attempt to duplicate a probability distribution. As a result, they should utilise loss functions that represent the distance between the GAN-generated data distribution and the distribution of the real data.

In GAN loss functions, how can you represent the difference between two distributions? This is a hotly debated topic, and a variety of techniques have been offered. Here, we'll look at two typical GAN loss functions that are both implemented in TF-GAN:

1. The loss function employed in the study that first described GANs was called minimax loss.
2. The default loss function for TF-GAN Estimators is the Wasserstein loss. A 2017 publication was the first to describe it.

TF-GAN also provides a variety of additional loss functions.

### Minimax Loss

The generator seeks to reduce the following function, whereas the discriminator strives to maximise it, according to the study that first proposed GANs:

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
    <i>E</i><sub style="font-size: 0.75em;"><i>x</i></sub> [log <i>D</i>(<i>x</i>)] + <i>E</i><sub style="font-size: 0.75em;"><i>z</i></sub> [log(1 − <i>D</i>(<i>G</i>(<i>z</i>)))]
</div>

In this function:

1. <i>D</i>(<i>x</i>) is the discriminator's assessment of the likelihood of whether a genuine data instance <i>x</i> exists.
2. <i>E</i><sub><i>x</i></sub> is the average of all real-world data occurrences.
3. <i>G</i>(<i>z</i>) is the outcome of the generator for input noise <i>z</i>.
4. <i>D</i>(<i>G</i>(<i>z</i>)) is the discriminator's estimation of the likelihood that a false example is genuine.
5. <i>E</i><sub><i>z</i></sub> is the estimated value across all provided by particular inputs (the expected value across all produced false instances <i>G</i>(<i>z</i>)).
6. The calculation is based on the difference in entropy between both the real and produced distribution.
7. The generator has no significant influence on the log(<i>D</i>(<i>x</i>)) term.

---

## GANs and Convolution Neural Networks

Convolutional Neural Networks [[15]](#ref-15), or CNNs, are used as the generator and discriminator models in GANs, which generally deal with picture data. This could be due to the fact that the technique was first described in the field of computer vision and used CNNs and image data, as well as the remarkable progress made in recent years using CNNs more broadly to achieve state-of-the-art results on a variety of computer vision tasks like object detection and face recognition. When the latent space, the generator's input, is used to model picture data, it offers a compressed representation of the collection of images or photographs used to train the model. It also implies that the generator creates fresh pictures or photographs, resulting in an output that developers or users of the model can readily examine and evaluate. It's possible that this characteristic, above all others, the capacity to visually judge the quality of the produced output, has both led to the emphasis of computer vision applications with CNNs and to the huge jumps in capabilities of GANs when compared to other generative models, deep learning-based or not.

---

## Variations of GANs

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(8)%20Types%20of%20GAN%20Model%20architectures%20and%20extensions.jpg" caption="Types of GAN Model architectures and extensions" align="center" >}}

### Deep Convolutional GAN

DCGAN [[16]](#ref-16) is an expansion of the GAN system that uses deep convolutional neural networks for both the generator and discriminator models, as well as model and training settings that result in robust training of a generator model. DCGANs employ stride and fractionally stride convolutions which are basic blocks of convolution that are used in CNN. This enables the model to learn about the operators used in up sampling and down sampling networks all through the training. Up sampling is expanding the conceptual images representations through multiple techniques to keep the spatial dimensions comparable to the input data. Down sampling is the loss of spatial resolution yet maintaining the same two-dimensional image representation.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(9)%20DCGAN.png" caption="The DCGAN generator was used to simulate the LSUN scenario. A 100-dimensional uniform distribution Z is projected to a limited spatial extent convolutional representation with numerous feature maps. This high-level representation is then converted into a 64 × 64-pixel picture via a sequence of four fractionally-strided convolutions (in some recent studies, they are incorrectly called deconvolutions). It is worth noting that no completely linked or pooling layers are employed." align="center" >}}

### Conditional GAN

Conditional GANs [[17]](#ref-17) (cGANs) are a type of network where both the generator and discriminator are conditioned by extra information during training. cGANs modify the network by introducing the label <i>y</i> as an extra argument to the generator so that the generator can produce matching pictures. Labels are also fed to the discriminator to improve the discrimination between real and fake samples. Conditional GANs use a labelled data set to train and allow to choose the label for each produced instance. An unconditional MNIST GAN, for example, will create random digits, but a conditional MNIST GAN will allow us to select which digit the GAN should generate. Conditional GANs represent the conditional probability <i>P</i>(<i>X</i> | <i>Y</i>) instead of the joint probability <i>P</i>(<i>X</i>, <i>Y</i>).

The use of the GAN for conditionally producing an output is a significant extension. The generative model may be trained to create new instances from the input domain, where the input, a random vector from the latent space, is supplemented (conditioned by) some extra information. In the case of producing photos of handwritten numbers, the extra input may be a class value, such as male or female in the case of generating photographs of humans, or even a figure in the event of photographing handwritten characters. If both the generator and the discriminator are conditioned on some additional information <i>y</i>, such as class labels or input from other modalities, generative adversarial networks can be expanded to a conditional model. We may do the conditioning by adding <i>y</i> as an additional input layer to both the discriminator and the generator.

The discriminator is additionally conditioned, which means it is given both a genuine and a false input picture as well as the additional input. The discriminator would therefore anticipate the input to be of that class in the case of a classification label type conditional input, training the generator to create instances of that class in order to mislead the discriminator. A conditional GAN may be used in this way to produce examples from a domain of a specific type.

GAN models can be conditioned on a domain exemplar, such as a picture, if taken a step further. This enables GANs to be used in applications such as text-to-image or image-to-image translation. This enables GANs to do some of their most spectacular tasks, such as style transfer, photo colourization, and photo transformations from summer to winter or day to night, among others.

When using conditional GANs for image-to-image translation, such as converting day to night, the discriminator is fed samples of actual and produced night-time pictures, as well as (conditioned on) real daytime photos. A random vector from the latent space, as well as (conditioned on) real daytime photographs, are fed into the generator.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(10)%20Conditional%20GAN%20Model%20Architecture.jpg" caption="Conditional GAN Model Architecture" align="center" >}}

### Information Maximizing GAN

Information Maximizing GAN [[18]](#ref-18) is a GAN derivative. It's an algorithm for learning unsupervised representations. This network magnifies the mutual information between the input noise vector and the latent code, which are basically variables that aren't observed during the training phase and the test phases. InfoGan solves the problem of entangled representations and gives a disentangled one. It separates the Generator input noise vector in two: the conventional noise vector and a new 'latent code' vector. Later, by maximising the mutual information between the code and the generator output, the latent code is made significant and are used to condition or control specific semantic properties in the generated image. The addition of the component which maximises the mutual information among the generative model's latent code input and its output, leads to the disentanglement of the significant features and assigns them to the enforced latent code space.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(11)%20InfoGAN.png" caption="InfoGAN" align="center" >}}

### Stacked GAN

The stacked generative adversarial network, or StackGAN [[19]](#ref-19)[[20]](#ref-20), is a GAN modification that uses a hierarchical stack of conditional GAN networks to create pictures from words. The structure is made up of conditional GAN models. There are two generators, the first one is text conditioned and produces a poor resolution image. The second one is regulated on the text and the output of the first generator; it produces a high-resolution picture. Our SGAN breaks down variations into several layers and gradually eliminates uncertainties in the top-down generating process, unlike the original GAN, which utilises a single noise vector to represent all variations.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(12)%20StackGAN.png" caption="StackGAN" align="center" >}}

### Pix2Pix

The Pix2Pix [[21]](#ref-21) GAN is a method for teaching convolutional neural networks to do an image-to-image conversion. When compared to previous GAN models (e.g., 256×256 pixels), the precise setup of architecture as a sort of image-conditional GAN provides for both the creation of big pictures and the capacity to perform well on a range of image-to-image machine translation. Pix2Pix is a form of conditional GAN, or cGAN, in which the output picture creation is dependent on input, in this instance a source image. An original picture and a target image are supplied to the discriminator, who must decide if the target is a reasonable translation of the input images.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(13)%20Pix2Pix.jpg" caption="Pix2Pix" align="center" >}}

### Wasserstein GAN

Wasserstein GAN [[22]](#ref-22) or WGAN is a GAN extension that looks for a different approach to train the generator model so that it can better mimic the distribution of data seen in a particular training dataset. For each iteration, it modifies the training method to update the discriminator model, several times more than the generating model. The discriminator is revised to produce a real-value (linear activation) rather than binary forecasting with a sigmoid function. Both the generator and the discriminator are trained with "Wasserstein loss". It is the average of the product of real and estimated values from the discriminator to give linear gradients useful for updating the model.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(14)%20Wasserstein%20GAN.jpg" caption="Wasserstein GAN" align="center" >}}

### Progressive Growing GAN

Progressive Growing GAN [[23]](#ref-23) is a GAN training method enhancement that enables for the steady training of generator networks capable of producing huge, high-quality pictures. The process consists of increasing the size of the model gradually for a very small picture. This will result in a rise in the output size of the generator and the input size of the discriminator. It will continue till the required picture size is obtained. The earliest layers of a progressive GAN create relatively low-quality pictures, but later layers add details. This method allows the GAN to train faster than non-progressive GANs while also producing higher-resolution pictures.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(15)%20ProGAN.jpg" caption="ProGAN" align="center" >}}

### BigGAN

Big Generative Adversarial Networks [[24]](#ref-24) is a method for demonstrating how existing class conditional models may be scaled up to produce high-quality output pictures. BigGAN is a GAN extension; the idea is to increase the size of the batches while also increasing the amount of parameters. As a result, high-quality, high-resolution images are generated. Modifying the architecture and training procedures, for example, will allow GANs to be scaled up.

### StyleGAN

The StyleGAN [[25]](#ref-25)[[26]](#ref-26), or style-based generative adversarial network, is a generator modification that enables the latent code to be utilised as input at various stages during the model to influence aspects of the produced picture. Rather than using the latent space point as input, the point is passed via a deep embedding system before it can be used as input at numerous places in the generator model. Along with the embedding network's output, noise is also included.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(16)%20StyleGAN.jpg" caption="StyleGAN" align="center" >}}

### CycleGAN

CycleGANs [[27]](#ref-27) are generative adversarial networks with two generators and two discriminators. Every generator has its discriminator that aims to differentiate its generated pictures from genuine ones.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(17)%20CycleGAN.jpg" caption="CycleGAN" align="center" >}}

CycleGANs learn to convert pictures from one set into images that may be from a different collection. When given the left-hand picture as input, a CycleGAN created the right-hand image below. It took a horse image and transformed it into a zebra image. The CycleGAN's training data consists of just two picture sets (in this case, a set of horse images and a set of zebra images). No labels or pairwise picture correspondences are required by the system.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(18)%20(A)%20Input%20Image%20(B)%20Output%20Image.png" caption="(A) Input Image (B) Output Image" align="center" >}}

### Super-Resolution GAN

Super-Resolution GAN [[28]](#ref-28), like other GAN designs, is separated into two sections: the generator and the discriminator. The generator generates data based on a probability distribution, and the discriminator attempts to predict if the data came from the input samples or generated samples.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(19)%20SRGAN.jpg" caption="SRGAN" align="center" >}}

To generate better quality pictures, SRGAN employs a network model in association with an adversarial network. GANs with super-resolution boost picture resolution by adding detail where it's needed to fill up hazy regions. The fuzzy middle picture on the right, for example, is a down-sampled reproduction of the original image on the left. A GAN created the clearer picture on the right from the fuzzy image:

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(20)%20(A)%20Input%20Image%20(B)%20Blurred%20(C)%20Restored%20with%20GAN.png" caption="(A) Input Image (B) Blurred (C) Restored with GAN" align="center" >}}

Although the GAN-generated picture appears to be extremely similar to the original, a careful examination of the headband reveals that the GAN did not replicate the original's starburst pattern. Instead, it created its own convincing pattern to replace the down-sampled pattern.

---

## Applications of GANs

Exploring recent advances for adversarial deep network training is an ongoing focus of study. Some examples of applications were selected to demonstrate some diverse methods to employ GAN-based representations for picture modification, analysis, or characterisation, and thus do not completely represent the possible range of use of GANs.

Image synthesis [[29]](#ref-29) is one of the core application GAN functions and it is used when there are some existing conditions for the produced images. Image to Image translation [[30]](#ref-30) shows the potential of GANs by translating input data into an output image. Super-resolution using GAN demonstrates the use of an existing technique that can be enhanced with supplement loss functions to generate high-quality outcomes.

### Image Synthesis

Recently, the research regarding image synthesis with GAN [[31]](#ref-31) mostly focuses on the quality of the generated images. We can distinguish three approaches for image synthesis: direct, hierarchical, and iterative.

Direct methods are methods in which the models contain a generator <i>G</i> and discriminator <i>D</i> and have a simple architecture with fewer connections. Of these, DCGAN is one of the most traditional, with a framework that is adopted by several subsequent models. In DCGAN, <i>G</i> adopts transposed convolution, batch-normalization and ReLU activation whereas <i>D</i> employs convolution, batch-normalization and Leaky ReLU activation. As its name indicates, this method is very direct for designing and implementing. DCGAN was implemented for the generation of apparel pictures for inclusion in the Fashion MNIST dataset. In this case, the noise was given as input to the generator, then moulded to produce a low image resolution. To obtain the final picture, this was up-sampled using Conv2DTranspose. The discriminator had an architecture based on CNN supervised learning for classifying the generated image.

Compared to the direct method, the hierarchical approach uses two pairs of generators and discriminators. Both the generators and discriminators have different purposes. The two generators' relationship might be either parallel or sequential. In the case of Structure-Style GAN, it contains two GANs, one GAN to create a surface map from latent space and the other one to take both the created surface normal map and a noise vector as input and produce an image.

The Iterative method is different from the Hierarchical method. This method uses several generators with similar structures and the generators produce images from rough to detailed, with the generators improving the previous output each and every time. Furthermore, for the architecture of the generators, shared weights can be employed between the generators. This however is not possible in the case of hierarchical models. For example, Text-to-Image synthesis, the text is used as input and the model generates pictures that are believable and accurately represented by the text. For text-to-image synthesis, StackGAN suggests using two distinct generators. The first generator produces low-quality images with rough forms and colors of objects. The second one takes as input the outcome of the previous generator and generates high-quality images. The floral image below, for example, was created by feeding a written description to a GAN.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(21)%20Caption%20-%20The%20floral%20image%20above%20was%20created%20by%20feeding%20a%20written%20description%20to%20a%20GAN..png" caption="The floral image above was created by feeding a written description to a GAN." align="center" >}}

### Image-to-Image Translation

The challenge of converting a potential representation of one image into the other, such as transforming black and white pictures into RGB images, or the other way around, is characterised as image-to-image translation. Image-to-image is not limited only to translating the images but also changing and modifying the characteristics of the images. GANs take an input image and map it to a produced output image with various characteristics. Based on the data, we can say that there are two types of translation, supervised and unsupervised.

In Supervised translation, there are paired images in several domains. It means that for each image of the source domain, there exists a corresponding image in the target domain. Pix2Pix merges the loss of a cGAN with the loss of L1 regularization for the generator to fool the discriminator but also produce actual, real images. Though Pix2Pix generates highly amazing synthetic pictures, its main restriction is that it must take coupled photos as supervision, because the data pair (<i>x</i>, <i>y</i>) is taken from the joint distribution <i>p</i>(<i>x</i>, <i>y</i>). Another image-to-image translation case is the White Box Cartoonization using extended GAN framework [[32]](#ref-32)[[33]](#ref-33). This network outputs a cartooned image from a given photo. The image is separated in three representations: surface, structure and texture representations. The first one smoothens the surface of the image, the second one segments the image and create a segmentation map. The third one focuses on the colors and the texture as it name indicates. The output is a high resolution and high-quality cartooned image which is very similar to the original photo, yet holds the characteristics of a cartooned picture.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(22)%20(A)%20Input%20Images%20(B)%20Real%20Images%20(C)%20Output%20Images.png" caption="(A) Input Images (B) Real Images (C) Output Images" align="center" >}}

In an Unsupervised setup [[34]](#ref-34)[[35]](#ref-35), there are two independent datasets: one has images from one domain while the other has images from another. Consequently, there is no paired data. This poses a challenge as there is no way of showing how the image could be translated into its respective image of another domain. The goal of unsupervised image-to-image translation is to learn a joint distribution of pictures in distinct domains by taking pictures from the probability distribution in each domain. Adversarial Open Domain Adaptation for sketch-to-photo synthesis [[36]](#ref-36) is a framework that has dealt with unsupervised translation. It uses two generators, <i>G</i><sub>1</sub> translates photo to sketch and <i>G</i><sub>2</sub> translates sketch to photo depending on the input tag, and two discriminators <i>D</i><sub>1</sub> and <i>D</i><sub>2</sub> for drawing and photo domains.

{{< figure src="Generative%20Adversarial%20Networks/Figures/Figure%20(23)%20Sketch-to-Photo%20Synthesis.png" caption="Sketch-to-Photo Synthesis" align="center" >}}

---

## Conclusions

GANs are a type of game-theoretic generative model. They've had a lot of success in the field of creating realistic data, particularly pictures. Training them is still a challenge. It will be required to create models, prices, or training algorithms that can consistently and rapidly identify appropriate Nash equilibria for GANs in order for them to become a more dependable technology. GANs have inspired a surge of interest due to their capacity to learn deep, highly non-linear mappings from a latent space to data space and back, as well as their ability to handle huge amounts of unlabelled picture data that are inaccessible to deep representation learning. There are several chances for theoretical and algorithmic advancements within the intricacies of GAN training, and with the strength of deep networks, there are numerous opportunities for new applications. By creating their own representations of the data they are trained on, GANs produce organised geometric vector spaces for a variety of domains. GANs may train representations that can be used for a variety of tasks, including image synthesis, semantic image editing, style transfer, image super-resolution, and classification, to name a few applications.

---

## Additional Resources

### Research Paper

Explore the published research paper and preprint:

<div style="display: flex; flex-direction: column; gap: 8px;">

  <div>
    <!-- viXra Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 8px;"><title>viXra</title><path d="M0 0h3v3h3v3h3v3h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3zM21 0h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3zM6 15h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3z" /></svg>
    <a href="https://vixra.org/pdf/2108.0169v1.pdf" target="_blank">viXra Preprint</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://doi.org/10.22214/ijraset.2021.37723" target="_blank">Full Paper (IJRASET)</a>
  </div>

  <div>
    <!-- Kaggle Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;">
        <path transform="matrix(.527027 0 0 .527027 -30.632288 -22.45559)"
            d="M105.75 102.968c-.06.238-.298.357-.713.357H97.1c-.477 0-.89-.208-1.248-.625L82.746 86.028l-3.655 3.477v12.93c0 .595-.298.892-.892.892h-6.152c-.595 0-.892-.297-.892-.892V43.5c0-.593.297-.89.892-.89H78.2c.594 0 .892.298.892.89v36.288l15.692-15.87c.416-.415.832-.624 1.248-.624h8.204c.356 0 .593.15.713.445.12.357.09.624-.09.803L88.274 80.588l17.297 21.488c.237.238.297.535.18.892" />
    </svg>
    <a href="https://www.kaggle.com/code/ameythakur20/generative-adversarial-network" target="_blank">Kaggle Notebook</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Generative Adversarial Networks". AmeyArc (Aug 2021). https://amey-thakur.github.io/posts/2021-08-27-generative-adversarial-networks/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2021gan,
  title   = "Generative Adversarial Networks",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Aug",
  url     = "https://amey-thakur.github.io/posts/2021-08-27-generative-adversarial-networks/"
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur and A. Konde</b>, "Fundamentals of Neural Networks," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET)</i>, vol. 9, no. 8, pp. 407-426, 2021, DOI: <a href="https://doi.org/10.22214/ijraset.2021.37362">10.22214/ijraset.2021.37362</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>I. Goodfellow et al.</b>, "Generative adversarial nets," in <i>Advances in neural information processing systems</i>, vol. 27, 2014, <a href="https://papers.nips.cc/paper/5423-generative-adversarial-nets">https://papers.nips.cc/paper/5423-generative-adversarial-nets</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>I. Goodfellow</b>, "Nips 2016 tutorial: Generative adversarial networks," <i>arXiv preprint arXiv:1701.00160</i>, 2016, <a href="https://arxiv.org/abs/1701.00160">https://arxiv.org/abs/1701.00160</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>A. Creswell, T. White, V. Dumoulin, et al.</b>, "Generative adversarial networks: An overview," <i>IEEE Signal Processing Magazine</i>, vol. 35, no. 1, pp. 53-65, 2018, DOI: <a href="https://doi.org/10.1109/MSP.2017.2765202">10.1109/MSP.2017.2765202</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>M.-Y. Liu and O. Tuzel</b>, "Coupled generative adversarial networks," in <i>Advances in neural information processing systems</i>, vol. 29, pp. 469-477, 2016, <a href="https://papers.nips.cc/paper/6544-coupled-generative-adversarial-networks">https://papers.nips.cc/paper/6544-coupled-generative-adversarial-networks</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>T. Jiang, J. L. Gradus, and A. J. Rosellini</b>, "Supervised machine learning: a brief primer," <i>Behavior Therapy</i>, vol. 51, no. 5, pp. 675-687, 2020, DOI: <a href="https://doi.org/10.1016/j.beth.2020.05.002">10.1016/j.beth.2020.05.002</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>R. Gentleman and V. J. Carey</b>, "Unsupervised machine learning," in <i>Bioconductor case studies</i>, New York, NY: Springer, 2008, pp. 137-157, DOI: <a href="https://doi.org/10.1007/978-0-387-77240-0_10">10.1007/978-0-387-77240-0_10</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>K. M. Leung</b>, "Naive bayesian classifier," <i>Polytechnic University Department of Computer Science/Finance and Risk Engineering</i>, 2007, DOI: <a href="https://doi.org/10.1016/j.engappai.2024.108972">10.1016/j.engappai.2024.108972</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>N. Rasiwasia and N. Vasconcelos</b>, "Latent dirichlet allocation models for image classification," <i>IEEE transactions on pattern analysis and machine intelligence</i>, vol. 35, no. 11, pp. 2665-2679, 2013, DOI: <a href="https://doi.org/10.1109/TPAMI.2013.69">10.1109/TPAMI.2013.69</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>D. A. Reynolds</b>, "Gaussian mixture models," in <i>Encyclopedia of biometrics</i>, 2009, pp. 659-663, DOI: <a href="https://doi.org/10.1007/978-0-387-73003-5_196">10.1007/978-0-387-73003-5_196</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>H. Larochelle et al.</b>, "Learning algorithms for the classification restricted boltzmann machine," <i>The Journal of Machine Learning Research</i>, vol. 13, no. 1, pp. 643-669, 2012, <a href="https://jmlr.org/papers/v13/larochelle12a.html">https://jmlr.org/papers/v13/larochelle12a.html</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>A. Krizhevsky and G. Hinton</b>, "Convolutional deep belief networks on cifar-10," <i>Unpublished manuscript</i>, vol. 40, no. 7, pp. 1-9, 2010, <a href="https://www.cs.toronto.edu/~kriz/conv-cifar10-aug2010.pdf">https://www.cs.toronto.edu/~kriz/conv-cifar10-aug2010.pdf</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[13]</span>
    <span class="reference-text"><a id="ref-13"></a><b>L. Mescheder, S. Nowozin, and A. Geiger</b>, "Adversarial variational bayes: Unifying variational autoencoders and generative adversarial networks," in <i>International Conference on Machine Learning</i>, PMLR, 2017, <a href="https://arxiv.org/abs/1701.04722">https://arxiv.org/abs/1701.04722</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[14]</span>
    <span class="reference-text"><a id="ref-14"></a><b>O. Adigun and B. Kosko</b>, "Training generative adversarial networks with bidirectional backpropagation," in <i>2018 17th IEEE international conference on machine learning and applications (ICMLA)</i>, IEEE, 2018, DOI: <a href="https://doi.org/10.1109/ICMLA.2018.00190">10.1109/ICMLA.2018.00190</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[15]</span>
    <span class="reference-text"><a id="ref-15"></a><b>S. Albawi, T. A. Mohammed, and S. Al-Zawi</b>, "Understanding of a convolutional neural network," in <i>2017 International Conference on Engineering and Technology (ICET)</i>, IEEE, 2017, DOI: <a href="https://doi.org/10.1109/ICEngTechnol.2017.8308186">10.1109/ICEngTechnol.2017.8308186</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[16]</span>
    <span class="reference-text"><a id="ref-16"></a><b>A. Radford, L. Metz, and S. Chintala</b>, "Unsupervised representation learning with deep convolutional generative adversarial networks," <i>arXiv preprint arXiv:1511.06434</i>, 2015, <a href="https://arxiv.org/abs/1511.06434">https://arxiv.org/abs/1511.06434</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[17]</span>
    <span class="reference-text"><a id="ref-17"></a><b>M. Mirza and S. Osindero</b>, "Conditional generative adversarial nets," <i>arXiv preprint arXiv:1411.1784</i>, 2014, <a href="https://arxiv.org/abs/1411.1784">https://arxiv.org/abs/1411.1784</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[18]</span>
    <span class="reference-text"><a id="ref-18"></a><b>X. Chen et al.</b>, "Infogan: Interpretable representation learning by information maximizing generative adversarial nets," in <i>Proceedings of the 30th International Conference on Neural Information Processing Systems</i>, 2016, <a href="https://arxiv.org/abs/1606.03657">https://arxiv.org/abs/1606.03657</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[19]</span>
    <span class="reference-text"><a id="ref-19"></a><b>X. Huang et al.</b>, "Stacked Generative Adversarial Networks," in <i>CVPR</i>, vol. 2, 2017, <a href="https://arxiv.org/abs/1612.04357">https://arxiv.org/abs/1612.04357</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[20]</span>
    <span class="reference-text"><a id="ref-20"></a><b>H. Zhang et al.</b>, "Stackgan: Text to photo-realistic image synthesis with stacked generative adversarial networks," in <i>Proceedings of the IEEE international conference on computer vision</i>, 2017, <a href="https://arxiv.org/abs/1612.03242">https://arxiv.org/abs/1612.03242</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[21]</span>
    <span class="reference-text"><a id="ref-21"></a><b>P. Isola et al.</b>, "Image-to-image translation with conditional adversarial networks," in <i>Proceedings of the IEEE conference on computer vision and pattern recognition</i>, 2017, <a href="https://arxiv.org/abs/1611.07004">https://arxiv.org/abs/1611.07004</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[22]</span>
    <span class="reference-text"><a id="ref-22"></a><b>M. Arjovsky, S. Chintala, and L. Bottou</b>, "Wasserstein generative adversarial networks," in <i>International conference on machine learning</i>, PMLR, 2017, pp. 214-223, <a href="https://arxiv.org/abs/1701.07875">https://arxiv.org/abs/1701.07875</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[23]</span>
    <span class="reference-text"><a id="ref-23"></a><b>T. Karras et al.</b>, "Progressive growing of gans for improved quality, stability, and variation," <i>arXiv preprint arXiv:1710.10196</i>, 2017, <a href="https://arxiv.org/abs/1710.10196">https://arxiv.org/abs/1710.10196</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[24]</span>
    <span class="reference-text"><a id="ref-24"></a><b>A. Brock, J. Donahue, and K. Simonyan</b>, "Large scale GAN training for high fidelity natural image synthesis," <i>arXiv preprint arXiv:1809.11096</i>, 2018, <a href="https://arxiv.org/abs/1809.11096">https://arxiv.org/abs/1809.11096</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[25]</span>
    <span class="reference-text"><a id="ref-25"></a><b>X. Wang and A. Gupta</b>, "Generative image modelling using style and structure adversarial networks," <i>arXiv preprint arXiv:1603.05631</i>, 2016, <a href="https://arxiv.org/abs/1603.05631">https://arxiv.org/abs/1603.05631</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[26]</span>
    <span class="reference-text"><a id="ref-26"></a><b>T. Karras, S. Laine, and T. Aila</b>, "A style-based generator architecture for generative adversarial networks," in <i>Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition</i>, 2019, pp. 4401-4410, <a href="https://arxiv.org/abs/1812.04948">https://arxiv.org/abs/1812.04948</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[27]</span>
    <span class="reference-text"><a id="ref-27"></a><b>J.-Y. Zhu et al.</b>, "Unpaired image-to-image translation using cycle-consistent adversarial networks," in <i>Proceedings of the IEEE international conference on computer vision</i>, 2017, <a href="https://arxiv.org/abs/1703.10593">https://arxiv.org/abs/1703.10593</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[28]</span>
    <span class="reference-text"><a id="ref-28"></a><b>C. Ledig et al.</b>, "Photo-realistic single image super-resolution using a generative adversarial network," in <i>Proceedings of the IEEE conference on computer vision and pattern recognition</i>, 2017, <a href="https://arxiv.org/abs/1609.04802">https://arxiv.org/abs/1609.04802</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[29]</span>
    <span class="reference-text"><a id="ref-29"></a><b>H. Huang, P. S. Yu, and C. Wang</b>, "An introduction to image synthesis with generative adversarial nets," <i>arXiv preprint arXiv:1803.04469</i>, 2018, <a href="https://arxiv.org/abs/1803.04469">https://arxiv.org/abs/1803.04469</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[30]</span>
    <span class="reference-text"><a id="ref-30"></a><b>P. Isola, J. Y. Zhu, T. Zhou, and A. A. Efros</b>, "Image-to-image translation with conditional adversarial networks," in <i>Proceedings of the IEEE conference on computer vision and pattern recognition</i>, 2017, pp. 1125-1134, <a href="https://arxiv.org/abs/1611.07004">https://arxiv.org/abs/1611.07004</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[31]</span>
    <span class="reference-text"><a id="ref-31"></a><b>P. Shamsolmoali et al.</b>, "Image synthesis with adversarial networks: A comprehensive survey and case studies," <i>Information Fusion</i>, 2021, DOI: <a href="https://doi.org/10.48550/arXiv.2012.13736">10.48550/arXiv.2012.13736</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[32]</span>
    <span class="reference-text"><a id="ref-32"></a><b>A. Thakur, H. Rizvi, and M. Satish</b>, "White-Box Cartoonization Using An Extended GAN Framework," <i>arXiv preprint arXiv:2107.04551</i>, 2021, <a href="https://arxiv.org/abs/2107.04551">https://arxiv.org/abs/2107.04551</a>, DOI: <a href="https://doi.org/10.48550/arXiv.2107.04551">10.48550/arXiv.2107.04551</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[33]</span>
    <span class="reference-text"><a id="ref-33"></a><b>A. Thakur, H. Rizvi, and M. Satish</b>, "WHITE-BOX CARTOONIZATION USING AN EXTENDED GAN FRAMEWORK," <i>International Journal of Engineering Applied Sciences and Technology (IJEAST)</i>, vol. 5, no. 12, pp. 294-298, 2021, DOI: <a href="https://doi.org/10.33564/IJEAST.2021.v05i12.049">10.33564/IJEAST.2021.v05i12.049</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[34]</span>
    <span class="reference-text"><a id="ref-34"></a><b>A. Radford, L. Metz, and S. Chintala</b>, "Unsupervised representation learning with deep convolutional generative adversarial networks," <i>arXiv preprint arXiv:1511.06434</i>, 2015, <a href="https://arxiv.org/abs/1511.06434">https://arxiv.org/abs/1511.06434</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[35]</span>
    <span class="reference-text"><a id="ref-35"></a><b>M.-Y. Liu, T. Breuel, and J. Kautz</b>, "Unsupervised image-to-image translation networks," in <i>Advances in neural information processing systems</i>, 2017, <a href="https://arxiv.org/abs/1703.00848">https://arxiv.org/abs/1703.00848</a> [Accessed: Aug. 27, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[36]</span>
    <span class="reference-text"><a id="ref-36"></a><b>X. Xiang et al.</b>, "Adversarial Open Domain Adaption for Sketch-to-Photo Synthesis," <i>arXiv preprint arXiv:2104.05703</i>, 2021, <a href="https://arxiv.org/abs/2104.05703">https://arxiv.org/abs/2104.05703</a> [Accessed: Aug. 27, 2021].</span>
</div>

</div>
