---
title: "Text Summarizer Using Julia"
date: 2022-01-24T00:00:00-05:00
draft: false
author: "Amey Thakur"
summary: "Special thanks to Mega Satish for her meaningful contributions, support, and wisdom that helped shape this work. The purpose of this paper is to introduce the Julia programming language with a concentration on Text Summarization. An extractive summarization algorithm is used for summarizing. Julia's evolution and features, as well as comparisons to other programming languages, are briefly discussed."
tags: ["AI", "Algorithms", "Artificial Intelligence", "Automatic Text Summarization", "Computational Linguistics", "Data Science", "Extractive Summarization", "Information Retrieval", "Julia", "Julia Programming", "Machine Learning", "NLP", "Natural Language Processing", "Sentence Scoring", "Text Summarization", "TextAnalysis.jl"]
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

The purpose of this paper is to introduce the Julia programming language with a concentration on Text Summarization. An extractive summarization algorithm is used for summarizing. Julia's evolution and features, as well as comparisons to other programming languages, are briefly discussed. The system's operation is depicted in a flow diagram, which illustrates the processes of sentence selection.

---

## Introduction

People are being overloaded by the massive number of digital content and papers as the Internet has grown dramatically. The need for material that has been summarized rather than read has also grown. We can now summarize text thanks to advances in machine learning and deep learning. Furthermore, the amount of data available online is massive, making it easier to train the models. The challenge of generating a short and fluent summary yet keeping vital information material and general context is known as automatic text summarization. Throughout the past few years, multiple techniques for text summarization have been devised and widely used in a variety of applications. For instance, search engine crawlers create snippets as document previews. Other examples are news websites that offer abbreviated summaries of news subjects, typically in the form of headlines, to aid browsing or knowledge extraction methodologies. Automatic text summarizing is difficult since, when we summarize a piece of text, we normally read it completely to build our knowledge, and then create a summary stressing its important points. Because computers and technology lack basic human understanding and linguistic aptitude, automated text summarization is a tough and time-consuming operation.

There are two techniques to automated summarization in general. Extractive summarizing approaches function by detecting key chunks of the text and reproducing them exactly; consequently, they rely only on phrase extraction from the original text. Abstractive summarization approaches, on the other hand, strive to generate important content in a novel way. In other words, they evaluate and analyze the content using powerful natural language techniques to develop a new shorter text that provides the most important information from the original text. Whereas most human-created summaries are not extractive, the majority of summarizing research today is focused on extractive summarization. When compared to automatic abstractive summaries, pure extractive summaries frequently produce better outcomes. That’s because abstractive summarization approaches deal with difficulties like semantics, reasoning, and natural language production, which are more difficult than data-driven methods.

---

## Related Work

### Extractive Summarization

Extractive summarization [[1]](#ref-1)[[3]](#ref-3) algorithms generate summaries by selecting a subset of the sentences in the original text. The most essential sentences from the input are included in these summaries. A single document or a collection of documents can be used as input. To get a better understanding of how summarizing systems function, we define three somewhat distinct activities that all summarizers do: First, they create an intermediate representation of the input text that communicates the text's essential points. Then give each sentence a score depending on its representation. Finally, they choose a summary made up of a few phrases.

While summarizing a text, every summarizing system develops an intermediate representation of it. It then applies this representation to find the most important material. Topic representation and indicator representation are two forms of representation-based techniques. Topic representation methods convert the text into an intermediate representation and understand the text's topic(s). The sophistication and representation model of topic representation-based summarization algorithms varies, and they are separated into frequency-driven approaches, topic word approaches, latent semantic analysis, and Bayesian topic models. Every sentence is described as a set of important qualities (indicators) such as sentence length, position in the text, and the presence of certain words in indicator representation techniques [[2]](#ref-2).

### Sentence Score

When working with textual data, sentence score [[4]](#ref-4) is one of the most commonly used procedures in the field of Natural Language Processing (NLP). It's a method of associating a numerical number with a statement dependent on the priority of the algorithm being employed. This method is widely used, particularly for text summaries. Many prominent sentence scoring systems exist, including TF-IDF, TextRank, and others [[4]](#ref-4).

We give a significance score to each sentence when the intermediate representation is created. In topic representation techniques, a sentence's score measures how effectively it communicates some of the text's most essential themes. The score is derived in most indicator representation systems by pooling data from several indicators.

### Topic Words Representations

One of the most prominent topic representation techniques [[3]](#ref-3) is the topic words procedure, which seeks to find words that characterize the source text's topic. In the news domain, using topic signature terms as topic representation was also quite beneficial and boosted the accuracy of complex abstract summarization. See this page for further information on the log-likelihood ratio test. The relevance of a sentence may be calculated in two ways: as a function of the number of subject signatures in the sentence or as a proportion of the topic signatures in the sentence. All sentence scoring systems use the same subject representation, but they may give sentences wildly different results. Lengthier phrases may receive better marks under the first technique since they include more information. The frequency of the topic terms is measured using the second method.

---

## Model Architecture

### Flow Diagram

{{< figure src="Text%20Summarizer%20Using%20Julia/Figures/figure-1-flow-diagram.png" caption="Flow Diagram" align="center" >}}

### Working of the System

The working of the text summarizer system is very simple and easy to understand and implement in Julia [[5]](#ref-5). As explained above, Julia is a high computational language that has been recently developed. It’s faster and easier than python which has been by far the easiest programming language to learn.

{{< figure src="Text%20Summarizer%20Using%20Julia/Figures/figure-2-flowchart-extractive-summarization.png" caption="Flowchart of Extractive Summarization" align="center" >}}

For our system, we first specify the stop words, which are terms that are not required and are removed to simplify the content. Then the sentence is split and each word is tokenized; if the length of the sentence is greater than 30, then that sentence is not considered. Furthermore, we determine the frequency of each word in the sentences by counting the number of times that particular word appears. We then calculate the sentence score after obtaining the word frequency. Based on the sentence score, we get the extracted summary from the original text. We have basically created a function capable of summarizing any text. We, later on, call the library in which the function is written in our driver code. The below code shows how the function can be called and summarizes a doc file.

{{< figure src="Text%20Summarizer%20Using%20Julia/Figures/figure-3-code-snippet.jpg" caption="Code Snippet" align="center" >}}

### Why Julia

Julia is a relatively new programming language that was originally released in 2012 and aspires to be both simple and quick. "It runs like C but reads like Python," [[8]](#ref-8). It was designed for scientific computing, with the ability to handle enormous quantities of data and processing while remaining relatively simple to manage, generate, and prototype code. The developers of the languages stated the reasons why they created this language: “We seek an open-source language with a permissive licence […] Ruby's dynamism combined with C's speed. […] a homoiconic language with genuine macros, similar to Lisp, but with obvious, familiar mathematical notation, similar to Matlab. […] as excellent at glueing programmes together as the shell, as good at general programming as Python, as easy to use for statistics as R, as natural for string processing as Perl, as powerful for linear algebra as Matlab, and as natural for string processing as Perl. Something that is really simple to understand while also satisfying the most ardent hackers”.

In pursuit of that goal, people from all over the world have been constantly updating and improving Julia, resulting in a vibrant and robust network. Over 700 people have contributed to Julia, and countless others have produced amazing open-source Julia packages [[5]](#ref-5).

Summarization is essential in today’s world. It is becoming more necessary to summarize News Articles, Scientific Articles, Books, Websites, Social Media Streams and Emails as daily tonnes of new data are released, making it a must to keep relevant material accessible in order to save time. This topic was quite interesting to implement in Julia [[6]](#ref-6) as the language is very much flexible to use.

### Julia Features

1.  **Dynamic**: Julia is dynamically typed, has a scripting aspect to it, and supports interactive use quite well.
2.  **Faster**: Julia was designed from the start-up to be a greater system. On a range of computers, the Low-Level Virtual Machine (LLVM) translates Julia programs into efficient native code.
3.  **General**: It does numerous relays as a model, which makes it easier to implement object-oriented programming design. The standard library contains asynchronous I/O, process control, logging, profiling, package management, and other features.
4.  **Easy Use Syntax**: Julia is a very rich language in terms of its syntax. The declarations of the data type can be used to define and strengthen computations in Julia.
5.  **Complexity**: Julia language is great when it comes to handling complex computational tasks [[7]](#ref-7) as it is easy to write mathematical formulas because of Julia’s syntax. Also, it supports a wide range of predefined arithmetic types of data, and established parallelism.

### Comparison with Other Languages

When it comes to speed, languages like C and Fortran are very fast as they are compiled before the execution. However, in terms of complexity and learning, it takes more time to get used to and implement it. In this case, Julia is very fast and very easy to write as well. Julia, like C or Fortran, is compiled, so it runs quickly. Julia, on the other hand, is compiled at runtime. So it appears to be an interpreted language: you can create a script, click 'run,' and it works exactly like Python [[7]](#ref-7).

Most generated languages utilize static typing since the compiler can only generate machine code for specified kinds — integers, floats, and so on. As a result, the programmer must define the type of each variable, making the code somewhat fragile. In comparison to dynamically typed languages such as Python, where every variable can be any type at any moment, this makes coding a little... hard. So, how does Julia handle dynamic typing while also compiling it before execution?

Here’s how: Julia reads the instructions and compiles them for the types it finds (a process known as type inference), then generates and stores the bytecode [[8]](#ref-8). When you run the same commands with a different type, Julia recompiles for that type and caches the resulting bytecode in a separate place. Later runs recompile and utilize the proper bytecode.

Additionally, Unicode characters are supported as variables and arguments in Julia. This means that you should no longer use sigma or sigma i, but rather σ or σi in mathematical notation. When you look at code for an algorithm or a mathematical problem, you'll see that the notation and idioms are nearly identical. This is a remarkable feature that we call "One-To-One Code and Math Relationship." This is a feature that is only possible in Julia.

{{< figure src="Text%20Summarizer%20Using%20Julia/Figures/figure-4-computational-comparison.png" caption="Comparison of Computational Resource for different operations in programming languages" align="center" >}}

### Results

As the method used is extractive summarization, the summarized text would be sentences that are extracted based on the sentence score. The system is less efficient as it requires additional and better techniques to enhance its performance. It is in the initial stage, so further work is needed.

{{< figure src="Text%20Summarizer%20Using%20Julia/Figures/figure-5-sample-result.png" caption="Sample of Result" align="center" >}}

---

## YouTube Demonstration

{{< youtube 2drrqsSB1Bc >}}

---

## Conclusion

Because of the Internet's rapid growth, a large amount of data is now available. Humans find it difficult to summarize large amounts of text. As a result, there is a high demand for automatic summarizing solutions in this age of information overload. In this research, we suggested a text summarizing system using Julia that is based on the extractive approach. As a paradigm, this new language employs multiple dispatches, making it simple to express a wide range of object-oriented and functional programming patterns. The standard library includes asynchronous input and output, operational processes, logging, profiling, a package manager, and other features. Until now, no text summarizing has been implemented in this language. The algorithm we developed computes the word frequency and sentence score and then provides a summary based on the highest sentence score. The system is currently in its first stages of development. If we raise the sentence's complexity, more problems may appear. It's still a pretty simple summarizer. However, more work on the system, particularly the implementation of a machine learning model with Julia, would greatly improve the project because Julia is a high computing language.

---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="/posts/2022-01-24-text-summarizer-using-julia/Text%20Summarizer%20Using%20Julia/text-summarizer-presentation.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

### Project Source, Research & Visualizations
Access the complete source code, full research paper, video demonstrations, and related engineering materials via the repositories below:

<div style="display: flex; flex-direction: column; gap: 10px;">

<div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/2drrqsSB1Bc" target="_blank">YouTube Demonstration</a>
  </div>

<div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/TEXT-SUMMARIZER" target="_blank">Text Summarizer Project Repository</a>
  </div>

<div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/JULIA" target="_blank">50 Days Julia Challenge - Challenge successfully completed with Mega Satish</a>
  </div>

<div>
    <!-- viXra Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 8px;"><title>viXra</title><path d="M0 0h3v3h3v3h3v3h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3zM21 0h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3zM6 15h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3z" /></svg>
    <a href="https://vixra.org/abs/2202.0017" target="_blank">viXra Preprint</a>
  </div>

<div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="http://dx.doi.org/10.22214/ijraset.2022.40066" target="_blank">Full Paper (IJRASET)</a>
  </div>

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II" target="_blank">Natural Language Processing</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://github.com/Amey-Thakur/NATURAL-LANGUAGE-PROCESSING-AND-COMPUTATIONAL-LAB-II?tab=readme-ov-file#the-wall" target="_blank">The Wall (Collaborative study notes by Amey & Mega)</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Text Summarizer Using Julia". AmeyArc (Jan 2022). https://amey-thakur.github.io/posts/2022-01-24-text-summarizer-using-julia/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2022textsummarizer,
  title   = "Text Summarizer Using Julia",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Jan",
  url     = "https://amey-thakur.github.io/posts/2022-01-24-text-summarizer-using-julia/"
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Nenkova and K. McKeown</b>, “A survey of text summarization techniques,” in <i>Mining text data</i>, pp. 43–76, Springer, Boston, MA, 2012, DOI: <a href="https://doi.org/10.1007/978-1-4614-3223-4_3">10.1007/978-1-4614-3223-4_3</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>M. Allahyari et al.</b>, “Text summarization techniques: a brief survey,” <i>arXiv preprint arXiv:1707.02268</i>, 2017, DOI: <a href="https://doi.org/10.48550/arXiv.1707.02268">10.48550/arXiv.1707.02268</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>N. Moratanch and S. Chitrakala</b>, “A survey on extractive text summarization,” in <i>2017 International Conference on Computer, Communication and Signal Processing (ICCCSP)</i>, pp. 1–6, IEEE, 2017, DOI: <a href="https://doi.org/10.1109/ICCCSP.2017.7944061">10.1109/ICCCSP.2017.7944061</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>R. Ferreira et al.</b>, “Assessing sentence scoring techniques for extractive text summarization,” <i>Expert Systems with Applications</i>, vol. 40, no. 14, pp. 5755–5764, 2013, DOI: <a href="https://doi.org/10.1016/j.eswa.2013.04.023">10.1016/j.eswa.2013.04.023</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>J. Bezanson et al.</b>, “Julia Language Documentation,” <i>The Julia Manual</i>, 2014, pp. 1–261, [Online], Available: <a href="https://docs.julialang.org/">https://docs.julialang.org/</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>K. Gao et al.</b>, “Julia language in machine learning: Algorithms, applications, and open issues,” <i>Computer Science Review</i>, vol. 37, p. 100254, 2020, DOI: <a href="https://doi.org/10.1016/j.cosrev.2020.100254">10.1016/j.cosrev.2020.100254</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>J. Bezanson, A. Edelman, S. Karpinski, and V. B. Shah</b>, “Julia: A fresh approach to numerical computing,” <i>SIAM Review</i>, vol. 59, no. 1, pp. 65–98, 2017, DOI: <a href="https://doi.org/10.1137/141000671">10.1137/141000671</a> [Accessed: Jan. 24, 2022].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>J. M. Perkel</b>, “Julia: Come for the syntax, Stay for the speed,” <i>Nature</i>, vol. 572, Aug. 2019, DOI: <a href="https://doi.org/10.1038/d41586-019-02310-3">10.1038/d41586-019-02310-3</a> [Accessed: Jan. 24, 2022].</span>
</div>

</div>
