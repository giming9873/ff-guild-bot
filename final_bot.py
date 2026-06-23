import os
import time
import random
import sys

# --- 4v4 क्लैश स्क्वाड बटन्स (Coordinates) ---
START_X, START_Y = 1600, 900
BACK_X, BACK_Y = 960, 850
FIRE_X, FIRE_Y = 1800, 600
BUY_GUN_X, BUY_GUN_Y = 500, 400 # CS मोड में गन खरीदने की जगह

def log_status(msg):
    print(f"[{time.strftime('%H:%M:%S')}] 🤖 AI: {msg}")

def cs_match_gameplay():
    log_status("मैच के अंदर 4 स्क्वाड ऑटो-प्ले शुरू...")
    # क्लैश स्क्वाड मैच लगभग 5-7 मिनट चलता है (360 सेकंड)
    match_end_time = time.time() + 360
    
    while time.time() < match_end_time:
        # एंटी-चीट को चकमा देने के लिए रैंडम इंसानी टच बदलाव
        off_x = random.randint(-20, 20)
        off_y = random.randint(-20, 20)
        
        # 1. गन शॉप पर रैंडम क्लिक (हर राउंड की शुरुआत में)
        os.system(f"adb shell input tap {BUY_GUN_X + off_x} {BUY_GUN_Y + off_y}")
        time.sleep(1)
        
        # 2. फायरिंग और मूवमेंट (JoyStick + Fire)
        os.system(f"adb shell input tap {FIRE_X + off_x} {FIRE_Y + off_y}")
        
        # इंसानी धोखा: फायरिंग के बीच रैंडम गैप (0.2 से 0.6 सेकंड)
        time.sleep(random.uniform(0.2, 0.6))

def start_cloud_booster():
    log_status("मास्टर सिस्टम एक्टिवेटेड। पूरी तरह आपके कंट्रोल में है।")
    match_count = 0

    while True:
        print("\n" + "="*40)
        user_input = input("👉 क्या 4 स्क्वाड मैच शुरू करना है? (Y = हाँ, N = गेम बंद करें): ")
        print("="*40)

        if user_input.lower() != 'y':
            log_status("आपके आदेश पर गेम को बंद किया जा रहा है...")
            os.system("adb shell am force-stop com.dts.freefireth")
            log_status("सिस्टम स्टॉप। दोबारा चालू करने के लिए 'Y' दबाएं।")
            continue

        match_count += 1
        log_status(f"मैच नंबर {match_count} लॉबी से स्टार्ट किया जा रहा है...")
        
        # स्टार्ट बटन क्लिक
        os.system(f"adb shell input tap {START_X} {START_Y}")
        time.sleep(20) # लोडिंग स्क्रीन टाइम
        
        # मैच खेलना शुरू
        cs_match_gameplay()
        
        # मैच खत्म होने पर लॉबी वापसी का लूप
        log_status("मैच खत्म। वापस गिल्ड लॉबी में आ रहे हैं...")
        for _ in range(5):
            os.system(f"adb shell input tap {BACK_X} {BACK_Y}")
            time.sleep(2)
            
        log_status(f"मैच {match_count} पूरा हुआ। गिल्ड पॉइंट्स बढ़ गए हैं।")

        # मैन्युअल ब्रेक का कंट्रोल पॉइंट
        break_check = input("👉 क्या इस मैच के बाद ब्रेक लेना है? (Y = हाँ, N = नहीं): ")
        if break_check.lower() == 'y':
            try:
                hours = int(input("👉 कितने घंटे का इंसानी ब्रेक लगाना है?: "))
            except ValueError:
                print("❌ गलत नंबर! ब्रेक नहीं लगा।")
                continue
                
            log_status(f"सुरक्षा के लिए गेम बंद। एआई {hours} घंटे के लिए सो रहा है...")
            os.system("adb shell am force-stop com.dts.freefireth")
            time.sleep(hours * 3600)
            log_status("ब्रेक खत्म! एआई आपके अगले आदेश के लिए ऑनलाइन आ गया है।")

if __name__ == "__main__":
    start_cloud_booster()
      
