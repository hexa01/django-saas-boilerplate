from django.shortcuts import render
import logging
from django.contrib.auth.decorators import login_required

# Create your views here.
logger = logging.getLogger(__name__)
def home(request):
    # logger.info("home page visited")
    return render(request, 'core/base.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')