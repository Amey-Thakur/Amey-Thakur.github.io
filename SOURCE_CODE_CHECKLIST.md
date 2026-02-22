# Source Code Checklist: Amey's Arc

This checklist tracks the functional and structural files within the `Source Code` directory. 
**Status: Audit & Cleanup (Task 2) Completed.** redundant template files removed.

## Root Configuration
- [ ] `Source Code/hugo.toml`
- [ ] `Source Code/theme.toml`
- [ ] `Source Code/LICENSE`
- [ ] `Source Code/README.md`

## Assets
### CSS (Styles)
- [ ] `Source Code/assets/css/common/404.css`
- [ ] `Source Code/assets/css/common/archive.css`
- [ ] `Source Code/assets/css/common/footer.css`
- [ ] `Source Code/assets/css/common/header.css`
- [ ] `Source Code/assets/css/common/main.css`
- [ ] `Source Code/assets/css/common/post-entry.css`
- [ ] `Source Code/assets/css/common/post-single.css`
- [ ] `Source Code/assets/css/common/profile-mode.css`
- [ ] `Source Code/assets/css/common/search.css`
- [ ] `Source Code/assets/css/common/terms.css`
- [ ] `Source Code/assets/css/core/reset.css`
- [ ] `Source Code/assets/css/core/theme-vars.css`
- [ ] `Source Code/assets/css/core/zmedia.css`
- [ ] `Source Code/assets/css/extended/blank.css`
- [ ] `Source Code/assets/css/includes/chroma-mod.css`
- [ ] `Source Code/assets/css/includes/chroma-styles.css`
- [ ] `Source Code/assets/css/includes/scroll-bar.css`

### JavaScript (Logic)
- [ ] `Source Code/assets/js/fastsearch.js`
- [ ] `Source Code/assets/js/fuse.basic.min.js`
- [ ] `Source Code/assets/js/thought-animation.js`

## Internationalization
- [ ] `Source Code/i18n/en.yaml`

## Layouts (Templates)
### Base & Error
- [ ] `Source Code/layouts/404.html`
- [ ] `Source Code/layouts/robots.txt`

### Partials
- [ ] `Source Code/layouts/partials/anchored_headings.html`
- [ ] `Source Code/layouts/partials/author.html`
- [ ] `Source Code/layouts/partials/breadcrumbs.html`
- [ ] `Source Code/layouts/partials/cover.html`
- [ ] `Source Code/layouts/partials/extend_footer.html`
- [ ] `Source Code/layouts/partials/extend_head.html`
- [ ] `Source Code/layouts/partials/footer.html`
- [ ] `Source Code/layouts/partials/head.html`
- [ ] `Source Code/layouts/partials/header.html`
- [ ] `Source Code/layouts/partials/home_info.html`
- [ ] `Source Code/layouts/partials/post_meta.html`
- [ ] `Source Code/layouts/partials/post_nav_links.html`
- [ ] `Source Code/layouts/partials/share_icons.html`
- [ ] `Source Code/layouts/partials/social_icons.html`
- [ ] `Source Code/layouts/partials/svg.html`
- [ ] `Source Code/layouts/partials/toc.html`

### Template Partials
- [ ] `Source Code/layouts/partials/templates/opengraph.html`
- [ ] `Source Code/layouts/partials/templates/schema_json.html`
- [ ] `Source Code/layouts/partials/templates/twitter_cards.html`
- [ ] `Source Code/layouts/partials/templates/_funcs/get-page-images.html`

### Shortcodes
- [ ] `Source Code/layouts/shortcodes/collapse.html`
- [ ] `Source Code/layouts/shortcodes/figure.html`
- [ ] `Source Code/layouts/shortcodes/social_grid.html`

### Default Layouts
- [ ] `Source Code/layouts/_default/archives.html`
- [ ] `Source Code/layouts/_default/baseof.html`
- [ ] `Source Code/layouts/_default/index.json`
- [ ] `Source Code/layouts/_default/list.html`
- [ ] `Source Code/layouts/_default/rss.xml`
- [ ] `Source Code/layouts/_default/search.html`
- [ ] `Source Code/layouts/_default/single.html`
- [ ] `Source Code/layouts/_default/terms.html`
- [ ] `Source Code/layouts/_default/_markup/render-image.html`

## Recent Deletions (Cleanup Phase)
- `Source Code/layouts/partials/index_profile.html` (Unused: Using `home_info` instead)
- `Source Code/layouts/partials/edit_post.html` (Unused: Not configured in site params)
- `Source Code/layouts/partials/post_canonical.html` (Unused: No canonical links in content)
- `Source Code/layouts/shortcodes/inTextImg.html` (Unused: No references in content)
- `Source Code/layouts/shortcodes/rawhtml.html` (Unused: No references in content)
