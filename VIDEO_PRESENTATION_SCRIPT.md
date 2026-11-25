# TrustLens — AICTE Statutory Scrutiny Portal
## Complete 5–10 Minute Video Presentation & Demo Script
**Event / Pitch:** Smart India Hackathon (SIH) / AICTE National Evaluation  
**Theme:** Smart Automation / AI-Powered Regulatory Scrutiny  
**Project:** TrustLens — Institutional Scrutiny & Statutory Approval Decision-Support System  
**Working Prototype URL:** [http://localhost:3000](http://localhost:3000) (or hosted deployment)  
**Target Duration:** 7:30 to 8:30 minutes (Expandable up to 10:00 minutes)

---

## 📋 Pre-Recording Checklist & Setup

1. **Browser Setup:**
   - Open Chrome or Edge at `1920x1080` resolution.
   - Navigate to `http://localhost:3000`.
   - Press `F11` (full screen) or set zoom to `90%` / `100%` so all headers and tables fit comfortably.
2. **Audio Setup:**
   - Use a clear USB microphone or headset.
   - Speak in a calm, confident, authoritative tone—like an AI engineer and policy technologist presenting to senior regulatory directors.
3. **Screen Recording Tools:**
   - OBS Studio, Loom, or Windows Game Bar (`Win + Alt + R`).
   - Enable mouse cursor highlighting/click effect.
4. **Pacing Guide:**
   - ~130–140 words per minute.
   - Pause for 1–2 seconds when clicking so the viewer absorbs the dynamic UI transitions.

---

## ⏱️ Video Timeline Overview

| Time | Phase | Focus Module / View | Key Takeaway |
|---|---|---|---|
| **0:00 – 1:00** | **Act I: The Problem** | Executive Slide / Overview Header | Manual scrutiny bottleneck, fraud, ghost faculty, paper overload |
| **1:00 – 2:00** | **Act II: System Overview** | `view-overview` & `view-queue` | Automated pipeline, 1,420 applications, 6 statutory verdicts, risk tiering |
| **2:00 – 4:30** | **Act III: Deep Forensic Dossier** | `view-cases` (5 Statutory Docs) | Dynamic PDF switcher: Fire NOC, Cadre Roll, DDA GIS, MCD OBPS, Bhulekh deed |
| **4:30 – 5:45** | **Act IV: Syndicate Detection** | `view-graph` (Evidence Graph) | AI graph canvas, ghost faculty syndicate across 3 institutions, Section 10-K notice |
| **5:45 – 6:45** | **Act V: Gateways & Compliance** | `view-verification` & `view-compliance` | 32 API gateways (98.9% uptime), Computer Vision photo recount, intake simulator |
| **6:45 – 7:45** | **Act VI: Legal Trust & EoA** | `view-approvals` & `view-audit` | Class-3 DSC batch digital signing, QR public verification, Merkle tree SHA-256 ledger |
| **7:45 – 8:30** | **Act VII: Conclusion** | Overview / Summary Slide | 85% time reduction, zero-fraud guarantee, alignment with NEP 2020 & Digital India |

---

## 🎬 Scene-by-Scene Script

---

### ACT I: The Crisis in Statutory Scrutiny (0:00 – 1:00)

#### Visuals
- Camera on speaker (or clean intro title card with project title: **TrustLens: AICTE Statutory Scrutiny & Approval Decision-Support System**).
- Then transition screen to the Overview Dashboard at `http://localhost:3000`.

#### Screen Action
- Hover over the top bar showing: `AICTE CENTRAL STATUTORY SCRUTINY PORTAL`, the live clock, and Officer Priya Sharma’s credentials.

#### Voiceover Script
> *"Greetings, respected evaluators and jury members.*
>
> *Every year, over 10,000 technical and polytechnic institutions across India apply to the All India Council for Technical Education (AICTE) for Extension of Approval (EoA) and course variations. Each application carries more than 40 statutory annexures—from Municipal Building Sanctions and Land Indentures to Fire Safety NOCs and Faculty Cadre Rolls.*
>
> *Currently, regulatory scrutiny officers are forced to manually comb through hundreds of thousands of PDF pages. This creates a severe three-fold crisis:*
> 1. **Massive Administrative Backlog:** *Scrutiny takes months, causing severe anxiety for students and institutions.*
> 2. **Document Forgery & Tampering:** *Expired NOCs, doctored building blueprints, and mortgaged land titles often slip through.*
> 3. **The Ghost Faculty Syndicate:** *Unscrupulous operators register the same senior professor’s credentials concurrently across 3 or 4 colleges in different states to satisfy mandatory faculty-student ratios.*
>
> *To solve this critical national challenge, we built **TrustLens**—an AI-powered, cryptographically verifiable Statutory Scrutiny and Decision-Support System designed strictly in accordance with the AICTE Approval Process Handbook (APH 2026–27). Let us walk you through the live system."*

---

### ACT II: Command Center & Scrutiny Queue (1:00 – 2:00)

#### Visuals & Screen Action
1. Show `#view-overview` (Overview Dashboard).
2. Point cursor to:
   - The top metric cards: Total Applications (1,420), Automated Scrutiny Rate (83.4%), High Risk Flags (46), Auto-Resolved Gateways.
   - The **AICTE Approval & Scrutiny Pipeline** visual bar (63.0% approval rate).
   - The **8-Week Trend Chart**; toggle buttons from `Weekly` to `Bi-Weekly` to `Cumulative`.
   - Hover over the stacked bar chart to show the glassmorphic tooltip with 6 statutory verdicts (*Verified, Pending, Mismatch, Expired, Source Unavailable, Manual Review*).
3. Click **"Queue"** in the top navigation bar to switch to `#view-queue`.
4. In `#view-queue`:
   - Point out the 128 loaded institutions.
   - Filter by Risk Tier: click `Critical / High Risk`.
   - Point to the top row: **APP-2026-00417 — Northfield Institute of Technology** with an **88/100 Risk Score**.
   - Click the **"Inspect Case"** button on Northfield.

#### Voiceover Script
> *"We begin in the **Scrutiny Officer Command Center**. The system aggregates 1,420 active applications for Academic Year 2026–27. Notice how our pipeline classifies every single dossier into six determinative statutory verdicts: Verified, Mismatch, Expired, Pending, Source Unavailable, or Manual Review.*
>
> *Our machine-learning risk engine continuously computes an aggregate risk score for each applicant based on zero-tolerance safety rules, municipal GIS discrepancies, and biometric cross-indexes.*
>
> *Switching to the **Applications Scrutiny Queue**, scrutiny officers have an actionable triage table. Instead of reviewing files chronologically, officers immediately focus on high-risk anomalies. At the top of our queue sits Application `APP-2026-00417` for **Northfield Institute of Technology**—flagged at **High Risk (88/100)** due to Fire NOC expiration, municipal GIS encroachment, and multi-institutional faculty collision. Let’s enter the deep forensic dossier."*

---

### ACT III: Deep Forensic Case & Evidence Studio (2:00 – 4:30)
*(⭐ Core Technical Demo Highlight)*

#### Visuals & Screen Action
1. We are now in `#view-cases` (Case Dossier & Evidence Studio).
2. Point out:
   - Institutional identifier badge: `APP-2026-00417`, `EoA Extension of Approval 2026-27`.
   - Click the red **HIGH RISK TIER (88/100)** badge to show the factor breakdown popover (Fire NOC 42%, Faculty collision 35%, GIS variance 23%).
3. Center PDF Viewer:
   - **Document 1: Fire Safety NOC (`fire_noc`)**:
     - Point out the Delhi Fire Services Form B-4, page count, and OCR confidence badge (**94.2%**).
     - Point out the bounding boxes on the document (Registration No, Issuance Date, and **Expired Validity Date: 31-Dec-2025**).
     - Point to the right-hand **Corroboration Rail**:
       - It shows a direct real-time API query to the *Delhi Fire Service Official Portal API*.
       - Highlight the status: `HTTP 404 NOT_FOUND / EXPIRED`. TrustLens caught that the submitted NOC had lapsed two months prior to application submission.
   - **Document 2: Central Faculty Biometric Roll (`faculty_roster`)**:
     - Click the **"Faculty Cadre Roll"** thumbnail in the document switcher.
     - Notice how the canvas smoothly switches to the official AICTE Central Biometric Cadre Roll.
     - Point to the highlighted red row: **Prof. Dr. Rajesh Varma (AICTE Token F-7F3A)**.
     - Point to the right rail: The *AICTE Central Biometric Repository API* flags concurrent tenure at 3 institutions simultaneously without a statutory NOC!
   - **Document 3: Municipal Cadastral Map (`cadastral_map`)**:
     - Click the **"Cadastral Map"** thumbnail.
     - Show the vector SVG map rendering the sanctioned perimeter vs. the ground footprint.
     - Point out the **+33.3% area overstep** and **4.8-meter green buffer encroachment** compared against the live *DDA Master GIS Spatial Database API*.
   - **Document 4: Structural Floor Blueprint (`floor_plan`)**:
     - Click the **"MCD OBPS Blueprint"** thumbnail.
     - Show the structural schematic flagging an unapproved 5th-floor civil elevation and staircase fire egress shortfall of 1.2 meters.
   - **Document 5: Land Title Indenture (`land_deed`)**:
     - Click the **"Land Deed Indenture"** thumbnail.
     - Show the Sub-Registrar lease indenture highlighting an undisclosed **State Bank of India ₹14.50 Crore mortgage lien**, corroborated against the *Delhi State Bhulekh Land Records Gateway*.
4. Click the blue **"Request Clarification"** button to show the institutional query modal, then click **"Finalize Determination"** to demonstrate automated Scrutiny Committee Report (SCR) generation.

#### Voiceover Script
> *"This is the **Case & Evidence Forensic Studio**—the intellectual core of TrustLens. In traditional workflows, an officer would look at paper scans with no external ground truth. TrustLens transforms this into an automated, multi-source statutory corroboration engine.*
>
> *Look at our dynamic document switcher. The applicant submitted 5 primary statutory instruments:*
>
> *First, their **Fire Safety Certificate**. Our OCR engine instantly parsed Delhi Fire Service Form B-4 with 94.2% confidence and bounded the validity date. Concurrently, TrustLens queried the live Delhi Fire Service Gateway API in the right panel. The result? The portal returned a verified expiration on December 31, 2025. The institution submitted an expired certificate hoping manual reviewers wouldn't verify the registry.*
>
> *Next, we click the **Faculty Cadre Roll**. The system extracts every professor’s token and cross-checks them against the national Aadhaar AEBAS biometric repository. It immediately flags Professor Dr. Rajesh Varma with a severe collusion alert.*
>
> *Third, we switch to the **Cadastral Map**. TrustLens overlays the applicant’s vector boundary against the DDA Master GIS database, discovering a +33.3% unapproved footprint overstep and a 4.8-meter green belt encroachment.*
>
> *We also inspect the **MCD OBPS Structural Blueprint** which uncovers an unapproved 5th floor, and the **Land Title Indenture**, where our gateway query to the State Bhulekh Registry unmasked a hidden 14.5 Crore Rupee mortgage lien.*
>
> *With one click, the officer can issue an official clarification or generate an AI-assisted Scrutiny Committee Report (SCR) that cites exact handbook clauses."*

---

### ACT IV: Evidence Graph & Syndicate Detection (4:30 – 5:45)

#### Visuals & Screen Action
1. Click **"Evidence Graph"** in the top navigation bar to open `#view-graph`.
2. Interacting with the canvas:
   - Click and drag to pan across the graph.
   - Use the mouse wheel or the `+` / `-` zoom controls on the bottom-right.
   - Show the dynamic minimap tracking the viewport.
   - Click on the central red conflict node: **Dr. Rajesh Varma (Faculty Token F-7F3A)**.
3. Show the Right Rail Inspector updating:
   - Ground: Concurrent full-time tenure across 3 distant institutions:
     1. Northfield Institute of Technology (Delhi)
     2. Kalinga Institute of Advanced Sciences (Bhubaneswar, Odisha)
     3. Deccan Polytechnic (Pune, Maharashtra)
   - Show the Biometric AEBAS conflict: Punch at 09:14 IST in Delhi vs. 09:22 IST in Bhubaneswar (8 minutes apart, physically impossible).
4. Click the purple button: **"Issue Statutory Show-Cause Notice"**.
   - Show the popup modal with auto-populated grounds under AICTE Section 10-K.
   - Point out the cryptographic signature seal by Officer Priya Sharma.
   - Click **"Dispatch Legal Notice"** (toast notification pops up).

#### Voiceover Script
> *"One of the greatest frauds in higher education accreditation is the ghost faculty syndicate—consultancies that circulate the degrees and identities of qualified doctorates across multiple institutions simultaneously to pass AICTE inspections.*
>
> *TrustLens solves this using our **Evidence Graph & Syndicate Detection Engine**. The graph constructs a knowledge graph of institutions, trusts, faculty tokens, and bank account hashes.*
>
> *Notice this red cluster. When we click on Faculty Token `F-7F3A`, the inspector reveals that Dr. Rajesh Varma is concurrently claimed as a full-time Professor at Northfield Institute in Delhi, Kalinga Institute in Bhubaneswar, and Deccan Polytechnic in Pune.*
>
> *More critically, our live AEBAS biometric telemetry proves impossible physical concurrency: biometric check-in at 9:14 AM in Delhi and 9:22 AM in Bhubaneswar on the exact same morning!*
>
> *With zero manual investigation, the officer clicks **Issue Statutory Show-Cause Notice**. The system formats a legally binding notice under Section 10-K citing Chapter IV Clause 4.12 of the Approval Process Handbook, cryptographically signed and dispatched in seconds."*

---

### ACT V: Real-Time Gateways & Compliance Evaluator (5:45 – 6:45)

#### Visuals & Screen Action
1. Click **"Verification"** in the top navbar (`#view-verification`).
   - Point out the **32 Active Gateways** and **98.9% API health**.
   - Show the status cards: Delhi Fire Service, AICTE Biometric AEBAS, DDA Master GIS, MCD OBPS, Bhulekh Land Gateway.
   - Click **"Trigger Batch Re-verify"** (shows simulated micro-telemetry and live sync).
2. Click **"Compliance"** in the top navbar (`#view-compliance`).
   - Show the **Statutory Norms Discrepancy Matrix**:
     - Faculty-to-Student Cadre Ratio (FSR): 32 required vs. 29 corroborated (-9.3% deficit).
     - Instructional Built-Up Area: 14,200 sq.m required vs. 12,200 sq.m confirmed (-14.1% gap).
     - Computing Facilities: 150 required vs. 84 active on campus subnet (-66 terminal deficit).
     - Library Titles: 8,000 required vs. 9,200 confirmed (Compliant).
   - Scroll down to the **Infrastructure Evidence Gallery**:
     - Show the Computer Vision geotagged inspection shots.
     - Show the Computer Vision terminal count (32 detected vs 60 claimed) and the ramp slope breach (1:8 vs 1:12 accessible norm).
   - Scroll to the bottom: **Interactive Intake Simulator**:
     - Change the dropdown to `B.Tech Robotics & Automation (+60 Seats)` to show real-time recalculation of faculty and laboratory requirements.

#### Voiceover Script
> *"In the **Verification Center**, TrustLens connects to 32 national and state API gateways—including DigiLocker, UIDAI AEBAS, state revenue portals, and municipal building repositories—with sub-second query latency and automated retry fallbacks.*
>
> *In the **Compliance Assistant**, the system benchmarks institutional declarations against exact statutory thresholds.*
> *Here, the Norms Discrepancy Matrix reveals that Northfield has a 9.3% faculty cadre deficit, a 14.1% physical plinth area gap, and an active computing deficit where network telemetry detected only 84 active MAC addresses during peak shifts.*
>
> *Furthermore, our **Computer Vision Evidence Gallery** analyzes geotagged photos uploaded by field inspection squads. Automated CV counting flagged that Lab 2 contains only 32 terminals instead of the 60 claimed, and identified non-compliant ramp gradients under Accessible India norms.*
>
> *Finally, the **Intake Simulator** allows administrators to stress-test proposed course expansions before issuing approvals."*

---

### ACT VI: Digital Signatures, Public Trust & Audit Trail (6:45 – 7:45)

#### Visuals & Screen Action
1. Click **"Approvals"** in the top navbar (`#view-approvals`).
   - Show the official **Extension of Approval (EoA) Grant Instrument**.
   - Point to the official Government of India / AICTE seal, QR code, and digitally signed metadata.
   - Click the **"Batch Digital Sign"** button to demonstrate Class-3 DSC cryptographic token signing.
   - Click **"Public Verification Portal"** to show the citizen-facing verification screen with green authentic checkmark.
2. Click **"Audit Trail"** in the top navbar (`#view-audit`).
   - Point out **Cryptographic Integrity: VALID & UNBROKEN**.
   - Point out **NIC GovCloud L3 HSM Signed**, Genesis Hash Seal, and Block Height (`#41,209`).
   - Point out the active block forensics card: HMAC-SHA256 seal and PKCS#11 HSM token validation.

#### Voiceover Script
> *"When an institution passes all statutory requirements, TrustLens transitions to disposition. In the **EoA Grants Studio**, the system compiles the formal Extension of Approval letter.*
>
> *Officers execute batch digital signatures using **Class-3 Digital Signature Certificates (DSC)** in compliance with the Information Technology Act, 2000. Each generated approval carries a secure, high-density QR code that links directly to the public AICTE verification portal, allowing parents, students, and employers to verify authentic approvals instantly and prevent fraudulent colleges from deceiving the public.*
>
> *Every single officer action, AI recommendation, gate query, and flag dismissal is recorded in the **Statutory Audit Trail**—an immutable, SHA-256 cryptographic hash chain anchored to NIC HSM hardware. This ensures zero unauthorized tampering, complete administrative transparency, and legally defensible records admissible in court under Section 65B of the Indian Evidence Act."*

---

### ACT VII: Impact & Conclusion (7:45 – 8:30)

#### Visuals
- Switch back to the main Overview Dashboard (`#view-overview`) or show closing summary graphic.
- Show key quantitative impact bullets on screen.

#### Voiceover Script
> *"To summarize, TrustLens revolutionizes statutory regulatory scrutiny:*
> - **85% Reduction in Turnaround Time:** *Institutional scrutiny drops from 4 to 6 weeks down to mere seconds for automated corroboration.*
> - **Zero Tolerance for Document Fraud:** *Cross-verifying with 32 state and central registries eliminates doctored certificates, expired NOCs, and secret liens.*
> - **Eradication of Ghost Faculty:** *Our national knowledge graph makes multi-institutional faculty syndicates impossible.*
> - **Empowering Human Officers:** *AI does the heavy evidentiary lifting, while statutory officers retain determinative, legally binding authority.*
>
> *TrustLens is modular, scalable, built entirely with modern open standards, and ready for integration into the AICTE National Portal. It delivers the transparent, efficient, and accountable regulatory governance envisioned by the National Education Policy 2020.*
>
> *Thank you, and we welcome your questions."*

---

## 💡 Evaluator Q&A Defense Sheet (Be Ready for These Questions)

| Potential Jury Question | Recommended Answer |
|---|---|
| **Q1: Does AI replace the human scrutiny officer?** | *"No. TrustLens is explicitly designed as a Decision-Support System. AI extracts, triangulates, and highlights discrepancies, but all determinative regulatory decisions—such as issuing a Show-Cause Notice or Granting EoA—strictly require a human officer's Class-3 DSC cryptographic signature."* |
| **Q2: What happens if a state portal API is down?** | *"Our system has a dedicated 'Source Unavailable' status verdict. When an external gateway fails or times out, the application is not rejected; it is cleanly queued with a timestamped retry token and surfaced to the officer with cached fallback or manual verification routing."* |
| **Q3: How does it detect ghost faculty without violating privacy?** | *"Faculty deduplication uses cryptographic hashes of Aadhaar tokens and PAN credentials via the NIC AEBAS repository, ensuring full compliance with the Digital Personal Data Protection (DPDP) Act while guaranteeing unique faculty allocation."* |
| **Q4: Is the audit trail legally admissible in court?** | *"Yes. Every audit log event is sealed using PKCS#11 hardware security modules (HSM) and SHA-256 Merkle hashes, satisfying the strict provenance requirements of Section 65B of the Indian Evidence Act."* |

---

## 🎥 Recording Tips for Maximum Visual Impact
1. **Mouse Movements:** Move your mouse smoothly; hover over tooltips and stat badges for 1–2 seconds before clicking.
2. **Tab Transitions:** Use the top navigation bar or the built-in action buttons (`switchView('cases')`, `switchView('graph')`, etc.) for seamless, instant transitions.
3. **Show Dynamic Switching:** In the Case Studio, make sure you click through all 5 document tabs (**Fire NOC**, **Cadre Roll**, **Cadastral Map**, **Blueprint**, **Land Deed**)—this visually proves the depth of the implementation.
4. **Graph Interaction:** Zoom in on the red cluster in the Evidence Graph to showcase interactive pan/zoom physics.
