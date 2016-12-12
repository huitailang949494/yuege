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
        affiliations = set(affiliations)
        paper_ids2 = set([])
        cnt = 0
        for author in authors:
            affiliations = Paper_Author_Affiliations.objects.filter(author=author)
            paper_ids = []
            for affiliation in affiliations:
                if affiliation.paper.paper_id not in paper_ids:
                    paper_ids.append(affiliation.paper.paper_id)
            if cnt == 0:
                paper_ids2 = paper_ids
                cnt = cnt + 1
            else:
                paper_ids2 = set(paper_ids) & set(paper_ids2)
        print paper_ids2
        paper_ids = list(paper_ids2)
        papers = Paper.objects.none()
        for paperid in paper_ids:
            papers = papers | Paper.objects.filter(paper_id=paperid)
    else:
        authors = Author.objects.all()
    return render(request, 'author.html', locals())
