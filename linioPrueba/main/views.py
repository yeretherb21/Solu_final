from django.views.generic import ListView, DetailView
from django.http import HttpResponse

def home(request):
  return HttpResponse("Hola Mundo. Te encuentras en la página de inicio del Linio Express")
def Saludo(request):
  return HttpResponse("Hola Mundo soy Yndira")



#producto
from .models import Producto
class ProductListView(ListView):
  model = Producto

class ProductDetailView(DetailView):
  model = Producto

#localizaciones
from .models import Localizacion
class LocalListView(ListView):
  model=Localizacion

class LocalDetailView(DetailView):
  model=Localizacion