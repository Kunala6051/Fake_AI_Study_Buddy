def username_processor(request):
    return {
        "user_name": request.session.get("user_name", "Guest")
    }
