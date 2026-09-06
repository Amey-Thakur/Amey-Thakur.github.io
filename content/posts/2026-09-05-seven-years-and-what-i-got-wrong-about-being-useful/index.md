---
title: "Seven Years, and What I Got Wrong About Being Useful"
date: 2026-09-05T23:34:07-04:00
draft: false
author: "Amey Thakur"
summary: "I opened this account on 5 September 2019 and pushed nothing to it for 425 days. The wait ended on 3 November 2020 with a coursework submission. Seven years on, the work of mine that reaches the most people is not the research, it is a folder of 8086 assembly programs written for a second-year lab, and understanding why changed how I think about what is worth publishing. Today I read every repository I have, oldest first."
tags: ["Open Source", "GitHub", "Documentation", "Metadata", "Computer Engineering", "Research", "Writing", "llms.txt", "codemeta", "Discoverability", "Career"]
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

## 5 September 2019, 09:48:39 UTC

That is when this account was opened. I know the second because GitHub keeps it.

I pushed nothing to it for **425 days**.

Not because I was building in private. I was waiting for something worth putting
up. At the time that felt like judgment. It was closer to hesitation, and
hesitation leaves no record at all.

## 3 November 2020

The wait ended with a car rental system and a chat room, pushed the same day.
Both coursework. A form writing to a database, and some HTML with a little AJAX
behind it.

Neither would survive a review today. Both mattered more than anything I had
written in the fourteen months before them, because everything that came after
finally had somewhere to land.

## What I got wrong

For most of these seven years I assumed the work that mattered would be the work
I found hardest.

It was not. The repository more people have used than any other on this account,
year after year, is
[8086 Assembly Language Programs](https://github.com/Amey-Thakur/8086-ASSEMBLY-LANGUAGE-PROGRAMS),
a second-year microprocessors lab. Behind it, notes for a cloud certification and
a course project on deepfake audio. None of it research. All of it coursework.

The tempting conclusion is that this says something disappointing about what the
internet rewards. The truer one is narrower and more useful.

**Those assembly programs are the only thing on that list somebody needed at two
in the morning.** A student with a lab due tomorrow has a problem of a very
precise shape, and a folder of working programs with the right names in it is
exactly the shape of the answer. Research is read by people who are browsing.
Coursework is read by people who are stuck.

Useful and impressive are different axes. I have been better at the first in the
years I was not aiming at it.

This is not an argument for less research. This year alone there is a
[zero-shot accident detection pipeline](https://github.com/Amey-Thakur/ACCIDENT-CVPR-2026)
released as a preprint, a
[geometric criterion that dates a hand gesture to the frame it happened on](https://amey-thakur.github.io/posts/2026-08-31-frame-synchronous-hand-gesture-detection-by-projected-winding-order/),
and, on 2 September, a fix merged into
[Google's OSV-Scanner](https://github.com/google/osv-scanner/pull/3032) for a
stack overflow that a few megabytes of open brackets could trigger in any scan. I
am glad about all three. I no longer assume they are the part of this work that
helps the most people.

## What the seven years actually hold

Most of the account is a degree, twice. The coursework is not loose in the
profile; it is indexed, semester by semester, in two repositories that exist so
the rest can be found.

| | |
| :--- | :--- |
| [Computer Engineering](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING) | B.E. Computer Engineering, University of Mumbai, 2018 to 2022. Every subject, lab and project, indexed by semester. |
| [M.Eng. Computer Engineering](https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING) | M.Eng. Computer Engineering, University of Windsor, 2023 to 2024. The same, for the master's. |

The rest is what was built once the degrees stopped setting the agenda.

| | |
| :--- | :--- |
| [GIT-GUIDE](https://github.com/Amey-Thakur/GIT-GUIDE) | Every Git and GitHub answer in one place. Ask in plain language, get the exact commands, the danger level and the undo. |
| [GITHUB-TRICKS](https://github.com/Amey-Thakur/GITHUB-TRICKS) | The features, URL tricks, search qualifiers and Actions patterns worth knowing, each verified against its source, with the trap nobody else writes down. |
| [NotebookLab](https://github.com/Amey-Thakur/NotebookLab) | A thinking partner that runs on your own machine. Import documents, ask questions, keep the answers local. |
| [PI](https://github.com/Amey-Thakur/PI) | Everything about one number: verified digits, working algorithms in three languages, a written atlas, and a site that makes it playable. |
| [CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS) | A study guide for all four Anthropic Claude certifications, built only from published material and given away. |
| [KAGGLE-COMPETITIONS](https://github.com/Amey-Thakur/KAGGLE-COMPETITIONS) | Competition solutions kept as they were worked, with the write-up explaining where each approach ran out. |
| [GESTURE-FX](https://github.com/Amey-Thakur/GESTURE-FX) | The gesture criterion, and the browser application it was derived for. |
| [RESUME-ENGINE](https://github.com/Amey-Thakur/RESUME-ENGINE) | One JSON file in, a typeset one-page resume and matching cover letter out. |
| [ACHIEVEMENTS](https://github.com/Amey-Thakur/ACHIEVEMENTS) | Every certificate and credential, each one with the link that verifies it. |

Reading them in sequence made one thing plain that reading any one of them
cannot. The coursework is not the early work and the projects the later work.
They interleave. The habits that make the recent repositories legible were
learned by writing up labs nobody asked me to write up well.

## What I did today

I read every repository on this account, oldest first, and gave each one three
files. None of them is written for a human reader.

| File | Written for |
| :--- | :--- |
| `llms.txt` | A language model arriving cold. What this is, who wrote it, what is inside, the subject terms. |
| `codemeta.json` | Machine-readable provenance in schema.org form, carrying the creation date and the keywords. |
| `CITATION.cff` | An identifiers entry recording when the work was created, kept separate from when it was released. |

A README is written for someone who has already arrived. Increasingly the first
arrival is not a person but a model answering somebody's question, with a few
hundred tokens in which to decide whether this work is worth citing. A page
written for a human skim is not the same artefact as an index written for that
decision.

[llms.txt](https://llmstxt.org/) is one attempt at the second thing.
[CodeMeta](https://codemeta.github.io/) is the older and more serious attempt at
machine-readable provenance, and
[Citation File Format](https://citation-file-format.github.io/) is what GitHub
already reads to render a citation box.

They went up in a deliberate order: bachelor's coursework in curriculum order,
then the master's, then everything after graduation. Not upload order, because
most of the undergraduate work reached GitHub years after it was done.

## Three things a day of reading taught me

**Repositories fail without ever turning red.** A link that now resolves to a
parked domain. A badge pointing at a service returning 503. A count that was true
once. Nothing errors. The page renders perfectly and says something false, and
keeps saying it until somebody reads it, which for most repositories is never.

**The order work is presented in is a claim about it.** GitHub sorts a profile by
last push, so sweeping in curriculum order turns the feed into a chronology:
second year at the bottom, current work at the top. That is a story, and it was
worth a day to tell it deliberately rather than let it be told by whichever file
I happened to touch last.

**What is typed by hand goes stale; what is generated does not.** Every number I
have written into a README by hand has eventually become wrong. That is why there
are no counts in this post. The dates are here because dates do not move.

## To anyone still waiting

Push it in the first week.

Those 425 days were not preparation. They were a wait for a confidence that never
arrives before the work does. What ended it was a coursework submission I would
not defend today, and it did not matter, because everything since had a place to
begin.

Then write the boring file. The one nobody asks for, that explains what the thing
is to a reader with no context and no patience. Seven years on, that file is the
reason any of this can be found at all.

## Where to look

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">Degrees</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING">Computer Engineering</a> at the University of Mumbai, and <a href="https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING">M.Eng. Computer Engineering</a> at the University of Windsor, both indexed by semester</span>
</div>

<div class="reference-item">
    <span class="reference-num">Most used</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/8086-ASSEMBLY-LANGUAGE-PROGRAMS">8086 Assembly Language Programs</a>, the second-year lab that quietly outperformed everything else</span>
</div>

<div class="reference-item">
    <span class="reference-num">Upstream</span>
    <span class="reference-text"><a href="https://github.com/google/osv-scanner/pull/3032">google/osv-scanner #3032</a>, merged 2 September 2026</span>
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
