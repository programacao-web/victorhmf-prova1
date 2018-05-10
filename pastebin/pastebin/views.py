from django.shortcuts import render, get_object_or_404, redirect
from .forms import PasteForm
from .models import Paste

def index(request):
    ctx = {}
    
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid(): 
            paste = form.save()
            return redirect('pastebin-detail', id=paste.id)
    else:
        form = PasteForm() 
    return render(request, 'pastebin/index.jinja2', {'form': form})


def paste(request, id):
    paste = get_object_or_404(Paste, pk=id)
    ctx = {
        'paste': paste
    }    
    return render(request, 'pastebin/paste-detail.jinja2', ctx)


def language_list(request, language):
    ctx = {'pastes': []}
    return render(request, 'pastebin/paste-language.jinja2', ctx)