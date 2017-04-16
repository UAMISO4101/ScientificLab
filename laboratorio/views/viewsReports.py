from django.shortcuts import render


def reports(request):
    return render(request, 'laboratorio/Reporte/ReportProgressByProject.html')