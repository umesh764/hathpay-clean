# add_bharat_data.py
from app import app
from modules.models import db, BharatDarshan
import json

def add_bharat_data():
    with app.app_context():
        # Check if data already exists
        if BharatDarshan.query.count() > 0:
            print(f"⚠️ Database already has {BharatDarshan.query.count()} records.")
            choice = input("Add more data anyway? (y/n): ")
            if choice.lower() != 'y':
                print("❌ No data added.")
                return
        
        # Sample data
        bharat_data = [
            # उत्तर प्रदेश - ताज महल
            {
                'name': 'Taj Mahal',
                'name_hindi': 'ताज महल',
                'description': '''ताज महल आगरा में स्थित एक विश्व प्रसिद्ध स्मारक है। इसे मुगल सम्राट शाहजहाँ ने अपनी पत्नी मुमताज महल की याद में 1632-1653 के बीच बनवाया था। यह प्रेम का प्रतीक है और विश्व के सात अजूबों में से एक है। सफेद संगमरमर से बना यह स्मारक यूनेस्को विश्व धरोहर स्थल है।''',
                'category': 'ऐतिहासिक स्थल',
                'subcategory': 'स्मारक',
                'state': 'उत्तर प्रदेश',
                'city': 'आगरा',
                'district': 'आगरा',
                'main_image': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800',
                'gallery': '["https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800"]',
                'latitude': 27.1751,
                'longitude': 78.0421,
                'best_time': 'अक्टूबर से मार्च',
                'entry_fee': 'भारतीय: ₹50, विदेशी: ₹1100',
                'timing': 'सूर्योदय से सूर्यास्त तक (शुक्रवार बंद)',
                'cultural_facts': 'ताज महल का निर्माण 1632 में शुरू हुआ और 1653 में पूरा हुआ। इसे 20,000 मजदूरों ने बनाया था।',
                'famous_food': 'आगरा का पेठा, दाल मोठ',
                'dress_code': 'कोई विशेष ड्रेस कोड नहीं',
                'video_url': 'https://www.youtube.com/results?search_query=taj+mahal+history+hindi'
            },
            # उत्तर प्रदेश - वाराणसी
            {
                'name': 'Varanasi Ghats',
                'name_hindi': 'वाराणसी घाट',
                'description': '''वाराणसी के घाट गंगा नदी के किनारे स्थित हैं। यह हिंदुओं का सबसे पवित्र स्थल है। यहां 80 से अधिक घाट हैं, जिनमें दशाश्वमेध घाट और मणिकर्णिका घाट प्रमुख हैं। हर शाम यहां भव्य गंगा आरती होती है।''',
                'category': 'आध्यात्मिक स्थल',
                'subcategory': 'घाट',
                'state': 'उत्तर प्रदेश',
                'city': 'वाराणसी',
                'district': 'वाराणसी',
                'main_image': 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800',
                'gallery': '["https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800"]',
                'latitude': 25.3176,
                'longitude': 82.9739,
                'best_time': 'अक्टूबर से मार्च',
                'entry_fee': 'नि:शुल्क',
                'timing': 'हर समय',
                'cultural_facts': 'यहां हर शाम गंगा आरती होती है जिसे देखने दूर-दूर से लोग आते हैं।',
                'famous_food': 'कचौड़ी सब्जी, मलाईयो, बनारसी पान',
                'dress_code': 'मंदिरों में प्रवेश के लिए पारंपरिक वस्त्र',
                'video_url': 'https://www.youtube.com/results?search_query=varanasi+ganga+aarti'
            },
            # राजस्थान - हवा महल
            {
                'name': 'Hawa Mahal',
                'name_hindi': 'हवा महल',
                'description': '''हवा महल जयपुर का एक प्रसिद्ध महल है। इसे महाराजा सवाई प्रताप सिंह ने 1799 में बनवाया था। इसकी 953 खिड़कियां हैं, जिनसे हवा आती-जाती रहती है। यह राजपूत वास्तुकला का बेहतरीन उदाहरण है।''',
                'category': 'ऐतिहासिक स्थल',
                'subcategory': 'महल',
                'state': 'राजस्थान',
                'city': 'जयपुर',
                'district': 'जयपुर',
                'main_image': 'https://images.unsplash.com/photo-1599661046827-dacff0c0f09a?w=800',
                'gallery': '["https://images.unsplash.com/photo-1599661046827-dacff0c0f09a?w=800"]',
                'latitude': 26.9239,
                'longitude': 75.8267,
                'best_time': 'अक्टूबर से मार्च',
                'entry_fee': 'भारतीय: ₹50, विदेशी: ₹200',
                'timing': '9:00 AM से 4:30 PM',
                'cultural_facts': 'हवा महल राजमहल की महिलाओं के लिए बनाया गया था ताकि वे बिना दिखे शहर की गतिविधियां देख सकें।',
                'famous_food': 'दाल बाटी चूरमा, गट्टे की सब्जी',
                'dress_code': 'कोई विशेष ड्रेस कोड नहीं',
                'video_url': 'https://www.youtube.com/results?search_query=hawa+mahal+history+hindi'
            },
            # केरल - बैकवाटर
            {
                'name': 'Alleppey Backwaters',
                'name_hindi': 'अलाप्पुझा बैकवाटर',
                'description': '''अलाप्पुझा के बैकवाटर केरल की पहचान हैं। यहां हाउसबोट में रहना एक अद्भुत अनुभव है। इसे 'पूर्व का वेनिस' भी कहा जाता है। नहरों, झीलों और लैगून का यह जाल 900 किमी से अधिक फैला है।''',
                'category': 'प्राकृतिक सौंदर्य',
                'subcategory': 'बैकवाटर',
                'state': 'केरल',
                'city': 'अलाप्पुझा',
                'district': 'अलाप्पुझा',
                'main_image': 'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800',
                'gallery': '["https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800"]',
                'latitude': 9.4981,
                'longitude': 76.3388,
                'best_time': 'सितंबर से मार्च',
                'entry_fee': 'हाउसबोट के हिसाब से अलग',
                'timing': 'हर समय',
                'cultural_facts': 'यहां की नहरें, झीलें और लैगून मिलकर बैकवाटर बनाते हैं।',
                'famous_food': 'केरल का सद्या, समुद्री भोजन, अप्पम',
                'dress_code': 'कोई विशेष ड्रेस कोड नहीं',
                'video_url': 'https://www.youtube.com/results?search_query=alleppey+backwaters+kerala'
            },
            # गुजरात - स्टैच्यू ऑफ यूनिटी
            {
                'name': 'Statue of Unity',
                'name_hindi': 'स्टैच्यू ऑफ यूनिटी',
                'description': '''स्टैच्यू ऑफ यूनिटी दुनिया की सबसे ऊंची प्रतिमा है। यह सरदार वल्लभभाई पटेल की 182 मीटर (597 फीट) ऊंची प्रतिमा है। यह नर्मदा नदी पर बने सरदार सरोवर बांध के पास स्थित है।''',
                'category': 'आधुनिक स्थल',
                'subcategory': 'प्रतिमा',
                'state': 'गुजरात',
                'city': 'केवडिया',
                'district': 'नर्मदा',
                'main_image': 'https://images.unsplash.com/photo-1589652717521-10c0d9aed7c5?w=800',
                'gallery': '["https://images.unsplash.com/photo-1589652717521-10c0d9aed7c5?w=800"]',
                'latitude': 21.8380,
                'longitude': 73.7191,
                'best_time': 'अक्टूबर से फरवरी',
                'entry_fee': '₹350 से ₹1200 तक',
                'timing': '8:00 AM से 6:00 PM',
                'cultural_facts': 'इसे 2018 में बनाया गया था और इसे बनाने में 3 साल लगे थे।',
                'famous_food': 'गुजराती थाली, ढोकला, खाखरा',
                'dress_code': 'कोई विशेष ड्रेस कोड नहीं',
                'video_url': 'https://www.youtube.com/results?search_query=statue+of+unity+documentary'
            },
            # त्योहार - दिवाली
            {
                'name': 'Diwali',
                'name_hindi': 'दिवाली',
                'description': '''दिवाली रोशनी का त्योहार है। यह भारत का सबसे बड़ा त्योहार है जो अक्टूबर-नवंबर में मनाया जाता है। यह बुराई पर अच्छाई की जीत का प्रतीक है। इस दिन लोग दीये जलाते हैं, पटाखे छोड़ते हैं और मिठाइयां बांटते हैं।''',
                'category': 'त्योहार',
                'subcategory': 'राष्ट्रीय त्योहार',
                'state': 'सभी राज्य',
                'city': 'सभी शहर',
                'district': 'सभी जिले',
                'main_image': 'https://images.unsplash.com/photo-1467810168020-65f1b3e13cef?w=800',
                'festival_month': 'अक्टूबर-नवंबर',
                'cultural_facts': 'यह त्योहार भगवान राम के 14 वर्ष के वनवास के बाद अयोध्या लौटने की खुशी में मनाया जाता है।',
                'famous_food': 'मिठाइयां, नमकीन',
                'video_url': 'https://www.youtube.com/results?search_query=diwali+festival+india'
            },
            # त्योहार - होली
            {
                'name': 'Holi',
                'name_hindi': 'होली',
                'description': '''होली रंगों का त्योहार है। यह फरवरी-मार्च में मनाया जाता है। इस दिन लोग एक-दूसरे पर रंग डालते हैं। यह वसंत के आगमन का स्वागत करता है और बुराई पर अच्छाई की जीत का प्रतीक है।''',
                'category': 'त्योहार',
                'subcategory': 'राष्ट्रीय त्योहार',
                'state': 'सभी राज्य',
                'city': 'सभी शहर',
                'district': 'सभी जिले',
                'main_image': 'https://images.unsplash.com/photo-1588351151404-1c3a9d3b5f5f?w=800',
                'festival_month': 'फरवरी-मार्च',
                'cultural_facts': 'उत्तर प्रदेश के बरसाना में लट्ठमार होली प्रसिद्ध है।',
                'famous_food': 'गुजिया, ठंडाई',
                'video_url': 'https://www.youtube.com/results?search_query=holi+festival+india'
            }
        ]
        
        # Data add करें
        added = 0
        skipped = 0
        
        for item_data in bharat_data:
            # Check if already exists
            existing = BharatDarshan.query.filter_by(name=item_data['name']).first()
            if not existing:
                item = BharatDarshan(**item_data)
                db.session.add(item)
                added += 1
                print(f"✅ Added: {item_data['name']} ({item_data['name_hindi']})")
            else:
                skipped += 1
                print(f"⏭️ Already exists: {item_data['name']}")
        
        db.session.commit()
        print("\n" + "="*50)
        print(f"📊 SUMMARY:")
        print(f"✅ Added: {added} new items")
        print(f"⏭️ Skipped: {skipped} existing items")
        print(f"📈 Total records now: {BharatDarshan.query.count()}")
        print("="*50)

if __name__ == '__main__':
    print("🚀 Starting Bharat Darshan Data Addition...")
    add_bharat_data()