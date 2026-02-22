# 🗺️ Architectural Excellence: Navigation Guide

Welcome to the standardized architecture of **Amey's Arc**. This codebase has been refactored from a generic template into a high-fidelity, scholarly engine. Every file is named for clarity, accessibility, and purpose.

---

## 🎨 1. Assets Folder (`/assets`)
Central repository for the site's visual and logical "physics."

### 📂 `css/Core` (The Foundation)
*Calculated design tokens and system resets.*
- **`Variables.css`**: The "Grand Design" file. Defines colors, spacing, and HSL tokens.
- **`Reset.css`**: Ensures cross-browser visual consistency.
- **`System.css`**: Handles scrollbar aesthetics and core responsive grid logic.

### 📂 `css/Interface` (The User Experience)
*Structural aesthetics for site components.*
- **`Global_Layout.css`**: Styling for the Header, Footer, and Main containers.
- **`Blog_Components.css`**: Design logic for post entries, lists, and individual articles.
- **`Discovery.css`**: Styles for Search and Archive views.

### 📂 `css/Design` (The Signature Layer)
*The "Soul" of the site.*
- **`Signature_Visuals.css`**: Bespoke animations, "Thought Balloon" particles, and interaction effects.
- **`Syntax.css`**: Academic code block highlighting (Chroma).

### 📂 `js/` (The Logic)
- **`Search_Engine.js`**: Orchestrates the instant-search functionality.
- **`Canvas_Animations.js`**: Handles the high-performance particle systems.

---

## 🧱 2. Layouts Folder (`/layouts`)
The blueprint for how content is translated into HTML.

### 📂 `partials/Internal` (The Skeleton)
- **`Site_Head.html`**: The critical entry point for metadata, styles, and scripts.
- **`Primary_Navigation.html`**: The header logic and menu orchestration.
- **`Primary_Footer.html`**: The site's base logic and analytics injection.
- **`SEO_Manifest.html`**: Unified engine for OpenGraph, Twitter Cards, and JSON-LD.

### 📂 `partials/Scholarly` (The Academic Layer)
- **`Abstract_Outline.html`** (TOC): High-level navigation for research posts.
- **`Reading_Metrics.html`**: Metadata showing dates, reading time, and word counts.
- **`Citation_Trail.html`**: Breadcrumbs for hierarchical navigation.
- **`Scholar_Identity.html`**: Displays author credentials and connection links.

### 📂 `partials/Assets` (Visual Resources)
- **`Vector_Library.html`**: Central library for all site icons (SVG).
- **`Media_Cover.html`**: Orchestrates featured images and headers.

### 📂 `shortcodes/` (Content Power-ups)
- **`Expandable_Section.html`**: For collapsing technical details.
- **`Social_Network_Grid.html`**: The visual scholarly "Connect" card.

---

## 📋 Standardized Workflow
1. **To change the look and feel**: Go to `assets/css/Core/Variables.css`.
2. **To fix SEO or Social Sharing**: Go to `layouts/partials/Internal/SEO_Manifest.html`.
3. **To edit the Header logic**: Go to `layouts/partials/Internal/Primary_Navigation.html`.
