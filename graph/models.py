from django.db import models
from django.urls import reverse

# Create your models here.
class GraphModel(models.Model):
    graph_name  = models.CharField(max_length=20, help_text='Enter graph name')
    Xlabel = models.CharField(max_length=20, help_text='Enter x-axis label')
    Ylabel = models.CharField(max_length=20, help_text='Enter y-axis label')
    X_value = models.AutoField()
    Y_value = models.AutoField()

    def __str__(self):
        return self.graph_name
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    
