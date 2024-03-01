import numpy as np
import os.path
from django.shortcuts import render
from django.http import HttpResponse
from bokeh.embed import components
from bokeh.plotting import figure
from graph import ToneGenerator
from graph.ToneGenerator import ToneGenerator


def index(request):
    context = {}
    return render(request, "graph/index.html", context)

def graph_creation(request):
    graph_name = request.POST.get('graph_name')
    x_values = request.POST.getlist('x_values[]')
    y_values = request.POST.getlist('y_values[]')



    # Create file path to save .wav file to static folder
    save_path = "graph/static/graph"
    file_name = "graph_audio.wav"
    graph_audio = os.path.join(save_path, file_name)


    # Create an instance of the ToneGenerator
    tone = ToneGenerator()

    # Create a list to hold the values for frequencies
    frequencies = []

    # This for loop goes throught the range of the y values entered by the user and adds them to the frequencies list
    for i in range(len(y_values)):
        frequencies.append(y_values[i])
    mellody = []
    for i in range(len(frequencies)):
        mellody += list(tone.render(0.5, int(frequencies[i]), "sin"))
    
    # Once the mellody list has been created we write it to the proper file as a .wav file
    ToneGenerator.write_to_file(np.array(mellody), graph_audio)

    if not x_values or not y_values:
        return HttpResponse("Error: x values or y values are missing")

    if len(x_values) != len(y_values):
        return HttpResponse("Error: Number of x values and y values do not match")

    p = figure(x_range=x_values, height=350, title=graph_name, x_axis_label='X Values', y_axis_label='Y Values', tools="pan,box_zoom,wheel_zoom,reset,save", toolbar_location="right")
    p.vbar(x=x_values, top=y_values, width=0.9)
    script, div = components(p)

    context = {
        'graph_name': graph_name,
        'script': script,
        'div': div,
    }

    return render(request, "graph/graph_creation.html", context)
