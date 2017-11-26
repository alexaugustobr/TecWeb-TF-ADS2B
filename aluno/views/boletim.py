from django.shortcuts import render
from django.http import HttpResponse
from core.components import *
from core.models import *
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test