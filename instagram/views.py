from django.core.checks import messages
from django.shortcuts import redirect, render

# Create your views here.
def registeruser(request):
    title = 'Register - instagram'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!. Check out our Email later :)')

            return redirect('login')