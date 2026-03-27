from app import create_app
from modules.models import db, BharatDarshan
import json

app = create_app()
with app.app_context():
    # पहले सारे पुराने डेटा हटाओ
    print("🧹 Clearing old data...")
    BharatDarshan.query.delete()
    db.session.commit()
    
    # ============================================
    # उत्तर प्रदेश (Uttar Pradesh)
    # ============================================
    uttar_pradesh_data = [
        # ========== त्योहार ==========
        {
            'state': 'उत्तर प्रदेश',
            'city': 'वाराणसी',
            'category': 'त्योहार',
            'subcategory': 'धार्मिक',
            'name': 'देव दीपावली',
            'name_hindi': 'देव दीपावली',
            'description': 'कार्तिक पूर्णिमा पर मनाया जाने वाला अद्भुत त्योहार। गंगा घाटों पर हजारों दीये जलाए जाते हैं।',
            'history': 'मान्यता है कि इस दिन देवता स्वर्ग से उतरकर गंगा स्नान करते हैं और दीपदान करते हैं।',
            'cultural_facts': 'पूरे वाराणसी के 84 घाटों पर लाखों दीये जलते हैं। गंगा आरती का विशेष महत्व है।',
            'dress_code': 'पारंपरिक साड़ी, धोती-कुर्ता',
            'cuisine': 'मालपुआ, खीर, पूरी-सब्जी',
            'best_time_to_visit': 'अक्टूबर-नवंबर',
            'duration': '3 दिन',
            'festival_month': 'कार्तिक पूर्णिमा',
            'latitude': 25.2820,
            'longitude': 82.9563,
            'how_to_reach': 'वाराणसी हवाई अड्डा, मुगलसराय रेलवे स्टेशन, सड़क मार्ग',
            'nearest_railway': 'वाराणसी सिटी, मुगलसराय',
            'nearest_airport': 'लाल बहादुर शास्त्री हवाई अड्डा, वाराणसी',
            'nearest_bus_stop': 'वाराणसी बस स्टैंड',
            'local_transport': 'ऑटो रिक्शा, साइकिल रिक्शा, ई-रिक्शा',
            'famous_markets': 'गोदौलिया, चौख, दशाश्वमेध रोड',
            'famous_food': 'कचौड़ी-सब्जी, मलैयो, बनारसी पान, ठंडाई',
            'languages': 'हिंदी, भोजपुरी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/7/7d/Dev_Deepawali_2016.jpg',
            'map_url': 'https://goo.gl/maps/varanasi-ghats'
        },
        # ========== बाज़ार ==========
        {
            'state': 'उत्तर प्रदेश',
            'city': 'वाराणसी',
            'category': 'बाज़ार',
            'subcategory': 'हस्तशिल्प बाज़ार',
            'name': 'विश्वनाथ गली',
            'name_hindi': 'विश्वनाथ गली',
            'description': 'बाबा विश्वनाथ मंदिर के पास बना पारंपरिक बाज़ार। बनारसी साड़ियों और चूड़ियों के लिए प्रसिद्ध।',
            'cultural_facts': 'यहाँ बनारसी जर्दोजी और ज़री का काम होता है। मुगल काल से यहाँ कारीगर काम करते हैं।',
            'dress_code': 'बनारसी साड़ी, धोती-कुर्ता',
            'cuisine': 'बनारसी पान, कचौड़ी-सब्जी',
            'best_time_to_visit': 'सुबह 8 से रात 10 बजे तक',
            'famous_markets': 'गोदौलिया, चौख, थातेरी बाज़ार',
            'famous_food': 'बनारसी पान, मलैयो',
            'languages': 'हिंदी, भोजपुरी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/9/9c/Vishwanath_Lane_Varanasi.jpg',
            'latitude': 25.3108,
            'longitude': 82.9739,
            'how_to_reach': 'वाराणसी कैंट से ऑटो या रिक्शा',
            'nearest_railway': 'वाराणसी सिटी',
            'nearest_airport': 'लाल बहादुर शास्त्री हवाई अड्डा'
        },
        # ========== वेशभूषा ==========
        {
            'state': 'उत्तर प्रदेश',
            'city': 'वाराणसी',
            'category': 'वेशभूषा',
            'subcategory': 'पारंपरिक परिधान',
            'name': 'बनारसी साड़ी',
            'name_hindi': 'बनारसी साड़ी',
            'description': 'भारत की सबसे प्रसिद्ध साड़ियों में से एक। शादियों और खास मौकों पर पहनी जाती है।',
            'history': 'मुगल काल में विकसित हुई यह कला आज भी जीवित है। जर्दोजी और जरी का काम इसे खास बनाता है।',
            'cultural_facts': 'असली बनारसी साड़ी में सोने और चांदी के धागे होते हैं। इसे बनने में 15 दिन से 6 महीने तक लग सकते हैं।',
            'dress_code': 'पारंपरिक बनारसी साड़ी, चूड़ियाँ, बिंदी',
            'cuisine': 'बनारसी पान, मलैयो',
            'best_time_to_visit': 'अक्टूबर-फरवरी (शादी का सीजन)',
            'famous_markets': 'गोदौलिया, चौख, विश्वनाथ गली',
            'languages': 'हिंदी, भोजपुरी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Banarasi_Saree_Weaving.jpg',
            'how_to_reach': 'वाराणसी शहर के बुनकर इलाके',
            'nearest_railway': 'वाराणसी सिटी',
            'nearest_airport': 'लाल बहादुर शास्त्री हवाई अड्डा'
        },
        # ========== प्रसिद्ध भोजन ==========
        {
            'state': 'उत्तर प्रदेश',
            'city': 'वाराणसी',
            'category': 'भोजन',
            'subcategory': 'मिठाई',
            'name': 'बनारसी मलैयो',
            'name_hindi': 'बनारसी मलैयो',
            'description': 'ठंड के मौसम की मशहूर मिठाई। गाढ़े दूध की मलाई पर केसर और ड्राई फ्रूट्स से सजी।',
            'cultural_facts': 'सर्दियों में सुबह-सुबह घाटों पर मलैयो बेचने वाले मिलते हैं। बनारस की पहचान है।',
            'cuisine': 'मलैयो, दूध, केसर',
            'best_time_to_visit': 'सुबह 6-9 बजे तक',
            'festival_month': 'अक्टूबर-फरवरी',
            'famous_markets': 'दशाश्वमेध घाट, गोदौलिया',
            'languages': 'हिंदी, भोजपुरी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/4/4a/Malaiyo.jpg',
            'how_to_reach': 'वाराणसी शहर के किसी भी इलाके में सुबह मिलता है'
        }
    ]
    
    # ============================================
    # राजस्थान (Rajasthan)
    # ============================================
    rajasthan_data = [
        # ========== त्योहार ==========
        {
            'state': 'राजस्थान',
            'city': 'जयपुर',
            'category': 'त्योहार',
            'subcategory': 'सांस्कृतिक',
            'name': 'गणगौर',
            'name_hindi': 'गणगौर',
            'description': 'राजस्थान का सबसे प्रसिद्ध त्योहार। महिलाएं गौर-गणेश की पूजा करती हैं।',
            'history': 'यह त्योहार शिव और पार्वती के विवाह का प्रतीक है। गण का मतलब शिव और गौर का मतलब पार्वती।',
            'cultural_facts': 'व्रत रखने वाली महिलाएं 16 दिनों तक पूजा करती हैं। आखिरी दिन भव्य शोभा यात्रा निकलती है।',
            'dress_code': 'पारंपरिक राजस्थानी साड़ी, चूड़ियाँ, कजली',
            'cuisine': 'गेहूं की बावड़ी, मीठी रोटी',
            'best_time_to_visit': 'मार्च-अप्रैल',
            'duration': '18 दिन',
            'festival_month': 'चैत्र शुक्ल प्रतिपदा',
            'latitude': 26.9124,
            'longitude': 75.7873,
            'how_to_reach': 'जयपुर हवाई अड्डा, रेलवे स्टेशन',
            'nearest_railway': 'जयपुर रेलवे स्टेशन',
            'nearest_airport': 'जयपुर अंतर्राष्ट्रीय हवाई अड्डा',
            'nearest_bus_stop': 'सिंधी कैंप बस स्टैंड',
            'local_transport': 'ऑटो रिक्शा, जीप, टैक्सी',
            'famous_markets': 'जोहरी बाज़ार, बापू बाज़ार, चांदपोल',
            'famous_food': 'दाल बाटी चूरमा, गट्टे की सब्जी',
            'languages': 'राजस्थानी, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/9/98/Gangaur_festival_2012.jpg'
        },
        # ========== बाज़ार ==========
        {
            'state': 'राजस्थान',
            'city': 'जयपुर',
            'category': 'बाज़ार',
            'subcategory': 'हस्तशिल्प बाज़ार',
            'name': 'जोहरी बाज़ार',
            'name_hindi': 'जोहरी बाज़ार',
            'description': 'जयपुर का सबसे प्रसिद्ध बाज़ार। आभूषण, जरी के काम, राजस्थानी जूतियों के लिए प्रसिद्ध।',
            'cultural_facts': 'यहां 100 साल पुरानी हवेलियां भी हैं। राजा-महाराजाओं के जमाने से यह बाज़ार चला आ रहा है।',
            'dress_code': 'राजस्थानी पोशाक, जूतियाँ',
            'cuisine': 'प्याज की कचौरी, मिर्ची वड़ा',
            'best_time_to_visit': 'सुबह 11 से रात 8 बजे तक',
            'famous_markets': 'बापू बाज़ार, चांदपोल, किशनपोल',
            'famous_food': 'प्याज कचौरी, दाल बाटी चूरमा',
            'languages': 'राजस्थानी, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/2/2f/Johari_Bazaar_Jaipur.jpg',
            'latitude': 26.9239,
            'longitude': 75.8267,
            'how_to_reach': 'जयपुर शहर के बीचों-बीच',
            'nearest_railway': 'जयपुर रेलवे स्टेशन',
            'nearest_airport': 'जयपुर हवाई अड्डा'
        },
        # ========== वेशभूषा ==========
        {
            'state': 'राजस्थान',
            'category': 'वेशभूषा',
            'subcategory': 'पारंपरिक परिधान',
            'name': 'राजस्थानी पोशाक',
            'name_hindi': 'राजस्थानी पोशाक',
            'description': 'राजस्थान की पहचान। चमकीले रंगों वाली घाघरा-चोली, ओढ़नी, मूंछों वाली पगड़ी।',
            'cultural_facts': 'राजस्थान की पोशाक उसके क्षेत्र के अनुसार बदलती है। मारवाड़, मेवाड़, शेखावाटी की पोशाकें अलग होती हैं।',
            'dress_code': 'पुरुष: पगड़ी, धोती, बांदी; महिला: घाघरा, चोली, ओढ़नी',
            'cuisine': 'दाल बाटी चूरमा',
            'famous_markets': 'जोहरी बाज़ार, बापू बाज़ार',
            'languages': 'राजस्थानी, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/e/e7/Rajasthani_women_in_traditional_dress.jpg'
        }
    ]
    
    # ============================================
    # गुजरात (Gujarat)
    # ============================================
    gujarat_data = [
        {
            'state': 'गुजरात',
            'city': 'अहमदाबाद',
            'category': 'त्योहार',
            'subcategory': 'सांस्कृतिक',
            'name': 'नवरात्रि',
            'name_hindi': 'नवरात्रि',
            'description': 'गुजरात का सबसे बड़ा त्योहार। 9 रातों तक गरबा और डांडिया रास चलता है।',
            'history': 'नवरात्रि दुर्गा मां की पूजा का पर्व है। यह असत्य पर सत्य की विजय का प्रतीक है।',
            'cultural_facts': 'गुजरात में नवरात्रि के दौरान हर गली-चौराहे पर गरबा होता है। पूरी रात लोग नाचते-गाते हैं।',
            'dress_code': 'महिला: चनिया चोली; पुरुष: केडिया, पगड़ी',
            'cuisine': 'फाफड़ा, जलेबी, थेपला',
            'best_time_to_visit': 'सितंबर-अक्टूबर',
            'duration': '9 दिन',
            'festival_month': 'अश्विन',
            'latitude': 23.0225,
            'longitude': 72.5714,
            'how_to_reach': 'अहमदाबाद हवाई अड्डा, रेलवे स्टेशन',
            'nearest_railway': 'अहमदाबाद रेलवे स्टेशन',
            'nearest_airport': 'सरदार वल्लभभाई पटेल हवाई अड्डा',
            'local_transport': 'बस, ऑटो रिक्शा, मेट्रो',
            'famous_food': 'ढोकला, खांडवी, मोहनथाल',
            'languages': 'गुजराती, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/c/c5/Garba_dance_at_Navratri.jpg'
        },
        {
            'state': 'गुजरात',
            'city': 'कच्छ',
            'category': 'बाज़ार',
            'subcategory': 'हथकरघा बाज़ार',
            'name': 'धोर्डो रण उत्सव बाज़ार',
            'name_hindi': 'धोर्डो रण उत्सव बाज़ार',
            'description': 'सफेद रण के बीच लगने वाला अद्भुत बाज़ार। कच्छी कढ़ाई और शिल्प के लिए प्रसिद्ध।',
            'cultural_facts': 'यहां की कच्छी कढ़ाई को GI टैग मिला है। इस कढ़ाई में दर्पण का काम होता है।',
            'dress_code': 'कच्छी पोशाक, रंगीन चूड़ियाँ',
            'cuisine': 'कच्छी ढोकला, सिंधी सैई',
            'best_time_to_visit': 'नवंबर-फरवरी (रण उत्सव के दौरान)',
            'famous_markets': 'भुज, मांडवी बीच',
            'languages': 'कच्छी, गुजराती',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/e/e2/Rann_Utsav_2022.jpg',
            'latitude': 23.8667,
            'longitude': 69.6667,
            'how_to_reach': 'भुज हवाई अड्डा, रेलवे स्टेशन से जीप'
        }
    ]
    
    # ============================================
    # पश्चिम बंगाल (West Bengal)
    # ============================================
    bengal_data = [
        {
            'state': 'पश्चिम बंगाल',
            'city': 'कोलकाता',
            'category': 'त्योहार',
            'subcategory': 'धार्मिक',
            'name': 'दुर्गा पूजा',
            'name_hindi': 'दुर्गा पूजा',
            'description': 'बंगाल का सबसे बड़ा त्योहार। 5 दिनों तक चलने वाला यह उत्सव पूरी दुनिया में प्रसिद्ध है।',
            'history': 'यह त्योहार महिषासुर पर दुर्गा की विजय का प्रतीक है। बंगाल में इसे 400 साल से मनाया जा रहा है।',
            'cultural_facts': 'कोलकाता में इस दौरान 50,000 से ज्यादा पंडाल बनते हैं। यूनेस्को ने इसे विश्व धरोहर में शामिल किया है।',
            'dress_code': 'बंगाली साड़ी, धोती-पंजाबी',
            'cuisine': 'भोग (खिचड़ी, लबड़ा, पायेश), फुचका',
            'best_time_to_visit': 'अक्टूबर',
            'duration': '5 दिन',
            'festival_month': 'अश्विन',
            'latitude': 22.5726,
            'longitude': 88.3639,
            'how_to_reach': 'कोलकाता हवाई अड्डा, रेलवे स्टेशन',
            'nearest_railway': 'हावड़ा, शियालदह',
            'nearest_airport': 'नेताजी सुभाष चंद्र बोस हवाई अड्डा',
            'local_transport': 'बस, मेट्रो, ट्राम, ऑटो रिक्शा',
            'famous_markets': 'न्यू मार्केट, गरियाहाट, दक्षिणी कोलकाता पंडाल',
            'famous_food': 'मिष्टी डोई, संदेश, रसगुल्ला, फुचका',
            'languages': 'बंगाली, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/6/60/Durga_Puja_Pandal_in_Kolkata_2010.jpg',
            'map_url': 'https://goo.gl/maps/kolkata-durga-puja'
        }
    ]
    
    # ============================================
    # तमिलनाडु (Tamil Nadu)
    # ============================================
    tamil_data = [
        {
            'state': 'तमिलनाडु',
            'city': 'मदुरै',
            'category': 'मंदिर',
            'subcategory': 'हिंदू मंदिर',
            'name': 'मीनाक्षी अम्मन मंदिर',
            'name_hindi': 'मीनाक्षी सुंदरेश्वर मंदिर',
            'description': 'दक्षिण भारत के सबसे बड़े और प्रसिद्ध मंदिरों में से एक। 1000 खंभों वाला मंडपम प्रसिद्ध है।',
            'history': '2500 साल पुराना यह मंदिर पांड्य राजाओं ने बनवाया था। मीनाक्षी और सुंदरेश्वर (शिव) को समर्पित।',
            'cultural_facts': 'मंदिर के 14 गोपुरम हैं, सबसे ऊंचा 51.9 मीटर है। रात में मंदिर की रोशनी अद्भुत लगती है।',
            'dress_code': 'पारंपरिक दक्षिण भारतीय परिधान (साड़ी, धोती)',
            'cuisine': 'मदुरै कढ़ाई, कांजी, मीठा पोंगल',
            'best_time_to_visit': 'सुबह 5-12:30, शाम 4-9:30',
            'address': 'मदुरै, तमिलनाडु - 625001',
            'latitude': 9.9195,
            'longitude': 78.1198,
            'how_to_reach': 'मदुरै हवाई अड्डा से 12 किमी, रेलवे स्टेशन से 2 किमी',
            'nearest_railway': 'मदुरै जंक्शन',
            'nearest_airport': 'मदुरै हवाई अड्डा',
            'local_transport': 'बस, ऑटो रिक्शा, टैक्सी',
            'famous_markets': 'मदुरै कपड़ा बाज़ार, मदुरै चूड़ी बाज़ार',
            'famous_food': 'मदुरै कढ़ाई, जिलेबी',
            'languages': 'तमिल, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/3/36/Meenakshi_Amman_Temple.jpg'
        }
    ]
    
    # ============================================
    # महाराष्ट्र (Maharashtra)
    # ============================================
    maharashtra_data = [
        {
            'state': 'महाराष्ट्र',
            'city': 'मुंबई',
            'category': 'बाज़ार',
            'subcategory': 'स्ट्रीट मार्केट',
            'name': 'चोर बाज़ार',
            'name_hindi': 'चोर बाज़ार',
            'description': 'मुंबई का सबसे प्रसिद्ध साप्ताहिक बाज़ार। पुरानी चीज़ों, फर्नीचर, एंटीक वस्तुओं के लिए जाना जाता है।',
            'history': 'ब्रिटिश काल से चल रहा यह बाज़ार हर रविवार को लगता है। यहां 100 साल पुरानी चीज़ें भी मिलती हैं।',
            'cultural_facts': 'बॉलीवुड की कई फिल्मों की शूटिंग यहां हुई है। पुराने जमाने की चीज़ों के शौकीनों के लिए स्वर्ग।',
            'best_time_to_visit': 'रविवार सुबह 7 से 3 बजे तक',
            'latitude': 18.9467,
            'longitude': 72.8325,
            'how_to_reach': 'मुंबई सेंट्रल, ग्रांट रोड स्टेशन से पैदल',
            'nearest_railway': 'मुंबई सेंट्रल, ग्रांट रोड',
            'nearest_airport': 'छत्रपति शिवाजी महाराज हवाई अड्डा',
            'local_transport': 'बस, टैक्सी, रिक्शा',
            'famous_food': 'पाव भाजी, भेलपुरी',
            'languages': 'मराठी, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/8/83/Chor_Bazaar_Mumbai.jpg'
        },
        {
            'state': 'महाराष्ट्र',
            'city': 'पुणे',
            'category': 'त्योहार',
            'subcategory': 'धार्मिक',
            'name': 'गणेश चतुर्थी',
            'name_hindi': 'गणेश चतुर्थी',
            'description': 'महाराष्ट्र का सबसे बड़ा त्योहार। 10 दिनों तक चलने वाला यह उत्सव पूरे राज्य में धूमधाम से मनाया जाता है।',
            'history': 'लोकमान्य तिलक ने 1894 में इसे सार्वजनिक रूप से मनाना शुरू किया था।',
            'cultural_facts': 'पुणे के दगडूशेठ गणपति को सबसे प्रसिद्ध माना जाता है। आखिरी दिन गणेश मूर्तियों का विसर्जन होता है।',
            'dress_code': 'पारंपरिक महाराष्ट्रीयन पोशाक (नौवारी साड़ी, फेटा)',
            'cuisine': 'मोदक, पुरण पोली',
            'best_time_to_visit': 'अगस्त-सितंबर',
            'duration': '10 दिन',
            'festival_month': 'भाद्रपद',
            'famous_markets': 'तुलशीबाग, लक्ष्मी रोड',
            'famous_food': 'मोदक, पुरण पोली',
            'languages': 'मराठी, हिंदी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/6/69/Ganesh_Chaturthi_festival_in_Pune.jpg'
        }
    ]
    
    # ============================================
    # जम्मू और कश्मीर
    # ============================================
    kashmir_data = [
        {
            'state': 'जम्मू और कश्मीर',
            'city': 'श्रीनगर',
            'category': 'बाज़ार',
            'subcategory': 'तैरता बाज़ार',
            'name': 'फ्लोटिंग वेजिटेबल मार्केट',
            'name_hindi': 'डल झील का तैरता सब्जी बाज़ार',
            'description': 'डल झील पर सुबह 5 से 7 बजे के बीच लगने वाला अनोखा बाज़ार। शिकारों पर सब्ज़ियां बेची जाती हैं।',
            'history': 'मुगल काल से चली आ रही यह परंपरा आज भी जीवित है। स्थानीय किसान अपनी ताज़ी सब्ज़ियां लेकर आते हैं।',
            'cultural_facts': 'यह बाज़ार केवल डेढ़ घंटे चलता है, लेकिन इसे दुनिया के सबसे अनोखे बाज़ारों में गिना जाता है।',
            'best_time_to_visit': 'सुबह 5-7 बजे',
            'cuisine': 'कश्मीरी कावा, नून चाय',
            'famous_food': 'रोगन जोश, यखनी',
            'languages': 'उर्दू, कश्मीरी',
            'main_image': 'https://upload.wikimedia.org/wikipedia/commons/e/e5/Dal_Lake_Floating_Market_Srinagar_India.jpg',
            'latitude': 34.1109,
            'longitude': 74.8645,
            'how_to_reach': 'श्रीनगर से शिकारा किराए पर लें'
        }
    ]
    
    # ============================================
    # सभी डेटा को एक साथ मर्ज करो
    # ============================================
    all_data = uttar_pradesh_data + rajasthan_data + gujarat_data + bengal_data + tamil_data + maharashtra_data + kashmir_data
    
    for item in all_data:
        db.session.add(BharatDarshan(**item))
    
    db.session.commit()
    print(f"✅ {len(all_data)} भारत दर्शन स्थल/त्योहार/बाज़ार सफलतापूर्वक जोड़े गए!")