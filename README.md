<div align="center">

  <a name="readme-top"></a>
  # <a href="https://amey-thakur.github.io/"><img src="Source Code/static/pwa_icon.svg" width="64" height="64" title="Amey's Arc | Scholarly Digital Identity"></a> Amey's Arc

  [![License: MIT/CC](https://img.shields.io/badge/License-MIT_%2F_CC_BY_4.0-blueviolet)](LICENSE)
  ![Status](https://img.shields.io/badge/Status-Active-success)
  [![Engine](https://img.shields.io/badge/Engine-Hugo_0.146.0%2B-blue)](https://github.com/Amey-Thakur/Amey-Thakur.github.io)
  [![Author](https://img.shields.io/badge/Author-Amey_Thakur-lightgrey)](https://github.com/Amey-Thakur)

  <br>

  *Scholarly digital identity and technical architectural archives.*

  **[Source Code](Source%20Code/)** &nbsp;·&nbsp; **[Archival Content](content/)** &nbsp;·&nbsp; **[Live Site](https://amey-thakur.github.io/)**

</div>

---

<div align="center">

  [Author](#author) &nbsp;·&nbsp; [Overview](#overview) &nbsp;·&nbsp; [Project Structure](#project-structure) &nbsp;·&nbsp; [Dual-Licensing](#dual-licensing-model) &nbsp;·&nbsp; [Tech Stack](#tech-stack)

</div>

---

<!-- AUTHOR -->
<div align="center">

  <a name="author"></a>
  ## Author

| <a href="https://github.com/Amey-Thakur"><img src="https://github.com/Amey-Thakur.png" width="150" height="150" alt="Amey Thakur"></a><br>[**Amey Thakur**](https://github.com/Amey-Thakur)<br><br>[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--5644--1575-green.svg)](https://orcid.org/0000-0001-5644-1575) |
| :---: |

</div>

---

<!-- OVERVIEW -->
<a name="overview"></a>
## Overview

**Amey's Arc** is a sovereign digital archive and technical identity hub. It serves as an authoritative repository for technical notes, research reflections, and architectural insights, meticulously documented to maintain scholarly rigor and engineering clarity. Developed using a decoupled Hugo architecture, the platform preserves the intellectual evolution of complex software engineering and research exploration.

> [!NOTE]
> ### <a href="https://amey-thakur.github.io/"><img src="Source Code/static/pwa_icon.svg" width="18" height="18" title="Architectural Engine Foundation"></a> Architectural Engine: Amey's Arc
> This repository utilizes a custom-configured **Hugo** engine with split configuration manifests (**Site.toml** and **Engine.toml**). The architecture separates functional infrastructure (Source Code) from archival prose (Content), ensuring modularity and long-term data integrity.

---

<!-- STRUCTURE -->
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

<!-- LICENSING -->
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

  <a href="https://amey-thakur.github.io/"><img src="Source Code/static/pwa_icon.svg" width="24" height="24" title="Amey's Arc | Global Entrance"></a> **[Amey's Arc](https://amey-thakur.github.io/)**

</div>
