---
title: "Multi-Client Chat Room: Socket Programming in Python"
date: 2021-06-28T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Networking", "Socket Programming", "Python", "Chat Application", "TCP/IP", "Multi-threading", "Client-Server"]
ShowToc: true
TocOpen: false
description: "A robust multi-threaded chat application demonstrating the fundamentals of TCP/IP socket programming."
---

## 📋 Abstract

Before WhatsApp or Slack, there were raw sockets. Understanding how data packets travel between two computers is fundamental to network engineering. This project builds a **Multi-Client Chat Room** from scratch using Python's `socket` and `threading` libraries. It implements a TCP-based server that can handle concurrent connections, broadcasting messages from one client to all others in real-time, effectively mimicking the core architecture of modern messaging platforms [[1]](#ref-1).

---

## 🔌 The Digital Switchboard

How does a server handle 100 people talking at once?

### The Analogy: The Telephone Operator
Imagine a vintage telephone switchboard.
*   **The Server**: The operator sitting at the board. They don't generate messages; they just connect lines.
*   **The Clients**: People calling in.
*   **The Challenge**: If the operator talks to Caller A, Caller B gets a busy signal.
*   **The Solution (Threading)**: We hire a team of operators (threads). The main operator just answers the phone and immediately hands the connection to a sub-operator. This way, the main line is always open for new calls, and existing calls can happen simultaneously.

---

## 🛠️ System Design

The application logic follows a strict Data Flow Diagram (DFD) to ensure reliable message delivery.

{{< figure src="figures/fig-1-flow-diagram.png" caption="Flow Diagram of Client-Server Interaction" align="center" >}}

### Core Components
1.  **The Server (`server.py`)**:
    *   Binds to a specific IP and Port (e.g., `127.0.0.1:55555`).
    *   Listens for incoming TCP connections.
    *   On `accept()`, it spawns a new thread to handle that specific client.
    *   Maintains a list of active `clients` to broadcast messages.

2.  **The Client (`client.py`)**:
    *   Connects to the server.
    *   Runs two threads: one for **Listening** (receiving messages) and one for **Writing** (sending user input). This separation allows sending a message without blocking incoming ones.

{{< figure src="figures/fig-3-1-level-dfd.png" caption="Level-1 Data Flow Diagram" align="center" >}}

### Live Demo
<video width="100%" controls>
  <source src="Chat%20Room.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
<p style="text-align: center; font-size: 14px; margin-top: 10px;"><em>Figure 3: Video Demonstration of the Chat Room Application</em></p>

---

## 📄 Publication Details

This project was published in the **International Research Journal of Engineering and Technology (IRJET)**.

### Additional Resources
*   [Full Paper (PDF)](IRJET-%20Chat%20Room%20using%20HTML,%20PHP,%20CSS,%20JS,%20AJAX.pdf)

{{< figure src="CHAT%20ROOM%20POSTER.png" caption="Project Poster Presentation" align="center" >}}

---

## Citation

**Cited as:**

> Thakur, Amey. \"Multi-Client Chat Room: Socket Programming in Python\". AmeyArc (Jun 2021). https://amey-thakur.github.io/posts/2021-06-28-chatroom/.

**BibTeX:**

```
@article{thakur2021chatroom,
  title   = "Multi-Client Chat Room: Socket Programming in Python",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jun",
  url     = "https://amey-thakur.github.io/posts/2021-06-28-chatroom/"
}
```

## 📚 References

1. <a id="ref-1"></a> **Thakur, A.** (2021). Chat Room using HTML, PHP, CSS, JS, AJAX. *International Research Journal of Engineering and Technology (IRJET)*, 8(6).

---
*Authored by Amey Thakur.*
