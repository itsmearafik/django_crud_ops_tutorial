from django.shortcuts import render
from .forms import OrderForm 
from .models import Orders 

# Create your views here.
# creating or adding 
def orderFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        
        template_name = 'crudapp/order.html'
        context = {'form': form }
        return render(request, template_name, context)
    


# read or view 
def showView(request):
    obj = Orders.objects.all()
    template_name = 'crudapp/show.html'
    context = {'obj': obj }
    return render(request, template_name, context)

# update or modify views 
def updateView(request, f_oid):
    obj = Orders.objects.get(oid=f_oid)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save() 
            return redirect('show_url')
        template_name = 'crudapp/order.html'
        context = {'form': form}
        return render(request, template_name, context)
    


def deleteView(request, f_oid):
    obj = Orders.objects.get
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'crudapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)

