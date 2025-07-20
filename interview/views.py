from django.shortcuts import render
from .utils import extract_text_from_pdf
from .voice import conduct_interview


def index(request):
    if request.method == 'POST' and request.FILES.get('resume'):
        pdf_file = request.FILES['resume']
        
        if not pdf_file.name.endswith('.pdf'):
            return render(request, 'interview/index.html', {'error': 'Please upload a valid PDF file.'})
        
        try:
            resume_text = extract_text_from_pdf(pdf_file)
            conduct_interview(resume_text)
            return render(request, 'interview/result.html', {'msg': 'Interview Complete'})
        except Exception as e:
            return render(request, 'interview/index.html', {'error': f"Error: {str(e)}"})

    return render(request, 'interview/index.html')
