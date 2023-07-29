from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Dashboard(LoginRequiredMixin, ListView):
    pass


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})