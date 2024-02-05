from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Cliente, Veiculo
from .forms import ClienteForm, VeiculoForm

def clientes(request):
    if request.method == "GET":
        clientes = Cliente.objects.all()
        context = {
            'lista': clientes,
        }
        return render(request, "pages/clientes.html", context)

def cadastrar(request):
    if request.method == "GET":
        form = ClienteForm()
        form_veiculo_factory = inlineformset_factory(Cliente, Veiculo, form=VeiculoForm, extra=0)
        form_veiculo = form_veiculo_factory()
        context = {
            'form': form,
            'form_veiculo': form_veiculo,
        }
        return render(request, "pages/cadastrar_cliente.html", context)
    elif request.method == "POST":
        form = ClienteForm(request.POST)
        form_veiculo_factory = inlineformset_factory(Cliente, Veiculo, form=VeiculoForm)
        form_veiculo = form_veiculo_factory(request.POST)
        if form.is_valid() and form_veiculo.is_valid():
            cliente = form.save()
            form_veiculo.instance = cliente
            form_veiculo.save()
            return redirect(reverse('inlineform_lista'))
        else:
            context = {
                'form': form,
                'form_veiculo': form_veiculo,
            }
            return render(request, "pages/cadastrar_cliente.html", context)

def editar(request, cliente_id):
    if request.method == "GET":
        objeto = Cliente.objects.filter(id=cliente_id).first()
        if objeto is None:
            return redirect(reverse('inlineform_lista'))
        form = ClienteForm(instance=objeto)
        form_veiculo_factory = inlineformset_factory(Cliente, Veiculo, form=VeiculoForm, extra=0)
        form_veiculo = form_veiculo_factory(instance=objeto)
        context = {
            'form': form,
            'form_veiculo': form_veiculo,
        }
        return render(request, "pages/cadastrar_cliente.html", context)
    elif request.method == "POST":
        objeto = Cliente.objects.filter(id=cliente_id).first()
        if objeto is None:
            return redirect(reverse('inlineform_lista'))
        form = ClienteForm(request.POST, instance=objeto)
        form_veiculo_factory = inlineformset_factory(Cliente, Veiculo, form=VeiculoForm)
        form_veiculo = form_veiculo_factory(request.POST, instance=objeto)
        if form.is_valid() and form_veiculo.is_valid():
            cliente = form.save()
            form_veiculo.instance = cliente
            form_veiculo.save()
            return redirect(reverse('inlineform_lista'))
        else:
            context = {
                'form': form,
                'form_veiculo': form_veiculo,
            }
            return render(request, "pages/cadastrar_cliente.html", context)