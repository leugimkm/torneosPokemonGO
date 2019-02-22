from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ParticiparForm
from .models import Participar

@login_required
def participar(request):
    if request.method == 'POST':
        form = ParticiparForm(request.POST,
                                   instance=request.user.participar)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.asistir = form.cleaned_data.get('asistir')
            t.save()
            messages.success(request, f"Tu eleccion ha sido confirmada!") 
            return redirect('/participar/')
    else:
        form = ParticiparForm(instance=request.user.participar)
    users = Participar.objects.filter(asistir='Si')
    context = {
        'form': form,
        'users': users,
    }
    return render(request, 'participar/great.html', context)
