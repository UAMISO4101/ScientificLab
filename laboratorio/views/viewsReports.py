from django.shortcuts import render


def progress(request):
    return render(request, 'laboratorio/Reporte/ReportProgressByProject.html')

def trazabilidad(request):
    return render(request, 'laboratorio/Reporte/ReporteTrazabilidad.html')