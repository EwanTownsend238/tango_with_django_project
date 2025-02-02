import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django_project.settings")

import django
django.setup()
from rango.models import Category, Page

def populate():
    #create list of dictionaries containing the pages and their details

    python_pages = [
        {"title" : "Official Python Tutorial", "url" : "http://docs.python.org/3/tutorial/", "views" : 56723},
        {"title" : "How To Think Like A Computer Scientist", "url" : "http://www.greenteapress.com/thinkpython/", "views" : 271},
        {"title" : "Learn Python in 10 Minutes", "url" : "http://www/korokithakis.net/tutorials/python/", "views" : 123},
    ]

    django_pages = [
        {"title" : "Official Django Tutorial", "url" : "https://docs.djangoproject.com/en/2.1/intro/tutorial01/", "views" : 5612},
        {"title" : "Django Rocks", "url" : "http://djangorocks.com/", "views" : 1337},
        {"title" : "How To Tango With Django", "url" : "http://www.tangowithdjango.com/", "views" : 4567},
    ]

    other_pages = [
        {"title" : "Bottle", "url" : "http://bottlepy.orgs/docs/dev", "views" : 67},
        {"title" : "Flask", "url" : "http://flask.pocoo.org", "views" : 12}
    ]


    cats = {"Python" : {"pages" : python_pages, "views" : 128, "likes" : 64},
            "Django" : {"pages" : django_pages, "views" : 64, "likes" : 32},
            "Other Frameworks" : {"pages" : other_pages, "views" : 32, "likes" : 16},
            }
            
    

    # go through cats dictionary, add each category and their pages

    for cat, cat_data in cats.items():
        c = add_cat(cat, views = cat_data["views"], likes = cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c,p["title"], p["url"])

    # print out the categories we have addded
    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f" - {c} : {p}")


# add page function
def add_page(cat, title, url, views = 0):
    p = Page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url
    p.views = views
    p.save()
    return p
    
#add category function
def add_cat(name, views = 0, likes = 0):
    c = Category.objects.get_or_create(name = name)[0]
    c.name = name
    c.views = views
    c.likes = likes
    c.save()
    return c
    

# only populate the database if the script is ran as a standalone script
if __name__ == "__main__":
    print("Starting rango population script")
    populate()