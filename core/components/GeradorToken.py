from django.template.loader import render_to_string
from django.conf import settings
import os
config = {}



for line in open('mail.pwd'):
    if not line.startswith('#') and not line.startswith('\n'):
        #arr = dict()
        print(line.replace(' ','').strip().split('='))
