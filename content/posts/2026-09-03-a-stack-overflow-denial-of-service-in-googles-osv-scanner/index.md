---
title: "A Stack-Overflow Denial of Service in Google's OSV-Scanner"
date: 2026-09-03T09:00:00-04:00
draft: false
author: "Amey Thakur"
summary: "OSV-Scanner parsed SPDX licence expressions with an unbounded recursive descent. Licence strings are untrusted input, so roughly three megabytes of open brackets exhausted the goroutine stack. In Go that is a fatal error rather than a panic, and recover cannot catch it, so one malformed package ended the entire scan. This is the report, the forty-line fix, and what the upstream process was actually like."
tags: ["Security", "Open Source", "Go", "Supply Chain Security", "Static Analysis", "SPDX", "Denial of Service", "CWE-674", "OSV-Scanner", "Google"]
ShowToc: true
TocOpen: false
---

[OSV-Scanner](https://github.com/google/osv-scanner) is the tool a great many
teams point at their dependency trees to ask whether anything in there has a
known vulnerability. It is maintained by Google and it sits, by design, in the
path of untrusted input: the whole job is reading metadata that somebody else
wrote.

One piece of that metadata is the licence expression. Before the scanner can
decide whether a package's licence is allowed, it parses a string in
[SPDX expression syntax](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/),
which supports `AND`, `OR`, `WITH` and brackets for grouping.

The parser followed those brackets with no limit on how deep they could go.

![The bug and its fix, animated](spdx-recursion-fix.gif)

## The mechanism

`spdx.Satisfies` is a recursive descent parser. The descent runs
`parseOr` into `parseAnd` into `parseExpression`, and `parseExpression` calls
back into `parseOr` on every opening bracket. Nothing counted how many times
that had happened.

So an expression like this, nested far enough, walks the parser down one stack
frame per bracket:

```text
((((((((((((((((((((MIT))))))))))))))))))))
```

Roughly three megabytes of open brackets is enough to exhaust the goroutine
stack on a default configuration.

## Why it is worse in Go than it looks

A stack overflow in Go is not a panic. It is a fatal error, and the runtime
prints `fatal error: stack overflow` and terminates the process. `recover`
cannot catch it, which is the property that turns an awkward parse into a
denial of service.

The practical consequence is the part worth sitting with. A scanner that
crashes on one malformed package does not skip that package and carry on. It
ends the entire run. In a pipeline that gates deployment on a clean scan, a
single crafted dependency anywhere in the tree stops the pipeline, and the
failure looks like a tooling problem rather than an attack.

This is CWE-674, uncontrolled recursion.

## The fix

Forty lines, across two files.

A `depth` field on the token stream, incremented when the parser descends into
a bracketed sub-expression and decremented on the way back out. Past a ceiling
of one thousand levels, the parser stops recursing and returns an ordinary
parse error, the same kind it already returns for any other malformed
expression.

```go
const maxDepth = 1000
```

The ceiling is deliberately generous. Real SPDX expressions nest a handful of
levels at most, and the most complicated licence strings in wide circulation do
not come close to a thousand. Nothing legitimate is rejected. An over-nested
expression now fails the way invalid input has always failed, and the scan
continues to the next package.

## Testing it

The regression test builds an expression two million levels deep and asserts a
parse error. Without the fix it terminates the test binary with a fatal stack
overflow. With it, the test passes in under half a second, because the parser
gives up at level one thousand and never allocates the rest.

The boundaries are checked as well: shallow nesting still parses, nesting
exactly at the ceiling still parses, one level past fails cleanly, and a long
run of sequential non-nested brackets does not accumulate depth, because the
counter decrements on the way out.

## The upstream process

Worth writing down, because it is the part people ask about.

I filed [issue #2993](https://github.com/google/osv-scanner/issues/2993) with a
reproduction rather than opening a pull request straight away. For anything with
a security shape, the report should come first: it lets the maintainers decide
whether it needs a private advisory before any code is public. They looked at
it, judged it an ordinary hardening fix rather than an embargoed vulnerability,
and assigned it back to me to implement.

The contribution then needed the [Google CLA](https://cla.developers.google.com/),
which is a one-time signature and took a couple of minutes.

[Pull request #3032](https://github.com/google/osv-scanner/pull/3032) was
reviewed and merged into `main` on 2 September 2026, and the issue closed as
completed the same minute.

One note on availability, current as I write: the fix is on `main` but not yet
in a tagged release. The newest release at the time of writing is v2.5.1 from
17 August 2026, which predates the merge. If you need it today, build from
`main`. Otherwise it arrives with the next release.

## What I took from it

The bug was not hiding in anything clever. There was no subtle concurrency
problem and no exotic misuse of the type system. It sat at the boundary where
somebody else's data becomes your control flow, which is where a great many of
them sit.

Recursive descent is the default way to write a small parser, and it is a good
default. The failure mode is simply that the input decides how deep you go. Any
parser that walks user-supplied structure, whether that is brackets, nested
JSON, a deeply linked object graph or a path expression, is making an implicit
promise about depth that it usually has not written down. Writing it down costs
a counter and a constant.

The second thing, less technical: reporting first and implementing second cost
me a few days and made the whole exchange straightforward. The maintainers knew
what was coming, had already agreed it was worth fixing, and reviewed a change
they had asked for.

---

The full record, including the animation above in three formats, is in
[the discussion on my fork](https://github.com/Amey-Thakur/osv-scanner/discussions/1).
