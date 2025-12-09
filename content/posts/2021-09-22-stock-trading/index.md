---
title: "Stock Trends Prediction: LSTM and Time-Series Analysis"
date: 2021-09-22T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Deep Learning", "LSTM", "Finance", "Time-Series", "Stock Market", "Prediction", "Python"]
ShowToc: true
TocOpen: false
description: "Leveraging Long Short-Term Memory (LSTM) networks to forecast stock market trends."
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




The stock market is a chaotic, non-linear system, notoriously difficult to predict. Traditional statistical models often fail to capture the complex temporal dependencies in price movements. This project applies **Long Short-Term Memory (LSTM)** networks, a specialized type of Recurrent Neural Network (RNN), to forecast stock trends. LSTMs are uniquely suited for this task due to their ability to remember long-term sequences and forget irrelevant noise, allowing them to detect patterns over days or weeks that simpler models miss [[1]](#ref-1).

---

## Predicting the Unpredictable

How do you guess tomorrow's price based on yesterday's?

### The Analogy: The Weather Forecaster
*   **Simple Prediction**: "It rained yesterday, so it will likely rain today" (Persistence Model).
*   **LSTM Prediction**: "It rained yesterday, but I remember that 2 weeks ago a cold front started moving in, and usually after 3 days of rain in this season, it clears up."

The LSTM has a "memory cell" that acts like a notebook. It writes down important events ("Fed raised rates") and keeps them in mind for 50 steps, then crosses them out when they are no longer relevant. This context helps it make a better guess than just looking at the previous day's candle.

---

## Model Architecture

We utilized a stacked LSTM architecture to model the time-series data:

*   **Input Layer**: 60 days of historical closing prices were used as the input sequence.
*   **LSTM Layers**: Two layers with 50 neurons each, using `tanh` activation to maintain long-term gradients.
*   **Dropout**: 20% dropout was applied to prevent overfitting, ensuring the model generalizes rather than memorizing a specific year's chart.
*   **Dense Output**: A single neuron predicting the normalized price for day 61.

---

## Publication Details

This work was published in the **International Journal of Research in Applied Science and Engineering Technology (IJRASET)**.

### Additional Resources
*   [Full Paper (PDF)](Optimizing%20Stock%20Trading%20Strategy%20With%20Reinforcement%20Learning/Optimizing%20Stock%20Trading%20Strategy%20With%20Reinforcement%20Learning.pdf)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Stock Trends Prediction: LSTM and Time-Series Analysis". AmeyArc (Sep 2021). https://amey-thakur.github.io/posts/2021-09-22-stock-trading/.</code></pre>

**Or use the BibTex citation:**

**BibTeX:**

```
@article{thakur2021stocktrading,
  title   = "Stock Trends Prediction: LSTM and Time-Series Analysis",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Sep",
  url     = "https://amey-thakur.github.io/posts/2021-09-22-stock-trading/"
}
```

## References

1. <a id="ref-1"></a> **Thakur, A.** (2021). Stock Trends Prediction Using Algorithms. *International Journal of Research in Applied Science and Engineering Technology (IJRASET)*, 9(9).

---
*Authored by Amey Thakur.*
