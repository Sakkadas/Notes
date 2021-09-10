from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView

from .forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'notes/users/profile.html', context)


class UserRegisterView(FormView, UserRegisterForm):
    template_name = 'articles/registration/registration.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user,
                  backend='django.contrib.auth.backends.ModelBackend')
        return super(UserRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('articles')
        else:
            return super(UserRegisterView, self).get(*args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'articles/registration/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('articles')
