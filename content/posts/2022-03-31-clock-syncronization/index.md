---
title: "Clock Synchronization: A Comparative Analysis of Berkeley and Cristian's Algorithms"
date: 2022-03-31T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Distributed Systems", "Clock Synchronization", "Berkeley Algorithm", "Cristian's Algorithm", "Time Coordination", "Network Protocols", "Python"]
ShowToc: true
TocOpen: false
description: "An in-depth analysis and implementation of two fundamental clock synchronization algorithms in distributed systems."
---

## 📋 Abstract

In distributed systems, there is no global clock. Each node maintains its own internal time, which inevitably drifts due to hardware imperfections. This drift can lead to chaotic system states, such as a file being "modified" before it was created. This project explores the two primary strategies for mitigating this chaos: **Cristian's Algorithm** (client-server) and the **Berkeley Algorithm** (master-slave averaging). We provide a Python-based implementation and a comparative analysis of their accuracy and fault tolerance [[1]](#ref-1).

---

## ⏳ The Problem of Digital Time

Why is it so hard for computers to agree on what time it is?

### The Analogy: The Wristwatch Dilemma
Imagine a group of friends trying to meet for a movie.
*   **Cristian's Approach**: Everyone asks one person (the one with the expensive Atomic Watch) "What time is it?" The problem is, it takes time to ask and receive an answer. By the time you hear "It's 2:00," it's actually 2:00 plus 5 seconds. Cristian's algorithm attempts to calculate that 5-second delay and adjust for it.
*   **Berkeley's Approach**: A leader looks at everyone's watch. One says 1:55, another 2:05, and the leader says 2:00. The leader averages them all (2:00) and tells the slow person to move forward by 5 minutes and the fast person to move back by 5 minutes. No one knows the "absolute" true time, but at least they all agree.

---

## 🕰️ Algorithm Details

We implemented and visualized both algorithms to understand their network behavior.

{{< figure src="Figures/Figure%205%20-%20Architecture%20of%20Network%20Working%20Protocol.png" caption="Architecture of the Synchronization Protocol" align="center" >}}

### 1. Cristian's Algorithm
*   **Type**: Probabilistic / External Synchronization.
*   **Mechanism**: A client sends a request to a time server $(T_1)$. The server records the receipt time $(T_2)$ and send time $(T_3)$. The client receives it at $(T_4)$.
*   **The Math**:
    $$ \text{Round Trip Time (RTT)} = (T_4 - T_1) - (T_3 - T_2) $$
    $$ \text{Synchronized Time} = T_3 + \frac{\text{RTT}}{2} $$
*   **Pros**: Simple, synchronizes to an external UTC source.
*   **Cons**: Fails if the server goes down; assumes network delay is symmetric.

{{< figure src="Figures/Figure%202%20-%20Cristian’s%20Algorithm%20Working.png" caption="Workflow of Cristian's Algorithm" align="center" >}}

### 2. The Berkeley Algorithm
*   **Type**: Internal Synchronization.
*   **Mechanism**: A daemon (master) polls all clients (slaves) for their local time. It discards outliers (faulty clocks), averages the remaining times, and sends an *offset* (adjustment) to each client.
*   **Pros**: Robust (if master fails, a new one is elected); does not require an external Internet connection.
*   **Cons**: Does not guarantee accuracy to UTC, only internal consistency.

{{< figure src="Figures/Figure%204%20-%20Berkeley’s%20Algorithm%20Working.png" caption="Workflow of the Berkeley Algorithm" align="center" >}}

---

## 📄 Publication Details

This work was published in the **International Research Journal of Engineering and Technology (IRJET)**.

### Additional Resources
*   [Full Paper (PDF)](IRJET-V9I3%20-%20Clock%20Synchronization%20in%20Distributed%20Systems.pdf)

---

## Citation

**Cited as:**

> Thakur, Amey. \"Clock Synchronization: A Comparative Analysis of Berkeley and Cristian's Algorithms\". AmeyArc (Mar 2022). https://amey-thakur.github.io/posts/2022-03-31-clock-syncronization/.

**BibTeX:**

```
@article{thakur2022clocksync,
  title   = "Clock Synchronization: A Comparative Analysis of Berkeley and Cristian's Algorithms",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Mar",
  url     = "https://amey-thakur.github.io/posts/2022-03-31-clock-syncronization/"
}
```

## 📚 References

1. <a id="ref-1"></a> **Thakur, A.** (2022). Clock Synchronization in Distributed Systems. *International Research Journal of Engineering and Technology (IRJET)*, 9(3).

---
*Authored by Amey Thakur.*
