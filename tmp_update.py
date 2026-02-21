import json
import os
import glob
from collections import OrderedDict

new_terms = {
  "termsPageTitle": "Terms and Conditions - TravelHawk",
  "termsTitle": "Terms and Conditions",
  "termsLastUpdated": "Last Updated: February 21, 2026",
  "termsSection1Title": "1. Acceptance of Terms",
  "termsSection1Para1": "By downloading, installing, or using the TravelHawk mobile application (“the App”), or any of its white-labeled counterparts or B2B enterprise services, you agree to be bound by these Terms and Conditions (“Terms”). If you do not agree to these Terms, do not use the App. We may amend these Terms at any time by posting the amended terms in the App or on our website. Your continued use of the App after such posting will constitute your acceptance of the amended terms.",
  "termsSection2Title": "2. Description of Service",
  "termsSection2Para1": "TravelHawk provides users with real-time, location-based crime statistics, danger hotspots (such as Car Stoning zones), and safety alerts. The information provided is aggregated from various public and private sources and is intended for informational and educational purposes only. While we strive for accuracy, we do not guarantee the completeness, timeliness, or reliability of any information provided through the App.",
  "termsSection3Title": "3. Explicit Disclaimer of Liability for Personal Safety",
  "termsSection3Para1": "<strong>CAUTION</strong><br><strong>CRITICAL SAFETY NOTICE:</strong> TravelHawk is a supplementary informational tool, not a physical security service or a guarantee of safety. You acknowledge and agree that Skeep Technologies (Pty) Ltd, its affiliates, partners, and B2B clients cannot and do not guarantee your personal safety. Following the App’s recommendations, routing advice, or safety alerts (including but not limited to, staying in \"Green Zones\") does <strong>not</strong> immunize you from the risk of crime.",
  "termsSection3Para2": "You remain solely responsible for your own safety and situational awareness at all times. Skeep Technologies (Pty) Ltd shall under no circumstances be held liable for any personal injury, death, mugging, theft, property damage, or any other loss or crime experienced by you or your companions, regardless of whether you were following the App’s guidance, using its safe routing features, or located in an area deemed \"safe\" by the App. Crime is inherently unpredictable, and the App's data may not reflect real-time, sudden, or unreported incidents.",
  "termsSection4Title": "4. B2B, White-Label, and Corporate Accounts",
  "termsSection4Para1": "Skeep Technologies (Pty) Ltd offers corporate packages, white-labeled versions of the App, and enterprise tiers.",
  "termsSection4Li1": "<strong>Corporate Users:</strong> If you are accessing the App via a corporate activation code, your use is still bound by these Terms. Your employer or the issuing organization does not assume liability for your safety through the provision of this App.",
  "termsSection4Li2": "<strong>B2B Clients:</strong> B2B partners utilizing our white-label solutions, App Store revenue share models, or webhook integrations are subject to separate Master Service Agreements (MSAs). However, all end-users of white-labeled apps remain bound by the safety disclaimers and usage terms outlined herein.",
  "termsSection5Title": "5. Subscriptions and In-App Purchases",
  "termsSection5Para1": "Certain features of the App may be subject to a subscription or In-App Purchase (IAP). Payments are processed securely via the Apple App Store or Google Play Store.",
  "termsSection5Li1": "You agree to abide by the respective app store's terms regarding subscriptions, renewals, and refunds.",
  "termsSection5Li2": "Skeep Technologies (Pty) Ltd does not directly process or store your credit card information.",
  "termsSection6Title": "6. User Conduct",
  "termsSection6Para1": "You agree to use the App only for lawful purposes. You are solely responsible for your use of the App and any consequences thereof. You must not use the App to harass, abuse, stalk, threaten, or otherwise violate the legal rights of others. Unauthorized scraping, data mining, or reverse engineering of the App's crime data and algorithms is strictly prohibited.",
  "termsSection7Title": "7. Disclaimer of Warranties",
  "termsSection7Para1": "The App is provided on an “as is” and “as available” basis. We expressly disclaim all warranties of any kind, whether express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. We make no warranty that the App will meet your requirements, be uninterrupted, timely, secure, or error-free.",
  "termsSection8Title": "8. Limitation of Liability",
  "termsSection8Para1": "You expressly understand and agree that Skeep Technologies (Pty) Ltd shall not be liable for any direct, indirect, incidental, special, consequential, or exemplary damages, including but not limited to, damages for loss of profits, goodwill, use, data, or other intangible losses resulting from the use or the inability to use the App, even if we have been advised of the possibility of such damages.",
  "termsSection9Title": "9. Intellectual Property",
  "termsSection9Para1": "All rights, title, and interest in and to the App (excluding user-provided content) are and will remain the exclusive property of Skeep Technologies (Pty) Ltd and its licensors. The App is protected by copyright, trademark, and other laws of both South Africa and foreign countries.",
  "termsSection10Title": "10. Governing Law and Jurisdiction",
  "termsSection10Para1": "These Terms shall be governed by and construed in accordance with the laws of the Republic of South Africa, without regard to its conflict of law provisions. You agree to submit to the exclusive jurisdiction of the courts located in Johannesburg, South Africa, to resolve any legal matter arising from these Terms.",
  "termsSection11Title": "11. Contact Information",
  "termsSection11Para1": "If you have any questions about these Terms and Conditions, please contact us at: <a href=\"mailto:support@travelhawk.co.za\">support@travelhawk.co.za</a>."
}

translations_dir = "/Users/tlotlisomofokeng/Documents/GitHub/travelhawkdev.github.io/translations/"
files = glob.glob(os.path.join(translations_dir, "*.json"))

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f, object_pairs_hook=OrderedDict)
    
    new_data = OrderedDict()
    
    # Copy all keys up to where terms start, then insert the new terms, then copy the rest
    terms_inserted = False
    
    for k, v in data.items():
        if k.startswith("terms"):
            if not terms_inserted:
                # Insert the new terms here
                for nk, nv in new_terms.items():
                    # For non-English files, we use the english text.
                    new_data[nk] = nv
                terms_inserted = True
            # Skip old terms* keys
        else:
            new_data[k] = v
            
    # In case there were no terms* keys in a file, insert at bottom
    if not terms_inserted:
        for nk, nv in new_terms.items():
            new_data[nk] = nv
            
    with open(file_path, "w", encoding="utf-8") as f:
        # Use dump with indent 2 to maintain formatting
        json.dump(new_data, f, ensure_ascii=False, indent=2)
        f.write('\n')
        
    print(f"Updated {file_path}")

print("Done updating translations.")
