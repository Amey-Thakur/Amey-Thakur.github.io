---
title: "Bangalore House Price Prediction"
date: 2021-09-07T00:00:00-05:00
draft: false
author: "Amey Thakur"
summary: "Special thanks to Mega Satish for her meaningful contributions, support, and wisdom that helped shape this work. We propose to implement a house price prediction model of Bangalore, India. It’s a Machine Learning model which integrates Data Science and Web Development. We have deployed the app on the Heroku Cloud Application Platform. Housing prices fluctuate on a daily basis and are sometimes exaggerated rather than based on worth."
tags: ["AI", "Analytics", "Artificial Intelligence", "Bangalore House Price Prediction", "Bangalore Real Estate", "Data Analytics", "Data Cleaning", "Data Science", "Data Science Projects", "Data Visualization", "Decision Tree Regression", "Deployment", "EDA", "End-to-End Project", "Exploratory Data Analysis", "Feature Engineering", "Flask", "Heroku", "House Price Prediction", "Kaggle", "Lasso Regression", "Linear Regression", "Machine Learning", "Machine Learning Projects", "Matplotlib", "Model Building", "NumPy", "Pandas", "Predictive Modeling", "PropTech", "Property Valuation", "Python", "Real Estate", "Real Estate Analytics", "Regression", "Scikit-Learn", "Supervised Learning", "Web Application"]
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

We propose to implement a house price prediction model of Bangalore, India. It’s a Machine Learning model which integrates Data Science and Web Development. We have deployed the app on the Heroku Cloud Application Platform. Housing prices fluctuate on a daily basis and are sometimes exaggerated rather than based on worth. The major focus of this project is on predicting home prices using genuine factors. Here, we intend to base an evaluation on every basic criterion that is taken into account when establishing the pricing. The goal of this project is to learn Python and get experience in Data Analytics, Machine Learning, and AI.

---

## Introduction

### Context
This project was made because we were intrigued and we wanted to gain hands-on experience with the Machine Learning Project.

### Motivation
We are highly interested in anything related to Machine Learning, the independent project provided us with the opportunity to study and reaffirm our passion for this subject. The capacity to generate guesses, forecasts, and offer machines the ability to learn on their own is both powerful and infinite in terms of application possibilities. Machine Learning may be applied in finance, medicine, and virtually any other field. That is why we opted to base our idea on Machine Learning.

### Objective
As a first project, we intended to make it as instructional as possible by tackling each stage of the machine learning process and attempting to comprehend it well. We have picked Bangalore Real Estate Prediction as a method, which is known as a "toy issue," identifying problems that are not of immediate scientific relevance but are helpful to demonstrate and practice. The objective was to forecast the price of a specific apartment based on market pricing while accounting for various "features" that would be established in the following sections.

---

## Literature Survey

Real Estate Property is not only a person's primary desire, but it also reflects a person's wealth and prestige in today's society. Real estate investment typically appears to be lucrative since property values do not drop in a choppy fashion. Changes in the value of the real estate will have an impact on many home investors, bankers, policymakers, and others. Real estate investing appears to be a tempting option for investors. As a result, anticipating the important estate price is an essential economic indicator. According to the 2011 census, the Asian country ranks second in the world in terms of the number of households, with a total of 24.67 crores. However, previous recessions have demonstrated that real estate costs cannot be seen. The expenses of significant estate property are linked to the state's economic situation. Regardless, we don't have accurate standardized approaches to live the significant estate property values.

First, we looked at different articles and discussions about machine learning for housing price prediction. The title of the article is house price prediction, and it is based on machine learning and neural networks. The publication's description is minimal error and the highest accuracy. The aforementioned title of the paper is Hedonic models based on price data from Belfast infer that submarkets and residential valuation this model is used to identify over a larger spatial scale and implications for the evaluation process related to the selection of comparable evidence and the quality of variables that the values may require. Understanding current developments in house prices and homeownership are the subject of the study. In this article, they utilized a feedback mechanism or social pandemic that fosters a perception of property as an essential market investment.

---

## Methodology

### Data Collection
The statistics were gathered from Bangalore home prices. The information includes many variables such as area type, availability, location, BHK, society, total square feet, bathrooms, and balconies.

### Linear Regression
Linear regression is a supervised learning technique. It is responsible for predicting the value of a dependent variable (Y) based on a given independent variable (X). It is the connection between the input (X) and the output (Y). It is one of the most well-known and well-understood machine learning algorithms. Simple linear regression, ordinary least squares, Gradient Descent, and Regularization are the linear regression models.

### Decision Tree Regression
It is an object that trains a tree-structured model to predict data in the future in order to provide meaningful continuous output. The core principles of decision trees, Maximizing Information Gain, Classification trees, and Regression trees are the processes involved in decision tree regression. The essential notion of decision trees is that they are built via recursive partitioning. Each node can be divided into child nodes, beginning with the root node, which is known as the parent node. These nodes have the potential to become the parent nodes of their resulting offspring nodes. The nodes at the informative features are specified as the maximizing information gain, to establish an objective function that is to optimize the tree learning method.

### Classification Trees
Classification trees are used to forecast the object into classes of a categorical dependent variable based on one or more predictor variables.

### Regression Trees
It supports both continuous and categorical input variables. Regression trees are regarded as research with various machine algorithms for the regression issue, with the Decision Tree approach providing the lowest loss. The R-Squared value for the Decision Tree is 0.998, indicating that it is an excellent model. The Decision Tree was used to complete the web development.

### Support Vector Regression
Supervised learning is linked with learning algorithms that examine data for classification and regression analysis.

### Random Forest Regression
It is an essential learning approach for classification and regression to create a large number of decision trees. Preliminaries of decision trees are common approaches for a variety of machine learning problems. Tree learning is required for serving n off the self-produce for data mining since it is invariant despite scaling and several other changes. The trees are grown very deep in order to learn a high regular pattern. Random forest is a method of averaging several deep decision trees trained on various portions of the same training set. This comes at the price of a slight increase in bias and some interoperability.

---

## Project

### Problem Statement
Create a model to estimate the price of houses in Bengaluru and host it on Heroku.

### Data
The data is the most important aspect of a machine learning assignment, to which special attention should be paid. Indeed, the data will heavily affect the findings depending on where we found them, how they are presented, if they are consistent, if there is an outlier, and so on. Many questions must be addressed at this stage to ensure that the learning algorithm is efficient and correct.
To obtain, clean, and convert the data, many sub steps are required. We will go through these steps to understand how they've been used in my project and why they're helpful for the machine learning section.

### Dataset
Dataset: [https://www.kaggle.com/ameythakur20/bangalore-house-prices](https://www.kaggle.com/ameythakur20/bangalore-house-prices)

### Model
Model: [https://www.kaggle.com/ameythakur20/bangalore-house-price-prediction-model](https://www.kaggle.com/ameythakur20/bangalore-house-price-prediction-model)

### Project Architecture

{{< figure src="Bangalore House Price Prediction/figures/Figure (1) Architecture of the Application.png" caption="Architecture of the Application" align="center" >}}

### Data Science
The first stage is standard data science work, in which we take a data set named ‘Bengaluru House pricing data' from Kaggle. We will do significant data cleaning on it to guarantee that it provides reliable predictions throughout prediction. This Jupyter notebook, ‘Bangalore-House-Price-Prediction-Model.ipynb,' is where we do all of our data science work. Because the Jupyter notebook is self-explanatory, we will only touch on the principles that we have implemented briefly. In terms of data cleansing, our dataset needs a significant amount of effort. In fact, 70% of the notebook is dedicated to data cleaning, in which we eliminate empty rows and remove superfluous columns that will not aid in prediction.
The process of obtaining valuable and significant information from a dataset that will contribute the most to a successful prediction is the next stage.
The final stage is to deal with outliers. Outliers are abnormalities that do massive damage to data and prediction. There is a lot to comprehend conceptually from the dataset in order to discover and eliminate these outliers.
Finally, the original dataset of over 13000 rows and 9 columns is reduced to about 7000 rows and 5 columns.

### Machine Learning
The resulting data is fed into a machine learning model. To find the optimal procedure and parameters for the model, we will mostly employ K-fold Cross-Validation and the GridSearchCV approach.
It turns out that the linear regression model produces the best results for our data, with a score of more than 80%, which is not terrible.
Now, we need to export our model as a pickle file (Bengaluru_House_Data.pickle), which transforms Python objects into a character stream. Also, in order to interact with the locations(columns) from the frontend, we must export them into a JSON (columns.json) file.

### Frontend
The front end is built up of straightforward HTML. To receive an estimated pricing, the user may fill-up the form with the number of square feet, BHK, bathrooms, and location and click the ‘ESTIMATE PRICE' button. We have used Flask Server and configured it in python. It takes the form data entered by the user and executes the function, which employs the prediction model to calculate the projected price in lakhs of rupees (1 lakh = 100000).

---

## Experimental Setup

### Steps to Create Model

1. **Import Libraries**

   We import the necessary libraries for data manipulation, mathematical operations, and plotting.

   **Input:**
   ```python
   import pandas as pd
   import numpy as np
   from matplotlib import pyplot as plt
   import matplotlib
   %matplotlib inline
   matplotlib.rcParams["figure.figsize"] = (20,10)
   ```

2. **Load Dataset**

   Load the CSV file into a Pandas DataFrame.

   **Input:**
   ```python
   df1 = pd.read_csv("/kaggle/input/bangalore-house-prices/bengaluru_house_prices.csv")
   print(df1.head())
   ```

   **Output:**
   ```
       area_type   availability                  location       size  \
   0  Super built-up  Area         19-Dec  Electronic City Phase II      2 BHK
   1            Plot  Area  Ready To Move          Chikka Tirupathi  4 Bedroom
   2        Built-up  Area  Ready To Move               Uttarahalli      3 BHK
   3  Super built-up  Area  Ready To Move        Lingadheeranahalli      3 BHK
   4  Super built-up  Area  Ready To Move                  Kothanur      2 BHK

      society total_sqft  bath  balcony   price
   0  Coomee        1056   2.0      1.0   39.07
   1  Theanmp       2600   5.0      3.0  120.00
   2      NaN       1440   2.0      3.0   62.00
   3  Soiewre       1521   3.0      1.0   95.00
   4      NaN       1200   2.0      1.0   51.00
   ```

3. **Exploratory Data Analysis**

   Understand the data structure, shape, and count of unique values.

   **Input:**
   ```python
   print("Shape:", df1.shape)
   print("Columns:", df1.columns)
   print(df1.groupby('area_type')['area_type'].agg('count'))
   ```

   **Output:**
   ```
   Shape: (13320, 9)
   Columns: Index(['area_type', 'availability', 'location', 'size', 'society',
          'total_sqft', 'bath', 'balcony', 'price'],
         dtype='object')
   area_type
   Built-up  Area          2418
   Carpet  Area              87
   Plot  Area              2025
   Super built-up  Area    8790
   Name: area_type, dtype: int64
   ```

4. **Data Cleaning**

   Drop unnecessary columns and handle missing values. We also fix the format of the size and total_sqft columns.

   **Input:**
   ```python
   # Drop unnecessary columns
   df2 = df1.drop(['area_type','society','balcony','availability'], axis='columns')

   # Drop missing values AND create a fresh copy to avoid SettingWithCopyWarning
   df3 = df2.dropna().copy()

   # Fix 'size' column (e.g., convert "2 BHK" to 2)
   # Now this line will work without warnings because df3 is an independent copy
   df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))

   # Fix 'total_sqft' column (convert ranges like "1133 - 1384" to average)
   def convert_sqft_to_num(x):
       tokens = x.split('-')
       if len(tokens) == 2:
           return (float(tokens[0]) + float(tokens[1])) / 2
       try:
           return float(x)
       except:
           return None

   df4 = df3.copy()
   df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_num)
   df4 = df4.dropna()
   ```

5. **Feature Engineering**

   Create a new feature price_per_sqft which helps in outlier detection later.

   **Input:**
   ```python
   df5 = df4.copy()
   df5['price_per_sqft'] = df5['price'] * 100000 / df5['total_sqft']
   print(df5.head())
   ```

   **Output:**
   ```
       location       size  total_sqft  bath   price  bhk  \
   0  Electronic City Phase II      2 BHK      1056.0   2.0   39.07    2
   1          Chikka Tirupathi  4 Bedroom      2600.0   5.0  120.00    4
   2               Uttarahalli      3 BHK      1440.0   2.0   62.00    3
   3        Lingadheeranahalli      3 BHK      1521.0   3.0   95.00    3
   4                  Kothanur      2 BHK      1200.0   2.0   51.00    2

      price_per_sqft
   0     3699.810606
   1     4615.384615
   2     4305.555556
   3     6245.890861
   4     4250.000000
   ```

6. **Dimensionality Reductions**

   Group locations with very few data points (less than 10) into a single category called "other" to reduce the number of columns when we do One Hot Encoding.

   **Input:**
   ```python
   df5.location = df5.location.apply(lambda x: x.strip())
   location_stats = df5.groupby('location')['location'].agg('count').sort_values(ascending=False)

   location_stats_less_than_10 = location_stats[location_stats<=10]

   df5.location = df5.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)
   print("Total unique locations:", len(df5.location.unique()))
   ```

   **Output:**
   ```
   Total unique locations: 241
   ```

7. **Outlier Removal using Business Logic**

   Remove properties where the square footage per bedroom is suspiciously low (less than 300 sqft per bedroom).

   **Input:**
   ```python
   df6 = df5[~(df5.total_sqft/df5.bhk < 300)]
   print("Shape after business logic removal:", df6.shape)
   ```

   **Output:**
   ```
   Shape after business logic removal: (12456, 7)
   ```

8. **Outlier Removal using Standard Deviation & Mean**

   We remove properties where the price per sqft is extremely high or low compared to other properties in the same location (using Mean and Standard Deviation). We also remove 2 BHK apartments that are more expensive than 3 BHK apartments in the same area.

   **Input:**
   ```python
   # Filter by Price Per Sqft (Mean +/- 1 Std Dev)
   def remove_pps_outliers(df):
       df_out = pd.DataFrame()
       for key, subdf in df.groupby('location'):
           m = np.mean(subdf.price_per_sqft)
           st = np.std(subdf.price_per_sqft)
           reduced_df = subdf[(subdf.price_per_sqft>(m-st)) & (subdf.price_per_sqft<=(m+st))]
           df_out = pd.concat([df_out,reduced_df],ignore_index=True)
       return df_out

   df7 = remove_pps_outliers(df6)

   # Filter by BHK Price (Remove 2 BHK > 3 BHK price)
   def remove_bhk_outliers(df):
       exclude_indices = np.array([])
       for location, location_df in df.groupby('location'):
           bhk_stats = {}
           for bhk, bhk_df in location_df.groupby('bhk'):
               bhk_stats[bhk] = {
                   'mean': np.mean(bhk_df.price_per_sqft),
                   'std': np.std(bhk_df.price_per_sqft),
                   'count': bhk_df.shape[0]
               }
           for bhk, bhk_df in location_df.groupby('bhk'):
               stats = bhk_stats.get(bhk-1)
               if stats and stats['count']>5:
                   exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
       return df.drop(exclude_indices,axis='index')

   df8 = remove_bhk_outliers(df7)
   print("Shape after all outlier removal:", df8.shape)
   ```

   **Output:**
   ```
   Shape after all outlier removal: (7317, 7)
   ```

9. **Data Visualization**

   Visualize the data to see the spread of 2 BHK vs 3 BHK prices and the distribution of Price Per Sqft.

   **Input:**
   ```python
   def plot_scatter_chart(df,location):
       bhk2 = df[(df.location==location) & (df.bhk==2)]
       bhk3 = df[(df.location==location) & (df.bhk==3)]
       matplotlib.rcParams['figure.figsize'] = (15,10)
       plt.scatter(bhk2.total_sqft,bhk2.price,color='blue',label='2 BHK', s=50)
       plt.scatter(bhk3.total_sqft,bhk3.price,marker='+', color='green',label='3 BHK', s=50)
       plt.xlabel("Total Square Feet Area")
       plt.ylabel("Price (Lakh Indian Rupees)")
       plt.title(location)
       plt.legend()

   # Scatter Plot
   plot_scatter_chart(df8,"Rajaji Nagar")

   # Histogram
   import matplotlib
   matplotlib.rcParams["figure.figsize"] = (20,10)
   plt.hist(df8.price_per_sqft,rwidth=0.8)
   plt.xlabel("Price Per Square Feet")
   plt.ylabel("Count")
   plt.show()
   ```

   {{< figure src="Bangalore House Price Prediction/figures/Figure (5) Data Visualization.png" caption="Data Visualization" align="center" >}}

10. **Building a Model**

    Prepare the data (One Hot Encoding), split into training and testing sets, and train a Linear Regression model.

    **Input:**
    ```python
    # Drop helper columns and filter outliers one last time
    df9 = df8[df8.price_per_sqft<10000]
    df10 = df9.drop(['price_per_sqft'],axis='columns')

    # One Hot Encoding
    dummies = pd.get_dummies(df10.location)
    df11 = pd.concat([df10,dummies.drop('other',axis='columns')],axis='columns')

    # FIX: Drop both 'location' AND 'size' columns
    df12 = df11.drop(['location', 'size'], axis='columns')

    # Define X and y
    X = df12.drop('price',axis='columns')
    y = df12.price

    # Train Test Split
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=10)

    # Train Linear Regression
    from sklearn.linear_model import LinearRegression
    lr_clf = LinearRegression()
    lr_clf.fit(X_train,y_train)
    print("Model Score:", lr_clf.score(X_test,y_test))
    ```

    **Output:**
    ```
    Model Score: 0.8980700692588083
    ```

11. **Test the Model for few properties**

    Create a helper function to predict prices for arbitrary locations and features.

    **Input:**
    ```python
    def predict_price(location, sqft, bath, bhk):
        # Find the index of the location column
        # If location is not found (e.g., it's 'other'), this block is skipped safely
        try:
            loc_index = np.where(X.columns == location)[0][0]
        except IndexError:
            loc_index = -1

        # Create an array of zeros with the same number of columns as X
        x = np.zeros(len(X.columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk

        # Set the location column to 1 if it exists
        if loc_index >= 0:
            x[loc_index] = 1

        # FIX: Create a DataFrame with column names to match training data
        x_df = pd.DataFrame([x], columns=X.columns)

        return lr_clf.predict(x_df)[0]

    # Test again
    print("Prediction 1:", predict_price('1st Phase JP Nagar', 1000, 2, 2))
    print("Prediction 2:", predict_price('1st Phase JP Nagar', 1000, 3, 3))
    print("Prediction 3:", predict_price('Indira Nagar', 1000, 2, 2))
    ```

    **Output:**
    ```
    Prediction 1: 84.25840465992951
    Prediction 2: 84.87720242072712
    Prediction 3: 85.22387691807114
    ```

12. **Export the tested model to a pickle file**

    Save the model and column information for use in deployment.

    **Input:**
    ```python
    import pickle
    with open('banglore_home_prices_model.pickle','wb') as f:
        pickle.dump(lr_clf,f)

    import json
    columns = {
        'data_columns' : [col.lower() for col in X.columns]
    }
    with open("columns.json","w") as f:
        f.write(json.dumps(columns))
    print("Export complete.")
    ```

    **Output:**
    ```
    Export complete.
    ```

    {{< figure src="Bangalore House Price Prediction/figures/Figure (6) Output Data.png" caption="Output Data" align="center" >}}

### Prerequisites
Before running these commands, ensure you have the following files in your project folder:

*   **app.py**: Your Python Flask/Streamlit application file.
*   **requirements.txt**: A list of libraries your app needs (e.g., scikit-learn, pandas, flask, gunicorn).
*   **Procfile**: A file named exactly `Procfile` (no extension) containing the command to start your app (e.g., `web: gunicorn app:app`).

### Steps to Deploy Model on Heroku

1.  **Login to Heroku**

    Connect your terminal to your Heroku account. It will open a browser window for you to log in.

    ```bash
    heroku login
    ```

2.  **Initialize Git Repository**

    Initialize a new empty Git repository inside your project folder.

    ```bash
    git init
    ```

3.  **Create Heroku App**

    Create a new application space on Heroku.
    > **Note:** The repository name `bangalorehousepriceprediction` is already taken by me. Please add your name or a numeric suffix to make it unique (for example, `bangalore-price-pred-amey`).

    ```bash
    heroku create bangalorehousepriceprediction
    ```

4.  **Add Files to Git**

    Stage all your files (model, python scripts, requirements) for the commit.

    ```bash
    git add .
    ```

5.  **Commit Changes**

    Save your changes to the local git repository with a message.

    ```bash
    git commit -am "initial commit"
    ```

6.  **Push to Heroku**

    Upload your code to Heroku's remote server. This triggers the building and deployment process.

    ```bash
    git push heroku master
    ```
    *(If you are using a newer version of Git where the default branch is `main` instead of `master`, use `git push heroku main`)*

### Tools used

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 1: </span>
    Tools Used
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center;">Tool</th>
            <th style="padding: 12px; text-align: center;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Anaconda</td>
            <td style="padding: 12px; vertical-align: top;">Python distribution for managing data science libraries and environments.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Jupyter Notebook</td>
            <td style="padding: 12px; vertical-align: top;">Interactive environment for experimentation, analysis, and model development.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Google Colab</td>
            <td style="padding: 12px; vertical-align: top;">Cloud-based notebooks for training and testing with scalable compute.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Flask</td>
            <td style="padding: 12px; vertical-align: top;">Lightweight web framework used to build the backend server.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Heroku</td>
            <td style="padding: 12px; vertical-align: top;">Platform-as-a-Service (PaaS) for application deployment.</td>
        </tr>
    </tbody>
</table>

</div>

### Technologies used

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 2: </span>
    Technologies Used
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center;">Technology</th>
            <th style="padding: 12px; text-align: center;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Python</td>
            <td style="padding: 12px; vertical-align: top;">Core language for model development and backend logic.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">HTML</td>
            <td style="padding: 12px; vertical-align: top;">Markup for structuring the web interface.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">CSS</td>
            <td style="padding: 12px; vertical-align: top;">Styling and layout of the frontend.</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; font-weight: bold; vertical-align: top;">Bootstrap</td>
            <td style="padding: 12px; vertical-align: top;">Framework for responsive and consistent UI design.</td>
        </tr>
    </tbody>
</table>

</div>

---

## Results

{{< figure src="Bangalore House Price Prediction/figures/Figure (2) User Interface.png" caption="User Interface" align="center" >}}

{{< figure src="Bangalore House Price Prediction/figures/Figure (3) Estimate Price.png" caption="Estimate Price" align="center" >}}

{{< figure src="Bangalore House Price Prediction/figures/Figure (4) Predict.png" caption="Predict" align="center" >}}

Heroku Web Application - [https://bhpp.herokuapp.com](https://bhpp.herokuapp.com),  [https://bangalorehousepriceprediction.herokuapp.com](https://bangalorehousepriceprediction.herokuapp.com)

---

## YouTube Demonstration

{{< youtube HaiXYHBPHVg >}}

---

## Additional Resources

### Project Source, Research & Demonstrations
Explore the complete source code, Kaggle notebooks, research publications, and video demonstrations for the Bangalore House Price Prediction project via the resources below:
<div style="display: flex; flex-direction: column; gap: 10px;">

  <div>
    <!-- Kaggle Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;">
        <path transform="matrix(.527027 0 0 .527027 -30.632288 -22.45559)"
            d="M105.75 102.968c-.06.238-.298.357-.713.357H97.1c-.477 0-.89-.208-1.248-.625L82.746 86.028l-3.655 3.477v12.93c0 .595-.298.892-.892.892h-6.152c-.595 0-.892-.297-.892-.892V43.5c0-.593.297-.89.892-.89H78.2c.594 0 .892.298.892.89v36.288l15.692-15.87c.416-.415.832-.624 1.248-.624h8.204c.356 0 .593.15.713.445.12.357.09.624-.09.803L88.274 80.588l17.297 21.488c.237.238.297.535.18.892" />
    </svg>
    <a href="https://www.kaggle.com/code/ameythakur20/bangalore-house-price-prediction-model" target="_blank">Bangalore House Price Prediction Model (Original)</a>
  </div>

  <div>
    <!-- Kaggle Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;">
        <path transform="matrix(.527027 0 0 .527027 -30.632288 -22.45559)"
            d="M105.75 102.968c-.06.238-.298.357-.713.357H97.1c-.477 0-.89-.208-1.248-.625L82.746 86.028l-3.655 3.477v12.93c0 .595-.298.892-.892.892h-6.152c-.595 0-.892-.297-.892-.892V43.5c0-.593.297-.89.892-.89H78.2c.594 0 .892.298.892.89v36.288l15.692-15.87c.416-.415.832-.624 1.248-.624h8.204c.356 0 .593.15.713.445.12.357.09.624-.09.803L88.274 80.588l17.297 21.488c.237.238.297.535.18.892" />
    </svg>
    <a href="https://www.kaggle.com/code/ameythakur20/bangalore-house-price-prediction" target="_blank">Bangalore House Price Prediction Model</a>
  </div>

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/BANGALORE-HOUSE-PRICE-PREDICTION" target="_blank">Bangalore House Price Prediction Repository (Amey Thakur)</a>
  </div>

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/msatmod/Bangalore-House-Price-Prediction" target="_blank">BHPP Repository (Mega Satish) - Special thanks to Mega for her significant help</a>
  </div>

  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/HaiXYHBPHVg" target="_blank">YouTube Demonstration</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://www.irjet.net/archives/V8/i9/IRJET-V8I934.pdf" target="_blank">Full Paper (IRJET)</a>
  </div>

  <div>
    <!-- ResearchGate Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;">
        <path d="M19.586 0c-.818 0-1.508.19-2.073.565-.563.377-.97.936-1.213 1.68a3.193 3.193 0 0 0-.112.437 8.365 8.365 0 0 0-.078.53 9 9 0 0 0-.05.727c-.01.282-.013.621-.013 1.016a31.121 31.123 0 0 0 .014 1.017 9 9 0 0 0 .05.727 7.946 7.946 0 0 0 .077.53h-.005a3.334 3.334 0 0 0 .113.438c.245.743.65 1.303 1.214 1.68.565.376 1.256.564 2.075.564.8 0 1.536-.213 2.105-.603.57-.39.94-.916 1.175-1.65.076-.235.135-.558.177-.93a10.9 10.9 0 0 0 .043-1.207v-.82c0-.095-.047-.142-.14-.142h-3.064c-.094 0-.14.047-.14.141v.956c0 .094.046.14.14.14h1.666c.056 0 .084.03.084.086 0 .36 0 .62-.036.865-.038.244-.1.447-.147.606-.108.385-.348.664-.638.876-.29.212-.738.35-1.227.35-.545 0-.901-.15-1.21-.353-.306-.203-.517-.454-.67-.915a3.136 3.136 0 0 1-.147-.762 17.366 17.367 0 0 1-.034-.656c-.01-.26-.014-.572-.014-.939a26.401 26.403 0 0 1 .014-.938 15.821 15.822 0 0 1 .035-.656 3.19 3.19 0 0 1 .148-.76 1.89 1.89 0 0 1 .742-1.01c.344-.244.593-.352 1.137-.352.508 0 .815.096 1.144.303.33.207.528.492.764.925.047.094.111.118.198.07l1.044-.43c.075-.048.09-.115.042-.199a3.549 3.549 0 0 0-.466-.742 3 3 0 0 0-.679-.607 3.313 3.313 0 0 0-.903-.41A4.068 4.068 0 0 0 19.586 0zM8.217 5.836c-1.69 0-3.036.086-4.297.086-1.146 0-2.291 0-3.007-.029v.831l1.088.2c.744.144 1.174.488 1.174 2.264v11.288c0 1.777-.43 2.12-1.174 2.263l-1.088.2v.832c.773-.029 2.12-.086 3.465-.086 1.29 0 2.951.057 3.667.086v-.831l-1.49-.2c-.773-.115-1.174-.487-1.174-2.264v-4.784c.688.057 1.29.057 2.206.057 1.748 3.123 3.41 5.472 4.355 6.56.86 1.032 2.177 1.691 3.839 1.691.487 0 1.003-.086 1.318-.23v-.744c-1.031 0-2.063-.716-2.808-1.518-1.26-1.376-2.95-3.582-4.355-6.074 2.32-.545 4.04-2.722 4.04-4.9 0-3.208-2.492-4.698-5.758-4.698zm-.515 1.29c2.406 0 3.839 1.26 3.839 3.552 0 2.263-1.547 3.782-4.097 3.782-.974 0-1.404-.03-2.063-.086v-7.19c.66-.059 1.547-.059 2.32-.059z"/>
    </svg>
    <a href="https://www.researchgate.net/publication/354403038_Bangalore_House_Price_Prediction" target="_blank">ResearchGate Publication</a>
  </div>

  <div>
    <!-- viXra Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 8px;"><title>viXra</title><path d="M0 0h3v3h3v3h3v3h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3zM21 0h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3zM6 15h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3z" /></svg>
    <a href="https://vixra.org/pdf/2110.0026v1.pdf" target="_blank">viXra Preprint</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Bangalore House Price Prediction". AmeyArc (Sep 2021). https://amey-thakur.github.io/posts/2021-09-07-bangalore-house-price-prediction/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2021houseprice,
  title   = "Bangalore House Price Prediction",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Sep",
  url     = "https://amey-thakur.github.io/posts/2021-09-07-bangalore-house-price-prediction/"
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur</b>, “Bangalore House Price Prediction Model,” <i>Kaggle</i>, 2021, <a href="https://www.kaggle.com/code/ameythakur20/bangalore-house-price-prediction-model">https://www.kaggle.com/code/ameythakur20/bangalore-house-price-prediction-model</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>Heroku</b>, “Documentation,” <i>Heroku Dev Center</i>, <a href="https://devcenter.heroku.com/">https://devcenter.heroku.com/</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>M. Satish</b>, “Bangalore House Price Prediction,” <i>GitHub Repository</i>, <a href="https://github.com/msatmod/Bangalore-House-Price-Prediction">https://github.com/msatmod/Bangalore-House-Price-Prediction</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>A. Thakur</b>, “Bangalore House Price Prediction,” <i>GitHub Repository</i>, <a href="https://github.com/Amey-Thakur/BANGALORE-HOUSE-PRICE-PREDICTION">https://github.com/Amey-Thakur/BANGALORE-HOUSE-PRICE-PREDICTION</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>Python</b>, “Pickle — Python object serialization,” <i>Python 3.10.0 Documentation</i>, <a href="https://docs.python.org/3/library/pickle.html">https://docs.python.org/3/library/pickle.html</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>A. Varma, A. Sarma, S. Doshi and R. Nair</b>, "House Price Prediction Using Machine Learning and Neural Networks," <i>2018 Second International Conference on Inventive Communication and Computational Technologies (ICICCT)</i>, 2018, pp. 1936-1939, DOI: <a href="https://doi.org/10.1109/ICICCT.2018.8473231">10.1109/ICICCT.2018.8473231</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>P. Furia and A. Khandare</b>, "Real Estate Price Prediction Using Machine Learning Algorithm," <i>e-Conference on Data Science and Intelligent Computing</i>, 2020, <a href="https://doi.org/10.1002/9781119792437.ch2">https://doi.org/10.1002/9781119792437.ch2</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>C. Musciano and B. Kennedy</b>, <i>HTML & XHTML: The Definitive Guide</i>. "O'Reilly Media, Inc.", 2002, ISBN: 978-0596527327, <a href="https://www.oreilly.com/library/view/html-xhtml/0596527322/">https://www.oreilly.com/library/view/html-xhtml/0596527322/</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>S. Aggarwal</b>, <i>Flask Framework Cookbook</i>. Packt Publishing Ltd, 2014, ISBN: 978-1783983407, <a href="https://www.packtpub.com/product/flask-framework-cookbook/9781783983407">https://www.packtpub.com/product/flask-framework-cookbook/9781783983407</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>M. Grinberg</b>, <i>Flask Web Development: Developing Web Applications with Python</i>. "O'Reilly Media, Inc.", 2018, ISBN: 978-1491991725, <a href="https://www.oreilly.com/library/view/flask-web-development/9781491991725/">https://www.oreilly.com/library/view/flask-web-development/9781491991725/</a> [Accessed: Sep. 07, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>N. Middleton and R. Schneeman</b>, <i>Heroku: Up and Running: Effortless Application Deployment and Scaling</i>. "O'Reilly Media, Inc.", 2013, ISBN: 978-1449341398, <a href="https://www.oreilly.com/library/view/heroku-up-and/9781449341381/">https://www.oreilly.com/library/view/heroku-up-and/9781449341381/</a> [Accessed: Sep. 07, 2021].</span>
</div>

</div>
