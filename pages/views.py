from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Homer
from .forms import HomerForm
from .local_python_scripts import ev_test1


class HomePageView(TemplateView):
    template_name = 'home.html'


def HomerEvaluatedPageView(request, pk):
    homerEx = get_object_or_404(Homer, pk=pk)
    return render(request, 'homer_evaluated.html', {'homerEx': homerEx})


def EvaluateHomerPageView(request):
    if request.method == "POST":
        form = HomerForm(request.POST, request.FILES)
        if form.is_valid():
            homerEx = Homer()
            homerEx.homer_picture = request.FILES['homer_picture']
            c = ev_test1(homerEx.homer_picture.url)
            if c == 1:
                homerEx.homer_mood = 'Happy'
            else:
                homerEx.homer_mood = 'Sad'
            homerEx.save()
            return redirect('homer_evaluated', pk=homerEx.pk)
    else:
        form = HomerForm()
    return render(request, 'evaluate_homer.html', {'form': form})
