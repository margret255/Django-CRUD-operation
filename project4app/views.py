from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users

# Create your views here.
def index(request):
    users = Users.objects.all()
    return render(request, 'index.html',{'users':users})

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        # Create the user instance
        user_data = Users(name=name, email=email, password=password, gender=gender)
        user_data.save()  # Save the user instance

        messages.success(request, "Account has been created successfully")
        return redirect('index')  # Adjust the redirect if necessary

    return render(request, 'register.html')



def login(request):
    return render(request, 'login.html')

def delete_user(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    messages.success(request, "User has been deleted successfully")
    return redirect('index')
def update_user(request, id):
    user = Users.objects.get(id=id)  # Get the user instance
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.gender = request.POST.get('gender')
        user.save()  # Save the updated user
        messages.success(request, "User updated successfully")
        return redirect('index')  # Redirect after updating

    return render(request, 'update.html', {'user': user})  # Render the update form
