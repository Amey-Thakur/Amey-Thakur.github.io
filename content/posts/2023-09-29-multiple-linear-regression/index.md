---
title: "Multiple Linear Regression"
date: 2023-09-29T00:00:00-04:00
draft: false
author: "Amey Thakur"
tags: ["Linear Regression", "Multiple Linear Regression", "Machine Learning", "Python", "Scikit-Learn", "Data Science", "Supervised Learning", "Regression Analysis", "Predictive Modeling", "Statistical Analysis", "R-squared", "NumPy", "Matplotlib", "Predictive Analytics", "Model Evaluation", "Feature Engineering", "AI", "Data Analysis"]
ShowToc: true
TocOpen: false

---

<style>
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

This study examines regression analysis within Supervised Machine Learning, focusing on Simple Linear Regression (SLR) and Multiple Linear Regression (MLR). A practical implementation demonstrates the predictive relationship between study hours and grades.

---

## Introduction

Machine Learning enables computational systems to identify patterns and generate predictions from data. Supervised Learning, a core paradigm, relies on labeled datasets to train models, with primary tasks including Classification and Regression.

Regression predicts continuous numerical outcomes by modeling relationships between dependent and independent variables. Simple Linear Regression captures the effect of a single predictor, while Multiple Linear Regression incorporates multiple predictors, providing a more detailed representation of complex relationships.

This discussion explores the theoretical foundations of SLR and MLR, the supervised learning workflow, and the statistical assumptions and evaluation metrics, including R-squared and p-values. Implementation examples illustrate both SLR and MLR, including a 3D visualization of MLR convergence. The relevance of regression analysis is further highlighted through applications in finance, healthcare, and marketing.

## Hierarchy of Machine Learning Algorithms

Machine learning algorithms are generally categorized according to their learning style. The primary paradigms include Supervised Learning, Unsupervised Learning, and Reinforcement Learning.

{{< figure src="figures/Figure 1 - ML Algorithms.png" caption="Hierarchy of Machine Learning Algorithms" align="center" >}}

### Supervised Learning

This paradigm relies on labeled datasets, where the “correct” answers are known, to train algorithms to make accurate predictions or classifications. Within supervised learning, tasks are typically divided into Regression and Classification. Regression focuses on predicting continuous outcomes, while classification addresses discrete categories.

### Unsupervised Learning

In unsupervised learning, algorithms analyze unlabeled data to identify hidden patterns, structures, or groupings without prior guidance.

### Reinforcement Learning
Reinforcement learning trains algorithms to make a sequence of decisions through trial-and-error interactions with an environment, receiving feedback in the form of rewards or penalties.

Since this study concentrates on predicting continuous variables, such as grades based on study hours, the scope is restricted to the Regression branch of Supervised Learning. Regression techniques can be further classified as:

*   **Simple Linear Regression (SLR):** Models the relationship between one dependent variable and a single independent variable.
*   **Multiple Linear Regression (MLR):** Extends SLR to include multiple independent variables, enabling more complex predictive modeling.
*   **Polynomial Regression:** Captures non-linear relationships between variables through polynomial transformations.

This hierarchical framework positions Multiple Linear Regression as a specialized method within Supervised Learning, suited for modeling complex, multi-factor relationships.


## Supervised Learning Workflow

The supervised learning workflow follows a structured cycle to ensure the model learns effectively and generalizes well to unseen data.

{{< figure src="figures/Figure 2 - Supervised Learning Workflow.png" caption="Supervised Learning Workflow" align="center" >}}

1. **Data Splitting**
    The dataset is divided into two subsets: Training Data, used to fit the model, and Validation Data, used to evaluate its predictive performance.

2. **Model Training**
    The Training Data is employed to train the model. This phase is analogous to a student studying lessons to acquire knowledge on a subject.

3. **Predictions**
    Once trained, the model applies the learned relationships to generate predictions on new inputs.

4. **Evaluation**
    Predictions are evaluated against the Validation Data to assess performance. This step functions like an examination, testing how well the model performs on data it has not encountered during training.

5. **Refinement or Finalization**
    *   If evaluation metrics indicate satisfactory performance, the model is finalized.
    *   If performance is inadequate, the model undergoes retraining. This iterative process continues until the desired predictive accuracy is achieved, similar to a student revising lessons to improve test scores.

## Theoretical Framework

### Simple Linear Regression (SLR)

Simple Linear Regression is a statistical method used to model the relationship between a single independent variable and a dependent variable. Its primary goal is to predict the dependent variable by fitting a straight line that minimizes the difference between predicted and observed values.

{{< figure src="figures/Figure 3 - Simple Linear Regression.png" caption="Simple Linear Regression" align="center" >}}

The mathematical form is:

{{< figure src="figures/Figure 4 - Linear Regression Equation.png" caption="Linear Regression Equation" align="center" >}}

**Y = β₀ + β₁X + ε**

Where:
*   **Y (Dependent Variable):** The outcome we want to predict, such as grades received.
*   **X (Independent Variable):** The predictor, for example, hours studied.
*   **β₀ (Intercept):** The expected value of Y when X is zero.
*   **β₁ (Slope):** How much Y changes for each unit increase in X.
*   **ε (Error Term):** The portion of Y not explained by X.

**Example:** In our case study, we predict students’ grades based on hours spent studying. The analysis reveals a positive correlation, meaning that, generally, as study hours increase, grades improve. The slope of the line quantifies this relationship, showing the expected increase in grades per additional hour of study.


### Multiple Linear Regression (MLR)

Multiple Linear Regression generalizes SLR by allowing multiple independent variables to predict a single dependent variable. This approach captures more complex relationships and improves predictive accuracy by accounting for additional factors that influence the outcome.

The mathematical form is:

{{< figure src="figures/Figure 5 - Multiple Linear Regression.png" caption="Multiple Linear Regression" align="center" >}}

**Y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε**

Where:
*   **Y (Dependent Variable):** The outcome we are predicting (grades).
*   **x₁, x₂, ..., xₙ (Independent Variables):** Multiple predictors, such as hours studied and hours of sleep.
*   **β₀ (Intercept):** Value of Y when all predictors are zero.
*   **β₁, ..., βₙ (Coefficients):** Change in Y for a one-unit change in each predictor while keeping other variables constant.
*   **ε (Error Term):** Variation in Y not explained by the predictors.

**Example:** Extending our study, suppose we include both hours studied and hours of sleep as predictors for grades. MLR models how both factors jointly influence performance. The resulting regression plane in three-dimensional space illustrates how changes in these two variables affect predicted grades. By considering multiple factors, MLR provides a more accurate and realistic prediction than SLR, especially when outcomes depend on more than one variable.

## Methodology and Implementation

### Experimental Setup (Python Implementation)

To demonstrate Simple Linear Regression, a Python model was implemented using `scikit-learn` to predict **Grades Received** based on **Hours Studied**.

**Installation:**

```bash
pip install scikit-learn matplotlib
```

**Code Implementation:**

```python
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
hours_studied = np.array([1.0, 3.0, 2.3, 6.0, 1.5, 7.0, 5.0, 3.3, 4.0, 2.0, 3.0, 0.0, 5.5, 4.3]).reshape(-1, 1)
grades_received = np.array([35, 55, 42, 94, 36, 96, 90, 70, 80, 39, 50, 34, 95, 83])

# Create and fit model
model = LinearRegression()
model.fit(hours_studied, grades_received)

# Predictions
grades_predicted = model.predict(hours_studied)

# Visualization
plt.scatter(hours_studied, grades_received, color='black')
plt.plot(hours_studied, grades_predicted, color='blue', linewidth=3)
plt.xlabel('Hours Studied')
plt.ylabel('Grades Received')
plt.title('Linear Regression: Best Fit Line')
plt.show()

# Coefficients
print('Slope:', model.coef_[0])
print('Intercept:', model.intercept_)
```

### Results and Visualization

The Simple Linear Regression implementation produces a “Best Fit Line” that demonstrates a positive correlation between study time and grades. The fitted line has a slope of 11.84 and an intercept of 23.68, indicating that each additional hour studied increases the predicted grade by approximately 11.84 points.

**Output:**

{{< figure src="figures/Figure 6 - Linear Regression Plot.png" caption="Linear Regression Plot" align="center" >}}

```
Slope: 11.84
Intercept: 23.68
```

In the context of Multiple Linear Regression, visualization extends to three dimensions. The regression plane, representing the relationship among two independent variables and a dependent variable, is demonstrated in the project’s supplementary video. The algorithm iteratively updates the weights (w₁, w₂) and bias (b) to minimize the Mean Squared Error (MSE). The initial MSE of 8313.18 converges substantially by iteration 49, confirming effective parameter optimization.

{{< figure src="figures/Figure 7 - MSE Convergence Plot.png" caption="MSE Convergence Plot: Demonstrates iterative reduction in error during model training." align="center" >}}

The animation below illustrates the convergence of the Multiple Linear Regression plane in three dimensions. It demonstrates how the model iteratively adjusts the weights and bias to minimize prediction error. The accompanying plot displays the progressive reduction of the Mean Squared Error over successive iterations.

{{< figure src="figures/Figure 8 - 3D Visualization of Multiple Linear Regression.gif" caption="3D visualization of Multiple Linear Regression convergence. The regression plane adjusts iteratively to fit the data points defined by two independent variables. The side plot displays the corresponding decrease in Mean Squared Error over successive iterations, illustrating the model’s optimization process." align="center" >}}


## ML Libraries

The successful implementation of the project utilized the following libraries:

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 2: </span>
    Library/Tool Used
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center;">Tool/Library</th>
            <th style="padding: 12px; text-align: center;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Scikit-Learn</td>
            <td style="padding: 12px;">Machine learning library for regression algorithms.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Numpy</td>
            <td style="padding: 12px;">Fundamental package for numerical computations.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Matplotlib</td>
            <td style="padding: 12px;">Plotting library for visualizing the regression line.</td>
        </tr>
    </tbody>
</table>

</div>

## Model Evaluation and Assumptions

### Evaluation Metrics

The performance of a Multiple Linear Regression model is assessed using several statistical measures that quantify model fit and the relevance of individual predictors.

**R-squared (R²)**
represents the proportion of variance in the dependent variable that is explained by the set of predictors. Values lie between 0 and 1. Higher values indicate that the model accounts for a greater share of the observed variability.

**P-values**
used to evaluate the statistical significance of each coefficient. A p-value below 0.05 is commonly interpreted as evidence that the associated predictor contributes meaningfully to the model and should be retained.

### Key Assumptions

The reliability of Multiple Linear Regression depends on satisfying several core assumptions. Violations can compromise coefficient estimates and reduce the interpretability of the model.

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 3: </span>
    Key Assumptions of Multiple Linear Regression
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center;">Assumption</th>
            <th style="padding: 12px; text-align: center;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Linearity</td>
            <td style="padding: 12px;">The relationship between each predictor and the response variable is assumed to be linear.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">No Multicollinearity</td>
            <td style="padding: 12px;">Predictors should not exhibit high intercorrelation, since strong multicollinearity inflates variance and destabilizes coefficient estimates.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Homoscedasticity</td>
            <td style="padding: 12px;">Residuals should display constant variance across the range of fitted values. Unequal variance indicates heteroscedasticity and can affect inference.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Independence</td>
            <td style="padding: 12px;">Observations should be independent of one another. Dependence among data points can bias standard errors and test statistics.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold;">Normality of Residuals</td>
            <td style="padding: 12px;">Model residuals are assumed to follow a normal distribution. This assumption supports valid hypothesis testing and confidence interval construction.</td>
        </tr>
    </tbody>
</table>

</div>

## Applications of Multiple Linear Regression

Multiple Linear Regression is widely used across many fields because it evaluates the distinct effect of several predictors on a continuous outcome. Its capacity to control for overlapping influences makes it a central method in quantitative analysis.

### Finance
Multiple Linear Regression is used to model asset price behavior, estimate determinants of market returns, evaluate credit risk, and forecast macroeconomic variables. By incorporating multiple economic and firm-specific predictors, analysts can determine how each factor contributes to financial performance.

### Healthcare
Clinical researchers apply Multiple Linear Regression to quantify relationships among risk factors and patient outcomes. It is frequently used to model disease progression, estimate the probability of hospitalization or readmission, and assess treatment effectiveness while adjusting for demographic and physiological variables.

### Marketing and Consumer Analytics
In marketing, Multiple Linear Regression supports demand analysis, sales forecasting, and consumer behavior studies. Predictors such as pricing, promotional activity, demographic segments, and seasonal trends are evaluated to identify which variables exert the strongest influence on purchasing behavior or revenue patterns.

### Social Sciences and Policy Research
Researchers use Multiple Linear Regression to study outcomes shaped by multiple societal influences, including educational performance, labor market participation, and housing dynamics. The model allows for more accurate interpretation of relationships within complex social systems.

### Engineering and Environmental Sciences
Multiple Linear Regression is applied to predict system performance, estimate energy consumption, evaluate material properties, and analyze environmental indicators such as pollution levels or climate variability. These applications require simultaneous assessment of several interacting predictors.

## Conclusion

Simple Linear Regression isolates the influence of a single predictor on a response variable, offering a narrow but interpretable view of their association. Multiple Linear Regression extends this framework by estimating the independent contribution of several predictors while controlling for mutual dependencies. This broader specification yields more informative parameter estimates, yet it also demands stricter diagnostic evaluation, particularly regarding multicollinearity, model specification error, and variance inflation. A clear understanding of these distinctions is essential for selecting an analytically sound regression approach and for drawing valid inferences from empirical data.

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="Multiple%20Linear%20Regression.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

## Additional Resources

#### Project Source & Presentation Materials
Access the complete source code, presentation slides, and related machine learning materials via the repositories below:

<div style="display: flex; flex-direction: column; gap: 8px;">
  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://github.com/Amey-Thakur/MACHINE--LEARNING/blob/main/In-Class%20Presentation/PPT%20Notes.pdf" target="_blank">Presentation Notes</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/MACHINE--LEARNING/blob/main/In-Class%20Presentation/Relationship%20between%20Hours%20Studied%20and%20Grades%20Received.ipynb" target="_blank">Python Notebook (Source Code)</a>
  </div>
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/MACHINE--LEARNING" target="_blank">Machine Learning</a>
  </div>
  <div>
    <!-- Graduation Cap Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    <a href="https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING" target="_blank">MEng Computer Engineering Resources</a>
  </div>
</div>

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Multiple Linear Regression". AmeyArc (Sep 2023). https://amey-thakur.github.io/posts/2023-09-29-multiple-linear-regression/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2023mlr,
  title   = "Multiple Linear Regression",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2023",
  month   = "Sep",
  url     = "https://amey-thakur.github.io/posts/2023-09-29-multiple-linear-regression/"
}
```

## References

1. <a id="ref-1"></a> **M. Batta**, "Machine learning algorithms - a review," [https://www.researchgate.net/profile/Batta-Mahesh/publication/344717762_Machine_Learning_Algorithms_-_A_Review/links/5f8b2365299bf1b53e2d243a/Machine-Learning-Algorithms-A-Review.pdf](https://www.researchgate.net/profile/Batta-Mahesh/publication/344717762_Machine_Learning_Algorithms_-_A_Review/links/5f8b2365299bf1b53e2d243a/Machine-Learning-Algorithms-A-Review.pdf) [Accessed: Sep. 25, 2023]. DOI: [10.21275/ART20203995](https://doi.org/10.21275/ART20203995).

1. <a id="ref-2"></a> **S. I. Bangdiwala**, "Regression: Simple linear," *International Journal of Injury Control and Safety Promotion*, vol. 25, no. 1, pp. 113–115, 2018, DOI: [10.1080/17457300.2018.1426702](https://doi.org/10.1080/17457300.2018.1426702).

1. <a id="ref-3"></a> **M. Tranmer, J. Murphy, M. Elliot, and M. Pampaka**, "Multiple Linear Regression," 2nd ed., 2020. [https://hummedia.manchester.ac.uk/institutes/cmist/archive-publications/working-papers/2020/multiple-linear-regression.pdf](https://hummedia.manchester.ac.uk/institutes/cmist/archive-publications/working-papers/2020/multiple-linear-regression.pdf) [Accessed: Sep. 25, 2023].

1. <a id="ref-4"></a> **R. Goldstein**, "Regression methods in biostatistics: Linear, logistic, survival and repeated measures models," *Technometrics*, vol. 48, no. 1, pp. 149–150, 2006, DOI: [10.1198/tech.2006.s357](https://doi.org/10.1198/tech.2006.s357).

1. <a id="ref-5"></a> **M. N. Williams, C. A. G. Grajales, and D. Kurkiewicz**, "Assumptions of Multiple Regression: Correcting Two Misconceptions," *Practical Assessment, Research, and Evaluation*, vol. 18, Nov. 2019. DOI: [10.7275/55hn-wk47](https://doi.org/10.7275/55hn-wk47). [Accessed: Sep. 25, 2023].

1. <a id="ref-6"></a> **A. E. Maxwell**, "Limitations on the use of the multiple linear regression model," *British Journal of Mathematical and Statistical Psychology*, vol. 28, no. 1, pp. 51–62, 1975, DOI: [10.1111/j.2044-8317.1975.tb00547.x](https://doi.org/10.1111/j.2044-8317.1975.tb00547.x). [Accessed: Sep. 25, 2023].

1. <a id="ref-7"></a> **J. Fernando**, "R-squared: Definition, calculation formula, uses, and limitations," *Investopedia*, [https://www.investopedia.com/terms/r/r-squared.asp](https://www.investopedia.com/terms/r/r-squared.asp) [Accessed: Sep. 25, 2023].

1. <a id="ref-8"></a> **B. Beers**, "P-value: What it is, how to calculate it, and why it matters," *Investopedia*, [https://www.investopedia.com/terms/p/p-value.asp](https://www.investopedia.com/terms/p/p-value.asp) [Accessed: Sep. 25, 2023].

1. <a id="ref-9"></a> **"Multiple Linear Regression in Python - Sklearn,"** 2022, [https://youtu.be/wH_ezgftiy0](https://youtu.be/wH_ezgftiy0) [Accessed: Sep. 25, 2023].

1. <a id="ref-10"></a> **M. Ralston**, “Multiple regression,” *SAGE Publications Inc*, [https://us.sagepub.com/en-us/nam/multiple-regression/book262446](https://us.sagepub.com/en-us/nam/multiple-regression/book262446) (accessed Sep. 25, 2023).
