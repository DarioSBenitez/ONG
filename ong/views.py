import imp
from django.http import HttpResponse


from django.http import HttpResponse


class inicio():
    
    def saludo1(self):
        return HttpResponse('primera pagina creada con una vista basada en una clase')
    
    

def saludo2(request): #primera vista
    return HttpResponse('segunda pagina creada con vista basada en una funcion')