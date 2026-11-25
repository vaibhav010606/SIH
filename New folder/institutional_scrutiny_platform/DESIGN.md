---
name: Institutional Scrutiny Platform
colors:
  surface: '#f7fafd'
  surface-dim: '#d7dadd'
  surface-bright: '#f7fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f7'
  surface-container: '#ebeef1'
  surface-container-high: '#e5e8eb'
  surface-container-highest: '#e0e3e6'
  on-surface: '#181c1e'
  on-surface-variant: '#3e494b'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f4'
  outline: '#6e797b'
  outline-variant: '#bec8cb'
  surface-tint: '#006876'
  primary: '#00616d'
  on-primary: '#ffffff'
  primary-container: '#0f7b8a'
  on-primary-container: '#dff9ff'
  inverse-primary: '#7dd3e4'
  secondary: '#4d5f7d'
  on-secondary: '#ffffff'
  secondary-container: '#c8dbfe'
  on-secondary-container: '#4e607e'
  tertiary: '#5f3dc1'
  on-tertiary: '#ffffff'
  tertiary-container: '#7858dc'
  on-tertiary-container: '#f9f2ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9eefff'
  primary-fixed-dim: '#7dd3e4'
  on-primary-fixed: '#001f24'
  on-primary-fixed-variant: '#004e59'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b5c7ea'
  on-secondary-fixed: '#071c36'
  on-secondary-fixed-variant: '#364764'
  tertiary-fixed: '#e8deff'
  tertiary-fixed-dim: '#cdbdff'
  on-tertiary-fixed: '#20005f'
  on-tertiary-fixed-variant: '#4e28b0'
  background: '#f7fafd'
  on-background: '#181c1e'
  surface-variant: '#e0e3e6'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '600'
    lineHeight: 2.5rem
    letterSpacing: -0.025em
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.5rem
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.5rem
    letterSpacing: -0.011em
  body-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.25rem
    letterSpacing: -0.006em
  body-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '400'
    lineHeight: 1rem
    letterSpacing: 0em
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 0.8125rem
    fontWeight: '500'
    lineHeight: 1rem
    letterSpacing: -0.01em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 0.6875rem
    fontWeight: '500'
    lineHeight: 0.875rem
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system serves high-stakes regulatory auditing, statutory compliance, and AI-assisted governance for technical education oversight. The user persona is an AICTE Scrutiny Officer operating under rigorous administrative liability, validating architectural floor plans, faculty rosters, endowment funds, land titles, and biometric verification data. 

The aesthetic is grounded in SecOps and financial-compliance systems—evoking the disciplined precision of Stripe, Vercel, and Linear. The interface balances statutory authority with modern productivity ergonomics: crisp light-mode working surfaces, dark structural frames, dense data density, and absolute absence of visual fluff. The emotional tone must communicate unimpeachable institutional authority, zero-error tolerance, and frictionless analytical flow.

## Colors

The palette establishes strict hierarchical clarity between operational workspaces, system navigation, and verification states.

- **Primary Brand Accent (`#0F7B8A`):** Deep Regulatory Teal. Used for primary interactive actions, selection focus rings, active tab indicators, and verified confidence scores.
- **Secondary Structural Canvas (`#0B1F3A`):** Deep Maritime Navy. Confined to persistent lateral sidebars, command palettes, and primary statutory navigation to reinforce institutional weight.
- **Canvas & Surface Neutral (`#F5F8FB`):** A high-purity, cool neutral canvas. Workspace cards sit on pure `#FFFFFF` with structural boundary borders in `#E2E8F0`.

### Regulatory Status Colors
Audit status indicators require immediate, non-negotiable semantic recognition:
- **Verified (`#1E9E6A`):** Direct statutory confirmation, authenticated by digital sign-off or API cross-match.
- **Mismatch Detected (`#D64545`):** Discrepancies between submitted institutional claims and government registry ground-truth.
- **Expired / Expiring (`#E39B1B`):** Time-invalidated documents (e.g., occupancy certificates, bank guarantees, fire safety permits).
- **Verification Pending (`#3B82F6`):** Asynchronous validation in progress or external service ping queued.
- **Source Unavailable (`#64748B`):** External repository uncontactable (e.g., land registry portal timeout).
- **Manual Review Required (`#7C5CE0`):** Edge-case visual inspections requiring human officer discretion.

### Risk Tier Palette
- **Low Risk:** Text and indicator `#1E9E6A` over surface `#ECFDF5` with border `#A7F3D0`.
- **Medium Risk:** Text and indicator `#D97706` over surface `#FFFBEB` with border `#FDE68A`.
- **High Risk:** Text and indicator `#DC2626` over surface `#FEF2F2` with border `#FECACA`.

## Typography

Typography is split strictly along semantic utility:
- **Inter** handles narrative copy, organizational descriptors, tabular text, compliance requirements, and high-level headings. It provides high legibility at dense standard sizes with precise tabular numeral alignment.
- **JetBrains Mono** is mandatory for all compliance artifacts: AICTE Application IDs, SHA-256 cryptographic document hashes, GIS geo-coordinates, transaction IDs, UTC timestamps, and API response payload inspectors.

Headings must maintain tight tracking (`letter-spacing: -0.02em`) to match modern engineering interfaces. Body copy maintains strict tabular lining numerals (`tnum`) across all scrutiny tables to ensure zero jitter when metrics update in real time.

## Layout & Spacing

The layout is architected around a fixed multi-pane productivity shell:
- **Navigation Pane:** Fixed 260px Maritime Navy sidebar (`#0B1F3A`) holding statutory context and institutional queues.
- **Main Audit Canvas:** Fluid 12-column grid system resting inside a maximum canvas bound of 1680px for desktop scrutiny terminals, scaling to 100% width on tablet inspection devices.
- **Inspector Rail:** Collapsible 380px secondary dock on the right for AI discrepancy summaries, document preview panes, and cryptographic logs.

Horizontal rhythm conforms to standard 4px baseline multiples. Large analytical surfaces favor generous internal padding (`space-xl` / 32px) within cards to mitigate cognitive fatigue during prolonged multi-hour audits, paired with compressed inter-row data padding (`space-xs` and `space-sm`) inside comparative scrutiny tables.

## Elevation & Depth

Visual hierarchy is maintained through crisp structural surface delineation rather than aggressive drop shadows.

- **Base Layer (`#F5F8FB`):** Ambient background canvas.
- **Card Tier 1 (`#FFFFFF`):** Work surfaces, audit tables, and dossier views framed with a hairline `1px solid #E2E8F0` border and a soft ambient shadow: `0 1px 3px rgba(11, 31, 58, 0.04), 0 1px 2px rgba(11, 31, 58, 0.02)`.
- **Card Tier 2 (Flyouts & Interactive Context Panes):** Raised inspection states utilize `0 10px 15px -3px rgba(11, 31, 58, 0.06), 0 4px 6px -2px rgba(11, 31, 58, 0.03)` with a hairline boundary of `1px solid #CBD5E1`.
- **Modals & Critical Overrides:** `0 20px 25px -5px rgba(11, 31, 58, 0.12), 0 10px 10px -5px rgba(11, 31, 58, 0.04)` over a backdrop blur of `blur(4px)` with `#0B1F3A` at 40% opacity.

## Shapes

The design uses standard 16px (`1rem` / `rounded-lg`) corner radii for primary analytical cards, dossier containers, and inspection modules, creating a modern, approachable software feel without sacrificing formal authority.

Interactive inputs, nested metric sub-panels, and standard buttons utilize a compact `0.5rem` (8px) radius to maintain dense operational precision. Status chips, micro-badges, and risk pills use full pill shaping (`9999px`) to immediately visually contrast against structural content cards.

## Components

### Buttons
- **Primary Statutory Action:** Solid Teal `#0F7B8A`, white text, 8px radius, height 40px, font weight 500 (Inter). Focus state shows an outer ring of `0 0 0 2px #FFFFFF, 0 0 0 4px #0F7B8A`.
- **Secondary Action:** White surface, 1px solid border `#E2E8F0`, text `#0B1F3A`. Hover transitions surface to `#F8FAFC` and border to `#CBD5E1`.
- **Destructive / Rejection Action:** Solid Crimson `#D64545`, white text. Used strictly for formal audit rejection or freeze commands.

### Status Badges & Risk Chips
- **Construction:** Height 24px, pill-shaped (`9999px`), inline-flex, gap 6px, padding `0 10px`.
- **Status Indicator:** 6px solid dot with the canonical status color, accompanied by `label-sm` (JetBrains Mono) uppercase text.
- **Risk Tier Chips:** Low (Green background tint, green text), Medium (Amber background tint, amber text), High (Red background tint, red text). Hairline border matching the respective token with 25% opacity.

### Audit Lists & Verification Tables
- **Header:** Background `#F8FAFC`, border-bottom `1px solid #E2E8F0`, text `label-sm` in `#64748B`, uppercase tracking at `0.05em`.
- **Row:** Height 48px, border-bottom `1px solid #F1F5F9`. Hover state shifts background to `#F8FAFC`.
- **Data Attributes:** Strict left-alignment for textual data, right-alignment for values/areas/capacities, center-alignment for verification status indicators.

### Inputs & Scrutiny Form Fields
- **Container:** Height 40px, border `1px solid #CBD5E1`, background `#FFFFFF`, border radius 8px, text `body-md` in `#0B1F3A`.
- **Active / Focused:** Border color shifts to `#0F7B8A` with a 3px ambient shadow ring in `rgba(15, 123, 138, 0.15)`.
- **Flagged Discrepancy Field:** Border color `#D64545` with contextual warning icon and inline AI observation message rendered in `body-sm` `#D64545`.

### Structural Scrutiny Cards
- **Card Shell:** Background `#FFFFFF`, border-radius 16px, border `1px solid #E2E8F0`.
- **Header Zone:** Padding 20px 24px, separated by a hairline divider `1px solid #F1F5F9`. Contains institution identifier, validation timestamp (JetBrains Mono), and risk pill docked top-right.
- **Content Zone:** Padding 24px, utilizing 16px layout gaps between audited criteria sections.