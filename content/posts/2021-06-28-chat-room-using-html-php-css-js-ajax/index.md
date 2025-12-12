---
title: "Chat Room Using HTML, PHP, CSS, JS, AJAX"
date: 2021-06-28T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["AJAX", "Anonymous Chat", "Bidirectional Communication", "Chat Application", "Chat Room", "Client-Server Architecture", "CSS", "Data Flow Diagram", "Database Design", "HTML", "Instant Messaging", "JavaScript", "jQuery", "Live Chat", "Multi-threading", "MySQL", "Networking", "Online Communication", "PHP", "phpMyAdmin", "Real-Time Messaging", "Socket Programming", "TCP/IP", "UI/UX Design", "Web Application", "Web Development"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Karan Dhiman for his meaningful contributions, support, and wisdom that helped shape this work. Earlier there was no mode of online communication between users. In big or small organizations communication between users posed a challenge. The main objective of our Simple Chat Room project is to create a chat application that helps different users to communicate with each other through a server connected."

---

<style>
.special-thanks {
    font-size: 0.9rem;
    color: #1a73e8; /* Standard Blue for Light Mode */
    margin-bottom: 1.5rem;
}

.special-thanks a {
    color: #1a73e8;
    text-decoration: underline;
    border: none;
    background-image: none;
    box-shadow: none;
    text-underline-offset: 3px;
    transition: all 0.3s ease;
}

.special-thanks a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676; /* Subtle glow/bolding effect without lift */
}

[data-theme="dark"] .special-thanks {
    color: #64b5f6; /* Lighter Blue for Dark Mode readability */
}

[data-theme="dark"] .special-thanks a {
    color: #64b5f6;
}

[data-theme="dark"] .special-thanks a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Invert diagrams in dark mode for better arrow visibility */
[data-theme="dark"] .post-content img[src*="Flow Diagram"],
[data-theme="dark"] .post-content img[src*="Fig."],
[data-theme="dark"] .post-content img[src*="DFD"],
[data-theme="dark"] .post-content img[src*="level"] {
    filter: invert(1) hue-rotate(180deg);
    mix-blend-mode: normal;
}
</style>

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=kKNKmqgAAAAJ&hl=en">Karan Dhiman</a> for his meaningful contributions, support, and wisdom that helped shape this work.
</p>

Earlier there was no mode of online communication between users. In big or small organizations communication between users posed a challenge. There was a requirement to record these communications and store the data for further evaluation. The idea is to automate the existing Simple Chat Room system and make the users utilize the software so that their valuable information is stored digitally and can be retrieved for further management purposes. There was no online method of communicating with different users. There were many different interfaces available in the market but this method of using windows sockets to communicate between nodes would be fast and reliable. The main objective of our Simple Chat Room project is to create a chat application that helps different users to communicate with each other through a server connected. This is a simple chat program with a server and can have many clients. The server needs to be started first and clients can be connected later. Simple Chat Room provides bidirectional communication between client and server. It enables users to seamlessly communicate with each other. The user can chat using this chat application. If the user at the other end is active then they can start a chat session. The chat is recorded in this application.

---

## Project Poster Presentation

{{< figure src="Chat Room Using HTML, PHP, CSS, JS, AJAX/CHAT ROOM POSTER.png" caption="Project Poster Presentation" align="center" >}}

---

## Introduction

We propose an application that allows users to create a chat room with a live server and share messages or talk while on the road. Create an instant messaging system that allows users to interact with one another while still being simple enough for a beginning user to utilise. For example, a real-time chat room (online). Teleconferencing, often known as chat, is a technique of bringing people and ideas "together" despite geographical obstacles. Although the technology has been accessible for many years, its adoption is relatively new. This is an example of a chat server in this small project. The chat application is straightforward. It doesn't require a login, has AJAX-style functionality, and will support numerous users. It consists of two applications: the client app, which runs on the user's device, and the server programme, which is hosted to operate the chat room live over the network. To begin talking, clients should connect to a server where they can practise two types of chatting, public (message is broadcasted to all connected users) and private (between any two users alone), and security precautions were implemented during the latter.

---

## Proposed System

### Architecture of Chat Room

Application for Chat Rooms A data flow diagram is usually used as a first stage to develop an overview of the Chat Application without going into depth, which could then be worked upon later. Some of the user’s flow and related entities described are Chat, Chat History, Smiley Chat, Chat User, Chat Group, Chat Profile, and Delete Conversation. The diagrams below are used to visualize data processing and a better design of the Chat Application process and activity.

{{< figure src="Chat Room Using HTML, PHP, CSS, JS, AJAX/figures/Fig. (1) Flow Diagram.png" caption="Flow Diagram" align="center" >}}

### Zero Level Data Flow Diagram (0 Level DFD) of Chat Room Application

This is the Zero Level DFD of an Online Chat Application, in which we have explained the high-level methodology of the Chat Application. It's meant to give you a brief explanation of Chat User, Chat Group, and Delete Chat by representing the system as a single high-level process with relations to various entities such as Chat, Chat History and Chat Profile. It is a high-level overview of the entire Online Chat Application or process that is being studied or modelled.
It should be understood to a number of different groups, including Chat Profile & Chat User. In the zero levels DFD of Chat Rooms Application, we described the high-level flow of the Chat Application system.
High-Level Entities and process flow of Online Chat Application are given in the diagram below:

{{< figure src="Chat Room Using HTML, PHP, CSS, JS, AJAX/figures/Fig. (2) 0 level DFD.png" caption="0 level DFD" align="center" >}}

### One Level Data Flow Diagram (1 Level DFD) of Chat Room Application

The first level DFD (1st Level) of the Chat Rooms Application provided in this section is segmented into subdivisions (processes), each of which handles one or more data flows to or from an external agent, and which together offers all of the Chat Rooms System application's functions. It also identifies internal data storage like Chat Users and Smiley Chat. DFD Level one is a more in-depth variation of DFD Level two. You'll outline the Chat Application's most key aspects in the diagram given below:

{{< figure src="Chat Room Using HTML, PHP, CSS, JS, AJAX/figures/Fig. (3) 1 level DFD.png" caption="1 level DFD" align="center" >}}

### Two-Level Data Flow Diagram (2 Level DFD) of Chat Room Application

DFD Level two then delves further into aspects of Level one of the Chat Application. More Chat Application features may be required to achieve the required amount of detail regarding the Chat Application's operation. The first level DFD (1st Level) of the Online Chat System demonstrates how the system is split into subsystems (processes). More about second-level DFD, one may have more information on Chat Group, Chat User, Smiley Chat, Delete Chat, Chat Profile, Chat History, and Chat.

{{< figure src="Chat Room Using HTML, PHP, CSS, JS, AJAX/figures/Fig. (4) 2 level DFD.png" caption="2 level DFD" align="center" >}}

### Applications of Chat Room System

Here are some examples of chat room system applications:
1.	Google Chat
2.	Chat Room on Google Meet
3.	Hangouts on Google
4.	Microsoft Teams Chat Room
5.	Chat Room for Zoom Meeting

---

## Literature Survey

Between ancient times till the 15th century, communication began to change. While it is exciting, we do have other things to do. So this is what I'll say in conclusion: Prior to the 15th century, communication depended mostly on verbal and minor written communication. People interacted with one another and made handwritten notes for people. Everything improved after the printing. The press was invented to reduce the necessity for all paper messages to be written by hand.

The public postal declaration was made in the 18th century. Before this time period, letters were distributed, but the procedure was broken and inefficient. It could take months before mail to reach, and even when it did, it was deposited at a random public spot.

As the 19th century began, great thinkers focusing on improving communication made great progress. The name telecommunications was developed after electricity was introduced into communication routes. Telecommunications provided people with a way to make long-distance written and verbal communication personal. For all of those who wished to connect orally, the distance became less of an obstacle, permitting greater information to flow.

In the early 1900s, radio and television became valuable sources of information. They not only offered musical delight, but they also alerted listeners with news, sports, and the weather. We all know that email and PCs were just the beginning of the most important innovations in communication. But these origins can’t be forgotten. Every communication tool used today was somehow influenced by simple ones from the long and never-ending history of communication.

21st-century communication. When thinking of modern-day communication, keeping the idea of the Information Age in mind is important. The Information Age refers to the transition from industry to information technology. Simply put, everything is digital and knowledge has never been more powerful. People want information, and the best way to get it is through communication tools.

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 1: </span>
    Comparison of Chat Room System with the Previous system
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9em;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 10px; text-align: center;">Basis</th>
            <th style="padding: 10px; text-align: center;">Chat Room</th>
            <th style="padding: 10px; text-align: center;">Google chat</th>
            <th style="padding: 10px; text-align: center;">Google Meet Chat Room</th>
            <th style="padding: 10px; text-align: center;">Microsoft Teams Chat Room</th>
            <th style="padding: 10px; text-align: center;">Zoom meeting chat room</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Number of participants</td>
            <td style="padding: 10px;">Limitless</td>
            <td style="padding: 10px;">150</td>
            <td style="padding: 10px;">250</td>
            <td style="padding: 10px;">250</td>
            <td style="padding: 10px;">100</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Number of characters</td>
            <td style="padding: 10px;">255</td>
            <td style="padding: 10px;">160</td>
            <td style="padding: 10px;">4000</td>
            <td style="padding: 10px;">1000</td>
            <td style="padding: 10px;">128</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Cost</td>
            <td style="padding: 10px;">Free</td>
            <td style="padding: 10px;">Paid</td>
            <td style="padding: 10px;">Free Trial</td>
            <td style="padding: 10px;">Free Trial</td>
            <td style="padding: 10px;">Paid</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Anonymity</td>
            <td style="padding: 10px;">Yes</td>
            <td style="padding: 10px;">No</td>
            <td style="padding: 10px;">No</td>
            <td style="padding: 10px;">No</td>
            <td style="padding: 10px;">No</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 10px; font-weight: bold;">Launch Year</td>
            <td style="padding: 10px;">2020</td>
            <td style="padding: 10px;">2017</td>
            <td style="padding: 10px;">2020</td>
            <td style="padding: 10px;">2017</td>
            <td style="padding: 10px;">2013</td>
        </tr>
    </tbody>
</table>

</div>

---

## Problem Statement

### Problem Statement

Develop an application that facilitates the creation of a chat room with a live server for the users to enable sharing messages or chat on the go. Develop an instant messaging system that allows users to connect effortlessly with each other and still being simple to use. I.e. Live chat room on the fly (online).

### Problem Solution

Chat Room as a service is a model of communication deployment where the server hosts a live chat room as a service for users on the Internet. Users are admissible to enter the chat room and share messages or interact with each other. The project has been created keeping in mind the fact that the anonymity of the users will not be compromised under any circumstances. Our aim is to identify a solution to use networks to serve people and ideas throughout geographical boundaries. 

### Chat Room scope and features

Chat Server Application will be a text communication programme that can communicate between two computers via a point-to-point connection. This project's main characteristic is its anonymity. Our project's drawback is that it does not support audio chats. Companies want communication software that allows them to communicate immediately inside their organisation. Because software operates on an intranet within the company, it is extremely safe from outside threats.

---

## Design and Connectivity

### Design Process

User experience or (UI) design is the process through which designers create interfaces in software or electronic devices with an emphasis on aesthetics or style. Designers strive to develop interfaces that are both easy to use and enjoyable for users. Graphical user interfaces and various kinds of user interface design are examples of UI design. To design System Layout Architecture we need to have UI and Database and to connect these two using PHP connectivity.

{{< figure src="Chat Room Using HTML, PHP, CSS, JS, AJAX/User Interface.png" caption="User Interface" align="center" >}} 

### Database Design

A database can be comparable to a sophisticated digital format cabinet. It's what might help us organise all or most of the data throughout our app. We have total control over inserting, altering, and deleting from our database.
Tables, that may be considered as file directories, make databases. Tables are rows of information that may be thought of as independent papers within a file folder. We will add new entries to that database every time an amount is charged, just as we could add further pieces of paper to our file folder.
Our database contains an amount of data, such as the amount, bill number, and date paid. We will be able to collect, preserve, modify, and examine information in our web app due to the database. We do have the capability to obtain information that has been submitted into our database 
A query is a command with which we could send to our database that directs it to perform specific operations.

### Database connection 

```php
<?php 
$host = "localhost"; 
$user = "root"; 
$pass = ""; 
$db_name = "chat_info"; 
$con = new mysqli($host,$user,$pass,$db_name); 
function formatDate($date) 
{ 
return date('g:i a',strtotime($date)); 
} 
?>
```

---

## YouTube Demonstration

{{< youtube Aem0k2Dl9fU >}}

---

## Conclusions

Chat Room achieves its goal by delivering an exceptionally rich conversation experience. We attempted to keep the UI clear and clean, with no obnoxious or unnecessary embellishments. Design flexibility encourages users to utilise their creativity, and as a result, even inexperienced users may create effective websites. We have used PHP, MySQL, JavaScript, and Ajax to build a dynamic internet messaging system.
There is always an opportunity for improvement in every product, and we attempted to adjust the design accordingly, while still keeping our constraints in mind. During the course of developing this application, we faced a slew of issues and learned how to solve them through study. With the end product, we think our idea was evident and well-presented.

---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="/posts/2021-06-28-chat-room-using-html-php-css-js-ajax/Chat%20Room%20Using%20HTML,%20PHP,%20CSS,%20JS,%20AJAX/Presentation%20-%20CHAT%20ROOM%20USING%20HTML,%20PHP,%20CSS,%20JS,%20AJAX%20PRESENTATION.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

### Research Paper, Source Code & Project Resources
Explore the published research paper, source code repository, video demonstration, and related project materials:

<div style="display: flex; flex-direction: column; gap: 8px;">

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://www.irjet.net/archives/V8/i6/IRJET-V8I6348.pdf" target="_blank">Full Paper (IRJET)</a>
  </div>

  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/Aem0k2Dl9fU" target="_blank">YouTube Demonstration</a>
  </div>

  <div>
    <!-- Globe/DOI Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
    <a href="https://doi.org/10.13140/RG.2.2.16257.38248" target="_blank">ResearchGate Presentation (DOI)</a>
  </div>

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/CHAT-ROOM" target="_blank">Chat Room Project Repository</a>
  </div>

  <div>
    <!-- Globe/DOI Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
    <a href="https://doi.org/10.13140/RG.2.2.19421.95203" target="_blank">ResearchGate Poster (DOI)</a>
  </div>
  
  <div>
    <!-- Globe/DOI Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
    <a href="https://doi.org/10.13140/RG.2.2.16257.38248" target="_blank">Preprint (DOI)</a>
  </div>

  <div>
    <!-- arXiv Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" stroke="none" style="vertical-align: middle; margin-right: 8px;"><path d="M3.8423 0a1.0037 1.0037 0 0 0-.922.6078c-.1536.3687-.0438.6275.2938 1.1113l6.9185 8.3597-1.0223 1.1058a1.0393 1.0393 0 0 0 .003 1.4229l1.2292 1.3135-5.4391 6.4444c-.2803.299-.4538.823-.2971 1.1986a1.0253 1.0253 0 0 0 .9585.635.9133.9133 0 0 0 .6891-.3405l5.783-6.126 7.4902 8.0051a.8527.8527 0 0 0 .6835.2597.9575.9575 0 0 0 .8777-.6138c.1577-.377-.017-.7502-.306-1.1407l-7.0518-8.3418 1.0632-1.13a.9626.9626 0 0 0 .0089-1.3165L4.6336.4639s-.3733-.4535-.768-.463zm0 .272h.0166c.2179.0052.4874.2715.5644.3639l.005.006.0052.0055 10.169 10.9905a.6915.6915 0 0 1-.0072.945l-1.0666 1.133-1.4982-1.7724-8.5994-10.39c-.3286-.472-.352-.6183-.2592-.841a.7307.7307 0 0 1 .6704-.4401Zm14.341 1.5701a.877.877 0 0 0-.6554.2418l-5.6962 6.1584 1.6944 1.8319 5.3089-6.5138c.3251-.4335.479-.6603.3247-1.0292a1.1205 1.1205 0 0 0-.9763-.689zm-7.6557 12.2823 1.3186 1.4135-5.7864 6.1295a.6494.6494 0 0 1-.4959.26.7516.7516 0 0 1-.706-.4669c-.1119-.2682.0359-.6864.2442-.9083l.0051-.0055.0047-.0055z"></path></svg>
    <a href="https://arxiv.org/abs/2106.14704" target="_blank">arXiv Preprint</a>
  </div>

  <div>
    <!-- Graduation Cap Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    <a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING" target="_blank">Computer Engineering Resources</a>
  </div>

</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Chat Room Using HTML, PHP, CSS, JS, AJAX". AmeyArc (Jun 2021). https://amey-thakur.github.io/posts/2021-06-28-chat-room-using-html-php-css-js-ajax/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2021chatroom,
  title   = "Chat Room Using HTML, PHP, CSS, JS, AJAX",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2021",
  month   = "Jun",
  url     = "https://amey-thakur.github.io/posts/2021-06-28-chat-room-using-html-php-css-js-ajax/"
}
```

---

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
    <span class="reference-text"><a id="ref-1"></a><b>H. Refsnes, S. Refsnes, K. J. Refsnes, J. E. Refsnes, and K. D. Henthorne</b>, "Learn JavaScript and Ajax with w3schools," <i>Wiley Publishing</i>, 2010, <a href="https://www.wiley.com/">https://www.wiley.com/</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>J. J. Garrett</b>, "Ajax: A new approach to web applications," <i>Adaptive Path</i>, Feb. 2005, <a href="https://web.archive.org/web/20080702075113/http://www.adaptivepath.com/ideas/essays/archives/000385.php">https://web.archive.org/web/20080702075113/http://www.adaptivepath.com/ideas/essays/archives/000385.php</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>M. Kofler</b>, "phpMyAdmin," in <i>The Definitive Guide to MySQL5</i>, pp. 87-116, Apress, Berkeley, CA, 2005, DOI: <a href="https://doi.org/10.1007/978-1-4302-0071-0_6">10.1007/978-1-4302-0071-0_6</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>C. Musciano and B. Kennedy</b>, "HTML & XHTML: The Definitive Guide," 6th ed., <i>O'Reilly Media, Inc.</i>, 2006, <a href="https://www.oreilly.com/library/view/html-xhtml/0596527322/">https://www.oreilly.com/library/view/html-xhtml/0596527322/</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>D. Raggett, A. Le Hors, and I. Jacobs</b>, "HTML 4.01 Specification," <i>W3C Recommendation</i>, Dec. 1999, <a href="https://www.w3.org/TR/html401/">https://www.w3.org/TR/html401/</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>Q. Li and Y.-L. Chen</b>, "Data flow diagram," in <i>Modeling and Analysis of Enterprise and Information Systems</i>, pp. 85-97, Springer, Berlin, Heidelberg, 2009, DOI: <a href="https://doi.org/10.1007/978-3-540-89556-5_4">10.1007/978-3-540-89556-5_4</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>W. Wu, L. Chen, and Q. Yang</b>, "Students' Personality and Chat Room Behavior in Synchronous Online Learning," in <i>UMAP (Extended Proceedings)</i>, 2016, <a href="https://pure.ecnu.edu.cn/zh/publications/students-personality-and-chat-room-behavior-in-synchronous-online/">https://pure.ecnu.edu.cn/zh/publications/students-personality-and-chat-room-behavior-in-synchronous-online/</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>B. D. Blansit</b>, "An Introduction to Cascading Style Sheets (CSS)," <i>Journal of Electronic Resources in Medical Libraries</i>, vol. 5, no. 4, pp. 395-409, 2008, DOI: <a href="https://doi.org/10.1080/15424060802453811">10.1080/15424060802453811</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>W3Schools</b>, "W3Schools Online Web Tutorials," 2013, <a href="https://www.w3schools.com/">https://www.w3schools.com/</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>B. Bibeault and Y. Katz</b>, "jQuery in Action," 2nd ed., <i>Manning Publications</i>, 2010, <a href="https://www.manning.com/books/jquery-in-action-second-edition">https://www.manning.com/books/jquery-in-action-second-edition</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>B. Efron and R. J. Tibshirani</b>, "An Introduction to the Bootstrap," <i>Chapman and Hall/CRC</i>, 1994, DOI: <a href="https://doi.org/10.1201/9780429246593">10.1201/9780429246593</a> [Accessed: Jun. 28, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>T. Hesterberg</b>, "Bootstrap," <i>Wiley Interdisciplinary Reviews: Computational Statistics</i>, vol. 3, no. 6, pp. 497-526, 2011, DOI: <a href="https://doi.org/10.1002/wics.182">10.1002/wics.182</a> [Accessed: Jun. 28, 2021].</span>
</div>

</div>
