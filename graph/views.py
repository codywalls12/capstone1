import numpy as np
import os.path
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from bokeh.embed import components
from bokeh.plotting import figure
from graph import ToneGenerator
from graph.ToneGenerator import ToneGenerator
from .forms import ExcelDataForm
from .forms import UploadFileForm

import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from .forms import UploadForm


#test
def excel_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            # Assuming the Excel file contains a column named 'data' for demonstration
            data = df['data']

            # Create graphs
            plt.figure(figsize=(10, 6))

            # Bar graph
            plt.subplot(1, 3, 1)
            data.plot(kind='bar')
            plt.title('Bar Chart')

            # Pie chart
            plt.subplot(1, 3, 2)
            data.plot(kind='pie')
            plt.title('Pie Chart')

            # Scatter plot
            plt.subplot(1, 3, 3)
            plt.scatter(data.index, data.values)
            plt.title('Scatter Plot')

            # Save the plot
            plot_filename = '/path/to/static/folder/plot.png'
            plt.savefig(plot_filename)

            return render(request, 'graph_result.html', {'plot_filename': plot_filename})

    else:
        form = UploadForm()
    
    return render(request, 'upload_excel.html', {'form': form})


def excel_upload_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['myFile']
            with open('path/to/save/file.xlsx', 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return HttpResponseRedirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = ExcelDataForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file, for example, save it to a specific location
            form.save()
            df = pd.read_excel(form)
            print(df)
    else:
        form = ExcelDataForm()
    return render(request, "graph/index.html", {'form': form})

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

    #if not x_values or not y_values:
       # return HttpResponse("Error: x values or y values are missing")

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

def excel_upload(request):
    print("Entered excel_upload")
    if request.method == 'POST':
        print("Entered request.method==post")
        form = ExcelDataForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            try:
                print(next(iter(request.FILES))) # this will print the name of the file
            except StopIteration:
                 print("No file was uploaded!")
            form.save()
            print(form.instance.filename())
            df = pd.read_excel("graph/static/graph/" + form.instance.filename())
            first_column = df.iloc[:, 1]
            print(first_column)
    else:
        print("request not POST")
        form = UploadForm()
    return render(request, 'graph/graph_creation.html', {'form': form})


