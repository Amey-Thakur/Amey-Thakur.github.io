<div align="center">
<a name="readme-top"></a>

# <a href="https://amey-thakur.github.io/"><img src="Source%20Code/static/pwa_icon.svg" width="48" height="48" title="Amey's Arc | Scholarly Digital Identity"></a> Amey's Arc

[![License: MIT/CC](https://img.shields.io/badge/License-MIT_%2F_CC_BY_4.0-lightgrey)](LICENSE)
![Status](https://img.shields.io/badge/Status-Active-success)
[![Engine](https://img.shields.io/badge/Engine-Hugo_0.146.0%2B-blueviolet)](https://github.com/Amey-Thakur/Amey-Thakur.github.io)
[![Author](https://img.shields.io/badge/Author-Amey_Thakur-blue)](https://github.com/Amey-Thakur)

  **Advancing ideas @ AmeyArc_**

  Hi, I’m Amey. This is my space for notes, reflections, and ideas in progress. Some thoughts are fully formed, others are just sparks, but all are here to explore, share, and grow. I hope these notes spark your thinking, and this space grows with every reflection, including yours.

**[Source Code](Source%20Code/)** &nbsp;·&nbsp; **[Archival Content](content/)** &nbsp;·&nbsp; **[Live Site](https://amey-thakur.github.io/)**

</div>

---

<div align="center">

[Author](#author) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Project Structure](#project-structure) &nbsp;·&nbsp; [Dual-Licensing](#dual-licensing-model) &nbsp;·&nbsp; [Tech Stack](#tech-stack)

</div>

---

<a name="author"></a>
<div align="center">

## Author

| <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) |
| :---: |

</div>

---

<a name="overview"></a>
## Overview

**Amey's Arc** is a curated digital archive of research work, technical projects, and evolving ideas. It serves as a standardized platform for documenting engineering reflections and scholarly exploration across diverse domains, including Artificial Intelligence, Distributed Systems, and Control Engineering. The repository provides the underlying documentation for the methodologies and insights presented on the live scholarly portal.

### Technical Archetypes
The archive preserves granular documentation for various research vectors:
- **Artificial Intelligence**: Exploration of Zero-Shot Video Generation, Generative Adversarial Networks (GANs), and Reinforcement Learning strategies.
- **Embedded Systems & Control**: Adaptive Cruise Control architectures using Arduino and Simulink environments.
- **Distributed Architectures**: Technical analysis of distributed file systems and clock synchronization protocols.
- **Computational Geometry**: Development of high-performance spatial partitioning through Quadtree visualizations.

---

<a name="project-structure"></a>
## Project Structure

```mermaid
graph TD
    Root[Amey-Thakur.github.io] --> Source[Source Code: Hugo Project Root]
    Root --> Content[Archival Content: Research & Reflections]
    
    Source --> Assets[Assets: Branding & Interaction]
    Source --> Layouts[Layouts: Structural Logic]
    Source --> Static[Static: System Resource Registry]
    
    Content --> Posts[Posts: Deep-Tech Archive]
    Content --> Archives[Archives: Historical Chronology]
    Content --> Connect[Connect: Identity Markers]
```

### Repository Topology

├── **[Source Code/](Source%20Code/)**           # Integrated Hugo application layer
│   ├── **[assets/](Source%20Code/assets/)**          # Global system resources & CSS Foundations
│   ├── **[layouts/](Source%20Code/layouts/)**         # Modular templates & scholarly partials
│   ├── **[static/](Source%20Code/static/)**          # Static assets & PWA identifiers
│   ├── **Site.toml**                   # Global environmental manifest
│   └── **Engine.toml**                 # Technical theme specifications
│
├── **[content/](content/)**               # Scholarly content & intellectual archives
│   ├── **[posts/](content/posts/)**             # Deep-tech & research publications
│   └── **[archives/](content/archives/)**          # Historical navigation indices
│
└── **README.md**                       # Primary architectural entrance

---

<a name="dual-licensing-model"></a>
## Dual-Licensing Protocol

This repository operates under a **dual-licensing framework** to distinguish between creative intellectual property and technical engineering logic.

### 🖋️ Content & Intellect
All original prose, research posts, and technical reflections are licensed under the **[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)**.
- **Academic Standard**: Citation and attribution are required for reproduction.
- **Scope**: Files within the **`content/`** directory.

### ⚙️ Infrastructure & Logic
All functional components, including Hugo templates, custom CSS/JS, and automation logic, are licensed under the **[MIT License](Source%20Code/LICENSE)**.
- **Engineering Standard**: Permissive reuse for infrastructure and toolchains.
- **Scope**: Files within the **`Source Code/`** directory.

---

### Tech Stack
- **Engine**: **Hugo 0.146.0+**
- **Markdown**: **Goldmark Rendering Framework**
- **Logic**: **Vanilla CSS / ES6 Modules**
- **Metadata**: **TOML Configuration Schema**
- **Deployment**: **GitHub Pages**

---

<div align="center">

[↑ Back to Top](#readme-top)

<a href="https://amey-thakur.github.io/"><img src="Source%20Code/static/pwa_icon.svg" width="24" height="24" title="Amey's Arc | Global Entrance"></a> **[Amey's Arc](https://amey-thakur.github.io/)**

</div>
