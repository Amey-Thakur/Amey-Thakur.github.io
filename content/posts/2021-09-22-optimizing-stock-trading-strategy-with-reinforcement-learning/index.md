---
title: "Optimizing Stock Trading Strategy With Reinforcement Learning"
date: 2021-09-22T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Deep Learning", "LSTM", "Finance", "Time-Series", "Stock Market", "Prediction", "Python"]
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


The core aim of this project is to take raw data, analyse it, and perform exploratory data analysis to clearly understand the underlying patterns. Using these insights, we build and train a Neural Network model to achieve accurate results. Finally, the complete system is deployed as a web application.

---

## Abstract

Our project focuses on identifying a single SPY (S&P 500 ETF) investment strategy that maximises overall wealth. We compare our model's performance with well-known approaches like the traditional buy-and-hold and the Moving Average Convergence Divergence (MACD) strategy. This work brings together Machine Learning, Data Science, and Web Development, with the final application deployed on the Heroku Cloud Platform.

The objective is to evaluate stock price behaviour based on essential market factors. We aim to forecast future price movements for specific stocks using historical price data and company-related financial news. Since reinforcement learning revolves around choosing optimal actions to maximise rewards, we use it here to predict stock closing prices based on past trends.

Using trained reinforcement learning models, we develop a multi-company predictor capable of estimating daily closing prices. By providing inputs such as open, high, and low prices, trading volume, and recent events related to each firm, the system determines the expected closing value for any given day.

Overall, this project is designed to build practical experience in Data Analytics, Machine Learning, and real-world model deployment.

---

## INTRODUCTION

The stock market's unpredictability has always fascinated us. With hundreds of stocks available and countless opportunities each day, the first challenge for a day trader is deciding what to trade. The next challenge is to identify strategies that can produce meaningful profit from these opportunities, whether in individual stocks, groups of stocks, or exchange-traded funds (ETFs).

Intraday traders use various techniques to capture short-term price movements. The best assets usually have high liquidity, noticeable volatility, and strong market participation. The main goal is to separate the actual market trend from surrounding noise and then take advantage of that trend at the correct moment.

Traditionally, traders relied on technical analysis, market sentiment, and current events to make trading decisions. With the growth of Data Science and Machine Learning, many of these time-consuming tasks can now be automated. Automated trading systems provide better timing, clearer insights, and more consistent predictions. They are especially useful for hedge funds and mutual funds, where even small improvements in accuracy can significantly improve returns. However, every profitable strategy comes with risk, and creating a reliable automated trading method is not simple.

Everyone who enters the stock market aims to maximise returns while keeping risk at a manageable level. To achieve this balance, reinforcement learning offers an effective approach. By learning from historical data, reinforcement learning agents can create trading strategies that adapt and improve over time.

This project was developed because we were interested in exploring these ideas and wanted practical experience with a Machine Learning project. It represents our attempt to understand how automated decision-making can be used to navigate the constantly changing environment of the stock market.

---

## REINFORCEMENT LEARNING

Reinforcement learning is a machine learning approach in which models learn to make a sequence of decisions. In an uncertain and often complex environment, the agent must figure out how to reach a specific goal. In reinforcement learning, artificial intelligence is placed in a game-like setting where it must experiment through trial and error to discover the best actions. The agent receives rewards or penalties based on its behaviour, which encourages it to perform actions that lead to the desired result. The aim is to maximise the total reward.

Although the designer defines the reward policy, which is essentially the set of rules for the task, the model is not given instructions or hints on how to solve it. The agent begins with random attempts and gradually learns more effective strategies, eventually developing advanced or even superhuman capabilities. It must discover the correct behaviour on its own in order to maximise its reward.

In reinforcement learning, developers use a framework that rewards useful actions and penalises harmful or unproductive ones. The agent receives positive values for desirable behaviour and negative values for undesirable behaviour. To find the optimal solution, the agent is encouraged to focus on long-term gains rather than short-term outcomes.

These long-term goals prevent the agent from getting stuck chasing smaller rewards. Over time, the agent learns to ignore negative patterns and continue reinforcing positive ones. This style of learning has been widely used in artificial intelligence to guide unsupervised behaviours through a system of rewards and penalties.

A simple example is teaching a dog. You allow the dog to behave freely, and when it does something good you say "Good dog." When it misbehaves, you say "Bad dog." Over time, the dog learns to repeat the good behaviours and avoid the bad ones.

{{< figure src="Optimizing%20Stock%20Trading%20Strategy%20With%20Reinforcement%20Learning/figures/image_2.png" caption="Example of teaching a dog" align="center" >}}


Trading is a continuous activity without a clear endpoint. Since we do not have complete information about market participants, trading can be viewed as a stochastic Markov Decision Process. We use model-free reinforcement learning, specifically Q-learning, because the reward function and transition probabilities are unknown.




---

## Markov Decision Process (MDP)

A Markov Decision Process is a mathematical framework used to model decision-making problems where outcomes are partly random and partly influenced by the decision-maker. It is similar to a Markov chain because it predicts future outcomes based only on the current state. However, unlike a simple Markov chain, an MDP also considers the effect of actions and the rewards associated with those actions.

At each step, the decision-maker selects an action available in the current state. This action moves the system to the next state and results in a reward. Over time, the goal is to choose actions that maximise the total reward.

{{< figure src="Optimizing%20Stock%20Trading%20Strategy%20With%20Reinforcement%20Learning/figures/image_3.png" caption="Markov Decision Process (MDP)" align="center" >}}

Machine learning algorithms often rely on MDPs when facing optimisation problems. In reinforcement learning, the agent interacts with an environment and aims to optimise its behaviour to achieve the highest possible long-term reward. While supervised learning requires correct input and output pairs, reinforcement learning uses the MDP framework to balance exploration and exploitation. This is useful when the probabilities of outcomes and the rewards associated with them are not fully known.

### Terminologies

**Agent**
The agent is the learner or decision-maker. It is the system we are training to make correct choices. For example, a robot being trained to move through a house without hitting obstacles.

**Environment**
The environment is the world in which the agent operates. In the example above, the house is the robot's environment. The agent cannot control the environment but can choose how to act within it. For instance, the robot cannot move a table, but it can walk around it.

**State**
The state represents the current situation of the agent. It may include the robot’s exact location, its posture, or the orientation of its legs, depending on how the problem is defined.

**Action**
Actions are the choices the agent can make at each time step. For example, moving its right leg, lifting an arm, turning left or right, or picking up an object. The set of possible actions is known in advance.

**Policy**
A policy defines the agent’s strategy for choosing actions. In practice, it is a probability distribution over all possible actions. Actions that lead to higher rewards have a higher probability of being selected. Low-probability actions can still be chosen, but they are less likely.

> **Note:** Even if an action has a low probability, it can still be selected. It simply has a lower chance of being chosen compared to actions with higher probabilities.

---

## Q-LEARNING

The Q in Q-learning stands for quality. In this context, quality represents how effective a particular action is in obtaining a future reward. Q-learning is an off-policy reinforcement learning algorithm that aims to determine the best possible action to take in a given state. It is considered off-policy because it can learn from actions that do not follow the current policy, including random exploratory actions. As a result, Q-learning does not require a predefined policy. Its main objective is to learn a policy that maximises the total accumulated reward.

An agent interacts with the environment in two primary ways: exploitation and exploration. During exploitation, the agent evaluates all available actions and chooses the one that offers the highest expected reward based on its current knowledge. During exploration, the agent chooses a random action to discover new possibilities, without focusing on immediate reward. Over time, the agent builds a Q-table that stores the value of taking each action in each state, allowing it to make better decisions as learning progresses.

### POINTS TO CONSIDER

*   **Gamification of trading**
    Historical and current prices, technical data, buy or sell or do nothing actions, and tracking profit and loss.

*   **Train the system**
    Treat each entry and exit as an individual game. Run through the price series both sequentially and randomly.

*   **Reward function design**
    Reward based on profit or loss at exit, otherwise zero, or cumulative profit and loss from the start of the trade to each time step.

*   **Features to use**
    Open, high, low, close, and volume (OHLCV), technical indicators, time of day, day of week, time of year, and different time granularities.

*   **Test the system**
    Use sine waves, trend curves, random walks, and add noise to clean test curves.

*   **Types of deep learning algorithms**
    Different architectures may be applied depending on the complexity of the environment and data.

### STEPS TO CREATE AND DEPLOY MODEL

1.  Import necessary libraries.
2.  Load the dataset.
3.  Perform exploratory data analysis.
4.  Create an environment.
5.  Prepare the data.
6.  Train the model.
7.  Test the model.
8.  Evaluate the model.
9.  Deploy the model.

---

## STOCK PRICE PREDICTION MODEL

### Import Modules

```python
import time
import copy
import numpy as np
import pandas as pd
import chainer
import chainer.functions as F
import chainer.links as L
from plotly import tools, subplots
from plotly.graph_objs import *
from plotly.offline import init_notebook_mode, iplot, iplot_mpl
init_notebook_mode()
```

### Load Dataset

```python
data = pd.read_csv('../input/nyse/prices-split-adjusted.csv')
data.head()
```

```python
data['date'] = pd.to_datetime(data['date'])
data = data[data['symbol'] == 'YHOO']
data = data.set_index('date')
data.head()
```

### Dataset Description

This dataset contains stock market data from 2013 to 2018. It includes information such as date, open, high, low, and close values, along with trading volume and stock names. The dataset is provided in CSV format.

Below is a brief explanation of each component in the dataset:

*   **DATE**: The specific day on which the stock was traded.
*   **OPEN**: The initial price at which a stock is traded when the market opens for the day.
*   **HIGH**: The highest price at which the stock was bought or sold during the trading day.
*   **LOW**: The lowest price at which the stock was bought or sold during the trading day.
*   **CLOSE**: The final price at which the stock was traded during the standard trading session.
*   **VOLUME**: The total number of shares or contracts traded within the given time period.
*   **NAME**: The name of the stock the data corresponds to.

### Data Visualization

```python
trace0 = Candlestick(x=data.index, open=data['open'], high=data['high'], low=data['low'], close=data['close'])
data0 = [trace0]
iplot(data0)
```

```python
date_split = '2016-01-01'
train = data[:date_split]
test = data[date_split:]
len(train), len(test)
```

### Preprocessing

```python
def plot_train_test(train, test, date_split):
    
    data = [
        Candlestick(x=train.index, open=train['open'], high=train['high'], low=train['low'], close=train['close'], name='train'),
        Candlestick(x=test.index, open=test['open'], high=test['high'], low=test['low'], close=test['close'], name='test')
    ]
    layout = {
         'shapes': [
             {'x0': date_split, 'x1': date_split, 'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper', 'line': {'color': 'rgb(0,0,0)', 'width': 1}}
         ],
        'annotations': [
            {'x': date_split, 'y': 1.0, 'xref': 'x', 'yref': 'paper', 'showarrow': False, 'xanchor': 'left', 'text': ' test data'},
            {'x': date_split, 'y': 1.0, 'xref': 'x', 'yref': 'paper', 'showarrow': False, 'xanchor': 'right', 'text': 'train data '}
        ]
    }
    figure = Figure(data=data, layout=layout)
    iplot(figure)
```

```python
plot_train_test(train, test, date_split)
```

### Define Environment

```python
class Environment1:
    
    def __init__(self, data, history_t=90):
        self.data = data
        self.history_t = history_t
        self.reset()
        
    def reset(self):
        self.t = 0
        self.done = False
        self.profits = 0
        self.positions = []
        self.position_value = 0
        self.history = [0 for _ in range(self.history_t)]
        return [self.position_value] + self.history # obs
    
    def step(self, act):
        reward = 0
        
        # act = 0: stay, 1: buy, 2: sell
        if act == 1:
            self.positions.append(self.data.iloc[self.t, :]['close'])
        elif act == 2: # sell
            if len(self.positions) == 0:
                reward = -1
            else:
                profits = 0
                for p in self.positions:
                    profits += (self.data.iloc[self.t, :]['close'] - p)
                reward += profits
                self.profits += profits
                self.positions = []
        
        # set next time
        self.t += 1
        self.position_value = 0
        for p in self.positions:
            self.position_value += (self.data.iloc[self.t, :]['close'] - p)
        self.history.pop(0)
        self.history.append(self.data.iloc[self.t, :]['close'] - self.data.iloc[self.t-1, :]['close'])
        
        # clipping reward
        if reward > 0:
            reward = 1
        elif reward < 0:
            reward = -1
        
        return [self.position_value] + self.history, reward, self.done # obs, reward, done
```

```python
env = Environment1(train)
print(env.reset())
for _ in range(3):
    pact = np.random.randint(3)
    print(env.step(pact))
```

### Train DQN

```python
def train_dqn(env):
    
    class Q_Network(chainer.Chain):

        def __init__(self, input_size, hidden_size, output_size):
            super(Q_Network, self).__init__(
                fc1 = L.Linear(input_size, hidden_size),
                fc2 = L.Linear(hidden_size, hidden_size),
                fc3 = L.Linear(hidden_size, output_size)
            )

        def __call__(self, x):
            h = F.relu(self.fc1(x))
            h = F.relu(self.fc2(h))
            y = self.fc3(h)
            return y

        def reset(self):
            self.zerograds()

    Q = Q_Network(input_size=env.history_t+1, hidden_size=100, output_size=3)
    Q_ast = copy.deepcopy(Q)
    optimizer = chainer.optimizers.Adam()
    optimizer.setup(Q)

    epoch_num = 50
    step_max = len(env.data)-1
    memory_size = 200
    batch_size = 20
    epsilon = 1.0
    epsilon_decrease = 1e-3
    epsilon_min = 0.1
    start_reduce_epsilon = 200
    train_freq = 10
    update_q_freq = 20
    gamma = 0.97
    show_log_freq = 5

    memory = []
    total_step = 0
    total_rewards = []
    total_losses = []

    start = time.time()
    for epoch in range(epoch_num):

        pobs = env.reset()
        step = 0
        done = False
        total_reward = 0
        total_loss = 0

        while not done and step < step_max:

            # select act
            pact = np.random.randint(3)
            if np.random.rand() > epsilon:
                pact = Q(np.array(pobs, dtype=np.float32).reshape(1, -1))
                pact = np.argmax(pact.data)

            # act
            obs, reward, done = env.step(pact)

            # add memory
            memory.append((pobs, pact, reward, obs, done))
            if len(memory) > memory_size:
                memory.pop(0)

            # train or update q
            if len(memory) == memory_size:
                if total_step % train_freq == 0:
                    shuffled_memory = np.random.permutation(memory)
                    memory_idx = range(len(shuffled_memory))
                    for i in memory_idx[::batch_size]:
                        batch = np.array(shuffled_memory[i:i+batch_size])
                        b_pobs = np.array(batch[:, 0].tolist(), dtype=np.float32).reshape(batch_size, -1)
                        b_pact = np.array(batch[:, 1].tolist(), dtype=np.int32)
                        b_reward = np.array(batch[:, 2].tolist(), dtype=np.int32)
                        b_obs = np.array(batch[:, 3].tolist(), dtype=np.float32).reshape(batch_size, -1)
                        b_done = np.array(batch[:, 4].tolist(), dtype=bool)

                        q = Q(b_pobs)
                        maxq = np.max(Q_ast(b_obs).data, axis=1)
                        target = copy.deepcopy(q.data)
                        for j in range(batch_size):
                            target[j, b_pact[j]] = b_reward[j]+gamma*maxq[j]*(not b_done[j])
                        Q.reset()
                        loss = F.mean_squared_error(q, target)
                        total_loss += loss.data
                        loss.backward()
                        optimizer.update()

                if total_step % update_q_freq == 0:
                    Q_ast = copy.deepcopy(Q)

            # epsilon
            if epsilon > epsilon_min and total_step > start_reduce_epsilon:
                epsilon -= epsilon_decrease

            # next step
            total_reward += reward
            pobs = obs
            step += 1
            total_step += 1

        total_rewards.append(total_reward)
        total_losses.append(total_loss)

        if (epoch+1) % show_log_freq == 0:
            log_reward = sum(total_rewards[((epoch+1)-show_log_freq):])/show_log_freq
            log_loss = sum(total_losses[((epoch+1)-show_log_freq):])/show_log_freq
            elapsed_time = time.time()-start
            print('\t'.join(map(str, [epoch+1, epsilon, total_step, log_reward, log_loss, elapsed_time])))
            start = time.time()
            
    return Q, total_losses, total_rewards
```

```python
Q, total_losses, total_rewards = train_dqn(Environment1(train))
```

### Plot Results

```python
def plot_train_test_by_q(train_env, test_env, Q, algorithm_name):
    
    # train
    pobs = train_env.reset()
    train_acts = []
    train_rewards = []

    for _ in range(len(train_env.data)-1):
        
        pact = Q(np.array(pobs, dtype=np.float32).reshape(1, -1))
        pact = np.argmax(pact.data)
        train_acts.append(pact)
            
        obs, reward, done = train_env.step(pact)
        train_rewards.append(reward)

        pobs = obs
        
    train_profits = train_env.profits
    
    # test
    pobs = test_env.reset()
    test_acts = []
    test_rewards = []

    for _ in range(len(test_env.data)-1):
    
        pact = Q(np.array(pobs, dtype=np.float32).reshape(1, -1))
        pact = np.argmax(pact.data)
        test_acts.append(pact)
            
        obs, reward, done = test_env.step(pact)
        test_rewards.append(reward)

        pobs = obs
        
    test_profits = test_env.profits
    
    # plot
    train_copy = train_env.data.copy()
    test_copy = test_env.data.copy()
    train_copy['act'] = train_acts + [np.nan]
    train_copy['reward'] = train_rewards + [np.nan]
    test_copy['act'] = test_acts + [np.nan]
    test_copy['reward'] = test_rewards + [np.nan]
    train0 = train_copy[train_copy['act'] == 0]
    train1 = train_copy[train_copy['act'] == 1]
    train2 = train_copy[train_copy['act'] == 2]
    test0 = test_copy[test_copy['act'] == 0]
    test1 = test_copy[test_copy['act'] == 1]
    test2 = test_copy[test_copy['act'] == 2]
    act_color0, act_color1, act_color2 = 'gray', 'cyan', 'magenta'

    data = [
        Candlestick(x=train0.index, open=train0['open'], high=train0['high'], low=train0['low'], close=train0['close'], increasing=dict(line=dict(color=act_color0)), decreasing=dict(line=dict(color=act_color0))),
        Candlestick(x=train1.index, open=train1['open'], high=train1['high'], low=train1['low'], close=train1['close'], increasing=dict(line=dict(color=act_color1)), decreasing=dict(line=dict(color=act_color1))),
        Candlestick(x=train2.index, open=train2['open'], high=train2['high'], low=train2['low'], close=train2['close'], increasing=dict(line=dict(color=act_color2)), decreasing=dict(line=dict(color=act_color2))),
        Candlestick(x=test0.index, open=test0['open'], high=test0['high'], low=test0['low'], close=test0['close'], increasing=dict(line=dict(color=act_color0)), decreasing=dict(line=dict(color=act_color0))),
        Candlestick(x=test1.index, open=test1['open'], high=test1['high'], low=test1['low'], close=test1['close'], increasing=dict(line=dict(color=act_color1)), decreasing=dict(line=dict(color=act_color1))),
        Candlestick(x=test2.index, open=test2['open'], high=test2['high'], low=test2['low'], close=test2['close'], increasing=dict(line=dict(color=act_color2)), decreasing=dict(line=dict(color=act_color2)))
    ]
    title = '{}: train s-reward {}, profits {}, test s-reward {}, profits {}'.format(
        algorithm_name,
        int(sum(train_rewards)),
        int(train_profits),
        int(sum(test_rewards)),
        int(test_profits)
    )
    layout = {
        'title': title,
        'showlegend': False,
         'shapes': [
             {'x0': date_split, 'x1': date_split, 'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper', 'line': {'color': 'rgb(0,0,0)', 'width': 1}}
         ],
        'annotations': [
            {'x': date_split, 'y': 1.0, 'xref': 'x', 'yref': 'paper', 'showarrow': False, 'xanchor': 'left', 'text': ' test data'},
            {'x': date_split, 'y': 1.0, 'xref': 'x', 'yref': 'paper', 'showarrow': False, 'xanchor': 'right', 'text': 'train data '}
        ]
    }
    figure = Figure(data=data, layout=layout)
    iplot(figure)
```

```python
plot_train_test_by_q(Environment1(train), Environment1(test), Q, 'DQN')
```

---




## Publication Details

This work was published in the **International Journal of Research in Applied Science and Engineering Technology (IJRASET)**.

### Additional Resources
*   [Full Paper (PDF)](Optimizing%20Stock%20Trading%20Strategy%20With%20Reinforcement%20Learning/Optimizing%20Stock%20Trading%20Strategy%20With%20Reinforcement%20Learning.pdf)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Optimizing Stock Trading Strategy With Reinforcement Learning". AmeyArc (Sep 2021). https://amey-thakur.github.io/posts/2021-09-22-optimizing-stock-trading-strategy-with-reinforcement-learning/.</code></pre>

**Or use the BibTex citation:**

**BibTeX:**

```
@article{thakur2021stocktrading,
  title   = "Optimizing Stock Trading Strategy With Reinforcement Learning",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Sep",
  url     = "https://amey-thakur.github.io/posts/2021-09-22-optimizing-stock-trading-strategy-with-reinforcement-learning/"
}
```

---

## References

1. <a id="ref-1"></a> **Thakur, A.** (2021). Stock Trends Prediction Using Algorithms. *International Journal of Research in Applied Science and Engineering Technology (IJRASET)*, 9(9).

---
*Authored by Amey Thakur.*
