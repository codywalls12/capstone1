from django.shortcuts import render
from django.http import HttpResponse
from .models import GraphModel, graphpoint




def index(request):
    context = {}
    return render(request, "graph/index.html", context)


def graph_creation(request):
    graph_name = request.POST.get('graph_name')
    test_graph = GraphModel.objects.all()
    context = {'test_graph': test_graph,
               'graph_name': graph_name}
    
    return render(request, "graph/graph_creation.html", context)