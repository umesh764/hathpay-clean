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
    # उत्तराखंड - केदारनाथ (बर्फ के साथ)
    # ============================================
    kedarnath = HeritageSite(
        name='केदारनाथ मंदिर',
        name_hindi='केदारनाथ मंदिर',
        category='मंदिर',
        country='भारत',
        state='उत्तराखंड',
        location='केदारनाथ',
        continent='एशिया',
        description='बारह ज्योतिर्लिंगों में से एक। भगवान शिव को समर्पित। हिमालय की ऊंची चोटियों के बीच स्थित यह मंदिर साल में 6 महीने बर्फ से ढका रहता है।',
        history='महाभारत काल से जुड़ी मान्यताएं। वर्तमान मंदिर का निर्माण आदि शंकराचार्य ने 8वीं शताब्दी में करवाया था।',
        architecture='उत्तर भारतीय मंदिर वास्तुकला। बड़े-बड़े पत्थरों से निर्मित, जो हिमालय की कठोर जलवायु में भी टिके रहते हैं।',
        built_year='8वीं शताब्दी',
        visiting_hours='सुबह 4 से रात 9 बजे तक (मौसम अनुसार)',
        best_time='मई से अक्टूबर (सर्दियों में बंद)',
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/3/32/Kedarnath_Temple_in_November_2017.jpg',
        night_image='https://upload.wikimedia.org/wikipedia/commons/5/5e/Kedarnath_Temple_evening_view.jpg'
    )
    
    # ============================================
    # आंध्र प्रदेश - तिरुपति बालाजी (सही मंदिर फोटो)
    # ============================================
    tirupati = HeritageSite(
        name='तिरुपति बालाजी मंदिर',
        name_hindi='श्री वेंकटेश्वर मंदिर',
        category='मंदिर',
        country='भारत',
        state='आंध्र प्रदेश',
        location='तिरुमाला',
        continent='एशिया',
        description='दुनिया के सबसे अमीर और सबसे ज्यादा देखे जाने वाले मंदिरों में से एक। भगवान वेंकटेश्वर (विष्णु) को समर्पित।',
        history='त्रेतायुग से जुड़ी पौराणिक कथाएं। वर्तमान मंदिर का निर्माण 300 ईस्वी के आसपास हुआ था।',
        architecture='द्रविड़ वास्तुकला का बेहतरीन उदाहरण। सात मंजिला अनंद निलयम विमान, सोने से मढ़ा हुआ।',
        built_year='300 ईस्वी',
        visiting_hours='सुबह 2:30 बजे से रात 2 बजे तक',
        entry_fee='मुफ्त (विशेष दर्शन के लिए अलग शुल्क)',
        best_time='सितंबर से मार्च',
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/f/f5/Tirupati_2003_016.jpg',
        architecture_image='https://upload.wikimedia.org/wikipedia/commons/3/35/Ananda_Nilayam_%28Tirupati%29.jpg',
        night_image='https://upload.wikimedia.org/wikipedia/commons/8/8b/Tirumala_2003_007.jpg'
    )
    
    # ============================================
    # उत्तर प्रदेश - ताजमहल
    # ============================================
    tajmahal = HeritageSite(
        name='ताजमहल',
        name_hindi='ताजमहल',
        category='स्मारक',
        country='भारत',
        state='उत्तर प्रदेश',
        location='आगरा',
        continent='एशिया',
        description='प्रेम का प्रतीक, मुगल वास्तुकला का उत्कृष्ट नमूना। विश्व के सात अजूबों में से एक।',
        history='मुगल बादशाह शाहजहाँ ने अपनी बेगम मुमताज महल की याद में 1632 में इसका निर्माण शुरू करवाया। 1653 में यह बनकर तैयार हुआ।',
        architecture='मुगल वास्तुकला का बेहतरीन उदाहरण। सफेद संगमरमर से निर्मित, चार मीनारें, फारसी इस्लामिक शैली।',
        built_by='शाहजहाँ',
        built_year='1632-1653',
        visiting_hours='सूर्योदय से सूर्यास्त तक (शुक्रवार बंद)',
        entry_fee='₹50 (भारतीय), ₹1100 (विदेशी)',
        best_time='अक्टूबर से मार्च',
        is_unesco=True,
        unesco_year=1983,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/b/bd/Taj_Mahal%2C_Agra%2C_India_edit3.jpg',
        night_image='https://upload.wikimedia.org/wikipedia/commons/3/38/Taj_Mahal_at_Night.jpg',
        architecture_image='https://upload.wikimedia.org/wikipedia/commons/1/1d/Taj_Mahal_%28Edited%29.jpeg'
    )
    
    # ============================================
    # दिल्ली - कुतुब मीनार
    # ============================================
    qutub = HeritageSite(
        name='कुतुब मीनार',
        name_hindi='कुतुब मीनार',
        category='स्मारक',
        country='भारत',
        state='दिल्ली',
        location='महरौली',
        continent='एशिया',
        description='विश्व की सबसे ऊंची ईंट की मीनार। 73 मीटर ऊंची।',
        built_by='कुतुबुद्दीन ऐबक',
        built_year='1193',
        visiting_hours='सुबह 7 से शाम 5',
        entry_fee='₹35 (भारतीय), ₹550 (विदेशी)',
        is_unesco=True,
        unesco_year=1993,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/8/8d/Qutub_Minar_2014.jpg',
        night_image='https://upload.wikimedia.org/wikipedia/commons/5/53/Qutub_Minar_at_Night.jpg'
    )
    
    # ============================================
    # दिल्ली - लाल किला
    # ============================================
    lalqila = HeritageSite(
        name='लाल किला',
        name_hindi='लाल किला',
        category='किला',
        country='भारत',
        state='दिल्ली',
        location='दिल्ली',
        continent='एशिया',
        description='मुगल बादशाहों का मुख्य निवास। लाल बलुआ पत्थर से निर्मित।',
        built_by='शाहजहाँ',
        built_year='1638-1648',
        is_unesco=True,
        unesco_year=2007,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/5/5b/Lal_Qila.jpg'
    )
    
    # ============================================
    # राजस्थान - आमेर का किला
    # ============================================
    amer = HeritageSite(
        name='आमेर का किला',
        name_hindi='आमेर का किला',
        category='किला',
        country='भारत',
        state='राजस्थान',
        location='जयपुर',
        continent='एशिया',
        description='राजपूत वास्तुकला का बेहतरीन उदाहरण। पहाड़ी पर स्थित भव्य किला।',
        built_by='राजा मान सिंह प्रथम',
        built_year='1592',
        visiting_hours='सुबह 8 से शाम 5:30',
        entry_fee='₹25 (भारतीय), ₹550 (विदेशी)',
        best_time='अक्टूबर से मार्च',
        is_unesco=True,
        unesco_year=2013,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/9/97/Amber_Fort%2C_Jaipur.jpg'
    )
    
    # ============================================
    # पंजाब - स्वर्ण मंदिर
    # ============================================
    golden = HeritageSite(
        name='स्वर्ण मंदिर',
        name_hindi='हरमंदिर साहिब',
        category='गुरुद्वारा',
        country='भारत',
        state='पंजाब',
        location='अमृतसर',
        continent='एशिया',
        description='सिख धर्म का सबसे पवित्र स्थल। सोने से मढ़ा अद्भुत गुरुद्वारा।',
        built_by='गुरु अर्जुन देव',
        built_year='1588-1604',
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/9/94/The_Golden_Temple_of_Amritsar.jpg',
        night_image='https://upload.wikimedia.org/wikipedia/commons/f/fd/Golden_Temple_Night.jpg'
    )
    
    # ============================================
    # महाराष्ट्र - गेटवे ऑफ इंडिया
    # ============================================
    gateway = HeritageSite(
        name='गेटवे ऑफ इंडिया',
        name_hindi='गेटवे ऑफ इंडिया',
        category='स्मारक',
        country='भारत',
        state='महाराष्ट्र',
        location='मुंबई',
        continent='एशिया',
        description='मुंबई का प्रसिद्ध स्मारक। भारत के प्रवेश द्वार के रूप में जाना जाता है।',
        built_by='जॉर्ज विटेट',
        built_year='1911-1924',
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/3/3a/Mumbai_03-2016_30_Gateway_of_India.jpg'
    )
    
    # ============================================
    # मध्य प्रदेश - खजुराहो
    # ============================================
    khajuraho = HeritageSite(
        name='खजुराहो के मंदिर',
        name_hindi='खजुराहो के मंदिर',
        category='मंदिर',
        country='भारत',
        state='मध्य प्रदेश',
        location='खजुराहो',
        continent='एशिया',
        description='कामुक मूर्तियों के लिए प्रसिद्ध मंदिर समूह। चंदेल वंश द्वारा निर्मित।',
        built_by='चंदेल राजवंश',
        built_year='950-1050 ईस्वी',
        is_unesco=True,
        unesco_year=1986,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/4/4f/Kandariya_Mahadev_Temple.jpg'
    )
    
    # ============================================
    # गुजरात - स्टैच्यू ऑफ यूनिटी
    # ============================================
    statue = HeritageSite(
        name='स्टैच्यू ऑफ यूनिटी',
        name_hindi='स्टैच्यू ऑफ यूनिटी',
        category='स्मारक',
        country='भारत',
        state='गुजरात',
        location='केवड़िया',
        continent='एशिया',
        description='दुनिया की सबसे ऊंची प्रतिमा। सरदार वल्लभभाई पटेल की 182 मीटर ऊंची मूर्ति।',
        built_year='2013-2018',
        visiting_hours='सुबह 8 से शाम 6',
        entry_fee='₹150-₹350',
        best_time='अक्टूबर से फरवरी',
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/c/cf/Statue_of_Unity_in_2019.jpg'
    )
    
    # ============================================
    # कर्नाटक - हम्पी
    # ============================================
    hampi = HeritageSite(
        name='हम्पी के स्मारक',
        name_hindi='हम्पी के स्मारक',
        category='पुरातात्विक',
        country='भारत',
        state='कर्नाटक',
        location='हम्पी',
        continent='एशिया',
        description='विजयनगर साम्राज्य की राजधानी के अवशेष।',
        built_year='1336-1565',
        is_unesco=True,
        unesco_year=1986,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/f/f4/Virupaksha_temple_at_Hampi.jpg'
    )
    
    # ============================================
    # तमिलनाडु - महाबलीपुरम
    # ============================================
    mahabalipuram = HeritageSite(
        name='महाबलीपुरम के स्मारक',
        name_hindi='महाबलीपुरम के स्मारक',
        category='पुरातात्विक',
        country='भारत',
        state='तमिलनाडु',
        location='महाबलीपुरम',
        continent='एशिया',
        description='चट्टानों को काटकर बनाए गए मंदिर और रथ। पल्लव वंश की कला।',
        built_year='7वीं-8वीं शताब्दी',
        is_unesco=True,
        unesco_year=1984,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/2/2d/Shore_Temple_Mamallapuram.jpg'
    )
    
    # ============================================
    # ओडिशा - कोणार्क
    # ============================================
    konark = HeritageSite(
        name='कोणार्क का सूर्य मंदिर',
        name_hindi='कोणार्क का सूर्य मंदिर',
        category='मंदिर',
        country='भारत',
        state='ओडिशा',
        location='कोणार्क',
        continent='एशिया',
        description='रथ के आकार में निर्मित प्रसिद्ध मंदिर। सूर्य भगवान को समर्पित।',
        built_by='नरसिंहदेव प्रथम',
        built_year='1238-1250',
        is_unesco=True,
        unesco_year=1984,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/4/48/Konarka_Temple.jpg'
    )
    
    # ============================================
    # मध्य प्रदेश - सांची का स्तूप
    # ============================================
    sanchi = HeritageSite(
        name='सांची का स्तूप',
        name_hindi='सांची का स्तूप',
        category='स्तूप',
        country='भारत',
        state='मध्य प्रदेश',
        location='सांची',
        continent='एशिया',
        description='बौद्ध वास्तुकला का उत्कृष्ट नमूना। सम्राट अशोक द्वारा निर्मित।',
        built_by='सम्राट अशोक',
        built_year='3री शताब्दी ईसा पूर्व',
        is_unesco=True,
        unesco_year=1989,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/f/f4/Sanchi_Stupa_from_Eastern_gate.jpg'
    )
    
    # ============================================
    # महाराष्ट्र - अजंता गुफाएं
    # ============================================
    ajanta = HeritageSite(
        name='अजंता की गुफाएं',
        name_hindi='अजंता की गुफाएं',
        category='गुफा',
        country='भारत',
        state='महाराष्ट्र',
        location='औरंगाबाद',
        continent='एशिया',
        description='बौद्ध गुफा मंदिर। अद्भुत भित्तिचित्र और मूर्तियां।',
        built_year='दूसरी शताब्दी ईसा पूर्व से 6ठी शताब्दी',
        is_unesco=True,
        unesco_year=1983,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/1/13/Ajanta_Caves_30.jpg'
    )
    
    # ============================================
    # गोवा - बेसिलिका ऑफ बॉम जीसस
    # ============================================
    goa = HeritageSite(
        name='बेसिलिका ऑफ बॉम जीसस',
        name_hindi='बेसिलिका ऑफ बॉम जीसस',
        category='चर्च',
        country='भारत',
        state='गोवा',
        location='गोवा',
        continent='एशिया',
        description='गोवा का प्रसिद्ध चर्च। संत फ्रांसिस जेवियर के अवशेष यहां रखे हैं।',
        built_year='1594-1605',
        is_unesco=True,
        unesco_year=1986,
        is_india=True,
        main_image='https://upload.wikimedia.org/wikipedia/commons/f/f9/Basilica_of_Bom_Jesus_Goa_India.jpg'
    )
    
    # सभी sites को add करो
    sites = [
        kedarnath, tirupati, tajmahal, qutub, lalqila, amer, 
        golden, gateway, khajuraho, statue, hampi, mahabalipuram,
        konark, sanchi, ajanta, goa
    ]
    
    for site in sites:
        db.session.add(site)
    
    db.session.commit()
    print(f"✅ {len(sites)} heritage sites with correct images added successfully!")