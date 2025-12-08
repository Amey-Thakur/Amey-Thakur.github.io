---
title: "QuadTree Visualizer: Spatial Indexing for Collision Detection"
date: 2022-04-27T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Data Structures", "Algorithms", "Simulation", "Collision Detection", "JavaScript", "p5.js", "Spatial Hashing"]
ShowToc: true
TocOpen: false
description: "A visual simulation of the QuadTree data structure, demonstrating its efficiency in optimizing 2D spatial queries and collision detection."
---

## 📋 Abstract

In game development and physical simulations, checking every object against every other object for collisions is an $O(N^2)$ operation—computationally disastrous. The **QuadTree** data structure solves this by recursively partitioning 2D space into four quadrants. This project provides an interactive visualizer built with **p5.js** that demonstrates how QuadTrees optimize spatial queries, reducing collision detection to near $O(N \log N)$ complexity [[1]](#ref-1).

---

## 🌳 Divide and Conquer

How do you find a needle in a haystack? You don't search the whole stack; you devide it into boxes.

### The Analogy: The Filing Cabinet
*   **Brute Force ($N^2$)**: Imagine a messy desk with 1,000 papers. To find duplicates, you compare Paper 1 with 999 others, then Paper 2 with 998... it takes forever.
*   **QuadTree ($N \log N$)**: You have a filing cabinet.
    1.  **Top Drawer**: A-F
    2.  **Second Drawer**: G-M
    
    If you are holding a paper starting with "B", you *only* look in the Top Drawer. You fundamentally ignore 75% of the other papers immediately. The QuadTree does this for 2D space—if a particle is in the Top-Left corner, we don't need to check for collisions with particles in the Bottom-Right.

---

## ⚙️ Algorithmic Design

The visualizer dynamically constructs the tree as particles move.

{{< figure src="figures/Figure%201%20-%20QuadTree%20Data%20Structure.png" caption="Recursive Partitioning of Space" align="center" >}}

### Core Logic
1.  **Insert**: Place a point into the root node.
2.  **Split**: If a node exceeds its capacity (e.g., 4 points), it subdivides into 4 children (NW, NE, SW, SE).
3.  **Query**: To check a range, only traverse nodes that intersect with that range.

{{< figure src="figures/Figure%207%20-%20Workflow%20of%20QuadTree.png" caption="Workflow of Insertion and Querying" align="center" >}}

---

## 💻 Simulation Interface

The interactive dashboard allows users to spawn thousands of particles and observe the real-time partitioning boundary updates.

{{< figure src="figures/Figure%203%20-%20QuadTree%20Spatial%20Indexing.png" caption="QuadTree Spatial Partitioning in Action" align="center" >}}

{{< figure src="figures/Figure%2016%20-%20Control%20Panel.png" caption="Simulation Control Panel" align="center" >}}

---

## 📄 Publication Details

This work was published in the **International Journal of Engineering Research & Technology (IJERT)**.

### Additional Resources
*   [Full Paper (PDF)](IJERTV11IS040156%20-%20QuadTree%20Visualizer.pdf)

---

## Citation

**Cited as:**

> Thakur, Amey. \"QuadTree Visualizer: Spatial Indexing for Collision Detection\". AmeyArc (Apr 2022). https://amey-thakur.github.io/posts/2022-04-27-quadtree-visualizer/.

**BibTeX:**

```
@article{thakur2022quadtree,
  title   = "QuadTree Visualizer: Spatial Indexing for Collision Detection",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Apr",
  url     = "https://amey-thakur.github.io/posts/2022-04-27-quadtree-visualizer/"
}
```

## 📚 References

1. <a id="ref-1"></a> **Thakur, A.** (2022). QuadTree Visualizer. *International Journal of Engineering Research & Technology (IJERT)*, 11(4).

---
*Authored by Amey Thakur.*
