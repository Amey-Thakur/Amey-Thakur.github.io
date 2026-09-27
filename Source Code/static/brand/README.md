# Brand

The AmeyARC mark, as files rather than as a character.

The site has always used the thought balloon emoji for its icon, set in
whichever emoji font the reader's machine happens to have. That renders
differently on every system, cannot be recoloured, cannot be animated, and on a
machine without an emoji font does not render at all. These are the same mark
rebuilt as geometry, so it looks the same everywhere and can be used for more
than a favicon.

| File | What it is | Use it for |
| --- | --- | --- |
| `ameyarc-mark.svg` | The cloud and its two bubbles, one traced outline | Anywhere the mark appears at rest |
| `ameyarc-thinking.svg` | The same, breathing, with the bubbles rising | A page header, a loading state |
| `ameyarc-lockup.svg` | The mark beside the AmeyARC wordmark | Headers and footers, so the two are never spaced by hand |
| `ameyarc-mark-512.png` | A 512px still on the dark tile | App icons, social previews, anywhere raster is required |
| `ameyarc-thinking.gif` | The animation, 240px | READMEs and posts, which do not run SVG animation |
| `ameyarc-thinking-small.gif` | The animation, 96px | Inline, beside a line of text |

## How they are made

The cloud is five overlapping circles. Rather than shipping five circles, the
union outline is traced once and written out as a single path, which is what
lets the shape take a stroke, a gradient or an animation without seams showing
where the lobes overlap.

The SVGs inherit `currentColor`, so one file serves a light page and a dark
one. The animation is CSS inside the file, needs nothing around it, and stops
for anyone who has asked their system to reduce motion.

The build script is kept with the course it was written for, at
`AI-ENGINEERING/tools/brand.py`.
