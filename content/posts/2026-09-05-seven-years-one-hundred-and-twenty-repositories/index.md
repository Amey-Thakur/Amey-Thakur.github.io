---
title: "Seven Years, One Hundred and Twenty Repositories"
date: 2026-09-05T23:34:07-04:00
draft: false
author: "Amey Thakur"
summary: "The account is seven years old today. It sat completely empty for the first 425 days of that, and the repository more people use than any other is a folder of 8086 assembly programs written for an undergraduate lab. Today I read all one hundred and twenty of them, oldest first, and gave each one a file written for machines rather than for people. This is what reading your own back catalogue in one sitting actually teaches you."
tags: ["Open Source", "GitHub", "Documentation", "Metadata", "Computer Engineering", "Research", "Writing", "llms.txt", "codemeta", "Discoverability"]
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

## The account is seven years old today

It was created on 5 September 2019 at 09:48:39 UTC. That is 2,557 days ago.

The first repository was pushed on 3 November 2020. The account therefore sat
completely empty for **425 days**, which is a sixth of its whole life. I do not
remember what I intended to put in it in 2019, and there is no evidence of it,
because an empty account leaves none.

Two repositories arrived on that first day, a car rental system and a chat room.
Both are coursework. Neither is interesting. That is the correct beginning.

## What is actually in it

| | |
| :--- | ---: |
| Repositories | 129 |
| Public | 119 |
| Private | 10 |
| Forks | 4 |
| Stars | 1,673 |
| Followers | 216 |

Today I swept **120** of them, one at a time, in a fixed order: bachelor's
coursework in curriculum order, then the master's, then everything after
graduation. Not creation order, because most of the undergraduate work was
uploaded to GitHub in February 2022, years after it was taken. Curriculum order
is the order the work actually happened in.

## The uncomfortable part

Here is the ranking by stars.

| Stars | Repository | What it is |
| ---: | :--- | :--- |
| 126 | 8086-ASSEMBLY-LANGUAGE-PROGRAMS | A second-year microprocessors lab |
| 81 | AWS-CERTIFIED-CLOUD-PRACTITIONER-CLF-C01 | Notes for a certification exam |
| 74 | DEEPFAKE-AUDIO | A course project |
| 58 | OPTIMIZING-STOCK-TRADING-STRATEGY-WITH-REINFORCEMENT-LEARNING | A final-year project |
| 46 | COMPUTER-ENGINEERING | An index of the degree |

Nothing in that list is research. The most used thing I have ever published is a
folder of 8086 assembly programs written to satisfy a lab requirement, and the
second is a set of exam notes.

The obvious reading is that this is a comment on what the internet values. I
think the real reading is narrower and more useful: **the assembly programs are
the only thing on the list that somebody needed at two in the morning.** A
student with a lab due tomorrow has a precisely shaped problem, and a folder of
working programs with the right names in it is precisely the shape of the
answer. Research papers are read by people who are browsing. Coursework is read
by people who are stuck.

That is not an argument for writing less research. It is an argument for
recognising that being useful and being impressive are different axes, and that
I have been much better at the first when I was not trying.

## What every repository was given today

Three files, and none of them are for a human reader.

| File | Written for |
| :--- | :--- |
| `llms.txt` | A language model arriving at the repository cold. What it is, who wrote it, what is inside, the subject terms. |
| `codemeta.json` | Machine-readable provenance in schema.org form, carrying the creation date and the keyword set. |
| `CITATION.cff` | An identifiers entry recording when the work was created, separate from when it was released. |

The reason is straightforward. A README is written for someone who has already
arrived. Increasingly, what arrives first is not a person but a model answering
somebody's question, and it has to decide in a few hundred tokens whether this
repository is relevant. A README optimised for a human skim is not the same
artefact as an index optimised for that decision.

The [llms.txt](https://llmstxt.org/) convention is one attempt at the second
thing. [CodeMeta](https://codemeta.github.io/) is the older and more serious
attempt at machine-readable software provenance, and
[Citation File Format](https://citation-file-format.github.io/) is what GitHub
already reads to render a citation box.

None of this is exciting. All of it is the difference between work that can be
found and work that merely exists.

## Three things reading all of it taught me

**Repositories rot in ways that never show up as an error.** A link that now
redirects to a parked domain. A badge pointing at a service that returns 503. A
count typed into a README that was true once. Nothing goes red. The page renders
perfectly and says something false, and it will keep doing so until somebody
reads it, which for most repositories is never.

**The order you present work in is a claim about it.** GitHub's profile sorts by
last push, so a sweep in curriculum order rewrites the feed into a chronology:
second year at the bottom, current work at the top. That is a narrative, and it
was worth spending the day to get right, because the alternative narrative,
sorted by whichever file I happened to touch last, is not one I chose.

**Anything typed by hand goes stale, and anything generated does not.** The
counts in this post came from the API a few minutes before it was written. The
tables in the repositories that carry counts are generated from the files they
count. Every number I have ever typed into a README by hand has eventually
become wrong.

## What I would tell myself in 2019

Push something in the first week. The 425 days of nothing were not spent
preparing; they were spent waiting to have something good enough, and the first
thing I eventually pushed was a car rental system that is good enough for
nobody. It did not matter. What mattered is that the next 118 things had
somewhere to go.

And write the boring file. The one nobody asks for, that explains what the thing
is to a reader who has no context and no patience. Seven years on, that file is
the only reason any of this is findable at all.

## Where to look

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">Index</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING">Computer Engineering</a>, the bachelor's degree, and <a href="https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING">M.Eng. Computer Engineering</a>, indexed by semester</span>
</div>

<div class="reference-item">
    <span class="reference-num">Most used</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/8086-ASSEMBLY-LANGUAGE-PROGRAMS">8086 Assembly Language Programs</a>, the second-year lab that outperformed everything else</span>
</div>

<div class="reference-item">
    <span class="reference-num">Profile</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur">github.com/Amey-Thakur</a></span>
</div>

</div>

<style>
.reference-container {
    padding-left: 0;
}
.reference-item {
    display: flex;
    margin-bottom: 0.8rem;
}
.reference-num {
    flex: 0 0 95px; /* Fixed width for the label column */
    font-weight: bold;
    color: inherit;
}
.reference-text {
    flex: 1; /* Takes remaining space */
}
</style>

---

<div align="center">

<i>Seven years, and the useful part was never the part I was proud of at the time.</i>

</div>
