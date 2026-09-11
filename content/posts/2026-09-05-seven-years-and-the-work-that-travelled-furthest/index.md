---
title: "Seven Years, and the Work That Travelled Furthest"
date: 2026-09-05T21:15:00-04:00
draft: false
author: "Amey Thakur"
summary: "I am Amey Thakur, and I opened github.com/Amey-Thakur on 5 September 2019, then left it empty for 425 days. Today, on its seventh anniversary, I read every repository on it in one sitting, oldest first. Three things became impossible to miss: the work that reaches people is the work a stranger can run without asking me anything, the quiet years were not idle years, and public work decays silently unless somebody audits it on purpose. This is the full account, with the figures, and what I gave every repository before closing it."
tags: ["Open Source", "GitHub", "Documentation", "Metadata", "Computer Engineering", "Research", "Writing", "llms.txt", "codemeta", "Discoverability", "Career", "Software Engineering"]
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

{{< Academic_Figure src="seven-years.png" alt="A GitHub contribution grid titled Seven Years, one square per month from September 2019 to September 2026, shaded by how many repositories were created in it, with a total beside each year: none in 2019, 2 in 2020, 38 in 2021, 46 in 2022, 12 in 2023, 3 in 2024, 1 in 2025 and 27 in 2026. Fourteen empty squares run from September 2019 to October 2020, the 425 days the account stood untouched before the first push in November 2020." caption="Seven years, one square per month, with each year's total on the right. The first push is November 2020. Every empty square before it is part of the 425 day wait." align="center" >}}

My name is Amey Thakur. Seven years ago today I opened a GitHub account,
[github.com/Amey-Thakur](https://github.com/Amey-Thakur), in Mumbai, in the
second year of a bachelor's degree. This is an honest accounting of what has
happened to it since, including the parts that do not flatter me.

## 5 September 2019, 09:48:39 UTC

That is when I opened it. I know the second because GitHub keeps it, and it is
the only part of the story I did not have to reconstruct.

That was 15:18:39 IST. I was in Mumbai, in the second year of a B.E. in
Computer Engineering. The account has changed countries since, to a master's at
Windsor and everything after it, and I have never opened another one.

{{< Academic_Figure src="two-universities.png" alt="A timeline from September 2019 to September 2026 marking the account opening in Mumbai, the first push after 425 days, the 8086 programs, the two degree indexes, this website, and the merge into google/osv-scanner, with the span divided between the University of Mumbai and the University of Windsor." caption="Seven years on one axis. The two spans are divided where the record changes, not at a date of travel the repositories cannot evidence." align="center" >}}

Nothing was pushed to it for **425 days**.

{{< Academic_Figure src="first-425-days.png" alt="Two panels either side of fourteen empty squares. On the left, the account created on 5 September 2019 at 15:18:39 IST, 09:48:39 UTC. On the right, the first code pushed on 3 November 2020 at 21:32:27 IST, 16:02:27 UTC. The heading above them reads 425 days, 6 hours, 13 minutes." caption="The exact distance between opening the account and putting anything into it, counted from the second of each. Fourteen months of the record are empty." align="center" >}}

Not because anything was being built in private. I was waiting until there was
something worth putting up. At the time that felt like having standards. In
hindsight it was a category error: I was treating publication as a reward for
work already finished, when publication is closer to the place work goes *in
order* to become finished. Nothing in those fourteen months improved by being
kept back.

## 3 November 2020

{{< Academic_Figure src="first-commit.png" alt="Two GitHub commit rows dated 3 November 2020. Car Rental Database Management System, committed at 21:32:27 IST, 233 files changed and 26,048 additions, hash b383db1. Chat Room, committed at 21:46:20 IST, 10 files changed and 293 additions, hash 579bcde. Both are marked Verified." caption="The first code on the account, both projects pushed within a quarter of an hour of each other. The hashes are still in their repositories today." align="center" >}}

The wait ended with a car rental system and a chat room, pushed on the same day.
Both are full-stack web systems: a database-backed booking platform with separate
user and administrator interfaces, and a real-time chat application using AJAX
for asynchronous updates and dynamic DOM changes.

Both were later published as research papers, the car rental system in the
*International Journal for Research in Applied Science and Engineering
Technology*, Volume 9, Issue 7.

That is the part worth sitting with. The work held back for fourteen months
because it did not yet feel worth publishing was, once published, worth
publishing twice. The judgment I was waiting to develop was not going to arrive
in private. It arrived from putting the thing where it could be judged.

## The shape of seven years

Repositories created per calendar year, counted today.

| Year | Created |
| :--- | ---: |
| 2020 | 2 |
| 2021 | 38 |
| 2022 | 46 |
| 2023 | 12 |
| 2024 | 3 |
| 2025 | **1** |
| 2026 | 27 |

The shape is not flattering at first glance, and I nearly left it out. It is the
most useful thing on this page.

The two peaks are the bachelor's degree going up as it happened. The trough
covers the master's and the move to Canada. **One repository in the whole of
2025.**

For a long time I read a year like that as a gap in the record, which is another
way of saying a gap in the person. It is not. The habits that produced 2026 were
formed in 2025, when nothing was shipping: reading more carefully, writing things
down for my own use, learning what a finished artefact actually requires. A
public feed measures publication, and publication is a lagging indicator of
almost everything that matters.

If you are in a year like that now, the useful reframing is that the graph is
recording your output, not your rate of improvement, and the two are allowed to
be a year apart.

{{< Academic_Figure src="shape-of-seven-years.png" alt="One square for every repository created, grouped by year, from two in 2020 to forty-six in 2022 and one in 2025." caption="The same figures as the table above, as proportions. Two peaks, a trough, and a return." align="center" >}}

## Year by year

The totals hide more than they show. Here is each year on its own, month by
month, with what the shape of it was actually caused by.

### 2020

{{< Academic_Figure src="year-2020.png" alt="A twelve month grid for 2020, empty except for November, which holds two repositories." align="center" >}}

The account was fourteen months old before anything went into it. What broke
the silence was a database-backed booking system with separate user and
administrator interfaces, and a real-time chat application using AJAX, pushed
on the same day.

Both were later published as research papers. That is the fact I would send
back to myself in 2019, because it inverts the reasoning that produced the
delay. I was holding work back until it was good enough to publish. It was
already good enough to publish. Waiting did not improve it; it only postponed
finding out.

### 2021

{{< Academic_Figure src="year-2021.png" alt="A twelve month grid for 2021, busiest in July with twenty-three repositories." align="center" >}}

Thirty-eight repositories, and the bachelor's went online in bulk: twenty-three
in July alone, long after the coursework itself was finished.

Read as a graph, that July is an extraordinary month. It was a backlog and some
free evenings. A profile records when you published, not when you learned, and
those two timelines can be years apart.

The more interesting entries are the ones nobody assigned. A neural voice
cloning studio in February, a reinforcement learning system for trading
strategies in September, a text summariser in December. This is the year the
account stopped being a submission folder and started being a body of work,
and the change was not announced. It shows up only as three squares that do not
belong to any syllabus.

### 2022

{{< Academic_Figure src="year-2022.png" alt="A twelve month grid for 2022, with twenty repositories in February." align="center" >}}

The busiest year, and still the one that defines the profile.

February produced the 8086 assembly programs, which remain the most used thing
here by a wide margin, and twenty repositories went up in that month alone.
December produced the Computer Engineering index: the least glamorous
repository on the account and, on reflection, close to the most valuable,
because it is the reason the dozens of repositories beneath it
can be found at all. An index is not
work. It is the thing that makes work findable, and I have never regretted the
day spent building one.

### 2023

{{< Academic_Figure src="year-2023.png" alt="A twelve month grid for 2023, with activity in January, May, July and August." align="center" >}}

Twelve repositories, a new country and a new degree.

The M.Eng index went up on 12 January, inside the first fortnight at Windsor,
before there was a single piece of coursework to put in it. Building the
container before the contents looks like procrastination and is the opposite:
everything that followed had somewhere to go on the day it was finished, which
is exactly what the account itself lacked in 2019.

### 2024

{{< Academic_Figure src="year-2024.png" alt="A twelve month grid for 2024, with three repositories across February and March." align="center" >}}

Three repositories in a whole year, and the end of the coursework.

March brought zero-shot video generation, the only one of the three that nobody
assigned, and the most used of the three by a comfortable margin.

I want to resist drawing the obvious moral from that, because the account
contradicts it: the single most used thing here is a microprocessors lab, which
was very much assigned. What the three of 2024 actually show is narrower and
truer. In a thin year, the work that survives being looked at later is the work
that was chosen rather than required.

### 2025

{{< Academic_Figure src="year-2025.png" alt="A twelve month grid for 2025, empty except for a single repository in December." align="center" >}}

One repository, in December, and it was this website.

Eleven months of nothing precede it. This is the year I would have hidden a few
years ago, and it is the one I now think is worth the most to anyone reading.
Nothing in that stretch was idle. It was reading more slowly, keeping notes
that were not for publication, and working out what a finished artefact
actually requires. None of that creates repositories, so none of it appears
above.

A contribution graph measures publication. Publication is a lagging indicator
of almost everything that causes it. If your own graph has a year like this in
it, the graph is not the measurement you think it is.

### 2026

{{< Academic_Figure src="year-2026.png" alt="A twelve month grid for 2026, with activity from March to September." align="center" >}}

Twenty-seven repositories, and the first year the work has been written down as
carefully as it was built.

Kaggle in March, NotebookLab in April, the Claude certification guide in July,
and in September a fix merged into one of Google's own projects. The difference
between this year and 2022 is not volume, and 2022 is still ahead on that. It
is that the work now arrives with its reasoning attached, and that the thing
built and the account of why it was built go up together.

That is the whole of what the quiet year bought.

## What travelled furthest, and why

The natural assumption is that the work which reaches people will be the work
that was hardest to do. Seven years of evidence says otherwise, and the reason
turned out to be more useful than the observation.

The most used repository on my GitHub is
[8086 Assembly Language Programs](https://github.com/Amey-Thakur/8086-ASSEMBLY-LANGUAGE-PROGRAMS):
525 documented Intel 8086 programs with a browser simulator that assembles and
runs every one of them, the full instruction set, nine flags, macros, DOS and
BIOS services, step-by-step debugging, verified by 2,010 tests. Behind it,
[AWS certification material](https://github.com/Amey-Thakur/AWS-CERTIFIED-CLOUD-PRACTITIONER-CLF-C01),
[a neural voice cloning studio](https://github.com/Amey-Thakur/DEEPFAKE-AUDIO)
built on SV2TTS, and
[a reinforcement learning system for stock trading strategies](https://github.com/Amey-Thakur/OPTIMIZING-STOCK-TRADING-STRATEGY-WITH-REINFORCEMENT-LEARNING).

For years I read that ranking as a verdict on what the internet rewards. It is
not. Every item on it shares one property that none of my papers has.

**You can run it without asking me anything.**

{{< Academic_Figure src="what-travelled.png" alt="Four GitHub repository cards: 8086 Assembly Language Programs in Assembly, AWS Certified Cloud Practitioner CLF-C01 in HTML, Deepfake Audio in Python, and Optimizing Stock Trading Strategy with Reinforcement Learning in Python." caption="The four most used repositories. Not one of them is a paper, and every one of them can be run by someone who never contacts me." align="center" >}}

A paper asks a reader to accept a result. A simulator lets them produce the
result themselves, at two in the morning, with a deadline tomorrow and no
appetite for correspondence. The distance between those two experiences accounts
for the entire difference in reach. This is not rigour losing to popularity. It
is a closed artefact losing to an open one.

That reframing changed how I finish things. The question at the end of a project
is no longer *is this correct*, which it has to be regardless. It is:

> What would a stranger have to ask me before this became useful to them?

Then I remove those questions one at a time. A simulator removes all of them at
once. So does a worked example, a downloadable file, a page that runs in a
browser with no key, a command someone can paste. Each removal is small. Together
they are the difference between work that exists and work that travels.

> Every idea I open-source is a spark handed to someone I may never meet. That
> is the whole point.
>
> **– Amey Thakur**

None of this is an argument for less research. This year alone there is a
[zero-shot accident detection pipeline](https://github.com/Amey-Thakur/ACCIDENT-CVPR-2026)
released as a preprint, a
[geometric criterion that dates a hand gesture to the frame it happened on](https://amey-thakur.github.io/posts/2026-08-31-frame-synchronous-hand-gesture-detection-by-projected-winding-order/),
and, on 2 September, a fix merged into
[Google's OSV-Scanner](https://github.com/google/osv-scanner/pull/3032) for a
stack overflow that a few megabytes of open brackets could trigger in any scan.
The gesture work shipped as a paper **and** as an application that runs in a
browser with no server and no key. That is the lesson applied rather than merely
noticed, and it is the first time I have done both deliberately.

## What my GitHub is actually made of

{{< Academic_Figure src="languages.png" alt="A stacked language bar for the account, with a legend: Python 28, HTML 14, Jupyter Notebook 14, JavaScript 12, Ruby 5, TeX 5, CSS 4, Java 4, MATLAB 4, C 3." caption="Primary language across the public repositories, in Linguist's own colours." align="center" >}}

That distribution is a biography. The Ruby is five repositories from 2022, a
Rails application and a pair of small games written the summer I wanted to learn
the language. The MATLAB is four repositories from the master's, 2023 to 2024:
computational methods, computational intelligence, digital communications and
adaptive cruise control. Every TeX repository was created in 2026, because that
is when the writing started. Nobody plans a distribution like this. It is a
curriculum and a set of interests, fossilised.

The sweep itself covered **120 repositories**, of which **58** serve a published
site and **64** run CI, totalling **114 workflows**. Slightly more than one
repository in three publishes something a browser can open, which is the
runnable-artefact principle showing up as infrastructure rather than as
intention.

## What the seven years hold

Most of my GitHub is a degree, twice. The coursework is not loose in the
profile; it is indexed, semester by semester, in two repositories that exist so
the rest can be found.

| | |
| :--- | :--- |
| [Computer Engineering](https://github.com/Amey-Thakur/COMPUTER-ENGINEERING) | B.E. Computer Engineering, University of Mumbai, 2018 to 2022. Every subject, lab and project, indexed by semester. |
| [M.Eng. Computer Engineering](https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING) | M.Eng. Computer Engineering, University of Windsor, 2023 to 2024. The same, for the master's. |

The rest divides in two. Some of it was built because it was useful.

| | |
| :--- | :--- |
| [GIT-GUIDE](https://github.com/Amey-Thakur/GIT-GUIDE) | Every Git and GitHub answer in one place. Ask in plain language, get the exact commands, the danger level and the undo. |
| [GITHUB-TRICKS](https://github.com/Amey-Thakur/GITHUB-TRICKS) | The features, URL tricks, search qualifiers and Actions patterns worth knowing, each verified against its source, with the trap nobody else writes down. |
| [NotebookLab](https://github.com/Amey-Thakur/NotebookLab) | A thinking partner that runs on your own machine. Import documents, ask questions, keep the answers local. |
| [PI](https://github.com/Amey-Thakur/PI) | Everything about one number: verified digits, working algorithms in three languages, a written atlas, and a site that makes it playable. |
| [CLAUDE-CERTIFICATIONS](https://github.com/Amey-Thakur/CLAUDE-CERTIFICATIONS) | A study guide for all four Anthropic Claude certifications, built only from published material and given away. |
| [KAGGLE-COMPETITIONS](https://github.com/Amey-Thakur/KAGGLE-COMPETITIONS) | Competition solutions kept as they were worked, with the write-up explaining where each approach ran out. |
| [ACHIEVEMENTS](https://github.com/Amey-Thakur/ACHIEVEMENTS) | Every certificate and credential, each with the link that verifies it. |

The rest was entered somewhere, or sent upstream, which is a different kind of
work. It has a deadline set by someone else and a judgement at the end of it
that is not mine to make.

{{< Academic_Figure src="competitions-and-research.png" alt="Seven repositories listed with their language, creation date and venue: GESTURE-FX, ACCIDENT-CVPR-2026, osv-scanner, and the four SAIR Foundation challenges." caption="Four SAIR Foundation challenges, two papers, and one fix that now runs inside a tool other people depend on." align="center" >}}

{{< Academic_Figure src="research-gesture-fx.png" alt="A card for GESTURE-FX: gesture-triggered camera effects in the browser, TypeScript, created 1 September 2026, runs on the client with no server or key." caption="The only piece here that shipped as a paper and as something you can open in a browser on the same day." align="center" >}}

{{< Academic_Figure src="research-accident-cvpr-2026.png" alt="A card for ACCIDENT-CVPR-2026: a zero-shot pipeline for traffic accident detection, Jupyter Notebook, created 16 August 2026, arXiv 2604.09685, with Sarvesh Talele." caption="Three modules that share no parameters, so any one of them can be replaced without disturbing the others." align="center" >}}

{{< Academic_Figure src="research-osv-scanner.png" alt="A card for osv-scanner: a stack-overflow denial of service in the SPDX licence parser, Go, issue 2993, merged 2 September 2026." caption="The only thing on this account that now runs inside software other people depend on." align="center" >}}

{{< Academic_Figure src="research-sair-lean-kernel-challenge.png" alt="A card for SAIR-LEAN-KERNEL-CHALLENGE: an independent Lean 4 proof checker, Python, created 29 August 2026, for the SAIR Foundation." caption="Writing a proof checker is the clearest way to find out whether you actually understand the thing being checked." align="center" >}}

{{< Academic_Figure src="research-sair-mathematics-distillation-challenge.png" alt="A card for SAIR-MATHEMATICS-DISTILLATION-CHALLENGE: equational theories in two stages, Lean, created 31 March 2026, for the SAIR Foundation." caption="The earliest of the four, and the one that made the other three possible." align="center" >}}

{{< Academic_Figure src="research-sair-modular-arithmetic-challenge.png" alt="A card for SAIR-MODULAR-ARITHMETIC-CHALLENGE: neural induction of exact modular multiplication, Python, created 15 July 2026, for the SAIR Foundation." caption="Inducing an exact operation rather than approximating it, which is a different problem from the one networks are usually given." align="center" >}}

{{< Academic_Figure src="research-sair-inverse-galois-problem-igp24.png" alt="A card for SAIR-INVERSE-GALOIS-PROBLEM-IGP24: degree 24 polynomial construction with Frobenius fingerprinting, Python, created 16 July 2026, for the SAIR Foundation." caption="A century-old open problem, approached from the one direction a computer is good for: construction and search." align="center" >}}

Reading them in sequence made plain something no single one of them shows. The
coursework is not the early work and the projects the later work. They interleave
throughout, and the habits that make the recent repositories legible were learned
writing up labs that nobody required to be written up well. What changed over
seven years is less the standard than the range of things it gets applied to.

## What I gave every repository today

Three files. None of them is written for a human reader.

| File | Written for |
| :--- | :--- |
| `llms.txt` | A language model arriving cold. What this is, who wrote it, what is inside, the subject terms. |
| `codemeta.json` | Machine-readable provenance in schema.org form, carrying the creation date and the keywords. |
| `CITATION.cff` | An identifiers entry recording when the work was created, kept separate from when it was released. |

This follows directly from the reach argument. A README is written for someone
who has already arrived. Increasingly the first arrival is not a person but a
model answering somebody's question, holding a few hundred tokens in which to
decide whether this work is worth citing. A page written for a human skim is not
the same artefact as an index written for that decision, and the second is now
part of what it means for work to be usable by a stranger.

[llms.txt](https://llmstxt.org/) is one attempt at it.
[CodeMeta](https://codemeta.github.io/) is the older and more serious attempt at
machine-readable provenance, and
[Citation File Format](https://citation-file-format.github.io/) is what GitHub
already reads to render a citation box.

They went up in a deliberate order: undergraduate coursework in curriculum order,
then the master's, then everything after graduation. Not upload order, because
most of the bachelor's work reached GitHub years after it was done, in a batch,
and upload order would have told a story that never happened.

## Three things a day of reading taught me

**Public work fails without ever turning red.** A link that now resolves to a
parked domain. A badge pointing at a service returning 503. A count that was true
when it was typed. Nothing errors. The page renders perfectly, says something
false, and keeps saying it until somebody reads it, which for most repositories
is never. Decay in published work is silent by construction, so it has to be
audited on a schedule rather than noticed by accident. Today was that audit, and
it was overdue by years.

**The order work is presented in is itself a claim.** GitHub sorts a profile by
last push, so sweeping in curriculum order turns the feed into a chronology:
second year at the bottom, current work at the top. Left alone, the same feed
tells a different story, ordered by whichever file was touched last, which is a
story about my week rather than about the work. Either way something is being
said about you. Only one of the two versions is chosen.

**What is typed by hand goes stale; what is generated does not.** Every number
written into a README by hand has eventually become wrong. The figures in this
post were read from the API today, 5 September 2026, and they will drift. The
dates will not, which is why the dates carry the argument and the counts only
illustrate it.

## To anyone still waiting

Push it in the first week.

Those 425 days were not preparation. They were a wait for a confidence that does
not arrive before the work does. What ended the wait was a student web project I
did not think was ready, and it became a published paper. The certainty I was
waiting for showed up **after** the push, which is the only order in which it
ever shows up.

Then make it runnable. Not polished, not impressive: runnable by someone who
cannot ask you a single question. That is the entire difference between work that
exists and work that travels, and seven years of my own evidence says it
is worth more than any further rigour applied to something nobody can start.

And if this is one of your quiet years, the graph is measuring what you shipped,
not what you became. Mine records a single repository for 2025. It was not a lost
year. It was the one that made this one possible.

## The people in it

Almost nothing above was done alone, and a profile is bad at showing that. A
commit has one author. A paper has several, and the work usually has more people
in it than either.

**[Mega Satish](https://github.com/msatmod)** is on more of this than anyone
else, and it is not close. **Twelve** of the papers in my record carry her name,
which is more than I can count on one hand twice, and they have gone on to be
read and cited well beyond anything we expected of them at the time. Her work is
collected on
[Google Scholar](https://scholar.google.ca/citations?user=7Ajrr6EAAAAJ&hl=en)
and under [ORCID 0000-0002-1844-9557](https://orcid.org/0000-0002-1844-9557),
and it runs alongside years of coursework, projects and competitions across the
whole bachelor's and past it.

She is the most sincere person I have worked with, and the quickest to learn
something she has never seen before. If you need a thing *done*, you go to Mega,
because she will find the way through whatever is in the way, usually before
anyone else has finished describing the problem. A great deal of what is indexed
under my name is work we did together, and the parts I am proudest of are the
parts we disagreed about first.

**[Hasan Rizvi](https://github.com/rizvihasan)** co-authored **three** of those
papers, collected on his
[Google Scholar](https://scholar.google.ca/citations?user=OJuGq08AAAAJ&hl=en),
and is the other half of that pair.

Where Mega will work a problem until it gives way, Hasan will make you
understand it. He has a better command of language than anyone I studied with,
he is a strong engineer, and he has the rarer skill of explaining a concept so
that it stays explained. If you need something *understood*, you go to Hasan. A
lot of what I know, I know because he took the time to say it a second way.

Between them they cover the two halves of any hard problem: someone who can
figure anything out, and someone who can explain anything.

**[Archit Konde](https://github.com/Archit-Konde)** I met in undergraduate. We
wrote *Fundamentals of Neural Networks* together, which is the most widely read
and cited thing either of us has published and sits at the top of his
[Google Scholar](https://scholar.google.ca/citations?user=njXhCdwAAAAJ&hl=en), and then, some years later, we both
moved to Canada, to the same university, and finished a master's there as well.
Two countries and two degrees is a long time to keep showing up for someone
else's half-finished work.

He is the strongest mathematician I know personally: algorithms, calculus,
physics, and a genuine command of how programming languages actually work rather
than how they are used. His mental arithmetic is faintly ridiculous. A good deal
of what I understand about all of it came out of arguing it through with him,
and he has the quality that matters more than any of the rest, which is aim. He
will stay with one problem until it gives, long past the point where most people
have decided it was not that interesting anyway.

He is also the person I take unfinished things to, because he will say plainly
when something is not ready. Almost everyone is kind instead. Much of what is in
this account is better because he was willing to be the exception.

**[Karan Dhiman](https://github.com/Karan-Dhiman)** co-authored **two** papers
with me during the bachelor's, collected on his
[Google Scholar](https://scholar.google.com/citations?user=kKNKmqgAAAAJ&hl=en).

He makes work worth looking at, which is a different skill from making it work,
and a rarer one among engineers. Videos, presentations, posters, Canva layouts,
anything in the Adobe suite: he produces them quickly, to a professional
standard, and with an eye for composition that no template supplies. What would
cost me an afternoon of nudging boxes into place, he has finished before I have
fully explained what I want, and the result is better than the one I had
pictured. If you need work to be *seen*, you go to Karan.

**Jason Horn**, at the Writing Support Desk of the University of Windsor, taught
me academic writing properly: structure, citation, and the discipline of
claiming only what you can support. Nearly every rule I now apply without
thinking about it, I learned in those sessions.
[WRITING-SUPPORT](https://github.com/Amey-Thakur/WRITING-SUPPORT) exists because
what he taught was worth passing on rather than keeping.

And to everyone else whose work ended up inside a repository with only my name
on the commit: it was never mine alone.

## If you got this far

You are past four thousand words about somebody else's repositories, so here is
the part I would only tell someone who finished.

None of this was a plan. There was no strategy behind the seven years, no
decision in 2019 about what the account should become. What actually happened is
that I kept putting things where other people could see them, mostly before I
felt ready, and the work slowly organised itself around that habit. The
narrative in this post is real, but I found it today, by reading. I was not
following it at the time.

That is the thing worth passing on, and it is the opposite of what these posts
usually say. You do not need the plan. You need somewhere to put the work and
the willingness to put it there early, and the shape shows up later, on a day
like this one, when you finally sit down and read the whole thing back.

So the honest closing line is not a conclusion. Seven years in, the useful
question is still the same one it was at the start: what is the next thing, and
where can somebody else find it.

If you build something and I can run it, send it to me. There is a
[connect page](https://amey-thakur.github.io/connect/) on this site, which is a
short form that reaches me directly and nothing else: no list, no newsletter, no
reply from anybody but me. I read every message that arrives, and the best part
of publishing in the open has always been the people who write back.

The journey is not finished. It never gets to be a destination, and I have
stopped wanting it to be.

## Where to look

<div class="reference-container">

<div class="reference-item">
    <span class="reference-num">Degrees</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/COMPUTER-ENGINEERING">Computer Engineering</a> at the University of Mumbai, and <a href="https://github.com/Amey-Thakur/MENG-COMPUTER-ENGINEERING">M.Eng. Computer Engineering</a> at the University of Windsor, both indexed by semester</span>
</div>

<div class="reference-item">
    <span class="reference-num">Furthest</span>
    <span class="reference-text"><a href="https://github.com/Amey-Thakur/8086-ASSEMBLY-LANGUAGE-PROGRAMS">8086 Assembly Language Programs</a>, 525 programs and a browser simulator that runs every one of them</span>
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

## How to cite this

```text
Thakur, A. (2026). Seven Years, and the Work That Travelled Furthest.
Amey's Arc. https://amey-thakur.github.io/posts/2026-09-05-seven-years-and-the-work-that-travelled-furthest/
```

```bibtex
@misc{thakur2026sevenyears,
  author       = {Thakur, Amey},
  title        = {Seven Years, and the Work That Travelled Furthest},
  year         = {2026},
  month        = {September},
  howpublished = {Amey's Arc},
  note         = {Written on the seventh anniversary of the account, 5 September 2026},
  url          = {https://amey-thakur.github.io/posts/2026-09-05-seven-years-and-the-work-that-travelled-furthest/}
}
```

---

<div align="center">

<i>The work that travels is the work a stranger can start without asking you anything.</i>

<b>– Amey Thakur</b>

</div>
