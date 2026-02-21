import json
import os
import time
from deep_translator import GoogleTranslator

# Keys to translate for Terms and Conditions
keys_to_translate = [
    "termsPageTitle", "termsTitle", "termsLastUpdated",
    "termsSection1Title", "termsSection1Para1",
    "termsSection2Title", "termsSection2Para1",
    "termsSection3Title", "termsSection3Para1", "termsSection3Para2",
    "termsSection4Title", "termsSection4Para1", "termsSection4Li1", "termsSection4Li2",
    "termsSection5Title", "termsSection5Para1", "termsSection5Li1", "termsSection5Li2",
    "termsSection6Title", "termsSection6Para1",
    "termsSection7Title", "termsSection7Para1",
    "termsSection8Title", "termsSection8Para1",
    "termsSection9Title", "termsSection9Para1",
    "termsSection10Title", "termsSection10Para1",
    "termsSection11Title", "termsSection11Para1"
]

# Supported languages mapping for google translate
lang_mapping = {
    "es": "es",
    "sv": "sv",
    "ar": "ar",
    "ko": "ko",
    "th": "th",
    "hi": "hi",
    "fr": "fr",
    "it": "it",
    "pt": "pt",
    "zh": "zh-CN",
    "nl": "nl",
    "ru": "ru",
    "de": "de",
    "ja": "ja"
}

def translate_files():
    translations_dir = "translations"
    en_file = os.path.join(translations_dir, "en.json")
    
    with open(en_file, "r", encoding="utf-8") as f:
        en_data = json.load(f)
        
    for lang_file, target_lang in lang_mapping.items():
        file_path = os.path.join(translations_dir, f"{lang_file}.json")
        if not os.path.exists(file_path):
            print(f"Skipping {lang_file}.json as it does not exist.")
            continue
            
        print(f"Translating to {lang_file} ({target_lang})...")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lang_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON in {file_path}: {e}")
            continue
            
        translator = GoogleTranslator(source='en', target=target_lang)
        
        updated = False
        for key in keys_to_translate:
            if key in en_data:
                text_to_translate = en_data[key]
                try:
                    translated = translator.translate(text_to_translate)
                    # Simple fix if translator messes up HTML slightly
                    translated = translated.replace("< br >", "<br>").replace("</ strong>", "</strong>").replace("< strong>", "<strong>")
                    lang_data[key] = translated
                    updated = True
                    time.sleep(0.3) # Avoid heavy rate limiting
                except Exception as e:
                    print(f"Failed to translate key {key} to {target_lang}: {e}")
                    
        if updated:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(lang_data, f, ensure_ascii=False, indent=2)
                f.write("\n")
            print(f"Successfully updated {lang_file}.json\n")
            
if __name__ == "__main__":
    print("Starting translation process...")
    translate_files()
    print("All translations completed.")
