from django.shortcuts import render


# Create your views here.

def inicio(request):
    
    return render(request, 'inicio/inicio.html', {})
    
   # template = loader.get_template('inicio.html')
   # template_renderizado = template.render({})
   # return HttpResponse(template_renderizado)
   
def sobremi(request):
    
    return render(request, 'inicio/aboutme.html', {})
    