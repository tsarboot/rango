import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_django.settings')
import django
django.setup()
from rango.models import Category,Car

def populate():
    Quadricycle_cars=[
        {"title":'Bubble car',
        "url":"https://en.wikipedia.org/wiki/Bond_Bug"
        },{
            "title":"Renault Twizy",
            "url":"https://en.wikipedia.org/wiki/Renault_Twizy"
        }
    ]
    A_mini_cars=[
        {"title":'Kei car',
        "url":'https://en.wikipedia.org/wiki/Opel_Corsa'
        },{
            "title":"Suzuki Alto",
            "url":"https://en.wikipedia.org/wiki/Suzuki_Alto"
        }
    ]
    C_medium_cars=[
        {"title":'Subcompact executive',
        "url":'https://en.wikipedia.org/wiki/BMW_1_Series'
        },{
            "title":"Acura ILX,",
            "url":"https://en.wikipedia.org/wiki/Acura_ILX"
        }
    ]
    D_large_cars=[
        {"title":'Entry-level luxury ',
        "url":'https://en.wikipedia.org/wiki/Alfa_Romeo_Giulia_(952)'
        },{
            "title":"BMW 3 Series, ",
            "url":"https://en.wikipedia.org/wiki/BMW_3_Series"
        }
    ]
    F_luxury_cars=[
        {"title":'Luxury saloon',
        "url":'https://en.wikipedia.org/wiki/BMW_7_Series'
        },{
            "title":"Porsche Panamera",
            "url":"https://en.wikipedia.org/wiki/Porsche_Panamera"
        }
    ]
    sports_coupé_cars=[
        {"title":'Sports car',
        "url":'https://en.wikipedia.org/wiki/BMW_Z4'
        },{
            "title":"LaFerrari",
            "url":"https://en.wikipedia.org/wiki/LaFerrari"
        }
    ]
    cars={
        "Quadricycle":{
            "Cars":Quadricycle_cars,
            "views":700,
            "likes":210},
        "A-mini":{
        "Cars":A_mini_cars,
        "views":128,
        "likes":11000},
        "C-medium":{
            "Cars":C_medium_cars,
            "views":7,
            "likes":2},
        "D-large":{
            "Cars":D_large_cars,
            "views":321,
            "likes":2},
        "F-luxury":{
            "Cars":F_luxury_cars,
            "views":70,
            "likes":21},
        "sports_coupé":{"Cars":sports_coupé_cars}
    }
    for key in cars:
        carDetails = list(cars[key].items())
        if len(carDetails) > 1 :
            c = add_cat(key,carDetails[1][1],carDetails[2][1])
            for Details in carDetails[0][1] :
                add_car(c,Details["title"],Details["url"])
        
        else:
            c = add_cat(key)
            for Details in carDetails[0][1] :
                add_car(c,Details["title"],Details["url"])


    for c in Category.objects.all():
        for carName in Car.objects.filter(category=c):
            print("- {0} - {1}".format(str(c),str(carName)))
def add_car(cat,title,url,views=0):
    carName = Car.objects.get_or_create(category=cat,title=title)[0]
    carName.url = url
    carName.views = views
    carName.save()
    return carName
def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population ....")
    populate()
