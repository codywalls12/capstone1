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

    plot = figure(width=400, height=400)
    plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
    script, div = components(plot)



    context = {'test_graph': test_graph,
               'graph_name': graph_name,
               'script': script,
               'div': div,}
    
    return render(request, "graph/graph_creation.html", context)