# add_gov_data.py
from app import app
from modules.models import db, StateDashboard
import json
from datetime import datetime

def add_maharashtra_data():
    """महाराष्ट्र के लिए गवर्नमेंट डैशबोर्ड डेटा जोड़ें"""
    with app.app_context():
        # Check if data already exists
        existing = StateDashboard.query.filter_by(state_name='महाराष्ट्र').first()
        if existing:
            print("⚠️ महाराष्ट्र का डेटा पहले से मौजूद है!")
            choice = input("डेटा अपडेट करें? (y/n): ")
            if choice.lower() != 'y':
                return
        
        # महाराष्ट्र का कंप्लीट डेटा
        maharashtra_data = {
            'state_name': 'महाराष्ट्र',
            
            # 🥇 मुख्यमंत्री और मंत्रीमंडल
            'cm_name': 'देवेंद्र फडणवीस',
            'cm_photo': 'https://example.com/cm_photo.jpg',  # Actual URL डालें
            'ministers': json.dumps([
                {"name": "देवेंद्र फडणवीस", "dept": "मुख्यमंत्री", "constituency": "नागपुर दक्षिण पश्चिम"},
                {"name": "एकनाथ शिंदे", "dept": "उपमुख्यमंत्री", "constituency": "कोपरी-पाचपाखाड़ी"},
                {"name": "अजित पवार", "dept": "उपमुख्यमंत्री", "constituency": "बारामती"},
                {"name": "चंद्रशेखर बावनकुले", "dept": "गृह मंत्री", "constituency": ""},
                {"name": "राधाकृष्ण विखे पाटील", "dept": "महसूल मंत्री", "constituency": ""},
                {"name": "गिरीश महाजन", "dept": "कृषि मंत्री", "constituency": ""},
                {"name": "प्रकाश सोलंके", "dept": "उद्योग मंत्री", "constituency": ""},
                {"name": "हसन मुश्रीफ", "dept": "वित्त मंत्री", "constituency": ""},
                {"name": "दीपक केसरकर", "dept": "शिक्षण मंत्री", "constituency": ""},
                {"name": "गुलाबराव पाटील", "dept": "ग्रामीण विकास मंत्री", "constituency": ""}
            ], ensure_ascii=False),
            
            # 🌾 कृषि डेटा - पिछले 5 साल
            'agri_data': json.dumps({
                "milk_production": {
                    "2021-22": "143.04 लाख टन",
                    "2020-21": "137.03 लाख टन",
                    "2019-20": "120.24 लाख टन",
                    "2018-19": "116.55 लाख टन",
                    "2017-18": "111.02 लाख टन"
                },
                "horticulture_production": {
                    "2024-25": "154.39 लाख टन",
                    "2023-24": "148.20 लाख टन",
                    "2022-23": "142.10 लाख टन"
                },
                "major_crops": {
                    "सोयाबीन": "48.23 लाख हेक्टर",
                    "कपास": "41.06 लाख हेक्टर",
                    "ज्वारी": "32.12 लाख हेक्टर",
                    "बाजरी": "12.34 लाख हेक्टर",
                    "तूर": "11.89 लाख हेक्टर"
                },
                "irrigated_area": "34.5% (2022)"
            }, ensure_ascii=False),
            
            # 👗 संस्कृति और वेशभूषा
            'culture_data': json.dumps({
                "traditional_dress": {
                    "पुरुष": "धोती, फेटा, सदरा",
                    "महिला": "नौवारी साड़ी, चोली",
                    "आभूषण": "तोडे, बाली, नथ, मंगळसूत्र"
                },
                "famous_food": [
                    "वड़ा पाव", "पूरण पोली", "मिसळ पाव", "पाव भाजी",
                    "साबुदाणा खिचडी", "मोदक", "आमरस", "श्रीखंड",
                    "कोल्हापुरी मटन", "थालीपीठ"
                ],
                "festivals": [
                    {"name": "गणेशोत्सव", "month": "भाद्रपद", "significance": "10 दिवसीय उत्सव"},
                    {"name": "गुड़ी पड़वा", "month": "चैत्र", "significance": "मराठी नववर्ष"},
                    {"name": "शिवजयंती", "month": "फाल्गुन", "significance": "छत्रपती शिवाजी महाराज जयंती"},
                    {"name": "दसरा", "month": "आश्विन", "significance": "रावण दहन"},
                    {"name": "दिवाळी", "month": "कार्तिक", "significance": "प्रकाशाचा सण"}
                ],
                "dance_forms": ["लावणी", "तमाशा", "पोवाडा", "कोली नृत्य"],
                "music": ["नाट्यसंगीत", "भावगीत", "भजन", "कीर्तन"]
            }, ensure_ascii=False),
            
            # 🏛️ प्राचीन स्थळे
            'ancient_sites': json.dumps([
                {
                    "name": "अजिंठा लेणी",
                    "location": "औरंगाबाद",
                    "period": "इ.स.पू. 2रे शतक",
                    "significance": "बौद्ध लेणी, UNESCO World Heritage"
                },
                {
                    "name": "एलोरा लेणी",
                    "location": "औरंगाबाद",
                    "period": "इ.स. 6-8वे शतक",
                    "significance": "हिंदू, बौद्ध, जैन लेणी"
                },
                {
                    "name": "रायगड किल्ला",
                    "location": "रायगड",
                    "period": "1656",
                    "significance": "छत्रपती शिवाजी महाराजांची राजधानी"
                },
                {
                    "name": "सिंहगड किल्ला",
                    "location": "पुणे",
                    "period": "1647",
                    "significance": "तानाजी मालुसरे यांचा बलिदान"
                },
                {
                    "name": "प्रतापगड किल्ला",
                    "location": "सातारा",
                    "period": "1656",
                    "significance": "अफझलखान वध"
                },
                {
                    "name": "पंढरपूर विठ्ठल मंदिर",
                    "location": "पंढरपूर",
                    "period": "13वे शतक",
                    "significance": "वारकरी संप्रदायाचे केंद्र"
                }
            ], ensure_ascii=False),
            
            # 🛍️ प्रसिद्ध बाजार
            'famous_markets': json.dumps([
                {
                    "name": "क्रॉफर्ड मार्केट",
                    "city": "मुंबई",
                    "established": "1869",
                    "specialty": "फळे, भाजीपाला, मसाले",
                    "best_time": "सकाळी 7-11"
                },
                {
                    "name": "चोर बाजार",
                    "city": "मुंबई",
                    "specialty": "प्राचीन वस्तू, फर्निचर",
                    "best_day": "रविवार सकाळी"
                },
                {
                    "name": "तुळशीबाग",
                    "city": "पुणे",
                    "specialty": "साड्या, दागिने, पूजा साहित्य"
                },
                {
                    "name": "महात्मा फुले मंडई",
                    "city": "पुणे",
                    "specialty": "भाजीपाला, फळे"
                },
                {
                    "name": "रविवार पेठ",
                    "city": "नाशिक",
                    "specialty": "कापड, भाजीपाला"
                },
                {
                    "name": "बडा बाजार",
                    "city": "कोल्हापूर",
                    "specialty": "कोल्हापुरी चप्पल, साड्या"
                }
            ], ensure_ascii=False),
            
            # 📊 सांख्यिकी डेटा
            'statistics': json.dumps({
                "population": "12.42 करोड (2024)",
                "area": "3,07,713 वर्ग किमी",
                "districts": 36,
                "literacy_rate": "82.9%",
                "sex_ratio": "929 महिला/1000 पुरुष",
                "gdp": {
                    "2024-25": "42.5 लाख करोड",
                    "2023-24": "38.2 लाख करोड",
                    "2022-23": "34.8 लाख करोड",
                    "2021-22": "31.2 लाख करोड"
                },
                "per_capita_income": "₹2,42,247 (2024)",
                "major_industries": ["आयटी", "औषध निर्माण", "ऑटोमोबाईल", "कापड", "साखर"]
            }, ensure_ascii=False),
            
            # 🌍 भौगोलिक माहिती
            'geography': json.dumps({
                "climate": "उष्णकटिबंधीय मान्सून",
                "temperature": "12°C ते 42°C",
                "rainfall": "1500 मिमी - 3000 मिमी",
                "soil_types": ["काळी माती", "भाताची माती", "लाल माती", "जांभी माती"],
                "rivers": ["गोदावरी", "कृष्णा", "भीमा", "तापी", "वर्धा", "वैनगंगा"],
                "mountains": ["सह्याद्री", "हरिश्चंद्रगड", "महाबळेश्वर"],
                "national_parks": ["ताडोबा", "गुगामल", "नवेगाव", "संजय गांधी"]
            }, ensure_ascii=False),
            
            # 👥 प्रसिद्ध व्यक्ती
            'famous_personalities': json.dumps([
                {"name": "छत्रपती शिवाजी महाराज", "field": "योद्धा/राज्यकर्ता"},
                {"name": "डॉ. बाबासाहेब आंबेडकर", "field": "सामाजिक सुधारक"},
                {"name": "लोकमान्य टिळक", "field": "स्वातंत्र्यसेनानी"},
                {"name": "गोपाळ कृष्ण गोखले", "field": "समाजसुधारक"},
                {"name": "पंडिता रमाबाई", "field": "समाजसेविका"},
                {"name": "अण्णाभाऊ साठे", "field": "लेखक"},
                {"name": "लता मंगेशकर", "field": "गायिका"},
                {"name": "सचिन तेंडुलकर", "field": "क्रिकेटपटू"}
            ], ensure_ascii=False),
            
            # 🚂 परिवहन
            'transport': json.dumps({
                "airports": [
                    {"name": "छत्रपती शिवाजी महाराज आंतरराष्ट्रीय विमानतळ", "city": "मुंबई"},
                    {"name": "पुणे आंतरराष्ट्रीय विमानतळ", "city": "पुणे"},
                    {"name": "नागपूर आंतरराष्ट्रीय विमानतळ", "city": "नागपूर"}
                ],
                "railway_zones": ["मध्य रेल्वे", "पश्चिम रेल्वे", "कोकण रेल्वे"],
                "major_highways": ["NH-3", "NH-4", "NH-6", "NH-7", "NH-8"],
                "port": ["जवाहरलाल नेहरू पोर्ट", "मुंबई पोर्ट"]
            }, ensure_ascii=False),
            
            'is_active': True,
            'created_at': datetime.utcnow()
        }
        
        # डेटा सेव्ह करा
        if existing:
            # Update existing
            for key, value in maharashtra_data.items():
                setattr(existing, key, value)
            db.session.commit()
            print("✅ महाराष्ट्र डेटा अपडेट केला!")
        else:
            # Add new
            new_data = StateDashboard(**maharashtra_data)
            db.session.add(new_data)
            db.session.commit()
            print("✅ महाराष्ट्र डेटा यशस्वीरित्या जोडला!")
        
        # वेरिफाय
        verify = StateDashboard.query.filter_by(state_name='महाराष्ट्र').first()
        if verify:
            print(f"\n📊 महाराष्ट्र डॅशबोर्ड:")
            print(f"   मुख्यमंत्री: {verify.cm_name}")
            print(f"   मंत्रीमंडळ: {len(json.loads(verify.ministers))} मंत्री")
            print(f"   दूध उत्पादन: {json.loads(verify.agri_data)['milk_production']['2021-22']}")
            print(f"   प्राचीन स्थळे: {len(json.loads(verify.ancient_sites))}")
            print(f"   बाजारपेठा: {len(json.loads(verify.famous_markets))}")

def add_all_states():
    """सर्व राज्यांसाठी डेटा जोडा"""
    with app.app_context():
        # महाराष्ट्र जोडा
        add_maharashtra_data()
        
        # यहाँ इतर राज्ये जोडा
        # add_karnataka_data()
        # add_gujarat_data()
        # add_up_data()
        # etc.

if __name__ == '__main__':
    print("="*50)
    print("🏛️ गवर्नमेंट डैशबोर्ड डेटा जोडा जात आहे...")
    print("="*50)
    
    with app.app_context():
        # पहिले टेबल तयार आहे का ते चेक करा
        db.create_all()
        
    add_all_states()
    print("\n🎯 सर्व डेटा यशस्वीरित्या जोडला गेला!") 