from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log user in and redirect to homepage
            return redirect('home')
    else:
        form = RegistrationForm()
        
    return render(request, 'registration/register.html', {'form': form})