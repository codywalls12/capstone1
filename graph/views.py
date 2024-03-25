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
            
            data = df['data']

            
            plt.figure(figsize=(10, 6))

            
            plt.subplot(1, 3, 1)
            data.plot(kind='bar')
            plt.title('Bar Chart')

            
            plt.subplot(1, 3, 2)
            data.plot(kind='pie')
            plt.title('Pie Chart')

            
            plt.subplot(1, 3, 3)
            plt.scatter(data.index, data.values)
            plt.title('Scatter Plot')

            
            plot_filename = '/path/to/static/folder/plot.png'
            plt.savefig(plot_filename)

            return render(request, 'graph_result.html', {'plot_filename': plot_filename})

    else:
        form = UploadForm()
    
    return render(request, 'upload_excel.html', {'form': form})


def excel_upload(request):
    print("Entered excel_upload")
    if request.method == 'POST':
        form = ExcelDataForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            try:
                print(next(iter(request.FILES))) # this will print the name of the file
            except StopIteration:
                 print("No file was uploaded!")
            form.save()
            #Check if excel file
            if form.instance.filename().endswith(".xlsx"):
                df = pd.read_excel("graph/static/graph/" + form.instance.filename())

            #Check if csv file
            elif form.instance.filename().endswith(".csv"):
                df = pd.read_csv("graph/static/graph/" + form.instance.filename())

            graph_x_axis = df.iloc[:, form.instance.x_values]
            graph_y_axis = df.iloc[:, form.instance.y_values]

            print(graph_x_axis, graph_y_axis)


            p = figure(x_range=graph_x_axis, height=350, title="Test", x_axis_label="X Values", y_axis_label='Y Values', tools="pan,box_zoom,wheel_zoom,reset,save", toolbar_location="right")
            p.vbar(x=graph_x_axis, top=graph_y_axis, width=0.9)
            p.xaxis.major_label_orientation = "vertical"
            script, div = components(p)


            # Create file path to save .wav file to static folder
            save_path = "graph/static/graph"
            file_name = "graph_audio.wav"
            graph_audio = os.path.join(save_path, file_name)

            # Create an instance of the ToneGenerator
            tone = ToneGenerator()

            # Create a list to hold the values for frequencies
            frequencies = []

            # This for loop goes throught the range of the y values entered by the user and adds them to the frequencies list
            for i in range(len(graph_y_axis)):
                frequencies.append(graph_y_axis[i])
            mellody = []
            for i in range(len(frequencies)):
                mellody += list(tone.render(0.5, int(frequencies[i]), "sin"))
            
            # Once the mellody list has been created we write it to the proper file as a .wav file
            ToneGenerator.write_to_file(np.array(mellody), graph_audio)




            context = {
                'script': script,
                'div': div,
                'form': form
            }


    else:
        print("request not POST")
        form = UploadForm()
    return render(request, 'graph/graph_creation.html', context)


