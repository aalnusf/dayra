#!/usr/bin/env python
import csv
import os
import sys

from unidecode import unidecode

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")



from app.models import Category, Item

import django
django.setup()

Item.objects.all().delete()

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dayra.csv")

csv_file = open(csv_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:

    new_category, created = Category.objects.get_or_create(type=row['type'])

    new_category.save()


    new_item, created = Item.objects.get_or_create(name =row['name'])

    new_item.description = row['description'].decode('unicode_escape')

    new_item.type = new_category # double check before importing

    if type(new_item.longitude) == 'float':
        new_item.hours = row['hours']
    else:
        new_item.hours = 0

    new_item.location = str(row['location']).decode('unicode_escape')

    new_item.link = str(row['link'])

    if type(new_item.longitude) == 'float':
        new_item.cost_per_hour = row['cost_per_hour']
    else:
        new_item.cost_per_hour = 0

    if type(new_item.longitude) == 'float':
        new_item.longitude = row['longitude']
    else:
        new_item.longitude = 0.0

    if type(new_item.longitude) == 'float':
        new_item.latitude = row['latitude']
    else:
        new_item.latitude = 0.0
    
    #images will be imported later

    new_item.save()

    print new_item.name
    print new_category