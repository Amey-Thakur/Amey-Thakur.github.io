---
title: "Car Rental System: A C++ Object-Oriented Design"
date: 2021-07-17T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["C++", "OOP", "Software Design", "System Architecture", "Console Application", "File Handling", "Management System"]
ShowToc: true
TocOpen: false
description: "A comprehensive console-based management system demonstrating Object-Oriented Programming principles in C++."
---

## 📋 Abstract

Legacy systems in the automotive rental industry often suffer from inefficiency and lack of scalability. This project presents a **Car Rental Management System** built using **C++**, designed to streamline operations through Object-Oriented Programming (OOP) principles. By encapsulating logic within `Car`, `Customer`, and `Rental` classes, the system ensures data integrity and modularity. Key features include real-time inventory tracking, bill generation, and persistent data storage using file handling.

---

## 🧩 Modularity in Design

Why use Classes instead of just functions?

### The Analogy: The Lego Kit
*   **Procedural Code**: Is like a clay model. It's one big blob. If you want to change the tire, you have to reshape the whole side of the car.
*   **OOP (This System)**: Is like a Lego kit. The "Tire" is a separate brick (Class). The "Engine" is a separate brick. You can swap the tire without touching the engine. In our system, we can upgrade the `billing` logic without breaking the `car inventory` logic because they are separate, self-contained objects.

---

## 💻 System Architecture

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

## 📄 Publication Details

This work was published in the **International Journal of Research in Applied Science and Engineering Technology (IJRASET)**.

**Publication Details:**
*   **Journal**: IJRASET - Volume 9, Issue 7
*   **Title**: Car Rental System
*   **Reference**: [IJRASET Publication](Car%20Rental%20System.pdf)

### Additional Resources
*   [Source Code](https://github.com/Amey-Thakur/Car-Rental-System)

## Citation

**Cited as:**

> Thakur, Amey. \"Car Rental System: A C++ Object-Oriented Design\". AmeyArc (Jul 2021). https://amey-thakur.github.io/posts/2021-07-17-car-rental-system/.

**BibTeX:**

```
@article{thakur2021carrental,
  title   = "Car Rental System: A C++ Object-Oriented Design",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jul",
  url     = "https://amey-thakur.github.io/posts/2021-07-17-car-rental-system/"
}
```

---
*Authored by Amey Thakur.*
