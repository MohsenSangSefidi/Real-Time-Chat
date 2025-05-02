from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from allauth.account.utils import send_email_confirmation
from users.forms import ProfileForm, EmailForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import User


@login_required
def profile_view(request, username, *args, **kwargs):
    if username:
        profile = get_object_or_404(User, username=username).profile

    else:

        try:
            profile = request.user.profile
        except:
            return redirect(reverse('account_login'))

    return render(request, "profile.html", {"profile": profile})


@login_required
def edit_profile_view(request, *args, **kwargs):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))

    if request.path == reverse('onboarding_profile'):
        onboarding = True
    else:
        onboarding = False

    return render(request, "edit_profile.html", {"form": form, "onboarding": onboarding})


@login_required
def profile_settings_view(request, *args, **kwargs):
    return render(request, 'profile_setting.html')


@login_required
def profile_change_email(request, *args, **kwargs):

    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/change_email.html', {'form': form})

    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                messages.error(request, f'{email} already registered.')
                return redirect(reverse('profile_settings'))

        form.save()

        send_email_confirmation(request, request.user)

        return redirect(reverse('profile_settings'))

    else:
        messages.warning(request, 'Form not valid')
        return redirect(reverse('profile_settings'))


@login_required
def profile_verify_email(request, *args, **kwargs):
    send_email_confirmation(request, request.user)
    return redirect(reverse('profile_settings'))


@login_required
def profile_delete_view(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect(reverse('index'))

    return render(request, 'delete_profile.html')
