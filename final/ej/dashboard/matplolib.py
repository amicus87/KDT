from django.shortcuts import render
from .models import hospital
import pandas as pd
import plotly.express as px


def index(request):
    hospitals = hospital.objects.all()
    df = pd.DataFrame(list(hospitals.values()))
    df_type = df.groupby(['place', 'type_short']).size().reset_index(name='count')
    fig = px.bar(df_type, x='place', y='count', color='type_short', title='Hospital Data')
    graph_json = fig.to_json()
    context = {
        'dashboard_hospital': hospitals,
        'graph_json': graph_json  # Pass the chart data to the template
    }
    return render(request, 'hospital/index.html', context)


