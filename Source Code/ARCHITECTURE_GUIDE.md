# Architectural Specification: Amey's Arc Infrastructure

This document serves as the formal technical manifest for the site's codebase. It outlines the modular hierarchy, directory logic, and functional purpose of each component within the `Source Code` directory.

---

## Technical Hierarchy Visualization

```mermaid
graph TD
    Root[Source Code] --> Assets[Assets Subsystem]
    Root --> Layouts[Layout Engine]
    
    Assets --> CSS_F[css/Foundations]
    Assets --> CSS_I[css/Interface]
    Assets --> CSS_D[css/Design]
    
    Layouts --> P_Internal[partials/Internal]
    Layouts --> P_Scholarly[partials/Scholarly]
    Layouts --> P_Interaction[partials/Interaction]
    Layouts --> P_Assets[partials/Assets]
```

---

## 1. Asset Subsystem (`/assets`)
Management of design tokens, structural aesthetics, and interactive logic.

| Category | File Path | Functional Description |
| :--- | :--- | :--- |
| **Foundations** | [`css/Foundations/Variables.css`](./assets/css/Foundations/Variables.css) | Global design tokens: HSL color scales, typography metrics, and spacing. |
| | [`css/Foundations/Reset.css`](./assets/css/Foundations/Reset.css) | Browser normalization and foundational reset rules. |
| | [`css/Foundations/System_Display.css`](./assets/css/Foundations/System_Display.css) | Visual system logic including scrollbar aesthetics. |
| **Interface** | [`css/Interface/Global_Layout.css`](./assets/css/Interface/Global_Layout.css) | Core site skeleton: Layout containers, responsive grid, and spacing. |
| | [`css/Interface/Article_Detailed.css`](./assets/css/Interface/Article_Detailed.css) | Refined typography and spacing for the primary reading experience. |
| | [`css/Interface/Navigation_UI.css`](./assets/css/Interface/Navigation_UI.css) | Interface logic for headers, menus, and navigation toggles. |
| **Design** | [`css/Design/Signature_Visuals.css`](./assets/css/Design/Signature_Visuals.css) | Bespoke interaction logic: Particle systems and "Thought Balloon" effects. |
| | [`css/Design/Syntax_Colorway.css`](./assets/css/Design/Syntax_Colorway.css) | Academic code syntax highlighting (Chroma implementation). |

---

## 2. Layout Engine (`/layouts`)
The structural blueprint governing content-to-HTML translation.

### Internal Operations (Core Infrastructure)
| Component | Purpose |
| :--- | :--- |
| [`partials/Internal/Site_Head.html`](./layouts/partials/Internal/Site_Head.html) | Technical initialization: Meta-tags, Resource bundling, and Scripts. |
| [`partials/Internal/Primary_Navigation.html`](./layouts/partials/Internal/Primary_Navigation.html) | Global Header architecture and accessibility logic. |
| [`partials/Internal/SEO_OpenGraph.html`](./layouts/partials/Internal/SEO_OpenGraph.html) | Semantic manifest for social and search discovery. |

### Scholarly Layer (Academic Features)
| Component | Purpose |
| :--- | :--- |
| [`partials/Scholarly/Abstract_Outline.html`](./layouts/partials/Scholarly/Abstract_Outline.html) | Hierarchical Table of Contents (TOC) generator. |
| [`partials/Scholarly/Reading_Metrics.html`](./layouts/partials/Scholarly/Reading_Metrics.html) | Academic metadata: Timestamps, reading duration, and word counts. |
| [`partials/Scholarly/Citation_Trail.html`](./layouts/partials/Scholarly/Citation_Trail.html) | Contextual navigation (Breadcrumbs) for site hierarchy. |

### Resource Management
| Component | Purpose |
| :--- | :--- |
| [`partials/Assets/Vector_Icon_Library.html`](./layouts/partials/Assets/Vector_Icon_Library.html) | Centralized SVG library for high-fidelity interface icons. |
| [`partials/Assets/Media_Processor.html`](./layouts/partials/Assets/Media_Processor.html) | Algorithmic logic for automated image resizing and distribution. |

---

## 3. Modular Augmentations (`/shortcodes`)
Reusable scholarly components for content enhancement.

- [`Expandable_Section.html`](./layouts/shortcodes/Expandable_Section.html): Logic for collapsible technical appendices.
- [`Professional_Grid.html`](./layouts/shortcodes/Professional_Grid.html): Structured visual layout for academic and professional networking.

---

## Operational Workflow Reference
- **Theme/Brand Adjustments**: Modify `css/Foundations/Variables.css`.
- **Structural Integrity**: Update `layouts/_default/baseof.html` and its `Internal/` partials.
- **Academic Feature Updates**: Focus on the `Scholarly/` modules within the partials directory.
