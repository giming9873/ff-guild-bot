import os
import time
import random

# --- 4v4 क्लैश स्क्वाड बटन्स (Coordinates) ---
START_X, START_Y = 1600, 900
BACK_X, BACK_Y = 960, 850
FIRE_X, FIRE_Y = 1800, 600
BUY_GUN_X, BUY_GUN_Y = 500, 400

def log_status(msg):
    print(f"[{time.strftime('%H:%M:%S')}] 🤖 AI: {msg}")

def cs_match_gameplay():
    log_status("मैच के अंदर 4 स्क्वाड ऑटो-प्ले चालू है...")
    # क्लैश स्क्वाड मैच 6 मिनट (360端) चलेगा
    match_end_time = time.time() + 360
    
    while time.time() < match_end_time:
        off_x = random.randint(-20, 20)
        off_y = random.randint(-20, 20)
        
        # गन शॉप और फायरिंग पर ऑटो-टैप
        os.system(f"adb shell input tap {BUY_GUN_X + off_x} {BUY_GUN_Y + off_y}")
        time.sleep(0.5)
        os.system(f"adb shell input tap {FIRE_X + off_x} {FIRE_Y + off_y}")
        
        # इंसानी धोखा गैप
        time.sleep(random.uniform(0.3, 0.7))

def start_cloud_booster():
    log_status("क्लाउड बूस्टर पूरी तरह ऑटोमैटिक मोड में चालू हो गया है।")
    match_count = 0

    # गिटहब सर्वर पर बिना रुके लगातार 15 मैच खेलने का लूप
    while match_count < 15:
        match_count += 1
        log_status(f"मैच नंबर {match_count} लॉबी से ऑटो-स्टार्ट हो रहा है...")
        
        # स्टार्ट बटन क्लिक
        os.system(f"adb shell input tap {START_X} {START_Y}")
        time.sleep(20) # लोडिंग टाइम
        
        # मैच खेलना शुरू
        cs_match_gameplay()
        
        # मैच खत्म होने पर लॉबी वापसी
        log_status("मैच पूरा हुआ। लॉबी में वापस जा रहे हैं...")
        for _ in range(5):
            os.system(f"adb shell input tap {BACK_X} {BACK_Y}")
            time.sleep(2)
            
        log_status(f"मैच {match_count} के गिल्ड पॉइंट्स जुड़ चुके हैं।")
        
        # मैचों के बीच 1 से 2 मिनट का इंसानी रैंडम आराम
        small_gap = random.randint(60, 120)
        log_status(f"एंटी-चीट सुरक्षा: अगले मैच से पहले {small_gap} सेकंड का ब्रेक...")
        time.sleep(small_gap)

if __name__ == "__main__":
    start_cloud_booster()
    
