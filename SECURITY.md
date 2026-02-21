# Security Policy

## Active Development

This repository, **Amey's Arc**, is a living professional space and an evolving record of engineering thought. It is actively developed and maintained as a hub for technical insights, research reflections, and project documentation. The content and code within reflect an ongoing commitment to academic and technical excellence.

## Supported Versions

As this repository is in active development, only the latest state of the `main` branch is considered authoritative:

| Version | Supported |
| ------- | --------- |
| Current | Yes       |

## Dual-Licensing Framework

To support both technical transparency and the creative integrity of the narrative, this repository follows a dual-licensing model:

- **Source Code**: The underlying engine, custom layouts, styling (CSS), and logic (JavaScript) are licensed under the **MIT License**.
- **Content and Posts**: All original writing, research notes, and reflective posts are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

## Vulnerability Reporting Protocol

If you identify a potential security-related concern or unintended behavior, please report it through the official repository channels. This ensures that observations are recorded professionally and can be addressed transparently.

To document a security concern, please communicate with the developer:
- **Developer**: [Amey Thakur](https://github.com/Amey-Thakur)
- **Reporting Method**: Please open a new [GitHub Issue](https://github.com/Amey-Thakur/Amey-Thakur.github.io/issues) to formally record your findings.

When reporting, please provide:
1. A clear description of the identified issue.
2. Technical evidence or steps to reproduce the behavior within the site environment.
3. A brief explanation of why the issue is relevant to the repository's security posture.

## Implementation Context: Static Execution Model

This project is built as a static site using **Hugo** and served via **GitHub Pages**. The security profile is based on:

- **Static Content**: Most content is served as pre-rendered HTML, which naturally minimizes the attack surface associated with server-side logic.
- **Client-Side Behavioral Features**: Interactive elements (such as `thought-animation.js`) are client-side only and execute within the browser's native sandbox.

- **Scope Limitation**: This policy applies specifically to the code, posts, and configurations found within this repository. It does not cover the Hugo framework itself, third-party libraries, or the hosting infrastructure provided by GitHub.

## Technical Integrity Statement

Responsible reporting and constructive feedback are highly valued as they contribute to the quality and reliability of this professional space. Submissions are documented for contextual reference and to maintain the overall technical integrity of the project.

---

*This document defines the security posture and licensing philosophy of Amey's Arc.*
