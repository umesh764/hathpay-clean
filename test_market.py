# test_market.py
import requests
import json

print("="*50)
print("🔍 HAT PAY - Live Market API Test")
print("="*50)

# Test 1: NIFTY API
print("\n1️⃣ Testing NIFTY API...")
try:
    url = "http://127.0.0.1:5000/market-live/api/nifty"
    response = requests.get(url, timeout=5)
    data = response.json()
    print(f"   ✅ Status: {response.status_code}")
    print(f"   📊 NIFTY: ₹{data.get('price', 'N/A')}")
    print(f"   📈 Change: {data.get('change', 'N/A')}")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 2: SENSEX API
print("\n2️⃣ Testing SENSEX API...")
try:
    url = "http://127.0.0.1:5000/market-live/api/sensex"
    response = requests.get(url, timeout=5)
    data = response.json()
    print(f"   ✅ Status: {response.status_code}")
    print(f"   📊 SENSEX: ₹{data.get('price', 'N/A')}")
    print(f"   📈 Change: {data.get('change', 'N/A')}")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 3: Top Gainers
print("\n3️⃣ Testing Top Gainers API...")
try:
    url = "http://127.0.0.1:5000/market-live/api/top-gainers"
    response = requests.get(url, timeout=5)
    data = response.json()
    print(f"   ✅ Status: {response.status_code}")
    print(f"   📈 Top Gainers:")
    for item in data[:3]:
        print(f"      - {item.get('symbol')}: ₹{item.get('price')} {item.get('change')}")
except Exception as e:
    print(f"   ❌ Error: {e}")

# Test 4: Top Losers
print("\n4️⃣ Testing Top Losers API...")
try:
    url = "http://127.0.0.1:5000/market-live/api/top-losers"
    response = requests.get(url, timeout=5)
    data = response.json()
    print(f"   ✅ Status: {response.status_code}")
    print(f"   📉 Top Losers:")
    for item in data[:3]:
        print(f"      - {item.get('symbol')}: ₹{item.get('price')} {item.get('change')}")
except Exception as e:
    print(f"   ❌ Error: {e}")

print("\n" + "="*50)
print("✅ Test Complete!")
print("="*50)