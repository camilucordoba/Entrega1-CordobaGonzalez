from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from clothes.models import Clothes
from clothes.forms import Product_form

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class List_clothes(ListView):
    model = Clothes
    template_name= 'clothes.html'
    queryset = Clothes.objects.filter(is_active = True)

class Detail_clothes(DetailView):
    model = Clothes
    template_name= 'detail_clothes.html'

class Create_clothes(LoginRequiredMixin, CreateView):
    model = Clothes
    template_name = 'create_clothes.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_clothes', kwargs={'pk':self.object.pk})

class Delete_clothes(DeleteView):
    model = Clothes
    template_name = 'delete_clothes.html'

    def get_success_url(self):
        return reverse('list_clothes')

class Update_clothes(UpdateView):
    model = Clothes
    template_name = 'update_clothes.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_clothes', kwargs = {'pk':self.object.pk})



# Create your views here.       
# def list_clothes(request):
#     clothes = clothes.objects.all()
#     context = {'clothes':clothes}
#     return render(request, 'clothes.html', context=context)

# def detail_clothes(request, pk):
#     try:
#         clothes = clothes.objects.get(id=pk)
#         context = {'clothes':clothes}
#         return render(request, 'clothes_detail.html', context=context)
#     except:
#         context = {'error':'El Producto no existe'}
#         return render(request, 'clothes.html', context=context)

# def create_clothes(request):
#     if request.method == 'GET':

#         form = Product_form()
#         context = {'form':form}

#         return render(request, 'create_clothes.html', context=context)

#     elif request.method == 'POST':
        
#         form = Product_form(request.POST)
#         if form.is_valid():
#             new_clothes = clothes.objects.create(
#                 name = form.cleaned_data['name'],
#                 price = form.cleaned_data['price'],
#                 description = form.cleaned_data['description'],
#                 bar_code = form.cleaned_data['bar_code'],
#                 is_active = form.cleaned_data['is_active'],
#             )
#             context = {'new_clothes':new_clothes}
#         else:
#             context = {'errors':form.errors}
#         return render(request, 'create_clothes.html', context = context)

#     else:
#         return HttpResponse('Only GET and POST methods are allowed')



# def delete_clothes(request, pk):
#     try:
#         if request.method == 'GET':
#             clothes = clothes.objects.get(id=pk)
#             context = {'clothes':clothes}
#         else:
#             clothes = clothes.objects.get(id=pk)
#             clothes.delete()
#             context = {'message':'Producto eliminado correctamente'}

#         return render(request, 'delete_clothes.html', context=context)

#     except:
#         context = {'error':'El Producto no existe'}
#         return render(request, 'delete_clothes.html', context=context)



def search_clothes(request):
    clothes = Clothes.objects.filter(name__icontains=request.GET['search'])
    if clothes.exists():
        context = {'clothes':clothes}
    else:
        context = {'errors':'No se encontro la prenda'}
    return render(request, 'search_clothes.html', context = context)