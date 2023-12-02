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
        x_values = request.POST.getlist('x_values[]')
        y_values = request.POST.getlist('y_values[]')

        p = figure(x_range=x_values, height=350, title=graph_name, tools="pan,box_zoom,wheel_zoom,reset,save", toolbar_location="right")
        p.vbar(x=x_values, top=y_values, width=0.9)
        script, div = components(p)

        context = {
            'graph_name': graph_name,
            'script': script,
            'div': div,
        }

        return render(request, "graph/graph_creation.html", context)

    
