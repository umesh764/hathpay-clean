"""
Heritage Images Check Script
यह स्क्रिप्ट चेक करेगी कि डेटाबेस में कौन-सी इमेज सेव हैं
"""

from app import create_app
from modules.models import HeritageSite
import json

app = create_app()

with app.app_context():
    sites = HeritageSite.query.all()
    print(f"Total sites: {len(sites)}")
    print("\n" + "="*80)
    
    for site in sites:
        print(f"\n🏛️  {site.name} (ID: {site.id})")
        print(f"   Main Image: {site.main_image}")
        
        if site.architecture_image:
            print(f"   Architecture Image: {site.architecture_image}")
        
        if site.night_image:
            print(f"   Night Image: {site.night_image}")
        
        if site.gallery_images:
            if isinstance(site.gallery_images, str):
                try:
                    gallery = json.loads(site.gallery_images)
                except:
                    gallery = []
            else:
                gallery = site.gallery_images
            
            print(f"   Gallery Images: {len(gallery)} images")
            for i, img in enumerate(gallery[:3]):
                print(f"     {i+1}. {img}")
        
        print("-"*50)