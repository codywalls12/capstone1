from django.shortcuts import render
from django.http import HttpResponse
from .models import GraphModel, graphpoint
from bokeh.embed import components
from bokeh.plotting import figure

def index(request):
    context = {}
    return render(request, "graph/index.html", context)

def graph_creation(request):
    graph_name = request.POST.get('graph_name')
    test_graph = GraphModel.objects.all()
   
    x_val = request.POST.get('x_values')
    y_val= request.POST.get('y_values')
    
    y_Values= [int(d) for d in y_val.split(',')]
    x_Values= x_val.split(',')
    p = figure(x_range=x_Values, height=350, title=graph_name, toolbar_location=None, tools="")
    p.vbar(x=x_Values, top=y_Values, width=0.9)
    script, div = components(p)

    context = {'test_graph': test_graph,
               'graph_name': graph_name,
               'script': script,
               'div': div,}

    return render(request, "graph/graph_creation.html", context)
