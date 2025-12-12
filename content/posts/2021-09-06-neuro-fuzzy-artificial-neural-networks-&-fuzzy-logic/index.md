---
title: "Neuro-Fuzzy: Artificial Neural Networks & Fuzzy Logic"
date: 2021-09-06T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Adaptive Control Systems", "AI", "ANFIS", "Artificial Intelligence", "Boolean Logic", "Computational Intelligence", "Control Systems", "Crisp Logic", "Decision Support Systems", "Deep Learning", "Defuzzification", "Expert Systems", "Fuzzy Inference System", "Fuzzy Logic", "Fuzzy Logic Applications", "Fuzzy Rules", "Fuzzy Set Theory", "Fuzzification", "Hybrid Intelligent Systems", "Hybrid Systems", "Intelligent Control", "Machine Learning", "Mamdani Fuzzy System", "Membership Function", "Neural Networks", "Neuro-Fuzzy", "Neuro-Fuzzy Control", "Pattern Recognition", "Soft Computing", "Takagi-Sugeno-Kang", "Uncertainty Handling", "Washing Machine Fuzzy Logic"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Karan Dhiman for his meaningful contributions, support, and wisdom that helped shape this work. Neuro Fuzzy is a hybrid system that combines Artificial Neural Networks with Fuzzy Logic. Provides a great deal of freedom when it comes to thinking. This phrase, on the other hand, is frequently used to describe a system that combines both approaches."

---

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

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=kKNKmqgAAAAJ&hl=en">Karan Dhiman</a> for his meaningful contributions, support, and wisdom that helped shape this work.
</p>

Neuro Fuzzy is a hybrid system that combines Artificial Neural Networks with Fuzzy Logic. Provides a great deal of freedom when it comes to thinking. This phrase, on the other hand, is frequently used to describe a system that combines both approaches. There are two basic streams of neural network and fuzzy system study. Modelling several elements of the human brain (structure, reasoning, learning, perception, and so on) as well as artificial systems and data: pattern clustering and recognition, function approximation, system parameter estimate, and so on. In general, neural networks and fuzzy logic systems are parameterized nonlinear computing methods for numerical data processing (signals, images, stimuli). These algorithms can be integrated into dedicated hardware or implemented on a general-purpose computer. The network system acquires knowledge through a learning process. Internal parameters are used to store the learned information (weights).

---

## Introduction

### Fuzzy Logic

Fuzzy Logic (FL) is a type of reasoning that is similar to human thinking [[1]](#ref-1). This approach is similar to how humans perform decision-making and it involves all other intermediate possibilities between yes and no.

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(1)%20Fuzzy%20Logic.png" caption="Fuzzy Logic" align="center" >}}

For example, suppose there is a question asked as is it raining? In the Boolean logic the answer can either be yes or no i.e. it only takes the value to be as 1 or 0. But when it comes to fuzzy logic and if we ask the same question, is it raining? we will get different answers like it's very much raining or it's a little rain or very less so we will also get the intermediate possibilities between yes and no [[2]](#ref-2)[[3]](#ref-3). The computer won't just take the values 0 & 1. The difference between the Boolean logic and the fuzzy logic is that in Boolean we only use the 0 & 1 or the yes and no values but in fuzzy logic we have intermediate values between this yes and no or 0 & 1. The conventional logic block that a computer understands takes precise input and produces a definite output as true or false which is equivalent to a human saying yes or no. The fuzzy logic was invented by Lotfi Zadeh who observed that unlike computers humans have a different range of possibilities between yes and no.

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(2)%20Example%20of%20Fuzzy%20Logic.png" caption="Example of Fuzzy Logic" align="center" >}}

There can be multiple possibilities such as Certainly Yes, Possibly Yes, Cannot Say, Possibly No or Certainly No. We just do not say only yes or no, we do have certainty or possibilities at times. Fuzzy logic operates on the levels of input possibilities to provide a definitive result. The implementation of this particular logic is it can be implemented in systems with different sizes and capabilities such as microcontrollers, large network or workstation-based systems also this can be implemented in hardware, software, or a hybrid of the two.

### Use of Fuzzy Logic

We use the fuzzy logic system for both commercial and practical purposes such as it controls machines and also the consumer products and if not accurate reasoning it at least provides acceptable reasoning so at times when we say Certainly Yes or Possibly Yes it's not giving accurate reasoning whether the answer is yes or no but at least it gives acceptable reasoning where you are saying that it might be or it can happen something like that. It helps in dealing with the uncertainty in engineering in case we are unsure or we don't know if the answer can be yes or no, we can find a middle path that is where it helps in dealing with the uncertainty. These are the different reasons for which we actually need to use fuzzy logic [[4]](#ref-4).

---

## Fundamentals of Neuro-Fuzzy

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(3)%20Soft%20Computing.png" caption="Soft Computing" align="center" >}}

Soft Computing is frequently associated with neural networks and fuzzy logic systems. Intersections include neuro-fuzzy systems and techniques, probabilistic approaches to neural networks (especially classification networks) and fuzzy logic systems and Bayesian reasoning.

### Soft Computing

It is an approach to computing which parallels the remarkable ability of the human mind to reason and learn in an environment of uncertainty and imprecision. It is distinguished by the use of approximate solutions to computationally difficult tasks, such as the solution of nonparametric complicated problems for which an exact solution cannot be obtained in polynomial time.

### Soft Computing Approach

For relatively basic systems, a mathematical model and analysis may be performed. More complicated systems in biology, medicine, and management systems continue to defy ordinary mathematical and analytical approaches. To achieve tractability, resilience, and cheap solution cost, soft computing deals with imprecision, uncertainty, partial truth, and approximation. It extends its application to various disciplines of Engineering and science. Typically, humans can:

1. Take decisions
2. Inference from previous situations experienced
3. Expertise in an area
4. Adapt to changing environment
5. Learn to do better
6. Social behaviour of collective intelligence

Intelligent control strategies have emerged from the above-mentioned characteristics of humans. The first two qualities gave rise to fuzzy logic; the second, third, and fourth led to neural networks; and the fourth, fifth, and sixth were utilized in evolutionary algorithms. Fuzzy Logic, Neural Networks, and Concepts are essential existing optimization aspects in the building of smart control systems.

### Characteristics of Neuro-Fuzzy & Soft Computing

1. Human Expertise
2. Biologically inspired computing models
3. New Optimization Techniques
4. Numerical Computation
5. New Application domains
6. Model-free learning
7. Intensive computation
8. Fault tolerance
9. Goal-driven characteristics
10. Real-world applications

### Fuzzification

Fuzzification is the process of converting a sharp input value to a fuzzy value using knowledge base information. It is the process of allocating a system's numerical input to fuzzy sets with varying degrees of membership. This level of membership might be anything between [0, 1]. If it is 0, the value does not belong to the specified fuzzy set, and if it is 1, the value belongs entirely to the fuzzy set.

For example, if the temperature is given to be 25-degree Celsius as the crisp input value, then it can be converted into a linguistic variable like a pleasant temperature for the human body or even hot or cold.

### Defuzzification

It is the inverse of fuzzification, where mapping is done to convert crisp results to fuzzy results, while here mapping is done to convert fuzzy results to crisp results. This technique can provide a non-fuzzy control action that depicts the probability distribution of an inferred fuzzy control action. The centre of area technique (COA), also known as the centroid method, is the most widely used defuzzification method. This function finds the centre of the fuzzy set's area and returns the matching crisp value. The centre of sums (COS) technique and the mean of maximum method are two defuzzification approaches.

---

## Fuzzy Inference System

The Fuzzy inference system is a prominent computer framework that is based on fuzzy set theory, fuzzy if-then logic, and fuzzy reasoning. It has been used successfully in fields such as automated control, data classification, decision analysis, expert systems, and computer visualisation. The fuzzy inference system is known by a variety of names due to its multidisciplinary character, including fuzzy-rule-based system, fuzzy expert system, fuzzy model, fuzzy associative memory, fuzzy logic controller, and simply fuzzy system. The aim to use imprecise data in mathematical models resulted in the creation of fuzzy modelling approaches. The tools of fuzzy modelling enable the transformation of a linguistic description into an algorithm, the output of which is an action. Fuzzy logic and fuzzy set theory are the two primary ideas used in fuzzy modelling. Variables in a fuzzy model may represent fuzzy subsets of the universe.

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(4)%20Fuzzy%20Inference%20System.png" caption="Fuzzy Inference System" align="center" >}}

As seen in the Figure, a fuzzy inference system (FIS) is made up of four functional components [[9]](#ref-9):

1. **Fuzzification**: Converts crisp inputs into degrees of correspondence with linguistic values.
2. **Knowledge Base**: A knowledge base is made up of a rule base and a database. A rule base is a collection of fuzzy if-then rules. The Membership Functions of the fuzzy sets used in the fuzzy rules are defined in a database.
3. **Fuzzy Inference Engine**: The inference operations on the rules are performed by the fuzzy inference engine.
4. **Defuzzification**: Turns the inference's fuzzy results into a crisp output.

Fuzzy inference systems include the Mamdani and Takagi-Sugeno fuzzy systems. A set of language rules acquired from human operators was used to operate a steam engine and boiler combination using the Mamdani fuzzy inference method for the first time.

Takagi and Sugeno were the first to introduce the Takagi-Sugeno fuzzy inference system. The Takagi-Sugeno model differs in that each rule has a distinct output, and the overall output is determined by a weighted average of the outputs of the individual rules.

### Mamdani Fuzzy System

When implementing the Mamdani rule-based system, which is the most well-known fuzzy system, the following procedure is followed:

1. Fuzzify all input values by converting them to fuzzy membership functions.
2. To compute the fuzzy output functions, run all applicable rules in the rulebase.
3. De-fuzzify the fuzzy output routines to get crisp output values.

**Fuzzy logic operators:** Fuzzy logic operates on membership values in a manner similar to Boolean logic. For that, substitutes for the basic operators AND, OR, and NOT must be offered. There are numerous approaches to this. The Zadeh operators are a popular replacement:

<div style="display: flex; flex-direction: column; align-items: center; margin: 1rem 0;">

<p style="font-size: 0.9em; margin-bottom: 10px; text-align: center;">
    <span style="user-select: none;">Table 1: </span>
    An Analogy of Boolean & Fuzzy Logic Operators
</p>

<table style="width: auto; min-width: 200px; border-collapse: collapse;">
  <thead>
    <tr style="border-bottom: 2px solid #ccc;">
      <th style="text-align: center; padding: 8px;">Boolean</th>
      <th style="text-align: center; padding: 8px;">Fuzzy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">AND (x, y)</td>
      <td style="padding: 8px; text-align: center;">MIN (x, y)</td>
    </tr>
    <tr style="border-bottom: 1px solid #eee;">
      <td style="padding: 8px; text-align: center;">OR (x, y)</td>
      <td style="padding: 8px; text-align: center;">MAX (x, y)</td>
    </tr>
    <tr>
      <td style="padding: 8px; text-align: center;">NOT (x)</td>
      <td style="padding: 8px; text-align: center;">1 - x</td>
    </tr>
  </tbody>
</table>

</div>

The fuzzy expressions provide the same result as the Boolean expressions for TRUE/1 and FALSE/0.

**IF-THEN rules:** IF-THEN rules are used to link input or calculated truth values to desired output truth values.

*Example:*
1. IF car_speed is very high THEN car_speed is slowed down.
2. IF car_speed is very slow THEN car_speed is increased.

If an output variable appears in several THEN parts, the values from the corresponding IF parts are merged using the OR operator.

### Takagi-Sugeno-Kang (TSK) System

TSK is identical to Mamdani, except that the defuzzification process is integrated into the fuzzy rule execution. These are also modified such that the rule's consequence is represented by a polynomial function, which is generally constant or linear.

The major benefit of adopting TSK over Mamdani is that it is more computationally efficient and works well with other algorithms such as PID control and optimization algorithms. It can also ensure the output surface's continuity. Mamdani, on the other hand, is more intuitive and simpler to deal with. As a result, TSK is typically used in conjunction with more advanced techniques, such as adaptive neuro fuzzy inference systems.

---

## Architecture of Neuro-Fuzzy

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(5)%20Architecture%20of%20Neuro-Fuzzy.png" caption="Architecture of Neuro-Fuzzy" align="center" >}}

Fuzzy Logic Architecture consists of four main parts: Rules, Fuzzifier, Intelligence, Defuzzifier.

1. **Rules** contain all the rules and the if-then conditions offered by the experts to control the decision-making system. The most current update to fuzzy theory gives several useful approaches for designing and adjusting fuzzy controllers. Usually these developments reduce the number of fuzzy rules as well.

2. **In Fuzzifier**, fuzzification takes place. In this step, the inputs or the crisp numbers are converted into fuzzy sets. We can measure the crisp inputs by sensors and pass them into the control system for further processing. Then the fuzzification splits the input signal into five steps like LP, MP, S, MN and LN where:
   - **LP** is where X is large positive.
   - **MP** is where it's medium positive.
   - **S** stands for small.
   - **MN** which is medium negative.
   - **LN** which is large negative.

3. **Inference Engine** which is the intelligence which determines the degree of match between fuzzy input and the rules. According to the input field it will decide the rules that are to be fired combining the fired rules form the control actions. Here we can see that from rules we go to the intelligence and from fuzzifier we have the fuzzy input set going into the inference engine now this will combine the fired rules and form the control actions and from here we will get our fuzzy output set so once we get this fuzzy output set we go to the defuzzifier where defuzzification takes place.

4. **The Defuzzification** technique transforms fuzzy sets into crisp values. There are different types of techniques available and you need to select the best suited one with an expert system so here first we have a crisp input going to the fuzzy-fire where fuzzification takes place and the crisp input is converted into a fuzzy input set. This fuzzy input set passes through the inference engine and we have a fuzzy output set. This fuzzy output set goes through defuzzification where again we get a crisp output.

---

## Membership Function

The membership function is a graph [[12]](#ref-12) that defines how each point in the input space is mapped to membership value between 0 & 1. It allows us to quantify linguistic terms and represents a fuzzy set graphically [[5]](#ref-5)[[7]](#ref-7). A membership function for a fuzzy set <i>A</i> on the universe of discourse <i>X</i> is defined as:

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
    <i>μ</i><sub style="font-size: 0.75em;"><i>A</i></sub> : <i>X</i> → [0, 1]
</div>

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(6)%20Membership%20Function.png" caption="Membership Function" align="center" >}}

This quantifies the degree of membership of the element in <i>X</i> to the fuzzy set <i>A</i> and the X-AXIS represents the universe of discourse whereas the Y-AXIS represents the degrees of membership in the [0,1] interval. There can be a multiple membership function applicable to falsify a numerical value. Simple membership functions are used as the complex functions that do not add precision in the output. Membership functions characterize fuzziness (i.e., all the information in a fuzzy set), whether the elements in fuzzy sets are discrete or continuous. Membership functions are represented by graphical forms. Rules for defining fuzziness are fuzzy too.

{{< figure src="Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/figures/Figure%20(7)%20Membership%20Functions%20for%20LP,%20MP,%20S,%20MN%20and%20LN..png" caption="Membership Functions for LP, MP, S, MN and LN" align="center" >}}

Membership functions for LP, MP, S, MN and LN. For the X and y axis we have the membership functions and input voltage. The triangular membership function shapes are most common among various other membership function shapes. The input to the 5 level fuzzifier varies from -10 volts to +10 volts. Hence the corresponding output also changes. Based on these volts the value for the membership function will also change as we can see in the graph where from -10 to +10 volt there has been a great variation in the graph of input voltage and membership function.

---

## Fuzzy Logic vs Probability

Fuzzy logic is often confused with probability. In Fuzzy Logic, we basically try to capture the essential concept of vagueness. We are not taking an exact value like 0 or 1. We are considering the vagueness, where there is a certainty or a possibility but probability is associated with events and not facts and those events will either occur or not occur so there's no such concept of vagueness. It's just about events which will either take place or not. Fuzzy logic also captures the meaning of partial truth where sometimes we say Possibly Yes or Possibly No or Certainly Yes or Certainly No. But Probability theory captures partial knowledge; it has nothing to do with the truth, it only deals with the partial knowledge. Fuzzy logic takes truth degrees as a mathematical basis whereas probability is a mathematical model of ignorance.

---

## Applications of Fuzzy Logic

It is used in various fields such as automotive systems, domestic goods, environment control, etc. and some of the common applications in fluid to the use in the aerospace field for altitude control of spacecraft and satellites. It also controls the speed and traffic in the automotive systems. It is also used for decision making support systems and personal evaluation in the large company business. It definitely helps you make certain decisions where you cannot just go for yes or no. We need certain other possibilities in between. In the chemical sector, it also manages the pH, drying, and chemical distillation processes. Fuzzy logic is also used in natural language processing and various intensive applications and artificial intelligence. It helps in the national language processing where we just do not need a Boolean logic of 0 or 1. We need to understand what we are converting and understand the sentiments and possibilities as well. It is extensively used in modern control systems such as the expert systems. Also fuzzy logic mimics how a person would make decisions only much faster suppose somebody asks you a question and sometimes answer may not be just a yes-or-no you might have to take other decisions as well so fuzzy logic things like a human being just that it works a little faster so you can also use it with Neural Networks [[6]](#ref-6)[[10]](#ref-10)[[11]](#ref-11). These were some of the common applications of fuzzy logic.

Purchasing a washing machine is as mature a decision as someone can make. When you purchase your individual washer, you know you've grown. When words like Fuzzy Logic are thrown at you, you'd be forgiven for thinking it's simply marketing jargon. However, while purchasing a washing machine, fuzzy logic is a crucial factor to consider. Why? As a result of the washing machine's failure, you're spending a lot of money on it, and it runs on this.

### Fuzzy Logic in Brief

Washing machines that use fuzzy logic are becoming extremely popular. Performance, productivity, simplicity, and productivity are all advantages of these devices. In fact, fuzzy logic is a mathematical concept [[8]](#ref-8). It is a mathematical system capable of interpreting and transforming analog input values into logical variables. In basic terms, Fuzzy Logic, in the context of a washing machine, combines sensors to evaluate shifting situations within the machine and adapts its operation correctly. In essence, sensors in the washing machine will supervise the whole washing process, conducting activities based on the various water input, wash interval, rinse performance, and spin speed.

### The Factors to be Considered

Not all Fuzzy Logic systems are identical, and the parameters sensed in the washing machine are probably different between models. Nevertheless, in general, the dependent factors are frequently kept in mind:

1. The mass of the burden
2. The fabric material
3. The quantity and water temperature
4. The quantity of detergent
5. The filth in the water or rinse must be removed.
6. The kind and duration of agitation necessary
7. The spin cycle's speed and length

### Process and Working

Fuzzy Logic is a method that optimizes your washing machine's performance based on changeable parameters. What does this mean in the actual world? A Fuzzy Logic machine will utilize sensors to assess the level of soiling on your garments.

This is accomplished by the use of optical sensors that measure the clarity of the water after the tub has been filled. More dirt or grease will decrease the clarity of the water. This allows the machine to compute saturation, which determines how much detergent and water are needed for a clean wash. It will also decide the time and direction of spin, among other things, to ensure that your clothing is as efficient as possible.

### Neuro Fuzzy Control

In some washing machines, a complicated theory known as Neuro Fuzzy Control is now at effect. This model has improved sensors and can also detect the fabric type of the garments in the load of washing. The washing is then controlled based on the fabric as well as other factors. This extends the life of your clothing and allows your washing machine to operate at peak efficiency while using only the necessary energy.

Since Fuzzy Logic utilizes a good degree of variable-based optimisation, your clothing is tossed and turned by the most appropriate settings. This ensures your garments will have less depreciation.

---

## Advantages and Disadvantages

### Advantages of Fuzzy Logic System

1. The structure of this logic system is very easy and understandable.
2. Fuzzy logic is widely used for commercial and practical purposes.
3. It helps to control machines and consumer products.
4. It helps to deal with uncertainty in engineering.
5. Motley robust as no precise inputs required.
6. If the feedback sensor stops working, one can program it into the situation.
7. It can be easily modified to improve or alter the system performance.
8. Inexpensive sensors can be employed, lowering the total system cost and complexity.

### Disadvantages of Fuzzy Logic System

1. Fuzzy logic is not always accurate.
2. It cannot recognize machine learning as well as neural network type patterns.
3. Validation and verification of a fuzzy knowledge-based system necessitate significant hardware testing.
4. Setting the exact fuzzy rules and membership functions is a difficult task.
5. At times the fuzzy logic is confused with probability theory.


---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="/posts/2021-09-06-neuro-fuzzy-artificial-neural-networks--fuzzy-logic/Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic/Neuro-Fuzzy%20-%20Artificial%20Neural%20Networks%20&%20Fuzzy%20Logic%20Presentation.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

### Research Paper

Explore the published research paper and preprint:

<div style="display: flex; flex-direction: column; gap: 8px;">

  <div>
    <!-- viXra Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 8px;"><title>viXra</title><path d="M0 0h3v3h3v3h3v3h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3zM21 0h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3zM6 15h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3z" /></svg>
    <a href="https://vixra.org/pdf/2109.0047v1.pdf" target="_blank">viXra Preprint</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://doi.org/10.22214/ijraset.2021.37930" target="_blank">Full Paper (IJRASET)</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Neuro-Fuzzy: Artificial Neural Networks & Fuzzy Logic". AmeyArc (Sep 2021). https://amey-thakur.github.io/posts/2021-09-06-neuro-fuzzy-artificial-neural-networks-&-fuzzy-logic/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2021neurofuzzy,
  title   = "Neuro-Fuzzy: Artificial Neural Networks & Fuzzy Logic",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Sep",
  url     = "https://amey-thakur.github.io/posts/2021-09-06-neuro-fuzzy-artificial-neural-networks-&-fuzzy-logic/"
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur and A. Konde</b>, "Fundamentals of Neural Networks," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET)</i>, vol. 9, no. 8, pp. 407-426, 2021, DOI: <a href="https://doi.org/10.22214/ijraset.2021.37362">10.22214/ijraset.2021.37362</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>V. Novák, I. Perfilieva, and J. Močkoř</b>, <i>Mathematical principles of fuzzy logic</i>. Dordrecht: Kluwer Academic, 1999, ISBN: 978-0-7923-8595-0, <a href="https://link.springer.com/book/10.1007/978-1-4615-5217-8">https://link.springer.com/book/10.1007/978-1-4615-5217-8</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>J.-S. R. Jang, C.-T. Sun, and E. Mizutani</b>, "Neuro-fuzzy and soft computing-a computational approach to learning and machine intelligence [Book Review]," <i>IEEE Transactions on Automatic Control</i>, vol. 42, no. 10, pp. 1482-1484, 1997, DOI: <a href="https://doi.org/10.1109/TAC.1997.633847">10.1109/TAC.1997.633847</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>Stanford Encyclopedia of Philosophy</b>, "Fuzzy Logic," Bryant University, <a href="https://plato.stanford.edu/entries/logic-fuzzy/">https://plato.stanford.edu/entries/logic-fuzzy/</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>L. A. Zadeh</b>, "Fuzzy sets," <i>Information and Control</i>, vol. 8, no. 3, pp. 338-353, 1965, DOI: <a href="https://doi.org/10.1016/s0019-9958(65)90241-x">10.1016/s0019-9958(65)90241-x</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>A. Thakur and M. Satish</b>, "Generative Adversarial Networks," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET)</i>, vol. 9, no. 8, pp. 2307-2325, 2021, DOI: <a href="https://doi.org/10.22214/ijraset.2021.37723">10.22214/ijraset.2021.37723</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>L. A. Zadeh et al.</b>, <i>Fuzzy Sets, Fuzzy Logic, Fuzzy Systems</i>. World Scientific Press, 1996, ISBN: 978-981-02-2421-9, <a href="https://www.worldscientific.com/worldscibooks/10.1142/2895">https://www.worldscientific.com/worldscibooks/10.1142/2895</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>N. A. Bansod, M. Kulkarni, and S. H. Patil</b>, "Soft Computing- A Fuzzy Logic Approach," in <i>Soft Computing</i>, Bharati Vidyapeeth College of Engineering, Ed. Allied Publishers, 2005, p. 73, ISBN: 978-81-7764-632-0, <a href="https://books.google.ca/books?hl=en&lr=&id=IkajJC9iGxMC&oi=fnd&pg=PA73&dq=info:Qt2qNle0AssJ:scholar.google.com&ots=wEiyI3hh7R&sig=o4vmalxzf3-mjdApppPxlT2pwQI&redir_esc=y#v=onepage&q&f=false">https://books.google.ca/books?id=IkajJC9iGxMC</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>K. Verma</b>, "Use of Fuzzy Set and Neural Network to Extract Fingerprint Minutiae Points and Location," 2021, <a href="https://www.researchgate.net/publication/268363154_Use_of_Fuzzy_Set_and_Neural_Network_to_Extract_Fingerprint_Minutiae_Points_and_Location">https://www.researchgate.net/publication/268363154</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>A. Thakur, H. Rizvi, and M. Satish</b>, "White-Box Cartoonization Using An Extended GAN Framework," <i>arXiv preprint arXiv:2107.04551</i>, 2021, DOI: <a href="https://doi.org/10.48550/arXiv.2107.04551">10.48550/arXiv.2107.04551</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>A. Thakur, H. Rizvi, and M. Satish</b>, "White-Box Cartoonization Using An Extended GAN Framework," <i>International Journal of Engineering Applied Sciences and Technology (IJEAST)</i>, vol. 5, no. 12, pp. 294-298, 2021, <a href="https://www.ijeast.com/papers/294-298,Tesma512,IJEAST.pdf">https://www.ijeast.com/papers/294-298,Tesma512,IJEAST.pdf</a> [Accessed: Sep. 06, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>M. A. Raharja, I. D. M. B. A. Darmawan, D. P. E. N. Kusumawati, and I. W. Supriana</b>, "Analysis of membership function in implementation of adaptive neuro fuzzy inference system (ANFIS) method for inflation prediction," in <i>Journal of Physics: Conference Series</i>, vol. 1722, no. 1, p. 012005, IOP Publishing, 2021, DOI: <a href="https://doi.org/10.1088/1742-6596/1722/1/012005">10.1088/1742-6596/1722/1/012005</a> [Accessed: Sep. 06, 2021].</span>
</div>

</div>
