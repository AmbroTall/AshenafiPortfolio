from django.shortcuts import render
from django.http import HttpResponse
import os

file_name = "AmbroseNdone.pdf"
def download_pdf(request):
    # Path to the PDF file you want to serve for download
    pdf_file_path = f"/home/ambrose/PycharmProjects/portfolioAsh/portfolio/static/static/{file_name}"

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    else:
        return HttpResponse("PDF file not found.", status=404)


def display_pdf(request):
    # Path to the PDF file you want to display
    pdf_file_path = f"/home/ambrose/PycharmProjects/portfolioAsh/portfolio/static/static/{file_name}"

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_content = pdf_file.read()
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = f'inline; filename="{file_name}"'
            return response
    else:
        return HttpResponse("PDF file not found.", status=404)

# Create your views here.
def home_page(request):
    return render(request, 'app/home.html')
