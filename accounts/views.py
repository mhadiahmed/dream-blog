from django.shortcuts import render
from .forms import CustomUserCreateForm
# Create your views here.
def singup(request):
    form = CustomUserCreateForm(request.POST or None)

    if form.is_valid():
        insance = form.save(commit=False)
        insance.save()
        return redirect('home')

    context = {
    'form':form
    }
    return render(request,'singup.html',context)



