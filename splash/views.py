from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
import logging

logger = logging.getLogger(__name__)

def submit_form(request):
    logger.info(f"submit_form called with method: {request.method}")
    if request.method == 'POST':
        form = UserForm(request.POST)
        logger.info(f"Received POST request with data: {request.POST}")
        if form.is_valid():
            try:
                user = form.save()
                logger.info(f"User {user.id} saved successfully")
                logger.info(f"Redirecting to home_page with user_id: {user.id}")
                return redirect('home_page', user_id=user.id)
            except Exception as e:
                logger.error(f"Error saving user: {e}", exc_info=True)
                return HttpResponse("An error occurred while saving the form.")
        else:
            logger.warning(f"Form is invalid. Errors: {form.errors}")
            return render(request, 'splash/splash_page.html', {'form': form})
    else:
        logger.warning(f"Invalid request method: {request.method}")
        return HttpResponse("Invalid request method")

def splash_page(request):
    logger.info("splash_page view called")
    form = UserForm()
    return render(request, 'splash/splash_page.html', {'form': form})

def home_page(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        logger.info(f"Rendering home page for user: {user.id}")
        return render(request, 'splash/home_page.html', {'user': user})
    except User.DoesNotExist:
        logger.error(f"User with id {user_id} not found", exc_info=True)
        return HttpResponse("User not found", status=404)