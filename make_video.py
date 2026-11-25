import os
import sys
import time
import json
import subprocess
import requests
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import imageio_ffmpeg

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
API_URL = "https://api.vachana.ai/api/v1/tts/inference"
API_KEY = os.environ.get("VACHANA_API_KEY", "")
VOICE = "Pranav"
MODEL = "timbre-v2.5"
LANGUAGE = "en-IN"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VOICE_DIR = os.path.join(BASE_DIR, "voiceover")
PARTS_DIR = os.path.join(VOICE_DIR, "parts")
FRAMES_DIR = os.path.join(VOICE_DIR, "frames")
CLIPS_DIR = os.path.join(VOICE_DIR, "clips")
OUTPUT_VIDEO = os.path.join(BASE_DIR, "TrustLens_SIH_Project_Presentation_Demo.mp4")
OUTPUT_VIDEO_WEB = os.path.join(VOICE_DIR, "TrustLens_SIH_Project_Presentation_Demo.mp4")

for d in [VOICE_DIR, PARTS_DIR, FRAMES_DIR, CLIPS_DIR]:
    os.makedirs(d, exist_ok=True)

# 39 Synchronized Moments across 7 Acts
MOMENTS = [
    # --- ACT I: PROBLEM STATEMENT (6 steps) ---
    {
        "act": "ACT I • PROBLEM STATEMENT & REGULATORY CRISIS",
        "act_idx": 1,
        "text": "Greetings, respected evaluators and jury members. Every year, over ten thousand technical and polytechnic institutions across India apply to the All India Council for Technical Education for Extension of Approval and course variations.",
        "action": "title_card",
        "title": "TrustLens — AICTE Statutory Scrutiny Portal",
        "subtitle_label": "Smart India Hackathon • Problem Statement: AI-Powered Scrutiny"
    },
    {
        "act": "ACT I • PROBLEM STATEMENT & REGULATORY CRISIS",
        "act_idx": 1,
        "text": "Each application carries more than forty statutory annexures, from Municipal Building Sanctions and Land Indentures to Fire Safety N O C certificates and Faculty Cadre Rolls.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT I • PROBLEM STATEMENT & REGULATORY CRISIS",
        "act_idx": 1,
        "text": "Currently, regulatory scrutiny officers are forced to manually comb through hundreds of thousands of P D F pages. This creates a severe three-fold crisis.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 200);"
    },
    {
        "act": "ACT I • PROBLEM STATEMENT & REGULATORY CRISIS",
        "act_idx": 1,
        "text": "First, a massive administrative backlog where scrutiny takes months, causing severe anxiety for students and colleges. Second, document forgery and tampering, where expired N O C s, doctored civil blueprints, and mortgaged land titles often slip through.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 400);"
    },
    {
        "act": "ACT I • PROBLEM STATEMENT & REGULATORY CRISIS",
        "act_idx": 1,
        "text": "And third, the ghost faculty syndicate, where unscrupulous operators register the same senior professor's credentials concurrently across three or four colleges in different states to satisfy mandatory faculty-student ratios.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 600);"
    },
    {
        "act": "ACT I • PROBLEM STATEMENT & REGULATORY CRISIS",
        "act_idx": 1,
        "text": "To solve this critical national challenge, we built TrustLens: an A I powered, cryptographically verifiable Statutory Scrutiny and Decision-Support System designed strictly in accordance with the A I C T E Approval Process Handbook. Let us walk you through the live system.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 0);"
    },

    # --- ACT II: OVERVIEW & QUEUE (5 steps) ---
    {
        "act": "ACT II • OVERVIEW COMMAND CENTER & QUEUE TRIAGE",
        "act_idx": 2,
        "text": "We begin in the Scrutiny Officer Command Center. The system aggregates fourteen hundred and twenty active applications for Academic Year 2026-27.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT II • OVERVIEW COMMAND CENTER & QUEUE TRIAGE",
        "act_idx": 2,
        "text": "Notice how our pipeline classifies every single dossier into six determinative statutory verdicts: Verified, Mismatch, Expired, Pending, Source Unavailable, or Manual Review.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 350);"
    },
    {
        "act": "ACT II • OVERVIEW COMMAND CENTER & QUEUE TRIAGE",
        "act_idx": 2,
        "text": "Our machine-learning risk engine continuously computes an aggregate risk score for each applicant based on zero-tolerance safety rules, municipal G I S discrepancies, and biometric cross-indexes.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 700);"
    },
    {
        "act": "ACT II • OVERVIEW COMMAND CENTER & QUEUE TRIAGE",
        "act_idx": 2,
        "text": "Switching to the Applications Scrutiny Queue, officers have an actionable triage table. Instead of reviewing files chronologically, officers immediately focus on high-risk anomalies.",
        "action": "js",
        "js": "switchView('queue'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT II • OVERVIEW COMMAND CENTER & QUEUE TRIAGE",
        "act_idx": 2,
        "text": "At the top of our queue sits Application APP-2026-00417 for Northfield Institute of Technology, flagged at High Risk with an eighty-eight out of one hundred score, due to Fire N O C expiration, municipal G I S encroachment, and multi-institutional faculty collision. Let us enter the deep forensic dossier.",
        "action": "js",
        "js": "switchView('queue'); window.scrollTo(0, 150);"
    },

    # --- ACT III: FORENSIC CASE STUDIO (8 steps) ---
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "This is the Case and Evidence Forensic Studio, the intellectual core of TrustLens. In traditional workflows, an officer would look at paper scans with no external ground truth. TrustLens transforms this into an automated, multi-source statutory corroboration engine.",
        "action": "js",
        "js": "switchView('cases'); selectCase('APP-2026-00417'); toggleCaseRiskPopover(); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "Look at our dynamic document switcher. The applicant submitted five primary statutory instruments.",
        "action": "js",
        "js": "switchView('cases'); selectCase('APP-2026-00417'); switchEvidenceDoc('fire_noc'); window.scrollTo(0, 60);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "First, their Fire Safety Certificate. Our O C R engine instantly parsed Delhi Fire Service Form B-4 with ninety-four point two percent confidence and bounded the validity date.",
        "action": "js",
        "js": "switchView('cases'); switchEvidenceDoc('fire_noc'); window.scrollTo(0, 100);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "Concurrently, TrustLens queried the live Delhi Fire Service Gateway A P I in the right panel. The portal returned a verified expiration on December thirty-first, 2025. The institution submitted an expired certificate hoping manual reviewers would not verify the registry.",
        "action": "js",
        "js": "switchView('cases'); switchEvidenceDoc('fire_noc'); window.scrollTo(0, 120);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "Next, we click the Faculty Cadre Roll. The system extracts every professor's token and cross-checks them against the national Aadhaar A E B A S biometric repository. It immediately flags Professor Doctor Rajesh Varma with a severe collusion alert.",
        "action": "js",
        "js": "switchView('cases'); switchEvidenceDoc('faculty_roster'); window.scrollTo(0, 100);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "Third, we switch to the Cadastral Map. TrustLens overlays the applicant's vector boundary against the D D A Master G I S database, discovering a thirty-three point three percent unapproved footprint overstep and a four point eight meter green belt encroachment.",
        "action": "js",
        "js": "switchView('cases'); switchEvidenceDoc('cadastral_map'); window.scrollTo(0, 100);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "We also inspect the M C D Online Building Sanction Blueprint, which uncovers an unapproved fifth floor, and the Land Title Indenture, where our gateway query to the State Bhulekh Registry unmasked a hidden fourteen point five crore rupee mortgage lien.",
        "action": "js",
        "js": "switchView('cases'); switchEvidenceDoc('floor_plan'); window.scrollTo(0, 100);"
    },
    {
        "act": "ACT III • FORENSIC CASE STUDIO & 5 STATUTORY INSTRUMENTS",
        "act_idx": 3,
        "text": "With one click, the officer can issue an official clarification or generate an A I assisted Scrutiny Committee Report citing exact handbook clauses.",
        "action": "js",
        "js": "switchView('cases'); switchEvidenceDoc('land_deed'); window.scrollTo(0, 80);"
    },

    # --- ACT IV: EVIDENCE GRAPH (5 steps) ---
    {
        "act": "ACT IV • EVIDENCE GRAPH & GHOST FACULTY SYNDICATE DETECTION",
        "act_idx": 4,
        "text": "One of the greatest frauds in higher education accreditation is the ghost faculty syndicate: consultancies that circulate the degrees and identities of qualified doctorates across multiple institutions simultaneously to pass A I C T E inspections.",
        "action": "js",
        "js": "switchView('graph'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT IV • EVIDENCE GRAPH & GHOST FACULTY SYNDICATE DETECTION",
        "act_idx": 4,
        "text": "TrustLens solves this using our Evidence Graph and Syndicate Detection Engine. The graph constructs a knowledge graph of institutions, trusts, faculty tokens, and bank account hashes.",
        "action": "js",
        "js": "switchView('graph'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT IV • EVIDENCE GRAPH & GHOST FACULTY SYNDICATE DETECTION",
        "act_idx": 4,
        "text": "Notice this red cluster. When we click on Faculty Token F-7F3A, the inspector reveals that Doctor Rajesh Varma is concurrently claimed as a full-time Professor at Northfield Institute in Delhi, Kalinga Institute in Bhubaneswar, and Deccan Polytechnic in Pune.",
        "action": "js",
        "js": "switchView('graph'); inspectGraphNode('faculty_rajesh');"
    },
    {
        "act": "ACT IV • EVIDENCE GRAPH & GHOST FACULTY SYNDICATE DETECTION",
        "act_idx": 4,
        "text": "More critically, our live A E B A S biometric telemetry proves impossible physical concurrency: biometric check-in at nine fourteen A M in Delhi, and nine twenty-two A M in Bhubaneswar on the exact same morning, just eight minutes apart across thirteen hundred kilometers.",
        "action": "js",
        "js": "switchView('graph'); inspectGraphNode('faculty_rajesh');"
    },
    {
        "act": "ACT IV • EVIDENCE GRAPH & GHOST FACULTY SYNDICATE DETECTION",
        "act_idx": 4,
        "text": "With zero manual investigation, the officer clicks Issue Statutory Show-Cause Notice. The system formats a legally binding notice under Section 10-K citing Chapter Four Clause four point twelve of the Approval Process Handbook, cryptographically signed and dispatched in seconds.",
        "action": "js",
        "js": "switchView('graph'); openGraphNoticeModal();"
    },

    # --- ACT V: GATEWAYS & COMPLIANCE (5 steps) ---
    {
        "act": "ACT V • 32 STATE GATEWAYS & COMPLIANCE ASSISTANT",
        "act_idx": 5,
        "text": "In the Verification Center, TrustLens connects to thirty-two national and state A P I gateways, including DigiLocker, U I D A I, state revenue portals, and municipal building repositories, with sub-second query latency and automated retry fallbacks.",
        "action": "js",
        "js": "closeGraphNoticeModal(); switchView('verification'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT V • 32 STATE GATEWAYS & COMPLIANCE ASSISTANT",
        "act_idx": 5,
        "text": "In the Compliance Assistant, the system benchmarks institutional declarations against exact statutory thresholds.",
        "action": "js",
        "js": "switchView('compliance'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT V • 32 STATE GATEWAYS & COMPLIANCE ASSISTANT",
        "act_idx": 5,
        "text": "Here, the Norms Discrepancy Matrix reveals that Northfield has a nine point three percent faculty cadre deficit, a fourteen point one percent physical plinth area gap, and an active computing deficit where network telemetry detected only eighty-four active M A C addresses during peak shifts.",
        "action": "js",
        "js": "switchView('compliance'); window.scrollTo(0, 400);"
    },
    {
        "act": "ACT V • 32 STATE GATEWAYS & COMPLIANCE ASSISTANT",
        "act_idx": 5,
        "text": "Furthermore, our Computer Vision Evidence Gallery analyzes geotagged photos uploaded by field inspection squads. Automated computer vision counting flagged that Lab Two contains only thirty-two terminals instead of the sixty claimed, and identified non-compliant ramp gradients under Accessible India norms.",
        "action": "js",
        "js": "switchView('compliance'); window.scrollTo(0, 950);"
    },
    {
        "act": "ACT V • 32 STATE GATEWAYS & COMPLIANCE ASSISTANT",
        "act_idx": 5,
        "text": "Finally, the Intake Simulator allows administrators to stress-test proposed course expansions before issuing approvals.",
        "action": "js",
        "js": "switchView('compliance'); window.scrollTo(0, 1450);"
    },

    # --- ACT VI: APPROVALS & AUDIT TRAIL (4 steps) ---
    {
        "act": "ACT VI • DIGITAL SIGNATURES & CRYPTOGRAPHIC AUDIT TRAIL",
        "act_idx": 6,
        "text": "When an institution passes all statutory requirements, TrustLens transitions to disposition. In the Extension of Approval Grants Studio, the system compiles the formal approval letter.",
        "action": "js",
        "js": "switchView('approvals'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT VI • DIGITAL SIGNATURES & CRYPTOGRAPHIC AUDIT TRAIL",
        "act_idx": 6,
        "text": "Officers execute batch digital signatures using Class-Three Digital Signature Certificates in compliance with the Information Technology Act. Each generated approval carries a secure, high-density Q R code that links directly to the public A I C T E verification portal, allowing parents, students, and employers to verify authentic approvals instantly and prevent fraudulent colleges from deceiving the public.",
        "action": "js",
        "js": "switchView('approvals'); window.scrollTo(0, 250);"
    },
    {
        "act": "ACT VI • DIGITAL SIGNATURES & CRYPTOGRAPHIC AUDIT TRAIL",
        "act_idx": 6,
        "text": "Every single officer action, A I recommendation, gateway query, and flag dismissal is recorded in the Statutory Audit Trail: an immutable, S H A two-fifty-six cryptographic hash chain anchored to N I C hardware security modules.",
        "action": "js",
        "js": "switchView('audit'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT VI • DIGITAL SIGNATURES & CRYPTOGRAPHIC AUDIT TRAIL",
        "act_idx": 6,
        "text": "This ensures zero unauthorized tampering, complete administrative transparency, and legally defensible records admissible in court under Section sixty-five B of the Indian Evidence Act.",
        "action": "js",
        "js": "switchView('audit'); window.scrollTo(0, 350);"
    },

    # --- ACT VII: CONCLUSION & IMPACT (6 steps) ---
    {
        "act": "ACT VII • TRANSFORMATIVE IMPACT & CONCLUSION",
        "act_idx": 7,
        "text": "To summarize, TrustLens revolutionizes statutory regulatory scrutiny.",
        "action": "js",
        "js": "switchView('overview'); window.scrollTo(0, 0);"
    },
    {
        "act": "ACT VII • TRANSFORMATIVE IMPACT & CONCLUSION",
        "act_idx": 7,
        "text": "First, an eighty-five percent reduction in turnaround time, dropping institutional scrutiny from weeks down to mere seconds for automated corroboration.",
        "action": "title_card",
        "title": "85% Turnaround Reduction",
        "subtitle_label": "From 4-6 Weeks of Manual Review to Instant Multi-Source Triangulation"
    },
    {
        "act": "ACT VII • TRANSFORMATIVE IMPACT & CONCLUSION",
        "act_idx": 7,
        "text": "Second, zero tolerance for document fraud, where cross-verifying with thirty-two state and central registries eliminates doctored certificates, expired N O C s, and secret liens.",
        "action": "title_card",
        "title": "100% Registry Cross-Corroboration",
        "subtitle_label": "Zero Tolerance for Forged NOCs, GIS Oversteps, or Mortgaged Deeds"
    },
    {
        "act": "ACT VII • TRANSFORMATIVE IMPACT & CONCLUSION",
        "act_idx": 7,
        "text": "Third, the eradication of ghost faculty, where our national knowledge graph makes multi-institutional faculty syndicates impossible.",
        "action": "title_card",
        "title": "Eradication of Ghost Faculty Syndicates",
        "subtitle_label": "Aadhaar AEBAS Biometric Telemetry & Graph Knowledge Base"
    },
    {
        "act": "ACT VII • TRANSFORMATIVE IMPACT & CONCLUSION",
        "act_idx": 7,
        "text": "And fourth, empowering human officers, where A I does the heavy evidentiary lifting, while statutory officers retain determinative, legally binding authority.",
        "action": "title_card",
        "title": "Human-in-the-Loop Authority",
        "subtitle_label": "Legally Binding Class-3 DSC Signatures & Tamper-Proof Audit Provenance"
    },
    {
        "act": "ACT VII • TRANSFORMATIVE IMPACT & CONCLUSION",
        "act_idx": 7,
        "text": "TrustLens is modular, scalable, built entirely with modern open standards, and ready for integration into the A I C T E National Portal. It delivers the transparent, efficient, and accountable regulatory governance envisioned by the National Education Policy 2020. Thank you, and we welcome your questions.",
        "action": "title_card",
        "title": "TrustLens — Built for AICTE & National Education Policy 2020",
        "subtitle_label": "Smart India Hackathon 2026 • Thank You"
    }
]

def synthesize_audio(text, output_path):
    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        return output_path
        
    headers = {"Content-Type": "application/json", "X-API-Key-ID": API_KEY}
    payload = {
        "text": text,
        "voice": VOICE,
        "model": MODEL,
        "language": LANGUAGE,
        "speed": 1.0,
        "audio_config": {"sample_rate": 24000, "container": "mp3"}
    }
    for attempt in range(1, 4):
        try:
            res = requests.post(API_URL, json=payload, headers=headers, timeout=45)
            if res.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(res.content)
                return output_path
            time.sleep(1)
        except Exception:
            time.sleep(1)
    raise RuntimeError(f"TTS Synthesis failed for: {text[:40]}...")

def get_audio_duration(audio_path):
    cmd = [FFMPEG_EXE, "-i", audio_path]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
            h, m, s = float(parts[0]), float(parts[1]), float(parts[2])
            return h * 3600 + m * 60 + s
    return 10.0

def create_title_card(title, subtitle_label):
    img = Image.new("RGB", (1920, 1080), color=(11, 31, 58))
    draw = ImageDraw.Draw(img)
    
    try:
        font_large = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 64)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32)
        font_tag = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    except Exception:
        font_large = font_sub = font_tag = ImageFont.load_default()
        
    # Subtle geometric decorative background
    draw.rectangle([0, 0, 1920, 12], fill=(0, 97, 109))
    draw.rectangle([0, 1068, 1920, 1080], fill=(0, 97, 109))
    
    # Tag
    draw.text((120, 360), "ALL INDIA COUNCIL FOR TECHNICAL EDUCATION • STATUTORY AUDIT SYSTEM", font=font_tag, fill=(0, 200, 220))
    # Main Title
    draw.text((120, 420), title, font=font_large, fill=(255, 255, 255))
    # Subtitle
    draw.text((120, 520), subtitle_label, font=font_sub, fill=(180, 205, 220))
    # Watermark
    draw.text((120, 960), "TrustLens Project Architecture • Smart India Hackathon Demo", font=font_tag, fill=(100, 130, 150))
    
    return img

def overlay_subtitles(base_img, act_label, subtitle_text, progress_ratio=0.5):
    img = base_img.copy().convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Font setup
    try:
        font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)
        font_text = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)
        font_header = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    except Exception:
        font_badge = font_text = font_header = ImageFont.load_default()
        
    # Top Banner Strip (Act name & live presentation pill)
    draw.rectangle([0, 0, 1920, 52], fill=(11, 31, 58, 235))
    draw.ellipse([40, 20, 52, 32], fill=(0, 210, 150, 255))
    draw.text((65, 14), act_label, font=font_header, fill=(255, 255, 255, 255))
    draw.text((1650, 14), "TrustLens Live Scrutiny Studio", font=font_badge, fill=(170, 210, 230, 255))
    
    # Bottom Subtitle Floating Glass Card (Width: 1720, Centered)
    card_x1, card_y1, card_x2, card_y2 = 100, 910, 1820, 1040
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=16, fill=(10, 25, 48, 235), outline=(0, 97, 109, 200), width=2)
    
    # Audio speaker icon badge
    draw.rounded_rectangle([card_x1 + 20, card_y1 + 18, card_x1 + 150, card_y1 + 46], radius=6, fill=(0, 97, 109, 255))
    draw.text((card_x1 + 30, card_y1 + 22), "NARRATION", font=font_badge, fill=(255, 255, 255, 255))
    
    # Wrap subtitle text into 2 lines if long
    words = subtitle_text.split()
    line1 = []
    line2 = []
    curr_len = 0
    for w in words:
        if curr_len < 105:
            line1.append(w)
            curr_len += len(w) + 1
        else:
            line2.append(w)
            
    t1 = " ".join(line1)
    t2 = " ".join(line2)
    
    draw.text((card_x1 + 175, card_y1 + 20), t1, font=font_text, fill=(255, 255, 255, 255))
    if t2:
        draw.text((card_x1 + 175, card_y1 + 62), t2, font=font_text, fill=(225, 240, 250, 255))
        
    # Bottom subtle progress line
    draw.rectangle([0, 1074, int(1920 * progress_ratio), 1080], fill=(0, 210, 150, 255))
    
    return Image.alpha_composite(img, overlay).convert("RGB")

def render_clip(img_path, audio_path, output_clip_path):
    cmd = [
        FFMPEG_EXE, "-y",
        "-loop", "1",
        "-framerate", "30",
        "-i", img_path,
        "-i", audio_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        output_clip_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def main():
    print("=" * 70)
    print("TrustLens — Complete 7-Minute Automated Video Producer")
    print(f"Target Video: {OUTPUT_VIDEO}")
    print(f"Moments Count: {len(MOMENTS)}")
    print("=" * 70)
    
    # Step 1: Initialize Headless Selenium
    print("\n[1/4] Launching Headless Chrome at 1920x1080...")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--hide-scrollbars")
    
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:3000/index.html")
    time.sleep(2)
    print("  Dashboard loaded successfully!")
    
    clip_files = []
    
    # Step 2: Capture Frames & Audio for Each Moment
    print("\n[2/4] Capturing UI Frames and Synchronizing Audio...")
    for idx, m in enumerate(MOMENTS, 1):
        step_id = f"step_{idx:02d}"
        audio_file = os.path.join(PARTS_DIR, f"{step_id}.mp3")
        raw_frame_file = os.path.join(FRAMES_DIR, f"{step_id}_raw.png")
        final_frame_file = os.path.join(FRAMES_DIR, f"{step_id}_final.png")
        clip_file = os.path.join(CLIPS_DIR, f"{step_id}.mp4")
        
        sys.stdout.write(f"  [{idx:02d}/{len(MOMENTS)}] {m['act'][:30]}... ")
        sys.stdout.flush()
        
        # Audio
        synthesize_audio(m["text"], audio_file)
        
        # UI Action & Screenshot
        if m["action"] == "title_card":
            base_img = create_title_card(m["title"], m["subtitle_label"])
        else:
            try:
                driver.execute_script(m["js"])
            except Exception as js_err:
                pass
            time.sleep(0.5)
            driver.save_screenshot(raw_frame_file)
            base_img = Image.open(raw_frame_file)
            
        # Overlay Subtitles & Branded Frame
        progress = idx / len(MOMENTS)
        final_img = overlay_subtitles(base_img, m["act"], m["text"], progress)
        final_img.save(final_frame_file, quality=95)
        
        # Render Video Clip
        render_clip(final_frame_file, audio_file, clip_file)
        clip_files.append(clip_file)
        print("OK")
        
    driver.quit()
    print("\nAll 39 synchronized video clips rendered!")
    
    # Step 3: Concatenate All Clips into Master Presentation Video
    print("\n[3/4] Stitched Final Presentation Video via FFmpeg...")
    concat_list_file = os.path.join(CLIPS_DIR, "concat_list.txt")
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for c in clip_files:
            # Format: file 'c:\path\to\clip.mp4'
            escaped = c.replace("\\", "/")
            f.write(f"file '{escaped}'\n")
            
    concat_cmd = [
        FFMPEG_EXE, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        OUTPUT_VIDEO
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Also copy to web folder
    import shutil
    shutil.copyfile(OUTPUT_VIDEO, OUTPUT_VIDEO_WEB)
    
    file_size_mb = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
    total_sec = get_audio_duration(OUTPUT_VIDEO)
    mins = int(total_sec // 60)
    secs = int(total_sec % 60)
    
    print("\n" + "=" * 70)
    print("SUCCESS! COMPLETE PRESENTATION VIDEO GENERATED!")
    print(f"Master Video File: {OUTPUT_VIDEO}")
    print(f"File Size: {file_size_mb:.2f} MB")
    print(f"Total Duration: {mins}:{secs:02d} minutes")
    print(f"Web Browser URL: http://localhost:3000/voiceover/index.html")
    print("=" * 70)

if __name__ == "__main__":
    main()
