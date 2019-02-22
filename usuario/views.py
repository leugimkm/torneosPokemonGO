from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def registrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = form.save()
            profile = user.profile
            team = form.cleaned_data.get('team')
            sexo = form.cleaned_data.get('sexo')
            profile.team = team
            profile.sexo = sexo
            profile.save()
            messages.success(request, f"{username} registrado! Ahora puedes acceder!")
            return redirect('entrar')
    else:
        form = UserRegisterForm()
    return render(request, 'usuario/registrar.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST,
                                   instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Tu cuenta ha sido actualizada!")
            return redirect('/perfil/')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'form': form,
    }
    return render(request, 'usuario/perfil.html', context)