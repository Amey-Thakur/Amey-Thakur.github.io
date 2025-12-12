---
title: "Car Rental System"
date: 2021-07-17T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["C++", "OOP", "Software Design", "System Architecture", "Console Application", "File Handling", "Management System"]
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




Legacy systems in the automotive rental industry often suffer from inefficiency and lack of scalability. This project presents a **Car Rental Management System** built using **C++**, designed to streamline operations through Object-Oriented Programming (OOP) principles. By encapsulating logic within `Car`, `Customer`, and `Rental` classes, the system ensures data integrity and modularity. Key features include real-time inventory tracking, bill generation, and persistent data storage using file handling.

---

## Modularity in Design

Why use Classes instead of just functions?

### The Analogy: The Lego Kit
*   **Procedural Code**: Is like a clay model. It's one big blob. If you want to change the tire, you have to reshape the whole side of the car.
*   **OOP (This System)**: Is like a Lego kit. The "Tire" is a separate brick (Class). The "Engine" is a separate brick. You can swap the tire without touching the engine. In our system, we can upgrade the `billing` logic without breaking the `car inventory` logic because they are separate, self-contained objects.

---

## System Architecture

The application is structured around three core interactions:

1.  **Inventory Management**:
    *   Uses a `std::vector<Car>` to dynamically store fleet information.
    *   Allows adding/removing vehicles during runtime.
2.  **Rental Processing**:
    *   Calculates costs based on rental duration and car model.
    *   Updates availability status automatically.
3.  **Data Persistence**:
    *   Writes all transaction logs to `.txt` files, ensuring data isn't lost when the program closes.

---

## Publication Details

This work was published in the **International Journal of Research in Applied Science and Engineering Technology (IJRASET)**.

**Publication Details:**
*   **Journal**: IJRASET - Volume 9, Issue 7
*   **Title**: Car Rental System
*   **Reference**: [IJRASET Publication](Car%20Rental%20System/Car%20Rental%20System.pdf)

### Additional Resources
*   [Source Code](https://github.com/Amey-Thakur/Car-Rental-System)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Car Rental System". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-17-car-rental-system/.</code></pre>

**Or use the BibTex citation:**


```
@article{thakur2021carrental,
  title   = "Car Rental System",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-17-car-rental-system/"
}
```

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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>International Research Journal of Engineering and Technology (IRJET)</i>, vol. 08, no. June, pp. 1948–1951, 2021, DOI: <a href="https://doi.org/10.6084/m9.figshare.14869167">10.6084/m9.figshare.14869167</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>ArXiv abs/2106.14704</i>, 2021, <a href="https://arxiv.org/abs/2106.14704">https://arxiv.org/abs/2106.14704</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>B. Waspodo, Q. Aini, and S. Nur</b>, "Development of car rental management information system," in <i>Proceeding International Conference on Information Systems For Business Competitiveness (ICISBC)</i>, pp. 101-105, 2011 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>M. N. Osman et al.</b>, "Online Car Rental System Using Web-Based and SMS Technology," <i>Computing Research & Innovation (CRINN)</i>, vol. 2, p. 277, 2017 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>A. Fink and T. Reiners</b>, "Modeling and solving the short-term car rental logistics problem," <i>Transportation Research Part E: Logistics and Transportation Review</i>, vol. 42, no. 4, pp. 272-292, 2006 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>S. M. Khaled et al.</b>, "Software Requirements Specification for Online Car Rental System," 2015 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>B. Harwani</b>, "Installing XAMPP and Joomla," in <i>Foundations of Joomla</i>, pp. 9-51, Apress, Berkeley, CA, 2015 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>Apache Friends</b>, "XAMPP Apache+ MariaDB+ PHP+ Perl," <i>Apache Friends</i>, 2017 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>H. A. Soares and R. S. Moura</b>, "A methodology to guide writing Software Requirements Specification document," in <i>2015 Latin American Computing Conference (CLEI)</i>, pp. 1-11, IEEE, 2015 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>W. J. Carroll and R. C. Grimes</b>, "Evolutionary change in product management: Experiences in the car rental industry," <i>Interfaces</i>, vol. 25, no. 5, pp. 84-104, 1995 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>K. Beck et al.</b>, "Manifesto for agile software development," 2001 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>P. Abrahamsson et al.</b>, "Agile software development methods: Review and analysis," <i>arXiv preprint arXiv:1709.08439</i>, 2017 [Accessed: Jul. 17, 2021].</span>
</div>

</div>


