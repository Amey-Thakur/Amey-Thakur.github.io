TECHNOCOLABS DATA SCIENCE INTERNSHIP

Project Report

Title: Optimizing Stock Trading Strategy With Reinforcement Learning


![Image](figures/image_1.png)
Submitted By [Team B] Anweasha Saha Roshni Jagadeesh T S Prakash

Karina Farheen Shareef Amey Mahendra Thakur

E. Sailesh

Under the Guidance of Deepthika Shiwani Muralikrishnan

## AIM
The main emphasis and objective of our project is to analyse given raw data and do exploratory data analysis in order to fully comprehend and identify patterns. Then, using a Neural Network approach, construct a model and train it to get the desired outcomes. Finally, it will be deployed as a web application.

## ABSTRACT
We propose to determine a single exchange-traded fund (SPY) investing strategy that will maximise our total wealth. We compare our findings to the tried-and-true “buy-and-hold” and Moving average convergence divergence (MACD) strategies. It’s a Machine Learning model which integrates Data Science and Web Development. We have deployed the app on the Heroku Cloud Application Platform. Here, we intend to base an evaluation on every basic criterion that is taken into account when establishing the pricing. As mentioned, we intend to forecast future price fluctuations for a specific stock. Prices from previous days, as well as financial media stories connected to the firm of interest, are used to create these forecasts. Reinforcement learning is all about taking the right steps to maximise your reward in a given situation. It is used by a variety of software and computers to determine the best feasible action or path in a given situation. The Reinforcement Machine Learning model is employed in this work to forecast the closure price using past data. We develop a predictor for multiple firms using these trained models that forecasts the every day close stock prices. By providing inputs such as open, high, and low prices, stock volume, and the latest events about each firm, this predictor may be used to determine the price at which the stock value will close for a certain day. The goal of this project is to learn and get hands-on experience in Data Analytics and Machine Learning.

## INTRODUCTION
We've always been captivated by the stock market's seeming unpredictability. There are hundreds of stocks to select from, and day traders can trade almost any of them. So, for a day trader, deciding what to trade is the first and most important step. The following stage is to come up with some ways to benefit from the trading opportunity (one stock, several stocks, exchange-traded funds, ETFs, etc.). Intraday

traders use a number of ways to profit from price movements in a particular asset. Day traders should look for equities with plenty of liquidity, moderate to high volatility, and a large number of followers. Isolating the present market trend from any surrounding noise and then capitalising on that trend is the key to finding the appropriate stocks for intraday trading.

This has traditionally been done in conjunction with the trade plan and current events. Various research techniques have been explored to automate this laborious procedure since the emergence of Data Science and Machine Learning. This automated trading method will assist in providing recommendations at the appropriate moment and with more accurate estimates. Mutual funds and hedge funds would benefit greatly from an automated trading approach that maximises profits. The type of profitable returns that may be expected will be accompanied by some risk. It's difficult to come up with a lucrative automated trading technique.

Every human being aspires to make as much money as possible in the stock market. It's critical to devise a well-balanced, low-risk plan that will benefit the majority of individuals. One such technique proposes the use of reinforcement learning agents to generate automated trading strategies based on previous data. This project was made because we were intrigued and we wanted to gain hands-on experience with the Machine Learning Project.

## REINFORCEMENT LEARNING
Machine learning models are taught to make a series of judgments via reinforcement learning. In an unpredictable and potentially complex environment, the agent must learn to attain a goal. Artificial intelligence is put in a game-like environment in reinforcement learning. To find a solution to the problem, the computer uses trial and error. Artificial intelligence is given either rewards or penalties for the acts it takes in order to get it to accomplish what the programmer desires. Its purpose is to increase the total prize as much as possible.

Despite the fact that the designer establishes the reward policy–that is, the game's rules–he provides the model with no clues or ideas for how to solve the game.

Starting with completely random trials and progressing to sophisticated tactics and superhuman skills, it's up to the model to find out how to do the task in order to maximise the reward.

In reinforcement learning, developers use a framework that rewards desired actions while penalising negative ones. To motivate the agent, this strategy assigns positive values to desired acts and negative values to undesirable behaviours. To obtain an ideal solution, the agent is programmed to seek long-term and greatest overall return.

These long-term objectives keep the agent from stagnating on smaller objectives. The agent eventually learns to ignore the unpleasant and focus on the good. This technique of learning has been used in artificial intelligence (AI) to drive unsupervised machine learning using incentives and punishments.

In simple terms, You let the dog do whatever it wants and then whenever it behaves well you go, “Good dog” and when it misbehaves you go “Bad Dog!” and then over time the dog learns to do more of the good dog things and fewer of the bad dog things.


![Image](figures/image_2.png)
Trading is a never-ending process with no conclusion in sight. Because we don't have comprehensive information about the traders in the market, trading is likewise a stochastic Markov Decision Process. We employ model-free reinforcement learning, also known as Q-Learning because we don't know the reward function or transition probability.

### Markov Decision Process (MDP):
It is a mathematical framework used for modelling decision-making problems where the outcomes are partly random and partly controllable.

A model of anticipating outcomes is the Markov decision process. The model, like a Markov chain, tries to predict a result based solely on the present state's information. The Markov decision process, on the other hand, takes into account the features of actions and motivations. The decision-maker may choose an action accessible in the current state at each phase of the process, causing the model to advance to the next step and rewarding the decision-maker.

At each step during the process, the decision-maker may choose to take any action available in the current state, resulting in the model moving to the next step and offering the decision-maker a reward.


![Image](figures/image_3.png)
An optimization problem may be given to a machine learning algorithm. The programme will use reinforcement learning to try to optimise the behaviours made inside a given environment in order to maximise the potential reward. Reinforcement learning employs Markov decision processes to establish an ideal balance of exploration and exploitation, whereas supervised learning approaches need accurate input/output pairings to construct a model. When the probability and rewards of a result are undefined or unknown, machine learning may employ reinforcement learning through the Markov decision process.

Terminologies:

Agent - An RL agent is a machine that we're teaching to make good judgments. For instance, a robot is being taught how to navigate a house without colliding.

Environment - The agent's environment is the setting in which the agent interacts. For example, the house where the Robot moves. The agent has no influence over the surroundings; all it has is control over its own actions. For instance, Although the Robot cannot control where a table is kept in the house, it can walk around it to avoid colliding with it.

State - The state defines the current situation of the agent, for example, It may be the Robot's specific position in the house, the alignment of its two legs, or its current posture, depending on how you approach the issue.

Action - The decision made by the agent in the current time step. For instance: it can move its right or left leg, or raise its arm, or lift an object, turn right or left, etc. We know ahead of time what actions or decisions the agent can take.

Policy - A policy is the thinking process that goes into deciding on a course of action. It is a probability distribution applied to the collection of activities in practice. Actions that are very rewarding will have a high likelihood, and vice versa.

Note: Even if an action has a low probability, that does not mean it will not be chosen. It's only that it has a lower chance of being chosen.

## Q-LEARNING
The ‘Q in Q-learning stands for quality. Quality in this case represents how useful a given action is in gaining some future reward. Q-learning is an off-policy reinforcement learning algorithm that seeks to find the best action to take given the current state. It’s considered off-policy because the q-learning function learns from actions that are outside the current policy, like taking random actions, and therefore a policy isn’t needed. More specifically, q-learning seeks to learn a policy that maximizes the total reward.

An agent interacts with the environment in one of two ways – exploit or explore – and a Q-table is produced with the dimensions. An exploit option implies that all options are evaluated and the one with the greatest environmental benefit is chosen. An explore option is one that considers a random action without regard for the maximum future payoff.

## POINTS TO CONSIDER
Gamification of trading - Historical & Current Prices, Technical Data, Buy/Sell/Do Nothing, Profit & Loss.

Train the system - Each entry and exit is an individual game, Run through the price series sequentially and randomly.

Reward function design - Pure Profit & Loss on exit, otherwise zero, PnL from the start of trade to every time step t.

Features to use - Open, High, Low, Close, Volume (OHLCV), Technical indicators, Time of day, Day of Week, Time of year, Different time granularity.

Test the system - Sine waves, Trend curves, Random walks, Adding Noise to clean test curves.

Types of Deep Learning Algorithms.

## STEPS TO CREATE AND DEPLOY MODEL
Import necessary Libraries.

Load Dataset.

Perform Exploratory Data Analysis.

Create An Environment.

Prepare Data.

Train Data.

Test Data.

Evaluate Model.

Deploy Model.

## IMPORT NECESSARY LIBRARIES

![Image](figures/image_4.png)
LOAD DATASET


![Image](figures/image_5.png)
Data on stock market values from 2013 to 2018 is included in this dataset. This dataset contains the following information: date, open, high, low, and close values, as well as volume and stock names. Also, the dataset is in CSV format.

The following is a quick description of each component in the dataset:

DATE - The day on which stock is exchanged.

OPEN - Any listed stock's daily opening price is the price at which it is initially traded.

HIGH - The maximum price at which a stock can be bought or sold during a trading day is known as the high.

LOW - The minimum price at which a stock can be bought or sold during a trading day is known as the low.

CLOSE - During a standard trading session, the last price at which a stock trades is referred to as the closing price.

VOLUME - The total number of shares or contracts exchanged in a securities or market within a certain time period.

NAME - The name of the stock.


![Image](figures/image_6.png)
## EXPLORATORY DATA ANALYSIS
In every Data Analysis or Data Science project, exploratory data analysis, or EDA, is a critical stage. EDA is the investigation of a dataset to find patterns and anomalies as well as to generate hypotheses based on our knowledge of the information.


![Image](figures/image_7.png)
During the course of a data science or machine learning project, EDA consumes around half of the time spent on data analysis, feature selection, feature engineering, and other processes. Because it is the most essential element or backbone of a data science project, where one has to perform several tasks like data cleaning, dealing with missing values, handling outliers, treating unbalanced datasets, handling categorical features, and many others. To automate our tasks in exploratory data analysis, we may utilise python packages like dtale, pandas profiling, sweetviz, and autoviz.

Find and resolve missing values in the dataset.


![Image](figures/image_8.png)

![Image](figures/image_9.png)
Use a pairplot to visualise data and find patterns and relationships.


![Image](figures/image_10.png)

![Image](figures/image_11.png)

![Image](figures/image_12.png)
To conduct calculations for better analysis, use the Groupby() method to break the data into distinct groups.


![Image](figures/image_13.png)
Detecting and removing outliers from the dataset. Z-Score Method to detect outliers.

Use Boxplot and IQR (Inter-Quartile Range) for anomaly detection.

Close


![Image](figures/image_14.png)

![Image](figures/image_15.png)
Open


![Image](figures/image_16.png)

![Image](figures/image_17.png)
High


![Image](figures/image_18.png)

![Image](figures/image_19.png)
Low


![Image](figures/image_20.png)

![Image](figures/image_21.png)
## CREATE AN ENVIRONMENT
In the reinforcement learning problem, the environment is a critical component. It's critical to have a solid grasp of the underlying world with which the RL agent will interact. This aids us in developing the best design and learning strategy for the agent.


![Image](figures/image_22.png)
The reinforcement learning task is intended to be a simple framing of the challenge of learning from interaction in order to accomplish a goal. The agent is the learner and decision-maker. The environment is the object it interacts with, and it consists of everything outside the agent. The agent chooses actions, and the environment reacts to those actions, presenting the agent with new scenarios. The environment also produces rewards, which are unique numerical values that the agent attempts to maximise over time.


![Image](figures/image_23.png)

![Image](figures/image_24.png)

![Image](figures/image_25.png)

![Image](figures/image_26.png)
## MODEL EVALUATION
Model evaluation is a step in the model creation process that is often overlooked. This is the stage where the model's performance is determined. As a result, it's important to think about the model's results in terms of every conceivable assessment technique. Using various approaches can result in a variety of viewpoints.

## MODEL DEPLOYMENT
The project is hosted on Heroku which is a cloud Platform as a container-based Service (PaaS). Heroku is used by developers to launch, manage, and grow contemporary programs. Heroku is an open-source software platform for machine learning and data science that makes it simple to develop and publish attractive, bespoke web apps. The benefit of web apps is that they are platform agnostic and may be operated by anybody with an Internet connection. Their code is run on a back-end server, which processes incoming requests and answers using a common protocol that all browsers can understand.

Necessary Files:

app.py

requirement.txt - Contains a list of all the dependencies that your code requires in order to function properly.

Procfile - In an app, a Procfile is a list of process types.

setup.sh

requirement.txt

This file contains all of the libraries that must be installed in order for the project to run. This file may be manually produced by walking through the project and identifying all of the libraries used. However, we used the pipreqs module instead, which generated a requirement.txt file for us.


![Image](figures/image_27.png)
Procfile and setup.sh

Using these two files, we tell Heroku the needed commands to start our application. In the setup.sh file we created a streamlit folder with credentials.toml and a config.toml file.

Following is the command to be pasted in setup.sh file.


![Image](figures/image_28.png)
The setup.sh script is first performed using the Procfile, and then the application is executed using streamlit run.

Procfile looks like this.


![Image](figures/image_29.png)
## RESULTS

![Image](figures/image_30.png)

![Image](figures/image_31.png)
WEB APPLICATION - https://stock-trading-with-rl.herokuapp.com


![Image](figures/image_32.png)

![Image](figures/image_33.png)
