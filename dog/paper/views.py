from django.shortcuts import render
from paper.models import Paper, Author, Paper_Author_Affiliations


def paper_list(request):
    if request.GET.get('id'):
        papers = Paper.objects.filter(paper_id=request.GET.get('id'))
    else:
        papers = Paper.objects.all()
    return render(request, 'paper.html', locals())


def author_list(request):
    is_search = False
    if request.GET.get('id'):
        authors = Author.objects.filter(author_id=request.GET.get('id'))
        is_search = True
        if request.GET.get('id2'):
            authors = authors | Author.objects.filter(author_id=request.GET.get('id2'))
        affiliations = Paper_Author_Affiliations.objects.all()
        for author in authors:
            affiliations = affiliations & Paper_Author_Affiliations.objects.filter(author_id=author)
        paper_ids = []
        for affiliation in affiliations:
            if affiliation.paper_id not in paper_ids:
                paper_ids.append(affiliation.paper_id)
        print paper_ids
        papers = Paper.objects.none()
        for paperid in paper_ids:
            papers = papers | Paper.objects.filter(id=paperid)
    else:
        authors = Author.objects.all()
    return render(request, 'author.html', locals())
