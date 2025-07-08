import json
import logging
import traceback
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .populate import initiate

# 🛠️ Logger setup
logger = logging.getLogger(__name__)

# 🔐 Login view
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("userName")
            password = data.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"userName": username, "status": "Authenticated"})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        except Exception as e:
            logger.error(f"Login error: {e}")
            return JsonResponse({"error": "Login failed"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)

# 🔓 Logout view
def logout_user(request):
    logout(request)
    return JsonResponse({"userName": ""})

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            raw_data = request.body.decode("utf-8")
            logger.info(f"Raw POST data: {raw_data}")

            data = json.loads(raw_data)
            username = data.get("userName")
            password = data.get("password")
            first_name = data.get("firstName")
            last_name = data.get("lastName")
            email = data.get("email")

            if not username or not password:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Already Registered"}, status=400)

            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name or "",
                last_name=last_name or "",
                email=email or ""
            )

            login(request, user)

            return JsonResponse({"userName": username, "status": "Registered"})

        except Exception as e:
            logger.error(f"Registration error: {e}")
            logger.error(traceback.format_exc())
            return JsonResponse({"error": str(e)}, status=500)


    logger.warning(f"Invalid request method: {request.method}")
    return JsonResponse({"error": "Invalid request method"}, status=405)

# 🏢 Dealership views (to be implemented)
# def get_dealerships(request):
#     ...

# 📣 Dealer review views (to be implemented)
# def get_dealer_reviews(request, dealer_id):
#     ...

# 📋 Dealer detail views (to be implemented)
# def get_dealer_details(request, dealer_id):
#     ...

# ✍️ Review submission view (to be implemented)
# def add_review(request):
#     ...
