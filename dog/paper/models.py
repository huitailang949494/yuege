from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_id = models.CharField(max_length=50)

    def __unicode__(self):
        return self.author_id


class Paper(models.Model):
    paper_id = models.CharField(max_length=50)
    original_title = models.CharField(max_length=50)
    normalized_title = models.CharField(max_length=50)
    publish_year = models.IntegerField()
    publish_date = models.DateTimeField()
    DOI = models.CharField(max_length=50)
    original_venue_name = models.CharField(max_length=50)
    normalized_venue_name = models.CharField(max_length=50)
    jornal_id = models.CharField(max_length=50)
    conference_id = models.CharField(max_length=50)
    paper_rank = models.CharField(max_length=50)

    def __unicode__(self):
        return self.paper_id


class Paper_Author_Affiliations(models.Model):
    paper = models.ForeignKey(Paper)
    author = models.ForeignKey(Author)
    affiliation_id = models.CharField(max_length=50)
    original_affiliation_name = models.CharField(max_length=50)
    normalized_affiliation_name = models.CharField(max_length=50)
    author_sequence_number = models.CharField(max_length=50)

    def __unicode__(self):
        return self.affiliation_id
