---
title: "Car Rental System"
date: 2021-07-17T00:00:00-05:00
draft: false
author: "Amey Thakur"
tags: ["Backend Development", "Car Rental System", "Database Management System", "DBMS", "Frontend Development", "MySQL", "Online Reservation System", "PHP", "PHP Project", "PhpMyAdmin", "Software Engineering", "System Analysis and Design", "Web Application Development", "Web Development", "XAMPP"]
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

Customers will be able to reserve their vehicles from anywhere in the world due to the Car Rental System. Consumers provide information to this application by filling in their personal information. When a consumer creates an account on the website, he or she can reserve a car. The proposed system is an online system that is fully integrated. It effectively and efficiently automates manual procedures. Customers are aided by this automated method, which allows them to fill in the specifics according to their needs. It contains information on the sort of car they want to hire as well as the location. The goal of this system is to create a website where customers can book their automobiles and request services from anywhere in the world. There are three phases to this car rental system mentioned in the introduction.

---

## Introduction

There are three phases to this car rental system.

1.  The first phase entails organising car rental locations into pools and allowing pooled car rental outlets to share a fleet of automobiles.
2.  The second phase for each pool determines the types and quantities of cars to be acquired and delivered to the auto manufacturer, as well as the geographic redistribution of automobiles among pools across the long-term planning horizon.
3.  The third phase entails day-to-day operations, during which the fleet's deployment within each pool and among its locations is determined.

### Need for Car Rental System

Nowadays, there is Online Car Rental, which benefits users greatly. A rental service is one where customers come to seek the rental of a rental unit. It is more convenient than paying for the unit's ownership and maintenance. A car rental company lends autos for a price for a few hours, a few days, or a week or more.

### Objective of Car Rental System

The project's goal is to automate vehicle rental and reservation so that clients don't have to waste time calling and waiting for a vehicle. To convert the manual car rental procedure into a digital method. A customer satisfaction test was used to validate the rental automobile system. As a system development reference, create documents such as Software Requirement Specification (SRS) and Software Design Description.

### Methodology/Procedure

The database was designed on PHPMYADMIN, the back end was developed in simple PHP, and we utilised the same basic PHP codes for the frontend. Software methods are concerned with the process of developing software, not so much with the technical elements as with the organisational ones. Since the dawn of information technology, a variety of software development methodologies have been employed.

### Project Framework

A framework is a set of defined concepts, techniques, and criteria for dealing with a certain type of problem that may be used as a guide for approaching and resolving future challenges of the same sort.

### Data and Information

Data gathering plays a vital function in a project's succession and also it plays an unavoidable role in the timely completion of the project. The project's data comprises the clients' contact information as well as their feedback/complaints, which are saved in a database. Only the admin has access to the information given by the clients in order to ensure security.

### Tools Used

1.  **XAMPP**:
    *   **Apache (Application Server)**: The Apache Software Foundation developed Apache, also known as Server, which is an open-source Java Servlet Container.
    *   **MySQL Server**: It is significantly quicker than previous methods of handling big databases. It comprises a multi-threaded SQL server that supports a variety of back ends, as well as a variety of client applications and libraries, administrative tools, and application programming interfaces (APIs). MySQL Server is well-suited for accessing databases via the Internet due to its connection, speed, and security.
2.  **Sublime Text**: Sublime Text is a powerful text editor that can handle code, markup, and prose. The sleek user interface, exceptional features, and outstanding performance will impress you.
3.  **Web Browsers**: Any web browser will suffice.
4.  **GitHub**: GitHub Inc. is a Git-based version control web hosting service. It's primarily utilised in computer programming. It has all of Git's distributed version control and source code management features, as well as those of its own.

---

## Related Work

### Problem Statement

A car rental is a vehicle that may be rented for a price and utilised for a specific length of time. Getting a rental automobile makes it easier for people to travel around when they don't have access to their own vehicle or don't own one at all. A person who needs transportation must call a rental car company and sign a contract. This method improves client retention while also making car and employee management more straightforward.

### Proposed Solution

Create a web-based system that allows consumers to register and reserve automobiles online while also allowing the firm to manage its car rental business efficiently. To make the process of renting an automobile easier for consumers.

### Scope And Features

This project covers a wide range of topics, from business concepts to computer science, and it necessitates the completion of numerous studies in order to meet the project's objectives.

Some of the topics covered include:

1.  Vehicle rental industry – This covers research on how the car rental industry operates, the processes involved, and the potential for improvement.
2.  The application was built using the PHP programming language.
3.  Customers, as well as corporate employees, will be able to make good use of the system.
4.  The web platform implies that the system will be accessible 24 hours a day, seven days a week, with the exception of minor server outages.

### Functional Requirements

Requirement analysis is a software engineering approach that consists of a series of activities that establish the demands or conditions that must be satisfied for a new or updated product while taking into account the potential for competing requirements from different users.

Functional requirements are those that are used to demonstrate the system's internal functioning nature, as well as the system's description and explanation of each subsystem. It comprises the task that the system should accomplish, the processes involved, the data that the system should contain, and the user interfaces.

The functional requirements discovered are as follows:

1.  **Customer registration** – New users should be able to register online and print membership cards.
2.  **Car reservation online** – Customers should be able to utilise the system to book and reserve automobiles online.
3.  **Automatic database update once a reservation is made or a new customer is registered** – The system should be able to update the database without any further effort from the administrator whenever a new reservation or registration is made.

### Non-functional Requirements

It describes system elements that are concerned with how the system fulfils functional requirements. They are as follows:

1.  **Security** – Only authorised corporate workers may get access to the firm's secured page on the systems, and only users with proper passwords and usernames can log in to see the users page.
2.  **Performance and Response Time** – The system should have a high-performance rate while executing user input and should be able to offer feedback or a response in a short amount of time, often 50 seconds for extremely difficult activities and 20 to 25 seconds for less sophisticated jobs.
3.  **Error handling** – Errors should be avoided as much as possible, and a suitable error message should be supplied to help the user through the recovery process. The importance of validating user input cannot be overstated. In addition, the time it takes to recover from a mistake should be between 15 and 20 seconds.
4.  **Availability** – This system must be accessible at all times, 24 hours a day, seven days a week. In the event of a catastrophic system failure, the system should be back up and running within 1 to 2 business days, ensuring that the business process is not disrupted.
5.  **Ease of use** – Given the consumers' level of understanding, a basic yet high-quality user interface should be created to make it simple to comprehend and need minimal training.

### Assumptions

1.  At any one moment, each booking is connected with only one automobile reservation.
2.  Cars that are part of the system should be available at a certain point.
3.  Discount codes may or may not be applied to billing.
4.  Due to various cancelled bookings, not all bookings are connected with billing.
5.  Since the renter may have his own insurance, the rental insurance may or may not be included in the booking.

---

## Literature Survey

### System Analysis

System analysis is a thorough examination of a system's different processes and their interrelationships both within and outside the system. The key question here is – why are there so many flaws in the current system? What measures should be taken to address the problem? When a user or management begins a study of the software utilising the current system, analysis begins. Data was collected on numerous files, decision points, and transactions handled by the current system during the analysis. For example Data Flow Diagrams, etc. are widely utilised in the system. For the collection of important information needed to create the system, training, experience, and common sense are necessary. The system's success is primarily determined by how well the problem is identified, fully studied, and appropriately implemented via the selection of a solution. A good analytical model should include not just methods for comprehending the problem, but also the framework for solving it. As a result, it should be extensively investigated by gathering data about the system. The suggested system should next be extensively examined in light of the requirements.

System analysis is divided into four sections.

1.  Initial research and system architecture.
2.  Using analytic tools to do structured analysis.
3.  Feasibility study.
4.  Analyze the cost and benefits.

### Problem Analysis

We are currently creating a new system because there is no existing system at this time. There is currently no system on the market with these features and capabilities. This system is designed for a wide range of users, with a highly adaptable and adjustable solution that will ensure worldwide marketing.

### Design and Development Problem

1.  There is a problem operating XAMPP.
2.  During the development process, to debug the mistake.
3.  To depict a connection between two or more entities.
4.  A database table has a minor mistake.

### Feasibility Analysis

Once the problem is fully recognised, a feasibility study is carried out. The goal of the research is to see if the problem is worth fixing. It is the process of analysing and evaluating a proposed project in order to evaluate if it is technically viable.

### Economical Analysis

The economic feasibility of a system is used to assess the project's or system's advantages as well as the expenses involved. A method known as cost-benefit analysis is used to accomplish this. It offers both concrete and intangible benefits, such as cost savings, increased flexibility, quicker activities, and efficient database administration.

The application is on a medium scale, and it is financially possible for us to complete. This necessitates a cost-benefit analysis. As a result, there is no issue with excessive costs or cost-benefit analyses.

### Software Analysis

1.  When developing web apps, it takes a long time.
2.  The expense of research and analysis to establish the real-world requirement.
3.  Implementation of the programme on the server, as well as the expense of web servers.

### Data Conversion

Data conversion is another expense connected with the implementation of this web application. The previously used software database must be saved and backed up so that no time or money is wasted in the implementation of the new web-based application.

### Operational Feasibility

The system is operationally practical since it can be used by ordinary users with basic computer abilities who do not require any further training. We created this system with the willingness and capacity to design, administer, and run a system that is simple for end-users to use.

### Use Case Diagram

{{< figure src="Car%20Rental%20System/figures/Fig.-1-Use-Case-Diagram.png" caption="Use Case Diagram" align="center" >}}

### Gantt Chart

The project's progress is represented on something like a Gantt chart. It connects with the customer and provides the project's anticipated completion date. It assists you in determining how long a project should take, determining the resources required, and planning the sequence in which tasks will be completed.

---

## Design

### Design Process

The process through which designers design interfaces in software or electronic devices with an emphasis on aesthetics or style is termed user interface (UI) design. Designers strive to develop interfaces that are both easy to use and enjoyable for users. Graphical user interfaces and various kinds of user interface design are examples of UI design.

### Data Flow Diagram

The Data Flow Diagram shown below illustrates the general structure of the system. It demonstrates how and what sorts of services the customer chooses, as well as the amount of admin engagement.

{{< figure src="Car%20Rental%20System/figures/Fig.-2-Data-Flow-Diagram.png" caption="Data Flow Diagram" align="center" >}}

### Sequence Diagram

A sequence diagram is comparable to an interaction diagram because it explains how and in what order a faction of items interact. A sequence diagram focuses on lifelines or processes and objects that exist concurrently, and the messages transferred between them to complete a function before the lifeline terminates.

{{< figure src="Car%20Rental%20System/figures/Fig.-3-Sequence-Diagram.png" caption="Sequence Diagram" align="center" >}}

The above picture depicts the project's Sequence Diagram, which is a sort of interaction diagram since it describes how—and in what order—a set of items interacts with one another. A sequence diagram focuses on lifelines or processes and objects that coexist, and the messages transferred between them to complete a function before the lifeline terminates.

### ER/EER Diagram

The ER diagram depicts all of the relationships between entity sets in the database. It demonstrates the database's logical structure.

{{< figure src="Car%20Rental%20System/figures/Fig.-4-ER-Diagram.jpg" caption="ER Diagram" align="center" >}}

### Relationship Model

It aids in visualising how data is linked in general.

{{< figure src="Car%20Rental%20System/figures/Fig.-5-Relationship-Model.jpg" caption="Relationship Model" align="center" >}}

---

## Database Management Structure

{{< figure src="Car%20Rental%20System/figures/Fig.-6-Database-Management-Structure.png" caption="Database Management Structure" align="center" >}}

---

## Implementation

### Graphical User Interface

#### Backend

{{< figure src="Car%20Rental%20System/figures/Fig.-7-Database-Structure.png" caption="Database Structure" align="center" >}}

#### Frontend

{{< figure src="Car%20Rental%20System/figures/Fig.-6-Home.jpg" caption="Home" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-7-Cars.jpg" caption="Cars" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-8-Contact-Us.jpg" caption="Contact Us" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-9-Sign-In.jpg" caption="Sign In" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-10-Make-My-Account.jpg" caption="Make My Account" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-11-Password-Recovery.jpg" caption="Password Recovery" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-12-My-Profile.jpg" caption="My Profile" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-12-Update-Password.jpg" caption="Update Password" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-13-My-Booking.jpg" caption="My Booking" align="center" >}}

{{< figure src="Car%20Rental%20System/figures/Fig.-14-About-Us.jpg" caption="About Us" align="center" >}}

### Database Connectivity

In PHP, make a database connection file.
Make a new PHP file called `db_connnection.php` and keep it safe. What's the point of creating a fresh database connection file? Because if you've generated numerous files in which you wish to insert or select data from databases, you won't have to write the database connection code every time. Simply include it at the start of your code using PHP's custom function include (`include 'connection.php'`) then call and utilise its function. It is particularly useful when changing your project location from one PC to another when you need to modify the values on a single file, and the changes are immediately applied to all the other files. Insert code into your `db_connection` file.

```php
<?php 

function OpenCon() 
{ 
$dbhost = "localhost"; 
$dbuser = "root"; 
$dbpass = "1234"; 
$db = "example"; 

$conn = new mysqli($dbhost, $dbuser, $dbpass,$db) or die("Connection failed: %s\n". $conn -> error); 

return $conn; 
} 

function CloseCon($conn) 
{ 
$conn -> close(); 
} 

?> 
```

The following is an explanation of the variable that we utilised in our `db_connection` file:

1.  `$dbhost` is the host on which your server is operating; it is often localhost.
2.  `$dbuser` is the root username, and `$dbpass` is the password you used to access PHPMyAdmin.
3.  `$dbname` is the name of the database that we built in this tutorial.

To test your database connection, make a new PHP file.
To connect to your database, create a new PHP file. Name it `index.php` and paste this code into it.

```php
<?php 
include 'db_connection.php'; 

$conn = OpenCon(); 

echo "Connected Successfully"; 

CloseCon($conn); 

?> 
```

Run it:
Now launch your browser and navigate to `localhost/practice/index.php`. Then you should see the following screen:

{{< figure src="Car%20Rental%20System/figures/Fig.-15-Successful-Connection.png" caption="Successful Connection" align="center" >}}

#### Message of Confirmation

Congratulations! You've successfully linked your database to localhost! If you can't view this screen, make sure you've done everything correctly in your `db_connection.php` file.

---

## Conclusion

In comparison to previous experiences, when every activity related to the vehicle rental business was restricted to a physical place alone, the car rental industry has emerged with new delicacies. Even if the physical location has not been completely eliminated, the internet's power has altered the nature of functions and how these tasks are accomplished. Customers may now book vehicles online, rent automobiles online, and have the car delivered to their home if they are a registered member, or they can travel to the office to pick up the car.

---

## Additional Resources

### Project Source & Study Materials

Access the complete source code for this Car Rental System project, research paper, preprint, lecture notes, and related Database Management System (DBMS) study materials via the links below:

<div style="display: flex; flex-direction: column; gap: 8px;">

  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/CAR-RENTAL-SYSTEM" target="_blank">Car Rental System Repository</a>
  </div>

  <div>
    <!-- viXra Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="vertical-align: middle; margin-right: 8px;"><title>viXra</title><path d="M0 0h3v3h3v3h3v3h3v3h3v3h3v3h3v3h3v3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3h-3v-3zM21 0h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3zM6 15h3v3h-3v3h-3v3h-3v-3h3v-3h3v-3z" /></svg>
    <a href="https://vixra.org/abs/2108.0140" target="_blank">viXra Preprint</a>
  </div>

  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://doi.org/10.22214/ijraset.2021.36339" target="_blank">Full Paper (IJRASET)</a>
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
    <span class="reference-text"><a id="ref-1"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>International Research Journal of Engineering and Technology (IRJET)</i>, vol. 08, no. June, pp. 1948–1951, 2021, DOI: <a href="https://doi.org/10.6084/m9.figshare.14869167">10.6084/m9.figshare.14869167</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[2]</span>
    <span class="reference-text"><a id="ref-2"></a><b>A. Thakur and K. Dhiman</b>, "Chat Room Using HTML, PHP, CSS, JS, AJAX," <i>ArXiv abs/2106.14704</i>, 2021, DOI: <a href="https://doi.org/10.48550/arXiv.2106.14704">10.48550/arXiv.2106.14704</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[3]</span>
    <span class="reference-text"><a id="ref-3"></a><b>B. Waspodo, Q. Aini, and S. Nur</b>, "Development of car rental management information system," in <i>Proceeding International Conference on Information Systems For Business Competitiveness (ICISBC)</i>, pp. 101-105, 2011. [Online]. Available: <a href="https://d1wqtxts1xzle7.cloudfront.net/96061491/Qurrotul_Aini-libre.pdf?1671489998=&response-content-disposition=inline%3B+filename%3DDevelopment_Of_Car_Rental_Management_Inf.pdf&Expires=1765660143&Signature=et0ejCyTRcyxkVNplCCP6619choSIT62LlaSxqOCYHw4X4-KYkKNwgDmfA6dCYTls-KZ7o4E5FnIhVrjJASdTx-7r-6xaHm63~n9XmLJWWkpoz2lPaJmdBCntKtXInDlikKOM5D0LxZA8uP8bHu2-sS3ZeXatiDXmpSL9SZFrDsspAG8TvxBN1MG34K8FPuNEQAXp4ojaWHMv4~2cGTFfosAdWQss85d5a2~2dQ5lEQgzYFhiibEN3ezHKyxhuCc0YrWjDisGlw5b~UKP-Ysqk8nfgcELvr0OkpKceevSs0~2hEm7hgAJ8aNOHthd9Se~wwqFMmjNHfPyPqv7lxoVQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA">https://d1wqtxts1xzle7.cloudfront.net/96061491/Qurrotul_Aini-libre.pdf?1671489998=&response-content-disposition=inline%3B+filename%3DDevelopment_Of_Car_Rental_Management_Inf.pdf&Expires=1765660143&Signature=et0ejCyTRcyxkVNplCCP6619choSIT62LlaSxqOCYHw4X4-KYkKNwgDmfA6dCYTls-KZ7o4E5FnIhVrjJASdTx-7r-6xaHm63~n9XmLJWWkpoz2lPaJmdBCntKtXInDlikKOM5D0LxZA8uP8bHu2-sS3ZeXatiDXmpSL9SZFrDsspAG8TvxBN1MG34K8FPuNEQAXp4ojaWHMv4~2cGTFfosAdWQss85d5a2~2dQ5lEQgzYFhiibEN3ezHKyxhuCc0YrWjDisGlw5b~UKP-Ysqk8nfgcELvr0OkpKceevSs0~2hEm7hgAJ8aNOHthd9Se~wwqFMmjNHfPyPqv7lxoVQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[4]</span>
    <span class="reference-text"><a id="ref-4"></a><b>M. N. Osman et al.</b>, "Online Car Rental System Using Web-Based and SMS Technology," <i>Computing Research & Innovation (CRINN)</i>, vol. 2, p. 277, 2017. [Online]. Available: <a href="https://ir.uitm.edu.my/id/eprint/54503">https://ir.uitm.edu.my/id/eprint/54503</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[5]</span>
    <span class="reference-text"><a id="ref-5"></a><b>A. Fink and T. Reiners</b>, "Modeling and solving the short-term car rental logistics problem," <i>Transportation Research Part E: Logistics and Transportation Review</i>, vol. 42, no. 4, pp. 272-292, 2006, DOI: <a href="https://doi.org/10.1016/j.tre.2004.10.003">10.1016/j.tre.2004.10.003</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[6]</span>
    <span class="reference-text"><a id="ref-6"></a><b>S. M. Khaled et al.</b>, "Software Requirements Specification for Online Car Rental System," 2015. [Online]. Available: <a href="https://www.academia.edu/37506444/Software_Requirements_Specification_for_Online_Car_Rental_System">https://www.academia.edu/37506444/Software_Requirements_Specification_for_Online_Car_Rental_System</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[7]</span>
    <span class="reference-text"><a id="ref-7"></a><b>B. Harwani</b>, "Installing XAMPP and Joomla," in <i>Foundations of Joomla</i>, pp. 9-51, Apress, Berkeley, CA, 2015, DOI: <a href="https://doi.org/10.1007/978-1-4842-0749-9_2">10.1007/978-1-4842-0749-9_2</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[8]</span>
    <span class="reference-text"><a id="ref-8"></a><b>Apache Friends</b>, "XAMPP Apache+ MariaDB+ PHP+ Perl," <i>Apache Friends</i>, 2017. [Online]. Available: <a href="https://www.apachefriends.org/">https://www.apachefriends.org/</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[9]</span>
    <span class="reference-text"><a id="ref-9"></a><b>H. A. Soares and R. S. Moura</b>, "A methodology to guide writing Software Requirements Specification document," in <i>2015 Latin American Computing Conference (CLEI)</i>, pp. 1-11, IEEE, 2015, DOI: <a href="https://doi.org/10.1109/CLEI.2015.7360001">10.1109/CLEI.2015.7360001</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[10]</span>
    <span class="reference-text"><a id="ref-10"></a><b>W. J. Carroll and R. C. Grimes</b>, "Evolutionary change in product management: Experiences in the car rental industry," <i>Interfaces</i>, vol. 25, no. 5, pp. 84-104, 1995, DOI: <a href="https://doi.org/10.1287/inte.25.5.84">10.1287/inte.25.5.84</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[11]</span>
    <span class="reference-text"><a id="ref-11"></a><b>K. Beck et al.</b>, "Manifesto for agile software development," 2001. [Online]. Available: <a href="http://agilemanifesto.org/">http://agilemanifesto.org/</a> [Accessed: Jul. 17, 2021].</span>
</div>

<div class="reference-item">
    <span class="reference-num">[12]</span>
    <span class="reference-text"><a id="ref-12"></a><b>P. Abrahamsson et al.</b>, "Agile software development methods: Review and analysis," <i>arXiv preprint arXiv:1709.08439</i>, 2017. [Online]. Available: <a href="https://arxiv.org/abs/1709.08439">https://arxiv.org/abs/1709.08439</a> [Accessed: Jul. 17, 2021].</span>
</div>

</div>
