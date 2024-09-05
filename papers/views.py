import requests
from django.shortcuts import render, redirect
from .models import ResearchPaper
from django.views.decorators.http import require_POST

def search_papers(request):
    query = request.GET.get('q', '') 
    papers = []
    no_results = False 

    if query:
        url = f"https://api.crossref.org/works?query={query}&rows=10"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('message', {}).get('items', [])
            
            if not items:
                no_results = True
            
            for item in items:
                paper = {
                    'title': item.get('title', ['No Title'])[0],
                    'authors': ', '.join([author.get('given', '') + ' ' + author.get('family', '') for author in item.get('author', [])]),
                    'year': item.get('published-print', {}).get('date-parts', [[None]])[0][0],
                    'citations': item.get('is-referenced-by-count', 0)
                }
                papers.append(paper)
    
    return render(request, 'papers/search.html', {'papers': papers, 'query': query, 'no_results': no_results})

def saved_papers(request):
    saved_papers = ResearchPaper.objects.all()
    return render(request, 'papers/saved.html', {'saved_papers': saved_papers})

@require_POST
def save_paper(request):
    title = request.POST.get('title')
    authors = request.POST.get('authors')
    year = request.POST.get('year')
    citations = request.POST.get('citations')

    if year:
        try:
            year = int(year)
        except ValueError:
            year = None
    else:
        year = None

    ResearchPaper.objects.update_or_create(
        title=title,
        defaults={
            'authors': authors,
            'year': year,
            'citations': citations
        }
    )

    return redirect('saved_papers')


def remove_paper(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ResearchPaper.objects.filter(title=title).delete()
    return redirect('saved_papers')

