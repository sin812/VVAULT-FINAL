from django.http import HttpResponse
from django.shortcuts import redirect

# Decorator to check if a user is unauthenticated
def unauthenticated_user(view_func):
    """
    Redirects authenticated users to the 'index' page.
    Allows unauthenticated users to access the view.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirect if user is authenticated
        else:
            return view_func(request, *args, **kwargs)  # Proceed to the view if not authenticated
    return wrapper_func

# Decorator to allow only users with specific roles
def allowed_users(allowed_roles=[]):
    """
    Allows access to the view only if the user belongs to one of the allowed roles.
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name  # Get the name of the first group the user belongs to
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)  # Proceed to the view if user is in allowed roles
            else:
                return HttpResponse("You are not authorized to view this page")  # Return unauthorized message if not in allowed roles
        return wrapper_func
    return decorator
