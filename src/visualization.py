from pathlib import Path
import plotly.express as px
import pandas as pd

def save_interactive_charts(dept_table, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    fig = px.bar(dept_table, x="departamento", y="discriminacion_pct",
        title="Percepción de discriminación por departamento",
        labels={"departamento":"Departamento","discriminacion_pct":"Porcentaje ponderado"})
    fig.write_html(out/"01_discriminacion_departamento.html")
    fig = px.bar(dept_table, x="departamento", y="victimizacion_pct",
        title="Victimización por departamento",
        labels={"departamento":"Departamento","victimizacion_pct":"Porcentaje ponderado"})
    fig.write_html(out/"02_victimizacion_departamento.html")
