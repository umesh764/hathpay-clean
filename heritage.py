from flask import Blueprint, render_template, request, jsonify
from modules.models import db, HeritageSite
from sqlalchemy import or_

heritage_bp = Blueprint('heritage', __name__, url_prefix='/heritage')

# महाद्वीप
CONTINENTS = ['एशिया', 'अफ्रीका', 'उत्तरी अमेरिका', 'दक्षिणी अमेरिका', 'यूरोप', 'ऑस्ट्रेलिया', 'अंटार्कटिका']

# प्रमुख देश
COUNTRIES = [
    'भारत', 'चीन', 'जापान', 'थाईलैंड', 'कंबोडिया', 'इंडोनेशिया',
    'मिस्र', 'ईरान', 'इराक', 'तुर्की', 'जॉर्डन', 'इज़राइल',
    'इटली', 'ग्रीस', 'फ्रांस', 'स्पेन', 'यूनाइटेड किंगडम', 'जर्मनी',
    'पेरू', 'मेक्सिको', 'ब्राजील', 'अमेरिका', 'कनाडा'
]

# भारत के राज्य
INDIAN_STATES = [
    'उत्तर प्रदेश', 'मध्य प्रदेश', 'राजस्थान', 'गुजरात', 'महाराष्ट्र',
    'कर्नाटक', 'तमिलनाडु', 'केरल', 'आंध्र प्रदेश', 'तेलंगाना',
    'उड़ीसा', 'पश्चिम बंगाल', 'बिहार', 'झारखंड', 'असम', 'हिमाचल प्रदेश',
    'उत्तराखंड', 'जम्मू और कश्मीर', 'लद्दाख', 'दिल्ली', 'गोवा'
]

# श्रेणियाँ
CATEGORIES = [
    'मंदिर', 'किला', 'स्मारक', 'गुफा', 'मस्जिद', 'गुरुद्वारा',
    'चर्च', 'स्तूप', 'महल', 'प्राकृतिक', 'पुरातात्विक', 'ऐतिहासिक शहर'
]

@heritage_bp.route('/')
def home():
    """विश्व धरोहर का होम पेज"""
    featured_india = HeritageSite.query.filter_by(is_active=True, is_india=True).limit(4).all()
    featured_world = HeritageSite.query.filter_by(is_active=True, is_india=False).limit(4).all()
    unesco_sites = HeritageSite.query.filter_by(is_unesco=True, is_active=True).limit(4).all()
    
    return render_template('heritage/home.html',
                         featured_india=featured_india,
                         featured_world=featured_world,
                         unesco_sites=unesco_sites,
                         categories=CATEGORIES,
                         indian_states=INDIAN_STATES,
                         countries=COUNTRIES,
                         continents=CONTINENTS)

@heritage_bp.route('/search')
def search():
    """धरोहर स्थलों में सर्च करें"""
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '')
    country = request.args.get('country', '')
    continent = request.args.get('continent', '')
    
    filters = [HeritageSite.is_active == True]
    
    if query:
        filters.append(
            or_(
                HeritageSite.name.ilike(f'%{query}%'),
                HeritageSite.name_hindi.ilike(f'%{query}%'),
                HeritageSite.description.ilike(f'%{query}%'),
                HeritageSite.tags.ilike(f'%{query}%'),
                HeritageSite.location.ilike(f'%{query}%')
            )
        )
    
    if category:
        filters.append(HeritageSite.category == category)
    
    if country:
        filters.append(HeritageSite.country == country)
    
    if continent:
        filters.append(HeritageSite.continent == continent)
    
    results = HeritageSite.query.filter(*filters).limit(30).all()
    
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'name_hindi': s.name_hindi,
        'category': s.category,
        'country': s.country,
        'state': s.state,
        'is_india': s.is_india,
        'is_unesco': s.is_unesco,
        'description': s.description[:150] + '...' if s.description else '',
        'image_url': s.image_url
    } for s in results])

@heritage_bp.route('/site/<int:site_id>')
def site_detail(site_id):
    """किसी एक स्थल का विस्तृत पेज"""
    site = HeritageSite.query.get_or_404(site_id)
    return render_template('heritage/site_detail.html', site=site)

@heritage_bp.route('/category/<string:category_name>')
def category_view(category_name):
    """श्रेणी के अनुसार स्थल"""
    page = request.args.get('page', 1, type=int)
    sites = HeritageSite.query.filter_by(category=category_name, is_active=True).paginate(page=page, per_page=12)
    return render_template('heritage/category.html',
                         sites=sites,
                         category=category_name,
                         title=f"{category_name} - विश्व धरोहर")

@heritage_bp.route('/country/<string:country_name>')
def country_view(country_name):
    """देश के अनुसार स्थल"""
    page = request.args.get('page', 1, type=int)
    sites = HeritageSite.query.filter_by(country=country_name, is_active=True).paginate(page=page, per_page=12)
    return render_template('heritage/country.html',
                         sites=sites,
                         country=country_name,
                         title=f"{country_name} की धरोहरें")

@heritage_bp.route('/continent/<string:continent_name>')
def continent_view(continent_name):
    """महाद्वीप के अनुसार स्थल"""
    page = request.args.get('page', 1, type=int)
    sites = HeritageSite.query.filter_by(continent=continent_name, is_active=True).paginate(page=page, per_page=12)
    return render_template('heritage/continent.html',
                         sites=sites,
                         continent=continent_name,
                         title=f"{continent_name} की धरोहरें")

@heritage_bp.route('/unesco')
def unesco_sites():
    """यूनेस्को विश्व धरोहर स्थल"""
    page = request.args.get('page', 1, type=int)
    sites = HeritageSite.query.filter_by(is_unesco=True, is_active=True).paginate(page=page, per_page=12)
    return render_template('heritage/unesco.html', sites=sites)

@heritage_bp.route('/map')
def heritage_map():
    """धरोहर स्थलों का नक्शा"""
    sites = HeritageSite.query.filter_by(is_active=True).all()
    return render_template('heritage/map.html', sites=sites)

@heritage_bp.route('/stats')
def stats():
    """धरोहर सांख्यिकी"""
    total = HeritageSite.query.filter_by(is_active=True).count()
    indian = HeritageSite.query.filter_by(is_india=True, is_active=True).count()
    world = HeritageSite.query.filter_by(is_india=False, is_active=True).count()
    unesco = HeritageSite.query.filter_by(is_unesco=True, is_active=True).count()
    
    category_stats = db.session.query(
        HeritageSite.category, db.func.count(HeritageSite.id)
    ).filter_by(is_active=True).group_by(HeritageSite.category).all()
    
    return jsonify({
        'total': total,
        'indian': indian,
        'world': world,
        'unesco': unesco,
        'categories': dict(category_stats)
    })