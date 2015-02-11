#coding: utf-8

from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(verbose_name=_("first_name"), max_length=20)  #można pominąć "v_n=", bo zawsze na 1.
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return _("{first_name} {last_name}").format(first_name=self.first_name, last_name=self.last_name)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = _('author')  #lepiej dopełniacz niż mianownik
        verbose_name_plural = _('authors')

class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return  self.name

class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Rękopis
    """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)
    #author = models.ForeignKey(Author)

    def __str__(self):
        return self.title

class BookEdition(models.Model):
    """
    Wydanie
    """
    book = models.ForeignKey(Book)
    isbn = models.CharField(max_length=17)
    date = models.DateField()
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(book=self.book, publisher=self.publisher)

COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard')    #wartość w bazie, wartość wyświetlana
)

class BookItem(models.Model):
    """
    Egzemplarz
    """
    book = models.ForeignKey(BookEdition)
    catalog_number = models.CharField(max_length=30)
    cover_type = models.CharField(choices=COVER_TYPES, max_length=4)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition, cover=self.get_cover_type_display())