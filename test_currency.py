# test_currency.py
import os
from dotenv import load_dotenv

# .env file load karo
load_dotenv()

# API key lo
api_key = os.getenv('CURRENCY_API_KEY')

print("="*50)
print("🔍 CURRENCY API KEY TEST")
print("="*50)

# 1. Check karo key mili ya nahi
if api_key:
    print(f"✅ API Key mil gayi!")
    print(f"   Key value: {api_key}")
    print(f"   Key length: {len(api_key)} characters")
    print(f"   First 10 chars: {api_key[:10]}...")
else:
    print("❌ API Key nahi mili!")
    print("   .env file check karo")

print("-"*50)

# 2. Ab actual API test karte hain
try:
    from currencyapinet import CurrencyApi
    
    print("🔄 API connection test ho raha hai...")
    
    # API connect karo
    currency_api = CurrencyApi(api_key)
    
    # Latest rates lo
    result = currency_api.latest()
    
    # Check karo response mein data hai ya nahi
    if result and 'data' in result:
        print("✅ API connection successful!")
        
        # USD to INR rate dekho
        if 'INR' in result['data']:
            inr_rate = result['data']['INR']['value']
            print(f"   🇺🇸 USD to 🇮🇳 INR: {inr_rate}")
        
        # Kuch aur major currencies bhi dekho
        for currency in ['EUR', 'GBP', 'JPY']:
            if currency in result['data']:
                rate = result['data'][currency]['value']
                print(f"   🇺🇸 USD to {currency}: {rate}")
    else:
        print("❌ API response mein data nahi hai")
        print(f"   Response: {result}")
        
except ImportError:
    print("❌ currencyapi package install nahi hai!")
    print("   Install karo: pip install currencyapi")
except Exception as e:
    print(f"❌ Error aaya: {e}")

print("="*50)