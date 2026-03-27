import os 
from dotenv import load_dotenv 
load_dotenv() 
 
print("=== ENV CHECK ===") 
gemini = os.getenv("GEMINI_API_KEY") 
openai = os.getenv("OPENAI_API_KEY") 
alpha = os.getenv("ALPHA_VANTAGE_KEY") 
 
if gemini: 
    print("OK: GEMINI found") 
else: 
    print("MISSING: GEMINI_API_KEY") 
 
if openai: 
    print("OK: OPENAI found") 
else: 
    print("MISSING: OPENAI_API_KEY") 
 
if alpha: 
    print("OK: ALPHA_VANTAGE found") 
else: 
    print("MISSING: ALPHA_VANTAGE_KEY") 
