from app import create_app
from modules.models import db, GovernmentDepartment

app = create_app()
with app.app_context():
    # पुराना सारा डेटा हटा दें (Clean Slate)
    print("Deleting all existing departments...")
    num_deleted = GovernmentDepartment.query.delete()
    db.session.commit()
    print(f"✅ {num_deleted} old departments deleted.")

    # अब नया डेटा डालें
    departments_to_add = [
        GovernmentDepartment(
            name='प्रधानमंत्री कार्यालय',
            name_hindi='PMO',
            description='भारत के प्रधानमंत्री का आधिकारिक कार्यालय',
            website_url='https://pmindia.gov.in',
            category='केंद्र सरकार',
            sub_category='मंत्रालय',
            search_tags='pmo, pm, प्रधानमंत्री, prime minister'
        ),
        GovernmentDepartment(
            name='नागपुर महानगरपालिका',
            name_hindi='NMC',
            description='नागपुर शहर का नगर निगम',
            website_url='https://www.nmcnagpur.gov.in',
            category='स्थानीय निकाय',
            sub_category='नगर निगम',
            state='महाराष्ट्र',
            city='नागपुर',
            search_tags='nmc, नागपुर, nagpur, महानगरपालिका'
        ),
        GovernmentDepartment(
            name='गृह मंत्रालय',
            name_hindi='Ministry of Home Affairs',
            description='आंतरिक सुरक्षा और गृह प्रशासन',
            website_url='https://mha.gov.in',
            category='केंद्र सरकार',
            sub_category='मंत्रालय',
            search_tags='गृह, home, मंत्रालय'
        ),
        GovernmentDepartment(
            name='बृहन्मुंबई महानगरपालिका',
            name_hindi='BMC',
            description='मुंबई शहर का महानगर निगम',
            website_url='https://portal.mcgm.gov.in',
            category='स्थानीय निकाय',
            sub_category='नगर निगम',
            state='महाराष्ट्र',
            city='मुंबई',
            search_tags='bmc, मुंबई, mumbai'
        ),
        # आप यहाँ और भी डिपार्टमेंट्स ऐड कर सकते हैं...
    ]

    for dept in departments_to_add:
        db.session.add(dept)

    db.session.commit()
    print(f'✅ {len(departments_to_add)} departments added successfully!')