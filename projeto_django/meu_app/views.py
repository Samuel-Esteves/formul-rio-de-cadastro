from django.shortcuts import render
from meu_app.forms import UsuarioForm
def formulario_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()
    return render(request,'formulario_usuario.html',{'form': form})
#
