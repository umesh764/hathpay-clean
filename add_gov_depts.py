# add_gov_depts.py
from app import app
from modules.models import db, GovernmentDepartment
from datetime import datetime

def add_all_state_data():
    """28 राज्यों और 8 केंद्रशासित प्रदेशों का डेटा"""
    
    all_states_data = [
        # ==== 28 STATES ====
        # उत्तर प्रदेश
        {
            'name': 'उत्तर प्रदेश सरकार',
            'category': 'राज्य सरकार',
            'sub_category': 'मुख्यमंत्री कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'उत्तर प्रदेश सरकार का आधिकारिक पोर्टल',
            'state': 'उत्तर प्रदेश',
            'city': 'लखनऊ',
            'website_url': 'https://up.gov.in',
            'logo_url': '/static/images/gov/up-logo.png',
            'search_tags': 'यूपी, lucknow, योगी आदित्यनाथ',
            'contact_email': 'cm@up.gov.in',
            'contact_phone': '0522-2235000',
            'address': 'मुख्यमंत्री कार्यालय, लखनऊ',
            'established_year': 1950,
            'is_active': True
        },
        {
            'name': 'उत्तर प्रदेश पुलिस',
            'category': 'पुलिस विभाग',
            'sub_category': 'कानून व्यवस्था',
            'parent_ministry': 'गृह विभाग',
            'description': 'उत्तर प्रदेश पुलिस की आधिकारिक वेबसाइट',
            'state': 'उत्तर प्रदेश',
            'city': 'लखनऊ',
            'website_url': 'https://uppolice.gov.in',
            'logo_url': '/static/images/gov/up-police.png',
            'search_tags': 'यूपी पुलिस, 112, डायल 100',
            'established_year': 1863,
            'is_active': True
        },
        
        # महाराष्ट्र
        {
            'name': 'महाराष्ट्र शासन',
            'category': 'राज्य सरकार',
            'sub_category': 'मुख्यमंत्री कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'महाराष्ट्र सरकार का आधिकारिक पोर्टल',
            'state': 'महाराष्ट्र',
            'city': 'मुंबई',
            'website_url': 'https://maharashtra.gov.in',
            'logo_url': '/static/images/gov/maha-logo.png',
            'search_tags': 'महाराष्ट्र, मुंबई, एकनाथ शिंदे',
            'contact_email': 'cm@maharashtra.gov.in',
            'established_year': 1960,
            'is_active': True
        },
        
        # ==== 8 केंद्रशासित प्रदेश ====
        {
            'name': 'दिल्ली सरकार',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'मुख्यमंत्री कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'राष्ट्रीय राजधानी क्षेत्र दिल्ली सरकार',
            'state': 'दिल्ली',
            'city': 'नई दिल्ली',
            'website_url': 'https://delhi.gov.in',
            'logo_url': '/static/images/gov/delhi-logo.png',
            'search_tags': 'दिल्ली, अरविंद केजरीवाल',
            'is_active': True
        },
        {
            'name': 'चंडीगढ़ प्रशासन',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'प्रशासक कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'चंडीगढ़ प्रशासन की आधिकारिक वेबसाइट',
            'state': 'चंडीगढ़',
            'city': 'चंडीगढ़',
            'website_url': 'https://chandigarh.gov.in',
            'logo_url': '/static/images/gov/chd-logo.png',
            'search_tags': 'चंडीगढ़, सेक्टर 17',
            'is_active': True
        },
        {
            'name': 'जम्मू-कश्मीर प्रशासन',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'उपराज्यपाल कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'जम्मू और कश्मीर प्रशासन',
            'state': 'जम्मू-कश्मीर',
            'city': 'श्रीनगर',
            'website_url': 'https://jk.gov.in',
            'is_active': True
        },
        {
            'name': 'लद्दाख प्रशासन',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'उपराज्यपाल कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'लद्दाख केंद्रशासित प्रदेश प्रशासन',
            'state': 'लद्दाख',
            'city': 'लेह',
            'website_url': 'https://ladakh.gov.in',
            'is_active': True
        },
        {
            'name': 'पुदुचेरी सरकार',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'मुख्यमंत्री कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'पुदुचेरी केंद्रशासित प्रदेश सरकार',
            'state': 'पुदुचेरी',
            'city': 'पुदुचेरी',
            'website_url': 'https://py.gov.in',
            'is_active': True
        },
        {
            'name': 'अंडमान-निकोबार प्रशासन',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'उपराज्यपाल कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'अंडमान और निकोबार द्वीपसमूह प्रशासन',
            'state': 'अंडमान-निकोबार',
            'city': 'पोर्ट ब्लेयर',
            'website_url': 'https://andaman.gov.in',
            'is_active': True
        },
        {
            'name': 'लक्षद्वीप प्रशासन',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'प्रशासक कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'लक्षद्वीप द्वीपसमूह प्रशासन',
            'state': 'लक्षद्वीप',
            'city': 'कवरत्ती',
            'website_url': 'https://lakshadweep.gov.in',
            'is_active': True
        },
        {
            'name': 'दादरा-नगर हवेली प्रशासन',
            'category': 'केंद्रशासित प्रदेश',
            'sub_category': 'प्रशासक कार्यालय',
            'parent_ministry': 'गृह मंत्रालय',
            'description': 'दादरा और नगर हवेली प्रशासन',
            'state': 'दादरा-नगर हवेली',
            'city': 'सिल्वासा',
            'website_url': 'https://dnh.gov.in',
            'is_active': True
        }
    ]
    
    with app.app_context():
        added = 0
        skipped = 0
        
        for dept_data in all_states_data:
            # Check if already exists
            existing = GovernmentDepartment.query.filter_by(name=dept_data['name']).first()
            if not existing:
                dept = GovernmentDepartment(**dept_data)
                db.session.add(dept)
                added += 1
                print(f"✅ Added: {dept_data['name']}")
            else:
                skipped += 1
                print(f"⏭️ Exists: {dept_data['name']}")
        
        db.session.commit()
        print(f"\n📊 Total: {added} added, {skipped} skipped")
        print(f"📈 Total records: {GovernmentDepartment.query.count()}")

if __name__ == '__main__':
    print("🚀 Adding Government Departments Data...")
    add_all_state_data()