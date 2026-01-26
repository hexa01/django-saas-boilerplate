from django.shortcuts import render
import logging
# Create your views here.
logger = logging.getLogger(__name__)
def home(request):
    # logger.info("home page visited")
    return render(request, 'core/base.html')
