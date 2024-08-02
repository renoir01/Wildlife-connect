from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import Report
from .forms import ReportForm

@login_required
def upload_report(request):
    if request.user.user_type != 'researcher':
        return redirect('core:home')  # Redirect non-researchers to the home page
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.uploaded_by = request.user
            report.save()
            return redirect('core:view_reports')
    else:
        form = ReportForm()
    return render(request, 'core/upload_report.html', {'form': form})

@login_required
def view_reports(request):
    reports = Report.objects.all()
    return render(request, 'core/view_reports.html', {'reports': reports})

# Custom Logout View
class CustomLogoutView(LogoutView):
    template_name = 'core/logout.html'

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    success_url = reverse_lazy('core:home')  # Redirect to home after login

# Custom Password Reset View
class CustomPasswordResetView(PasswordResetView):
    template_name = 'core/password_reset.html'

# Redirect to Home
@login_required(login_url="/login/")
def home_redirect(request):
    template_name = "core/home.html"
    return render(request, template_name)

# Contact Form Handling
@login_required(login_url="/login/")
def contact_form(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'core/contact_form.html')

# User Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:login")
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

# Static Pages requiring login
@login_required(login_url="/login/")
def about(request):
    return render(request, 'core/about.html')

@login_required(login_url="/login/")
def parks(request):
    return render(request, 'core/parks.html')

@login_required(login_url="/login/")
def booking(request):
    return render(request, 'core/booking.html')

@login_required(login_url="/login/")
def community(request):
    return render(request, 'core/community.html')

@login_required(login_url="/login/")
def forum(request):
    return render(request, 'core/forum.html')

@login_required(login_url="/login/")
def donate(request):
    return render(request, 'core/donate.html')

@login_required(login_url="/login/")
def events(request):
    return render(request, 'core/events.html')

@login_required(login_url="/login/")
def donation(request):
    return render(request, 'core/donation.html')

@login_required(login_url="/login/")
def booking_park(request):
    return render(request, 'core/booking_park.html')

@login_required(login_url="/login/")
def booking_form(request):
    park = request.GET.get('park')
    return render(request, 'booking_form.html', {'park': park})

@login_required(login_url="/login/")
def home(request):
    return render(request, 'home.html')