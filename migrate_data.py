import os

from pathlib import Path
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()


from oc_lettings_site.models import Profile as Old_Profile
from oc_lettings_site.models import Address as Old_Address
from oc_lettings_site.models import Letting as Old_Letting

from profiles.models import Profile
from lettings.models import Letting, Address


data_profile = Old_Profile.objects.all().values()
for item_data in data_profile:
    Profile.objects.create(**item_data)


data_address = Old_Address.objects.all().values()
for item_data in data_address:
    Address.objects.create(**item_data)


data_letting = Old_Letting.objects.all().values()
for item_data in data_letting:
    Letting.objects.create(**item_data)
