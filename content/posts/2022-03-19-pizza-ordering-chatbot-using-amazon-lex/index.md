---
title: "Pizza Ordering Chatbot Using Amazon Lex"
date: 2022-03-19T00:00:00-05:00
draft: false
author: "Amey Thakur"
summary: "Special thanks to Mega Satish for her meaningful contributions, support, and wisdom that helped shape this work. Because of breakthroughs in machine learning and deep learning, which are causing a change in every industry area and managing various types of activities better than people. The majority of monotonous jobs that were formerly performed by humans are now replaced by AI."
tags: ["AI", "Amazon Lex", "Artificial Intelligence", "ASR", "AWS Chatbot", "AWS Lambda", "Cloud Computing", "Conversational AI", "Natural Language Processing", "NLU", "Pizza Ordering Bot", "Serverless", "Voice Assistant"]
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

Because of breakthroughs in machine learning and deep learning, which are causing a change in every industry area and managing various types of activities better than people. The majority of monotonous jobs that were formerly performed by humans are now replaced by AI. Every firm is aiming to replace the least skilled labour with AI robots that can do comparable tasks more efficiently, especially when it comes to chatbots. A chatbot is computer software that mimics human interaction by using voice instructions, text dialogues, or both. Chatbots are being employed to address consumer concerns or problems in food delivery app businesses such as Zomato and Swiggy, but are chatbots truly useful in that business model? This business model's target customers are those who don't have time to go outside to obtain food, prefer convenience at home, or are unwilling to endure discomfort, thus their concerns should be resolved in the most convenient way possible. To fulfil the user's request, a chatbot is employed. It is critical for the chatbot to plan how to carry out the task that the user has asked. New tools are available now to create and deploy chatbots; Amazon Lex by AWS is one of them. This project focuses on creating a Pizza Ordering Chatbot using Amazon Lex to help the user order pizza.

---

## Introduction

### Chatbot

A chatbot is a computer program that conducts a conversation in natural language via text or speech, understands the intent of the user and sends a response based on business rules and data of the organization.

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%201%20-%20A%20Timeline%20of%20Evolution%20of%20Bots.png" caption="A Timeline of Evolution of Bots" align="center" >}}

One of the first chatbots was ELIZA. It was also an early test case for the Turing Test, which determines if a machine can demonstrate cognition that is comparable to, or indistinguishable from, that of a person. The computer used "pattern matching" and replacement methods to provide prepared replies, giving early users the impression that they were speaking with someone who understood their input. The scripts in the software limited the program's capabilities. Joseph Weizenbaum, a researcher at MIT's Artificial Intelligence Laboratory, created an early natural language processing algorithm in the mid-1960s. It was allegedly made to show how shallow human-computer connections were at the time. Humans, on the other hand, found it highly entertaining when it was put on computers. In today’s world, chatbots have many applications such as online shopping, ticket booking, news reports, food ordering, etc.

### Advent of Conversational Interactions

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%202%20-%20Advent%20of%20Conversational%20Interactions.png" caption="Advent of Conversational Interactions" align="center" >}}

### Amazon Lex
Amazon Lex is a robust discussion tool that enables developers to incorporate interactive experiences into new and existing applications by integrating voice and text interfaces. Alexa is powered by this behind-the-scenes service. Amazon Lex is a service that allows you to create these conversational user interfaces.

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Amazon%20Lex%20Overview.png" caption="Amazon Lex Overview" align="center" >}}

### Amazon Web Services
AWS (Amazon Web Services) is a sophisticated, developing cloud computing platform offered by Amazon that comprises infrastructure as a service (IaaS), platform as a service (PaaS), and integrated software as a service (SaaS) solutions. AWS services can offer organisation tools such as compute power, database storage and content delivery services.

AWS was founded in 2006 as an extension of the internal operations established by Amazon.com to manage its online sales activities. AWS was among the first firms to provide a pay-as-you-go cloud computing model, which grows to give users with computation, storage, or networking as required.
AWS provides a wide range of tools and solutions for businesses and software engineers that may be utilised in cloud services in up to 200 countries and territories. AWS services are available to government agencies, educational institutions, charities, and commercial organisations.

#### How does AWS Work?
- AWS is separated into different services; each can be configured in different ways based on the user's needs. For an AWS service, users are allowed to access configuration choices as well as specific server mappings.
- More than 100 services comprise the Amazon Web Services portfolio, including those for compute, databases, infrastructure management, application development and security. These services, by category, include:
    - Compute
    - Storage databases
    - Data management
    - Migration
    - Hybrid cloud
    - Networking
    - Development tools
    - Management
    - Monitoring
    - Security
    - Governance
    - Big data management
    - Analytics
    - Artificial intelligence (AI)
    - Mobile development
    - Messages and notification

---

## Problem Statement

An artificial intelligence chatbot is a system that enables natural language communications between humans and robots. We discovered from the literature that chatbots, in general, work like a typical search engine. Although the chatbot only provided one output instead of several outputs/results, the essential process flow remains the same, with the fresh search being performed each time an input is submitted. Nothing is related to the previous output. This project is focused on enabling a chatbot to assist in ordering a pizza that can process the customers' needs with relation to the previous search output. In the chatbot context, this functionality will enhance the capability of the chatbot’s input processing.

---

## Overview of Amazon Lex

### Amazon Lex
Amazon Lex is a service that allows you to integrate speech and text-based conversational agents into any application. Amazon Lex provides advanced deep learning functionalities of Automatic Speech Recognition, and Natural Language Understanding to recognise text intent, enabling customers to build applications with highly engaging user experiences and lifelike conversational interactions.

With Amazon Lex, the same conversational engine that powers Amazon Alexa is now available to any developer, enabling you to build sophisticated, natural language chatbots into your new and existing applications. Amazon Lex empowers any programmer to instantly create talking chatbots. It handles the discourse and dynamically alters the replies. You may use the console to create, evaluate, and launch your text or speech bot. You can then add conversational interfaces to bots on mobile devices, web applications, and chat platforms (for example, Facebook Messenger).

Amazon Lex has pre-built connectivity with AWS Lambda and can be easily integrated with many other AWS technology platforms, such as Amazon Cognito, AWS Mobile Hub, Amazon CloudWatch, and Amazon DynamoDB. Integration with Lambda provides bots access to pre-built serverless enterprise connectors to link to data in SaaS applications, such as Salesforce, HubSpot, or Marketo.

### Features of Amazon Lex
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Features%20of%20Amazon%20Lex.png" caption="Features of Amazon Lex" align="center" >}}

### The Need For Amazon Lex
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%203%20-%20The%20Need%20For%20Amazon%20Lex.png" caption="The Need For Amazon Lex" align="center" >}}

### Benefits of Amazon Lex
- Offers an easy-to-use console & predefined bot.
- Employs advanced deep learning functionalities.
- Provides seamless deploying & Scaling.
- Offers built-in integration with AWS platform.
- Cost-effective platform to create bots.

### Applications of Amazon Lex

1. **Build virtual agents and voice assistants:**
    - Enable self-service capabilities with virtual contact centre agents and interactive voice response (IVR). Users may reset their passwords or make appointments without having to talk with a live person.

2. **Automate informational responses:**
    - Design conversational solutions that respond to frequently asked questions. Optimize your Connect & Lex conversation flows for tech support, HR benefits, or finance by using Amazon Kendra's computational linguistics search for FAQs. Amazon Kendra is a highly accurate and intelligent search service that enables your users to search unstructured and structured data using natural language processing and advanced search algorithms.

3. **Improve productivity with application bots:**
    - Using smart chatbots, you can automate fundamental user actions in your app. Link to other corporate software effortlessly with AWS Lambda while maintaining precise network access using IAM.

### Working of Amazon Lex
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%204%20-%20Working%20of%20Amazon%20Lex.png" caption="Working of Amazon Lex" align="center" >}}

### Amazon Lex Use Case

- To get banking information through an Amazon Lex chatbot.

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%205%20-%20Workflow%20of%20getting%20banking%20information%20through%20a%20Chatbot.png" caption="Workflow of getting banking information through a Chatbot" align="center" >}}

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%206%20-%20Preview%20of%20Flow%20of%20Conversation.png" caption="Preview of Flow of Conversation" align="center" >}}

#### Other Use Cases

1. **Informational Bots:**
    - Chatbots for everyday consumer requests.
    - Examples include the Latest news, meteorology, sports stats, and so forth.

2. **Application Bots:**
    - Build powerful interfaces to mobile applications.
    - Examples: Book tickets, order food, Manage bank accounts, etc.

3. **Enterprise Productivity Bots:**
    - Streamline enterprise work activities and improve efficiencies.
    - Examples: Check sales figures, marketing, inventory condition, and so forth.

4. **Internet of Things (IoT) Bots:**
    - Enable conversational interfaces for device interactions.
    - Examples: Wearables, Appliances, etc.

### How Amazon Lex Operates?
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Figure%207%20-%20AWS%20Lambda%20Function.png" caption="AWS Lambda Function" align="center" >}}

**Steps to follow while working with Amazon Lex -**
1. Create a chatbot & configure it with intents, slots & utterances.
2. Lex Console provides a textual display slide for you to try the bot on.
3. Publish a version and create an alias.
4. Deploy the bot on a suitable platform.

### Core Concepts & Technologies
1. **Amazon Bot:** A computer software that simulates interactive communication.
2. **Intent:** An intent expresses a desired action by the user.
3. **Slots:** Slots are characteristics that may be required by purpose.
4. **Slot Types:** Each slot has a unique kind. It is possible to construct designed or custom slot kinds.

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Intent%20Fulfilment.png" caption="Intent Fulfilment" align="center" >}}

---

## Implementation

### Steps of Creating a Chatbot

**To create an Amazon Lex bot (console):**
1. Sign in to the AWS Management Console and open the Amazon Lex console at https://console.aws.amazon.com/lex/.
2. Assuming this is your first bot, select **Get Started**; else, select **Create** from the Bots page.
3. Fill up the form on the **Create your Lex bot** page with the following information, then click **Create**.
    - Choose the **FoodOrdering** blueprint.
    - Leave the default bot name (**FoodOrdering**).
    - For **COPPA**, choose **No**.
    - For **User utterance storage**, choose the appropriate response.
4. Choose to **Create** to preserve the settings, the console sends the appropriate queries to Amazon Lex. The bot editing screen is then displayed by the console.
5. Wait till you get the confirmation that your bot was built successfully.
6. Test the bot.

> **Note:** You can test the bot by typing text into the test window, or, for compatible browsers, by choosing the microphone button in the test window and speaking.

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%201.jpg" caption="Step 1" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%202.jpg" caption="Step 2" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%203.jpg" caption="Step 3" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%204.jpg" caption="Step 4" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%205.jpg" caption="Step 5" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%206.jpg" caption="Step 6" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%207.jpg" caption="Step 7" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Step%208.jpg" caption="Step 8" align="center" >}}

### Snapshots of Testing a Bot

1. **Conversation of confirming the order of pizza**

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%201.png" caption="Conversation 1 - Part 1" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%202.png" caption="Conversation 1 - Part 2" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%203.png" caption="Conversation 1 - Part 3" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%204.png" caption="Conversation 1 - Part 4" align="center" >}}

2. **Conversation of cancelling an order**

{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%205.png" caption="Conversation 2 - Part 1" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%206.png" caption="Conversation 2 - Part 2" align="center" >}}
{{< figure src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/figures/Snapshot%207.png" caption="Conversation 2 - Part 3" align="center" >}}

---

## YouTube Demonstration

### Project Demo
{{< youtube 6iLgN_1e4DU >}}

### Complete Tutorial
{{< youtube FHbXSo95S7A >}}

### Presentation Recording
{{< youtube cI8Wv2aW37I >}}

---

## Conclusion

Through the proposed system, we can draw the conclusion that the PizzaOrdering chatbot will efficiently manage clients and accept their orders in a simple yet cohesive manner. The chatbot conducts the discussion in a nice manner, carefully inquiring about the type of pizza, the pizza dough, and the appetisers. It also requests the delivery time and confirms the order. We can also use Amazon Lex to improve the appearance and utterances of the chatbot and deploy it on a full-scale website using Amazon Cloud Services.

---

## Presentation

<div style="position: relative; width: 100%; height: 0; padding-bottom: 56.25%; margin-bottom: 20px;">
    <iframe src="Pizza%20Ordering%20Chatbot%20Using%20Amazon%20Lex/PRESENTATION%20-%20PIZZA%20ORDERING%20CHATBOT%20USING%20AMAZON%20LEX.pdf" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" allowfullscreen></iframe>
</div>

---

## Additional Resources

#### Course & Certification Resources
Access the detailed notes, source code, and complete video tutorials for the AWS Certified Cloud Practitioner (CLF-C01) certification via the links below:

<div style="display: flex; flex-direction: column; gap: 8px;">
  <div>
    <!-- GitHub Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
    <a href="https://github.com/Amey-Thakur/AWS-CERTIFIED-CLOUD-PRACTITIONER-CLF-C01" target="_blank">AWS Certified Cloud Practitioner (CLF-C01) Repository</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtube.com/playlist?list=PLGOc13Pt03SZuZA2eS79J4EUtBBgR0JCs&si=fKjjLeWV-Irl5O-I" target="_blank">AWS Certified Cloud Practitioner (CLF-C01) Playlist</a>
  </div>
  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://doi.org/10.22214/ijraset.2022.40861" target="_blank">Full Paper (PDF)</a>
  </div>
  <div>
    <!-- File Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
    <a href="https://github.com/Amey-Thakur/AWS-CERTIFIED-CLOUD-PRACTITIONER-CLF-C01?tab=readme-ov-file#mega-notes" target="_blank">Mega's Notes (Special thanks to Mega Satish for her helpful notes)</a>
  </div>
  <div>
    <!-- Graduation Cap Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
    <a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING" target="_blank">Computer Engineering Resources</a>
  </div>
</div>

#### AWS YouTube Playlist
Detailed tutorials for specific AWS services:

<div style="display: flex; flex-direction: column; gap: 8px;">
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/dnmuv0PC7W8" target="_blank">AMAZON IAM TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/y-oACtu8djc" target="_blank">AMAZON EC2 INSTANCE TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/Ey8Tm4cC6yo" target="_blank">AMAZON LIGHTSAIL WORDPRESS TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/CnM07Vg7pW8" target="_blank">AMAZON S3 TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/D8Vt_wIuDHQ" target="_blank">AMAZON EBS VOLUME TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/jShMHcYju4Y" target="_blank">AMAZON EFS TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/9Quw6uln1Zc" target="_blank">AMAZON RDS TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/EhV8I2ElVRk" target="_blank">AMAZON VPC AURORADB TUTORIAL</a>
  </div>
  <div>
    <!-- YouTube Icon -->
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon></svg>
    <a href="https://youtu.be/3TIzIHqkvvU" target="_blank">AMAZON LOAD BALANCER TUTORIAL</a>
  </div>
</div>

---

## Citation

**Please cite this work as:**

<pre style="white-space: pre-wrap;"><code>Thakur, Amey. "Pizza Ordering Chatbot Using Amazon Lex". AmeyArc (Mar 2022). https://amey-thakur.github.io/posts/2022-03-19-pizza-ordering-chatbot-using-amazon-lex/.</code></pre>

**Or use the BibTex citation:**

```
@article{thakur2022amazonlex,
  title   = "Pizza Ordering Chatbot Using Amazon Lex",
  author  = "Thakur, Amey",
  journal = "amey-thakur.github.io",
  year    = "2022",
  month   = "Mar",
  url     = "https://amey-thakur.github.io/posts/2022-03-19-pizza-ordering-chatbot-using-amazon-lex/"
}
```

---

## References

1. <a id="ref-1"></a> **Jinesh Varia and Sajee Mathew**, "Overview of Amazon Web Services", *Amazon Web Services*, 2014, [https://d36cz9buwru1tt.cloudfront.net/AWS_Overview.pdf](https://d36cz9buwru1tt.cloudfront.net/AWS_Overview.pdf) [accessed Mar. 19, 2022].

2. <a id="ref-2"></a> **Radhika Soni and Radhika Thapar**, "Acceptance of Chatbots by Millennial Consumers", *International Journal of Research in Advance Engineering*, Nov. 2018, [https://www.researchgate.net/publication/332961953_Acceptance_of_Chat_bots_by_Millennial_Consumers](https://www.researchgate.net/publication/332961953_Acceptance_of_Chat_bots_by_Millennial_Consumers) [accessed Mar. 19, 2022].

3. <a id="ref-3"></a> **AWS Documentation**, *Amazon Web Services*, [https://docs.aws.amazon.com](https://docs.aws.amazon.com) [accessed Mar. 19, 2022].

4. <a id="ref-4"></a> **Amazon Lex Documentation**, *Amazon Web Services*, [https://docs.aws.amazon.com/lex](https://docs.aws.amazon.com/lex) [accessed Mar. 19, 2022].

5. <a id="ref-5"></a> **AWS Lex**, *Amazon Web Services*, [https://aws.amazon.com/lex](https://aws.amazon.com/lex) [accessed Mar. 19, 2022].

6. <a id="ref-6"></a> **Amey Thakur**, "Pizza Ordering Chatbot Demo", *YouTube*, [https://youtu.be/6iLgN_1e4DU](https://youtu.be/6iLgN_1e4DU) [accessed Mar. 19, 2022].

7. <a id="ref-7"></a> **Amey Thakur**, "The Complete Guide To The Pizza Ordering Chatbot", *YouTube*, [https://youtu.be/FHbXSo95S7A](https://youtu.be/FHbXSo95S7A) [accessed Mar. 19, 2022].

8. <a id="ref-8"></a> **Amey Thakur**, "AWS Certified Cloud Practitioner (CLF-C01) Repository", *GitHub*, [https://github.com/Amey-Thakur/AWS-CERTIFIED-CLOUD-PRACTITIONER-CLF-C01](https://github.com/Amey-Thakur/AWS-CERTIFIED-CLOUD-PRACTITIONER-CLF-C01) [accessed Mar. 19, 2022].
