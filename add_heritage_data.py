from app import create_app
from modules.models import db, HeritageSite
import json

app = create_app()
with app.app_context():
    # पहले सारे पुराने डेटा हटाओ
    print("🧹 Clearing old data...")
    HeritageSite.query.delete()
    db.session.commit()
    
    # ============================================
    # ताजमहल - सबसे ज्यादा images
    # ============================================
    taj_images = {
        'main': 'https://images.unsplash.com/photo-1564507592333-c60657eea523?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
        'architecture': 'https://images.unsplash.com/photo-1600623472131-2c9c2c8b6b2a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80',
        'night': 'https://images.pexels.com/photos/1603650/pexels-photo-1603650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'sketch': 'https://images.pexels.com/photos/5320015/pexels-photo-5320015.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/1603650/pexels-photo-1603650.jpeg',
            'https://images.pexels.com/photos/1603649/pexels-photo-1603649.jpeg',
            'https://images.pexels.com/photos/1308940/pexels-photo-1308940.jpeg',
            'https://images.pexels.com/photos/3889786/pexels-photo-3889786.jpeg'
        ]
    }
    
    taj = HeritageSite(
        name='ताजमहल',
        name_hindi='ताजमहल',
        category='स्मारक',
        country='भारत',
        state='उत्तर प्रदेश',
        location='आगरा',
        continent='एशिया',
        description='प्रेम का प्रतीक, मुगल वास्तुकला का उत्कृष्ट नमूना। विश्व के सात अजूबों में से एक।',
        history='मुगल बादशाह शाहजहाँ ने अपनी बेगम मुमताज महल की याद में 1632 में इसका निर्माण शुरू करवाया।',
        architecture='मुगल वास्तुकला का बेहतरीन उदाहरण। सफेद संगमरमर से निर्मित, चार मीनारें, फारसी इस्लामिक शैली।',
        built_by='शाहजहाँ',
        built_year='1632-1653',
        visiting_hours='सूर्योदय से सूर्यास्त तक',
        entry_fee='₹50 (भारतीय), ₹1100 (विदेशी)',
        best_time='अक्टूबर से मार्च',
        is_unesco=True,
        unesco_year=1983,
        is_india=True,
        main_image=taj_images['main'],
        architecture_image=taj_images['architecture'],
        night_image=taj_images['night'],
        sketch_image=taj_images['sketch'],
        gallery_images=json.dumps(taj_images['gallery'])
    )
    
    # ============================================
    # कुतुब मीनार
    # ============================================
    qutub_images = {
        'main': 'https://images.pexels.com/photos/7334757/pexels-photo-7334757.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'architecture': 'https://images.pexels.com/photos/5729879/pexels-photo-5729879.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'night': 'https://images.pexels.com/photos/3879169/pexels-photo-3879169.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/5729882/pexels-photo-5729882.jpeg',
            'https://images.pexels.com/photos/3879168/pexels-photo-3879168.jpeg',
            'https://images.pexels.com/photos/5729883/pexels-photo-5729883.jpeg'
        ]
    }
    
    qutub = HeritageSite(
        name='कुतुब मीनार',
        name_hindi='कुतुब मीनार',
        category='स्मारक',
        country='भारत',
        state='दिल्ली',
        location='महरौली',
        continent='एशिया',
        description='विश्व की सबसे ऊंची ईंट की मीनार। 73 मीटर ऊंची।',
        architecture='इंडो-इस्लामिक वास्तुकला, लाल बलुआ पत्थर और संगमरमर से निर्मित।',
        built_by='कुतुबुद्दीन ऐबक',
        built_year='1193',
        visiting_hours='सुबह 7 से शाम 5',
        entry_fee='₹35 (भारतीय), ₹550 (विदेशी)',
        is_unesco=True,
        unesco_year=1993,
        is_india=True,
        main_image=qutub_images['main'],
        architecture_image=qutub_images['architecture'],
        night_image=qutub_images['night'],
        gallery_images=json.dumps(qutub_images['gallery'])
    )
    
    # ============================================
    # आगरा का किला
    # ============================================
    agra_fort_images = {
        'main': 'https://images.pexels.com/photos/5745201/pexels-photo-5745201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'architecture': 'https://images.pexels.com/photos/5745202/pexels-photo-5745202.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'night': 'https://images.pexels.com/photos/3225533/pexels-photo-3225533.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/3225534/pexels-photo-3225534.jpeg',
            'https://images.pexels.com/photos/3225535/pexels-photo-3225535.jpeg'
        ]
    }
    
    agra_fort = HeritageSite(
        name='आगरा का किला',
        name_hindi='आगरा का किला',
        category='किला',
        country='भारत',
        state='उत्तर प्रदेश',
        location='आगरा',
        continent='एशिया',
        description='मुगलों का प्रमुख किला। लाल बलुआ पत्थर से निर्मित।',
        architecture='मुगल वास्तुकला, लाल बलुआ पत्थर, भव्य महल और मस्जिदें।',
        built_by='अकबर',
        built_year='1565-1573',
        is_unesco=True,
        unesco_year=1983,
        is_india=True,
        main_image=agra_fort_images['main'],
        architecture_image=agra_fort_images['architecture'],
        night_image=agra_fort_images['night'],
        gallery_images=json.dumps(agra_fort_images['gallery'])
    )
    
    # ============================================
    # ग्रेट वॉल ऑफ चाइना
    # ============================================
    great_wall_images = {
        'main': 'https://images.pexels.com/photos/5169070/pexels-photo-5169070.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'architecture': 'https://images.pexels.com/photos/5169071/pexels-photo-5169071.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'location': 'https://images.pexels.com/photos/5169072/pexels-photo-5169072.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/5169073/pexels-photo-5169073.jpeg',
            'https://images.pexels.com/photos/5169074/pexels-photo-5169074.jpeg'
        ]
    }
    
    great_wall = HeritageSite(
        name='ग्रेट वॉल ऑफ चाइना',
        name_hindi='चीन की महान दीवार',
        category='किला',
        country='चीन',
        continent='एशिया',
        description='दुनिया की सबसे लंबी दीवार। 21,000 किमी से अधिक लंबी।',
        architecture='प्राचीन चीनी वास्तुकला, पत्थर और ईंटों से निर्मित।',
        built_year='220 BC',
        is_unesco=True,
        unesco_year=1987,
        is_india=False,
        main_image=great_wall_images['main'],
        architecture_image=great_wall_images['architecture'],
        location_image=great_wall_images['location'],
        gallery_images=json.dumps(great_wall_images['gallery'])
    )
    
    # ============================================
    # पेट्रा
    # ============================================
    petra_images = {
        'main': 'https://images.pexels.com/photos/5737875/pexels-photo-5737875.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'architecture': 'https://images.pexels.com/photos/5737876/pexels-photo-5737876.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'night': 'https://images.pexels.com/photos/5737877/pexels-photo-5737877.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/5737878/pexels-photo-5737878.jpeg',
            'https://images.pexels.com/photos/5737879/pexels-photo-5737879.jpeg'
        ]
    }
    
    petra = HeritageSite(
        name='पेट्रा',
        name_hindi='पेट्रा',
        category='पुरातात्विक',
        country='जॉर्डन',
        continent='एशिया',
        description='गुलाबी शहर, चट्टानों में बसा प्राचीन नगर।',
        architecture='नबातियन वास्तुकला, चट्टानों को काटकर बनाए गए मंदिर और मकबरे।',
        built_year='300 BC',
        is_unesco=True,
        unesco_year=1985,
        is_india=False,
        main_image=petra_images['main'],
        architecture_image=petra_images['architecture'],
        night_image=petra_images['night'],
        gallery_images=json.dumps(petra_images['gallery'])
    )
    
    # ============================================
    # माचू पिचू
    # ============================================
    machu_images = {
        'main': 'https://images.pexels.com/photos/9141309/pexels-photo-9141309.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'architecture': 'https://images.pexels.com/photos/9141310/pexels-photo-9141310.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'location': 'https://images.pexels.com/photos/9141311/pexels-photo-9141311.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/9141312/pexels-photo-9141312.jpeg',
            'https://images.pexels.com/photos/9141313/pexels-photo-9141313.jpeg'
        ]
    }
    
    machu = HeritageSite(
        name='माचू पिचू',
        name_hindi='माचू पिचू',
        category='पुरातात्विक',
        country='पेरू',
        continent='दक्षिणी अमेरिका',
        description='इंका सभ्यता का खोया हुआ शहर।',
        architecture='इंका वास्तुकला, पत्थरों को बिना मसाले के जोड़ा गया।',
        built_year='1450',
        is_unesco=True,
        unesco_year=1983,
        is_india=False,
        main_image=machu_images['main'],
        architecture_image=machu_images['architecture'],
        location_image=machu_images['location'],
        gallery_images=json.dumps(machu_images['gallery'])
    )
    
    # ============================================
    # कोलोसियम
    # ============================================
    colosseum_images = {
        'main': 'https://images.pexels.com/photos/9168143/pexels-photo-9168143.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'architecture': 'https://images.pexels.com/photos/9168144/pexels-photo-9168144.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'night': 'https://images.pexels.com/photos/9168145/pexels-photo-9168145.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2',
        'gallery': [
            'https://images.pexels.com/photos/9168146/pexels-photo-9168146.jpeg',
            'https://images.pexels.com/photos/9168147/pexels-photo-9168147.jpeg'
        ]
    }
    
    colosseum = HeritageSite(
        name='कोलोसियम',
        name_hindi='कोलोसियम',
        category='स्मारक',
        country='इटली',
        continent='यूरोप',
        description='रोमन साम्राज्य का सबसे बड़ा अखाड़ा।',
        architecture='प्राचीन रोमन वास्तुकला, कंक्रीट और पत्थर से निर्मित।',
        built_year='70-80 ईस्वी',
        is_unesco=True,
        unesco_year=1980,
        is_india=False,
        main_image=colosseum_images['main'],
        architecture_image=colosseum_images['architecture'],
        night_image=colosseum_images['night'],
        gallery_images=json.dumps(colosseum_images['gallery'])
    )
    
    # सभी sites को add करो
    sites = [taj, qutub, agra_fort, great_wall, petra, machu, colosseum]
    
    for site in sites:
        db.session.add(site)
    
    db.session.commit()
    print(f"✅ {len(sites)} heritage sites added with multiple images!")