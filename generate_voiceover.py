import os
import sys
import time
import requests

API_URL = "https://api.vachana.ai/api/v1/tts/inference"
API_KEY = os.environ.get("VACHANA_API_KEY", "")
VOICE = "Pranav"  # Professional Indian English Male voice (Kaveri / Nalini also available)
MODEL = "timbre-v2.5"
LANGUAGE = "en-IN"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voiceover")

os.makedirs(OUTPUT_DIR, exist_ok=True)

ACTS = [
    {
        "id": "01_act1_problem_statement",
        "title": "Act I: Problem Statement & Regulatory Bottleneck",
        "duration_est": "0:00 - 1:00",
        "paragraphs": [
            "Greetings, respected evaluators and jury members. Every year, over ten thousand technical and polytechnic institutions across India apply to the All India Council for Technical Education for Extension of Approval and course variations.",
            "Each application carries more than forty statutory annexures, from Municipal Building Sanctions and Land Indentures to Fire Safety N O C certificates and Faculty Cadre Rolls.",
            "Currently, regulatory scrutiny officers are forced to manually comb through hundreds of thousands of P D F pages. This creates a severe three-fold crisis.",
            "First, a massive administrative backlog where scrutiny takes months, causing severe anxiety for students and colleges. Second, document forgery and tampering, where expired N O C s, doctored civil blueprints, and mortgaged land titles often slip through.",
            "And third, the ghost faculty syndicate, where unscrupulous operators register the same senior professor's credentials concurrently across three or four colleges in different states to satisfy mandatory faculty-student ratios.",
            "To solve this critical national challenge, we built TrustLens: an A I powered, cryptographically verifiable Statutory Scrutiny and Decision-Support System designed strictly in accordance with the A I C T E Approval Process Handbook. Let us walk you through the live system."
        ]
    },
    {
        "id": "02_act2_overview_and_queue",
        "title": "Act II: Overview Command Center & Scrutiny Queue",
        "duration_est": "1:00 - 2:00",
        "paragraphs": [
            "We begin in the Scrutiny Officer Command Center. The system aggregates fourteen hundred and twenty active applications for Academic Year 2026-27.",
            "Notice how our pipeline classifies every single dossier into six determinative statutory verdicts: Verified, Mismatch, Expired, Pending, Source Unavailable, or Manual Review.",
            "Our machine-learning risk engine continuously computes an aggregate risk score for each applicant based on zero-tolerance safety rules, municipal G I S discrepancies, and biometric cross-indexes.",
            "Switching to the Applications Scrutiny Queue, officers have an actionable triage table. Instead of reviewing files chronologically, officers immediately focus on high-risk anomalies.",
            "At the top of our queue sits Application APP-2026-00417 for Northfield Institute of Technology, flagged at High Risk with an eighty-eight out of one hundred score, due to Fire N O C expiration, municipal G I S encroachment, and multi-institutional faculty collision. Let us enter the deep forensic dossier."
        ]
    },
    {
        "id": "03_act3_forensic_cases_dossier",
        "title": "Act III: Deep Forensic Case & Evidence Studio",
        "duration_est": "2:00 - 4:30",
        "paragraphs": [
            "This is the Case and Evidence Forensic Studio, the intellectual core of TrustLens. In traditional workflows, an officer would look at paper scans with no external ground truth. TrustLens transforms this into an automated, multi-source statutory corroboration engine.",
            "Look at our dynamic document switcher. The applicant submitted five primary statutory instruments.",
            "First, their Fire Safety Certificate. Our O C R engine instantly parsed Delhi Fire Service Form B-4 with ninety-four point two percent confidence and bounded the validity date.",
            "Concurrently, TrustLens queried the live Delhi Fire Service Gateway A P I in the right panel. The portal returned a verified expiration on December thirty-first, 2025. The institution submitted an expired certificate hoping manual reviewers would not verify the registry.",
            "Next, we click the Faculty Cadre Roll. The system extracts every professor's token and cross-checks them against the national Aadhaar A E B A S biometric repository. It immediately flags Professor Doctor Rajesh Varma with a severe collusion alert.",
            "Third, we switch to the Cadastral Map. TrustLens overlays the applicant's vector boundary against the D D A Master G I S database, discovering a thirty-three point three percent unapproved footprint overstep and a four point eight meter green belt encroachment.",
            "We also inspect the M C D Online Building Sanction Blueprint, which uncovers an unapproved fifth floor, and the Land Title Indenture, where our gateway query to the State Bhulekh Registry unmasked a hidden fourteen point five crore rupee mortgage lien.",
            "With one click, the officer can issue an official clarification or generate an A I assisted Scrutiny Committee Report citing exact handbook clauses."
        ]
    },
    {
        "id": "04_act4_evidence_graph_syndicates",
        "title": "Act IV: Evidence Graph & Syndicate Detection",
        "duration_est": "4:30 - 5:45",
        "paragraphs": [
            "One of the greatest frauds in higher education accreditation is the ghost faculty syndicate: consultancies that circulate the degrees and identities of qualified doctorates across multiple institutions simultaneously to pass A I C T E inspections.",
            "TrustLens solves this using our Evidence Graph and Syndicate Detection Engine. The graph constructs a knowledge graph of institutions, trusts, faculty tokens, and bank account hashes.",
            "Notice this red cluster. When we click on Faculty Token F-7F3A, the inspector reveals that Doctor Rajesh Varma is concurrently claimed as a full-time Professor at Northfield Institute in Delhi, Kalinga Institute in Bhubaneswar, and Deccan Polytechnic in Pune.",
            "More critically, our live A E B A S biometric telemetry proves impossible physical concurrency: biometric check-in at nine fourteen A M in Delhi, and nine twenty-two A M in Bhubaneswar on the exact same morning, just eight minutes apart across thirteen hundred kilometers.",
            "With zero manual investigation, the officer clicks Issue Statutory Show-Cause Notice. The system formats a legally binding notice under Section 10-K citing Chapter Four Clause four point twelve of the Approval Process Handbook, cryptographically signed and dispatched in seconds."
        ]
    },
    {
        "id": "05_act5_verification_and_compliance",
        "title": "Act V: Gateways & Compliance Assistant",
        "duration_est": "5:45 - 6:45",
        "paragraphs": [
            "In the Verification Center, TrustLens connects to thirty-two national and state A P I gateways, including DigiLocker, U I D A I, state revenue portals, and municipal building repositories, with sub-second query latency and automated retry fallbacks.",
            "In the Compliance Assistant, the system benchmarks institutional declarations against exact statutory thresholds.",
            "Here, the Norms Discrepancy Matrix reveals that Northfield has a nine point three percent faculty cadre deficit, a fourteen point one percent physical plinth area gap, and an active computing deficit where network telemetry detected only eighty-four active M A C addresses during peak shifts.",
            "Furthermore, our Computer Vision Evidence Gallery analyzes geotagged photos uploaded by field inspection squads. Automated computer vision counting flagged that Lab Two contains only thirty-two terminals instead of the sixty claimed, and identified non-compliant ramp gradients under Accessible India norms.",
            "Finally, the Intake Simulator allows administrators to stress-test proposed course expansions before issuing approvals."
        ]
    },
    {
        "id": "06_act6_approvals_and_audit_trail",
        "title": "Act VI: Digital Signatures & Cryptographic Audit Trail",
        "duration_est": "6:45 - 7:45",
        "paragraphs": [
            "When an institution passes all statutory requirements, TrustLens transitions to disposition. In the Extension of Approval Grants Studio, the system compiles the formal approval letter.",
            "Officers execute batch digital signatures using Class-Three Digital Signature Certificates in compliance with the Information Technology Act. Each generated approval carries a secure, high-density Q R code that links directly to the public A I C T E verification portal, allowing parents, students, and employers to verify authentic approvals instantly and prevent fraudulent colleges from deceiving the public.",
            "Every single officer action, A I recommendation, gateway query, and flag dismissal is recorded in the Statutory Audit Trail: an immutable, S H A two-fifty-six cryptographic hash chain anchored to N I C hardware security modules.",
            "This ensures zero unauthorized tampering, complete administrative transparency, and legally defensible records admissible in court under Section sixty-five B of the Indian Evidence Act."
        ]
    },
    {
        "id": "07_act7_conclusion_and_impact",
        "title": "Act VII: Conclusion & Transformative Impact",
        "duration_est": "7:45 - 8:30",
        "paragraphs": [
            "To summarize, TrustLens revolutionizes statutory regulatory scrutiny.",
            "First, an eighty-five percent reduction in turnaround time, dropping institutional scrutiny from weeks down to mere seconds for automated corroboration.",
            "Second, zero tolerance for document fraud, where cross-verifying with thirty-two state and central registries eliminates doctored certificates, expired N O C s, and secret liens.",
            "Third, the eradication of ghost faculty, where our national knowledge graph makes multi-institutional faculty syndicates impossible.",
            "And fourth, empowering human officers, where A I does the heavy evidentiary lifting, while statutory officers retain determinative, legally binding authority.",
            "TrustLens is modular, scalable, built entirely with modern open standards, and ready for integration into the A I C T E National Portal. It delivers the transparent, efficient, and accountable regulatory governance envisioned by the National Education Policy 2020. Thank you, and we welcome your questions."
        ]
    }
]

def synthesize_text(text, voice=VOICE):
    headers = {
        "Content-Type": "application/json",
        "X-API-Key-ID": API_KEY
    }
    payload = {
        "text": text,
        "voice": voice,
        "model": MODEL,
        "language": LANGUAGE,
        "speed": 1.0,
        "audio_config": {
            "sample_rate": 24000,
            "container": "mp3"
        }
    }
    
    for attempt in range(1, 4):
        try:
            res = requests.post(API_URL, json=payload, headers=headers, timeout=45)
            if res.status_code == 200:
                return res.content
            else:
                print(f"    [WARN] Attempt {attempt} failed ({res.status_code}): {res.text[:120]}")
                time.sleep(2)
        except Exception as e:
            print(f"    [WARN] Exception on attempt {attempt}: {e}")
            time.sleep(2)
            
    raise RuntimeError(f"Failed to synthesize text after 3 attempts: {text[:60]}...")

def main():
    print("=" * 65)
    print("TrustLens — Gnani.ai Vach Voiceover Generation")
    print(f"Voice: {VOICE} | Model: {MODEL} | Language: {LANGUAGE}")
    print(f"Output Directory: {OUTPUT_DIR}")
    print("=" * 65)
    
    full_audio_bytes = bytearray()
    manifest = []
    
    for idx, act in enumerate(ACTS, 1):
        act_id = act["id"]
        title = act["title"]
        duration = act["duration_est"]
        print(f"\n[{idx}/{len(ACTS)}] Processing {title} ({duration})...")
        
        act_audio_bytes = bytearray()
        for p_idx, paragraph in enumerate(act["paragraphs"], 1):
            sys.stdout.write(f"  -> Synthesizing chunk {p_idx}/{len(act['paragraphs'])} ({len(paragraph)} chars)... ")
            sys.stdout.flush()
            audio_chunk = synthesize_text(paragraph)
            act_audio_bytes.extend(audio_chunk)
            print(f"OK ({len(audio_chunk):,} bytes)")
            time.sleep(0.4) # Gentle rate-limit pause
            
        # Save individual act MP3
        act_filename = f"{act_id}.mp3"
        act_filepath = os.path.join(OUTPUT_DIR, act_filename)
        with open(act_filepath, "wb") as f:
            f.write(act_audio_bytes)
            
        file_size_kb = len(act_audio_bytes) / 1024
        print(f"  [SAVED] {act_filename} ({file_size_kb:.1f} KB)")
        
        manifest.append({
            "act": idx,
            "id": act_id,
            "title": title,
            "duration": duration,
            "file": act_filename,
            "bytes": len(act_audio_bytes)
        })
        
        full_audio_bytes.extend(act_audio_bytes)
        
    # Save combined master presentation MP3
    full_filename = "00_full_presentation_voiceover.mp3"
    full_filepath = os.path.join(OUTPUT_DIR, full_filename)
    with open(full_filepath, "wb") as f:
        f.write(full_audio_bytes)
        
    total_mb = len(full_audio_bytes) / (1024 * 1024)
    print("\n" + "=" * 65)
    print(f"ALL ACTS SUCCESSFULLY GENERATED!")
    print(f"Master Audio: {full_filename} ({total_mb:.2f} MB)")
    print(f"Directory: {OUTPUT_DIR}")
    print("=" * 65)
    
    # Save JSON manifest for web player
    import json
    with open(os.path.join(OUTPUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

if __name__ == "__main__":
    main()
