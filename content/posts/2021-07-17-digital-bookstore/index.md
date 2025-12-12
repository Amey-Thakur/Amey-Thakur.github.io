---
title: "Digital Bookstore"
date: 2021-07-17T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["C++", "E-commerce", "Database Management", "System Design", "CLI", "Bookstore", "Inventory System"]
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




The transition from physical ledgers to digital databases is a critical step for modern retail. This project implements a **Digital Bookstore Management System** using **C++**, designed to automate the lifecycle of book sales. From inventory management to customer billing, the system leverages efficient data structures to provide search times of $O(\log n)$ and secure transaction handling. It serves as a case study in applying computer science fundamentals to real-world business problems.

---

## The Virtual Librarian

Managing a bookstore manually is prone to human error.

### The Analogy: The Index Card System
*   **Manual**: To find a book, you walk to a physical cabinet and flip through index cards. If a card is misfiled, the book is "lost."
*   **Digital (This System)**: The computer is the librarian. You type "Harry Potter," and it instantly checks the digital index. It doesn't just tell you *where* it is, but *how many* are left, *how much* it costs, and *automatically* deducts one when sold. It's a librarian with a photographic memory and a calculator.

---

## Key Features

*   **Smart Search**: Allows users to find books by Title, Author, or ISBN.
*   **Stock Alerts**: Automatically flags books when inventory dips below a threshold.
*   **Admin Dashboard**: A secure interface for managers to update prices and stock levels.

---

## Publication Details

This work was published in the **International Journal of Research in Applied Science and Engineering Technology (IJRASET)**.

**Publication Details:**
*   **Journal**: IJRASET - Volume 9, Issue 7
*   **Title**: Digital Bookstore
*   **Reference**: [IJRASET Publication](Digital%20Bookstore/Digital%20Bookstore.pdf)

### Additional Resources
*   [Source Code](https://github.com/Amey-Thakur/Digital-Bookstore)

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Digital Bookstore". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-17-digital-bookstore/.</code></pre>

**Or use the BibTex citation:**


```
@article{thakur2021bookstore,
  title   = "Digital Bookstore",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-17-digital-bookstore/"
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>International Research Journal of Engineering and Technology (IRJET)</i>, pp. 1948–1951, June 2021, DOI: <a href="https://doi.org/10.6084/m9.figshare.14869167">10.6084/m9.figshare.14869167</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>ArXiv</i>, abs/2106.14704, 2021 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>A. Thakur</b>, "Car Rental System," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET)</i>, vol. 9, no. 7, pp. 402-412, 2021, DOI: <a href="https://doi.org/10.22214/ijraset.2021.36339">10.22214/ijraset.2021.36339</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>D. Raggett, A. Le Hors, and I. Jacobs</b>, "HTML 4.01 Specification," <i>W3C recommendation</i>, Dec. 1999 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>H. Refsnes, S. Refsnes, and K. J. Refsnes</b>, "Learn JavaScript and Ajax with w3school," <i>Wiley Publishing, Inc</i>, 2010 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>G. K. Gill and C. F. Kemerer</b>, "Cyclomatic complexity density and software maintenance productivity," <i>IEEE Transactions on Software Engineering</i>, 1991 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>C. Ebert, J. Cain, G. Antoniol, S. Counsell, and P. Laplante</b>, "Cyclomatic complexity," <i>IEEE Software</i>, vol. 33, no. 6, pp. 27-29, 2016 [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>M. Delisle</b>, "Mastering phpMyAdmin 3.1 for effective MySQL management," <i>Packt Publishing Ltd</i>, 2009 [Accessed: Jul. 17, 2021].</span>
</div>

</div>


