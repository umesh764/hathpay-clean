import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# .env फाइल से API key लोड करें
load_dotenv()

# API key को .env से पढ़ें
API_KEY = os.getenv("NEWS_API_KEY")

def get_hindi_news():
    """हिंदी में खबरें लाने के लिए"""
    if not API_KEY:
        print("❌ API_KEY नहीं मिली! कृपया .env फाइल चेक करें।")
        return []
    
    url = f"https://newsapi.org/v2/top-headlines?country=in&language=hi&apiKey={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "ok":
            return data["articles"]
        else:
            print("❌ Error:", data.get("message", "Unknown error"))
            return []
    except Exception as e:
        print("❌ Connection error:", e)
        return []

def show_news(news_list):
    """खबरों को अच्छे से दिखाने के लिए"""
    if not news_list:
        print("⚠️ कोई खबर नहीं मिली")
        return
    
    print("\n" + "="*65)
    print(f"  📰 DAILY HUNT - {datetime.now().strftime('%A, %d %B %Y')}")
    print(f"  ⏰ समय: {datetime.now().strftime('%I:%M %p')}")
    print("="*65)
    
    for i, article in enumerate(news_list[:10], 1):
        title = article.get("title", "कोई शीर्षक नहीं")
        source = article.get("source", {}).get("name", "अज्ञात")
        print(f"\n{i}. {title}")
        print(f"   📍 स्रोत: {source}")
    
    print("\n" + "="*65)
    print(f"  📊 कुल {len(news_list[:10])} खबरें दिखाई गईं")
    print("="*65 + "\n")

if __name__ == "__main__":
    print("\n🔄 खबरें लोड हो रही हैं... कृपया प्रतीक्षा करें\n")
    news = get_hindi_news()
    show_news(news)