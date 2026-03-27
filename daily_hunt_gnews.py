import os
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
import sys

load_dotenv()
API_KEY = os.getenv("GNEWS_API_KEY")

os.system('color 0B')

def animate_ring(frame):
    frames = [
        "◜ ◝", " ◝◜ ", "  ◞◟ ", "◟ ◞", " ◞◟ ", "◜ ◝", " ◝◜ "
    ]
    return frames[frame % len(frames)]

def clear_screen():
    os.system('cls')

def get_hindi_news():
    """GNews se hindi news lane ke liye"""
    if not API_KEY:
        return []
    
    # Hindi news for India
    url = f"https://gnews.io/api/v4/search?q=india&lang=hi&country=in&max=10&apikey={API_KEY}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if "articles" in data:
            return data["articles"]
        else:
            print(f"❌ Error: {data.get('message', 'Unknown')}")
            return []
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return []

def show_notification(news, frame):
    title = news.get("title", "कोई शीर्षक नहीं")
    source = news.get("source", {}).get("name", "अज्ञात")
    ring = animate_ring(frame)
    
    print("\n" + "█"*70)
    print(f"█  {ring}  🔔 नई खबर! 🔔  {ring}  █")
    print("█"*70)
    print(f"█  📰 {title[:60]}")
    print(f"█  📍 {source}")
    print(f"█  ⏰ {datetime.now().strftime('%H:%M:%S')}")
    print("█"*70 + "\n")
    
    # Beep sound
    print('\a', end='', flush=True)

def live_notifications():
    clear_screen()
    
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║     🔔  LIVE DAILY HUNT - हिंदी न्यूज़ नोटिफिकेशन  🔔           ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║     ⚡ रिंग एनीमेशन चल रहा है                                   ║
    ║     ⚡ हर 30 सेकंड में नई खबरें चेक होंगी                       ║
    ║     ⚡ नई खबर आने पर 🔔 बजेगा                                    ║
    ║     ⚡ बंद करने के लिए Ctrl+C दबाएं                             ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    
    seen_titles = set()
    frame = 0
    
    try:
        while True:
            frame += 1
            
            # Ring animation
            ring = animate_ring(frame)
            sys.stdout.write(f"\r⏳ {ring} मॉनिटरिंग चल रही है... नई खबरों के लिए प्रतीक्षा करें {ring} ⏳")
            sys.stdout.flush()
            
            articles = get_hindi_news()
            
            if articles:
                for article in articles[:5]:
                    title = article.get("title", "")
                    if title and title not in seen_titles:
                        seen_titles.add(title)
                        print("\n" + "="*70)
                        show_notification(article, frame)
            
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n\n👋 नोटिफिकेशन बंद किया गया। अलविदा!")
        time.sleep(1)

if __name__ == "__main__":
    if not API_KEY:
        print("❌ API_KEY नहीं मिली!")
        print("कृपया .env फाइल में GNEWS_API_KEY=apni_key डालें")
        print("\n🔑 Free key लेने के लिए: https://gnews.io/register")
    else:
        live_notifications()