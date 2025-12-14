---
title: "Digital Bookstore"
date: 2021-07-17T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Backend Development", "Basis Path Testing", "Cyclomatic Complexity", "Data Flow Diagram (DFD)", "Database Management System", "DBMS", "E-commerce", "Frontend Development", "Online Bookstore", "PHP", "PHP Project", "PhpMyAdmin", "Software Engineering", "Software Testing", "System Analysis and Design", "UML Diagrams", "Waterfall Model", "Web Application Development", "Web Development", "White Box Testing", "XAMPP"]
ShowToc: true
TocOpen: false
summary: "Special thanks to Mega Satish for her meaningful contributions, support, and wisdom that helped shape this work. The project's main goal is to build an online book store where users can search for and buy books based on title, author, and subject. The chosen books are shown in a tabular style and the customer may buy them online using a credit card."
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
</style>

<p class="special-thanks">
Special thanks to <a href="https://scholar.google.com/citations?user=7Ajrr6EAAAAJ&hl=en">Mega Satish</a> for her meaningful contributions, support, and wisdom that helped shape this work.
</p>

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




The project's main goal is to build an online book store where users can search for and buy books based on title, author, and subject. The chosen books are shown in a tabular style and the customer may buy them online using a credit card. Using this Website, the user may buy a book online rather than going to a bookshop and spending time. Many online bookstores, such as Powell's and Amazon, were created using HTML. We suggest creating a comparable website with .NET and SQL Server. An online book store is a web application that allows customers to purchase ebooks. Through a web browser the customers can search for a book by its title or author, later can add it to the shopping cart and finally purchase using a credit card transaction. The client may sign in using his login credentials, or new clients can simply open an account. Customers must submit their full name, contact details, and shipping address. The user may also provide a review of a book by rating it on a scale of one to five. The books are classified into different types depending on their subject matter, such as software, databases, English, and architecture. Customers can shop online at the Online Book Store Website using a web browser. A client may create an account, sign in, add things to his shopping basket, and buy the product using his credit card information. As opposed to a frequent user, the Administrator has more abilities. He has the ability to add, delete, and edit book details, book categories, and member information, as well as confirm a placed order. This application was created with PHP and web programming languages. The Online Book Store is built using the Master page, data sets, data grids, and user controls.


---

## Introduction

### Problem Statement

The software to be designed is for a bookstore that wishes to go online. lt is to be developed to improve the efficiency for the customer.
The important features to be developed include:

1.  The Login/Registration module requires the customer to login into the system or he can create an account if he does not yet have one.
2.  Order module requires a customer to enter the book details that he/she wants to buy.
3.  Book detail(s) module allows the system to keep book information in detail by name, genre etc.
4.  Stock management will tell you about the number of books left in the store.
5.  Payment module allows the customer to make online payments like Paytm and credit/debit cards or cash on delivery.
6.  Delivery and tracking module gives information about tracking and by whom it is delivered.
7.  User feedback module.

### Purpose And Motivation

The main objective of the project is to create an online book store that allows users to search and purchase a book based on the title, author and subject. The selected books are displayed in a tabular format and the user can order their books online through credit card payment. The Administrator will have additional functionalities when compared to the common user.

The motivation to create this project has many sources:

1.  Interest to develop a good user-friendly website with many online transactions using a database.
2.  To increase my knowledge horizon in technologies like .NET, SQL, CSS, HTML.
3.  To gain good experience in .NET before joining a full-time job.
4.  To gain expertise using Data Grid, Data Set, Data Table, Data Adapter and Data Readers.

---

## Process Model

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(1)%20Process%20Model.png" caption="Process Model" align="center" >}}

We choose the WATERFALL MODEL due to the following reasons:

1.  This model is chosen because our requirements are very well known, clear and fixed.
2.  Product definition is stable.
3.  There are no ambiguous requirements in our project.
4.  The project is short.
5.  This model is simple and easy to understand and use.
6.  It is easy to manage due to the rigidity of the model – each phase has specific deliverables and a review process.
7.  In this model, phases are processed and completed one at a time. Phases do not overlap.
8.  Waterfall model works well for smaller projects where requirements are very well understood.

First of all the feasibility study is done. Once that part is over the requirement analysis and project planning begins. After the requirements study is done, the design process begins, followed by the coding process. Once the programming is completed the testing is done.

In this model, the sequence of activities performed in a software development project are:

1.  Requirement Analysis
2.  Project Planning
3.  System design
4.  Detail design
5.  Coding
6.  Unit testing
7.  System integration & testing

Here the linear ordering of these activities is critical. End of the phase and the output of one phase is the input of another phase. The output of each phase is to be consistent with the overall requirement of the system. Some of the qualities of the spiral model are also incorporated after the people concerned with the project review completion of each of the phases of the work done.

WATERFALL MODEL was chosen because all requirements were known beforehand and the objective of our software development is the computerization/automation of an already existing manual working system.

---

## Data Flow Diagram (DFD)

The data flow diagram is a graphical representation of the flow of data in an information system. It is capable of depicting incoming data flow, outgoing data flow and stored data. The DFD does not mention anything about how data flows through the system. There is a prominent difference between DFD and Flowchart. The flowchart depicts a flow of control in program modules. DFDs depict the flow of data in the system at various levels. DFD does not contain any control or branch elements.

### Zero Level Data flow Diagram (0 Level DFD) of Digital Bookstore

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(2)%20Zero%20Level%20DFD.jpg" caption="Zero Level DFD" align="center" >}}

### First Level Data flow Diagram (1 Level DFD) of Digital Bookstore

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(3)%20First%20Level%20DFD.jpg" caption="First Level DFD" align="center" >}}

### Second Level Data flow Diagram (2 Level DFD) of Digital Bookstore

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(4)%20Second%20Level%20DFD.jpg" caption="Second Level DFD" align="center" >}}

---

## Class Diagram

The class diagram is a static diagram. It represents the static view of an application. The class diagram is not only used for visualizing, describing, and documenting different aspects of a system but also for constructing executable code of the software application. The class diagram describes the attributes and operations of a class and also the constraints imposed on the system. Since they're the only UML diagrams that can be translated directly to object-oriented languages, class diagrams are frequently utilised in the designing of object-oriented systems. The class diagram shows a collection of classes, interfaces, associations, collaborations, and constraints.

### Purpose of Class Diagram

The class diagram is used to represent the basic perspective of a system. Class diagrams are the only designs that can be highly associated with object-oriented languages and are thus generally applied throughout development. UML diagrams like activity diagrams, sequence diagrams can only give the sequence flow of the application, however, the class diagram is a bit different. That's the most widely used UML diagram in the computing world.

The class diagram's aim may be described as:

1.  Design and development of a software's static view.
2.  Describe the responsibilities of a system.
3.  The base for component and deployment diagrams.
4.  Forward and reverse engineering.

UML class diagrams are useful when modelling business data. By accurately modelling attributes and associations of class entities, we can easily map these class diagram specifications to entity beans with CMP. Class attributes map to abstract access methods for persistent fields, and association roles map to abstract access methods for relationship fields. Navigability determines whether relationship access methods appear in both related entity beans or just one. Furthermore, multiplicity notation determines the correct type for relationship fields, life cycle issues, and cascading delete characteristics.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(5)%20Class%20Diagram.jpg" caption="Class Diagram" align="center" >}}

---

## Sequence Diagram

The sequence diagram represents the flow of messages in the system and is also termed an event diagram. It helps in envisioning several dynamic scenarios. It portrays the communication between any two lifelines as a time-ordered sequence of events, such that these lifelines took part at the run time. In UML, the lifeline is represented by a vertical bar, whereas the message flow is represented by a vertical dotted line that extends across the bottom of the page. It incorporates the iterations as well as branching.

### Purpose of Sequence Diagram

1.  To model high-level interaction among active objects within a system.
2.  To model interaction among objects inside a collaboration realizing a use case.
3.  It either models generic interactions or some certain instances of interaction.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(6)%20Sequence%20Diagram.jpg" caption="Sequence Diagram" align="center" >}}

---

## Collaboration Diagram

The collaboration diagram is used to show the relationship between the objects in a system. Both the sequence and the collaboration diagrams represent the same information but differently. Instead of showing the flow of messages, it depicts the architecture of the object residing in the system as it is based on object-oriented programming. An object consists of several features. Multiple objects present in the system are connected to each other. The collaboration diagram, which is also known as a communication diagram, is used to portray the object's architecture in the system.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(7)%20Collaboration%20Diagram.jpg" caption="Collaboration Diagram" align="center" >}}

---

## Statechart Diagram

A state-chart diagram depicts the various modes of an element in a system. The stages are unique to a system component or item. A state machine is depicted by a Statechart diagram. A state machine is a device that specifies distinct states of an item and controls these states through explicit or implicit events.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(8)%20Statechart%20Diagram.jpg" caption="Statechart Diagram" align="center" >}}

---

## Activity Diagram

Another essential diagram in UML for describing the dynamic features of the system is the activity diagram. It is essentially a flowchart that represents the transition from one activity to another. The action can be defined as a system operation. The control flow is directed from one activity to the next. This flow might be linear, branching, or parallel in nature.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(9)%20Activity%20Diagram.jpg" caption="Activity Diagram" align="center" >}}

---

## Use Case Diagram

A UML use case diagram is the principal form of system/software specifications for an undeveloped computer program. Use cases specify the expected behaviour (what), and not the exact method of making it happen (how). Use cases once specified can be denoted by both textual and visual representation (i.e. use case diagram). A key concept of use case modelling is that it helps us design a system from the end user's perspective. It is an effective technique for communicating system behaviour in the user's terms by specifying all externally visible system behaviour.

A use case diagram is usually simple. It does not show the detail of the use cases:

1.  It only outlines several of the connections between use cases, actors, and systems.
2.  It does not show the order in which steps are performed to achieve the goals of each use case.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(11)%20Use%20Case%20Diagram.jpg" caption="Use Case Diagram" align="center" >}}

---

## Gantt Chart

A Gantt chart is a typical bar chart that is used in project management to visually depict the progress of a development plan across time. Contemporary Gantt charts generally indicate the timetable and status of each job in the task, as well as who is accountable for them.

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(10)%20Gantt%20Chart.jpg" caption="Gantt Chart" align="center" >}}

---

## Database

### Database Connectivity

```php
<?php
define('DB_HOST', 'localhost');
define('DB_NAME', 'digital_bookstore');
define('DB_USER','root');
define('DB_PASSWORD','');
$con=mysqli_connect(DB_HOST,DB_USER,DB_PASSWORD) or die("Failed to connect to MySQL: " . mysql_error());
$db=mysqli_select_db($con,DB_NAME) or die("Failed to connect to MySQL: " . mysql_error());
?>
```

### Database

{{< figure src="Digital%20Bookstore/Figures/Database%20Tables.jpg" caption="Database Tables" align="center" >}}

---

## Testing

We performed White Box Testing (Basis Path Testing) on a function of Online Bookstore and developed the test cases for the same.

### Function (Login Function)

```php
//login function//
Function submit()
{
    $username=$_POST['login_username'];
    $password=$_POST['login_password'];
    $query = "SELECT * from users where UserName = '$username' AND Password = '$password'";
    $result = mysqli_query($con,$query) or die(mysql_error());
    if(mysqli_num_rows($result) > 0)
    {
        $row = mysqli_fetch_assoc($result);
        $_SESSION['user']=$row['UserName'];
        header("Location: index.php?login=" . "Successfully Logged In");
    }
    else
        echo "Incorrect username or password";
}
```

### Flow Graph

{{< figure src="Digital%20Bookstore/Figures/Fig.%20(12)%20Flow%20Graph.jpg" caption="Flow Graph" align="center" >}}

### Independent Paths

**Path 1:** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 14

**Path 2:** 1 → 2 → 3 → 4 → 5 → 6 → 12 → 13 → 14

### Cyclomatic Complexity

1.  **Method 1:**

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
    <i>V</i>(<i>G</i>) = <i>e</i> - <i>n</i> + 2<br>
    In the above control flow graph, where, <i>e</i> = 4 and <i>n</i> = 4<br>
    Therefore, Cyclomatic Complexity<br>
    <i>V</i>(<i>G</i>) = 4 – 4 + 2 = 2
</div>

2.  **Method 2:**

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
     <i>V</i>(<i>G</i>) = <i>P</i> + 1<br>
    In the above control flow graph, where, <i>P</i> = 1<br>
    Therefore, Cyclomatic Complexity<br>
     <i>V</i>(<i>G</i>) = 1 + 1 = 2
</div>

3.  **Method 3:**

<div style="font-family: 'Times New Roman', Times, serif; font-size: 1.5rem; text-align: center; background: rgba(128, 128, 128, 0.08); padding: 30px; border-radius: 8px; margin: 2rem 0; line-height: 1.8;">
     <i>V</i>(<i>G</i>) = Number of Regions<br>
    In the above control flow graph, there are 2 regions
</div>

#### Test Cases

<div align="center">

<p style="font-size: 0.9em; margin-bottom: 10px;">
    <span style="user-select: none;">Table 1: </span>
    Test Cases
</p>

<table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
    <thead>
        <tr style="border-bottom: 2px solid #ccc;">
            <th style="padding: 12px; text-align: center;">Test Case ID</th>
            <th style="padding: 12px; text-align: center;">Input Number</th>
            <th style="padding: 12px; text-align: center;">Output</th>
            <th style="padding: 12px; text-align: center;">Independent Path Covered</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; text-align: center;">1</td>
            <td style="padding: 12px; text-align: center;">1</td>
            <td style="padding: 12px; text-align: center;">Login</td>
            <td style="padding: 12px; text-align: left;">1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 14</td>
        </tr>
        <tr style="border-bottom: 1px solid #eee;">
            <td style="padding: 12px; text-align: center;">2</td>
            <td style="padding: 12px; text-align: center;">0</td>
            <td style="padding: 12px; text-align: center;">No Login</td>
            <td style="padding: 12px; text-align: left;">1 → 2 → 3 → 4 → 5 → 6 → 12 → 13 → 14</td>
        </tr>
    </tbody>
</table>

</div>

---

## YouTube Demonstration

{{< youtube JuUix8olOC8 >}}

---

## Conclusion

The transition from buying written books in bookshops to ordering them online or even simply digital versions has had a significant impact on the industry, including retailers and libraries, as well as the general public throughout the globe. We present an application developed using software engineering methodologies. Digital Bookstore allows the users to buy as well as review books online. Consumers can login and search for their books, whether it is available or out of stock. Users can also give feedback. We have implemented and tested the web application to satisfy the user specifications.

---

## Additional Resources

### Project Source & Study Materials

Access the complete source code for this Digital Bookstore project, research paper, preprint, lecture notes, and related Database Management System (DBMS) study materials via the links below:

<div style="display: flex; flex-direction: column; gap: 8px;">

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/DIGITAL-BOOKSTORE" target="_blank">Digital Bookstore Repository</a>
  </div>

  <div>
    <!-- viXra Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 8px;"><title>viXra</title><path d="M0 0h3v3h3v3h3v3h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3zM21 0h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3zM6 15h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3z" /></svg>
    <a href="https://vixra.org/abs/2108.0142" target="_blank">viXra Preprint</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://doi.org/10.22214/ijraset.2021.36609" target="_blank">Full Paper (IJRASET)</a>
  </div>

  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/JuUix8olOC8" target="_blank">YouTube Demonstration</a>
  </div>

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/DATABASE-MANAGEMENT-SYSTEM-AND-DATABASE-MANAGEMENT-SYSTEM-LAB" target="_blank">Database Management System</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://github.com/Amey-Thakur/DATABASE-MANAGEMENT-SYSTEM-AND-DATABASE-MANAGEMENT-SYSTEM-LAB?tab=readme-ov-file#mega-notes" target="_blank">Mega's Notes (Special thanks to Mega Satish for her helpful notes)</a>
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>International Research Journal of Engineering and Technology (IRJET)</i>, pp. 1948–1951, June 2021, DOI: <a href="https://doi.org/10.6084/m9.figshare.14869167">10.6084/m9.figshare.14869167</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>ArXiv abs/2106.14704</i>, 2021, DOI: <a href="https://doi.org/10.48550/arXiv.2106.14704">10.48550/arXiv.2106.14704</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>A. Thakur</b>, "Car Rental System," <i>International Journal for Research in Applied Science and Engineering Technology (IJRASET)</i>, vol. 9, no. 7, pp. 402-412, 2021, DOI: <a href="https://doi.org/10.22214/ijraset.2021.36339">10.22214/ijraset.2021.36339</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>D. Raggett, A. Le Hors, and I. Jacobs</b>, "HTML 4.01 Specification," <i>W3C recommendation</i>, Dec. 1999. [Online]. Available: <a href="https://www.w3.org/TR/html401/">https://www.w3.org/TR/html401/</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>H. Refsnes, S. Refsnes, and K. J. Refsnes</b>, "Learn JavaScript and Ajax with w3school," <i>Wiley Publishing, Inc</i>, 2010. [Online]. Available: <a href="https://dokumen.pub/learn-javascript-and-ajax-with-w3schools-0470611944-9780470611944.html">https://dokumen.pub/learn-javascript-and-ajax-with-w3schools-0470611944-9780470611944.html</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>G. K. Gill and C. F. Kemerer</b>, "Cyclomatic complexity density and software maintenance productivity," <i>IEEE Transactions on Software Engineering</i>, vol. 17, no. 12, pp. 1284-1288, 1991, DOI: <a href="https://doi.org/10.1109/32.106988">10.1109/32.106988</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>C. Ebert, J. Cain, G. Antoniol, S. Counsell, and P. Laplante</b>, "Cyclomatic complexity," <i>IEEE Software</i>, vol. 33, no. 6, pp. 27-29, 2016, DOI: <a href="https://doi.org/10.1109/MS.2016.147">10.1109/MS.2016.147</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>M. Delisle</b>, "Mastering phpMyAdmin 3.1 for effective MySQL management," <i>Packt Publishing Ltd</i>, 2009. [Online]. Available: <a href="https://www.abebooks.com/9781847197863/Mastering-phpMyAdmin-3.1-Effective-MySQL-1847197868/plp">https://www.abebooks.com/9781847197863/Mastering-phpMyAdmin-3.1-Effective-MySQL-1847197868/plp</a> [Accessed: Jul. 17, 2021].</span>
</div>

</div>


