---
title: "Distributed File Systems: Architecting for Scale"
date: 2022-03-31T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Distributed Systems", "File Systems", "Scalability", "Fault Tolerance", "NFS", "AFS", "Architecture"]
ShowToc: true
TocOpen: false
description: "A comparative study of distributed file storage architectures, creating a unified namespace across networked machines."
---

## 📋 Abstract

As data grows beyond the capacity of a single hard drive, **Distributed File Systems (DFS)** become a necessity. This project explores the architecture required to store a single logical file across multiple physical machines. We analyze the design trade-offs between **Network File System (NFS)** and **Andrew File System (AFS)**, focusing on caching mechanisms, transparency, and fault tolerance. The result is a simulation demonstrating how a DFS maintains data consistency when multiple clients access shared files simultaneously [[1]](#ref-1).

---

## 📂 The Library Analogy

How do you manage a library so big it doesn't fit in one building?

### The Analogy: The Inter-Library Loan
*   **Centralized (Your Laptop)**: All books are in one room. Easy to find, but if the room burns down, everything is gone.
*   **Distributed (DFS)**:
    *   **Transparency**: You search the catalog for "Moby Dick." The system tells you it's on "Shelf 3." You don't need to know that "Shelf 3" is actually in a warehouse in Ohio. To you, it looks like a local shelf.
    *   **Caching (AFS)**: When you borrow the book, you take it home (Local Cache). You read it there. Only when you return it (Close File) does the library update its records. This reduces traffic to the warehouse.
    *   **Direct Access (NFS)**: You read the book at the library counter. Every page turn is a request to the librarian. It's chattier but ensures you have the absolute latest version.

---

## ⚙️ Protocols Analyzed

We conducted a comparative analysis of three major file system architectures.

{{< figure src="figures/Comparison%20of%20different%20FIle%20Systems.png" caption="Comparison of File System Architectures" align="center" >}}

### 1. NFS (Network File System)
*   **Stateless**: The server doesn't remember if you have a file open. If the server crashes and reboots, you can keep reading without errors.
*   **Usage**: Great for local area networks (LAN) where speed is key.

{{< figure src="figures/Architecture%20of%20NFS.png" caption="NFS Architecture" align="center" >}}

### 2. AFS (Andrew File System)
*   **Stateful + Callbacks**: The server knows who has cached copies. If User A changes the file, the server calls User B to say "Your copy is old, get a new one."
*   **Usage**: Better for wide area networks (WAN) due to aggressive caching.

{{< figure src="figures/Structure%20of%20AFS.png" caption="AFS Structure and Venus/Vice Components" align="center" >}}

---

## 📄 Publication Details

This work was presented as a technical analysis for a **Distributed Systems** course.

### Additional Resources
*   [Full Presentation (PDF)](PRESENTATION%20-%20A%20COMPARATIVE%20STUDY%20ON%20DISTRIBUTED%20FILE%20SYSTEMS.pdf)

---

## Citation

**Cited as:**

> Thakur, Amey. \"Distributed File Systems: Architecting for Scale\". AmeyArc (Mar 2022). https://amey-thakur.github.io/posts/2022-03-31-distributed-file-systems/.

**BibTeX:**

```
@article{thakur2022dfs,
  title   = "Distributed File Systems: Architecting for Scale",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Mar",
  url     = "https://amey-thakur.github.io/posts/2022-03-31-distributed-file-systems/"
}
```

## 📚 References

1. <a id="ref-1"></a> **Thakur, A.** (2022). A Comparative Study on Distributed File Systems. *Course Technical Report*.

---
*Authored by Amey Thakur.*
