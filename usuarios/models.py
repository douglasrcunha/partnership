from django.db import models

# Create your models here.from django.db import models
DOC_CHOICES = (
    ('a', 'ABD'),
    ('c', 'CAU'),
    ('r', 'CREA')
)
 
# Create your models here.
class Dashboard(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    senha = models.CharField(max_length=50)
    data_nasc = models.DateField(blank=True, null=True)
    associacao = models.CharField(max_length=1, choices=DOC_CHOICES)
    resgistro = models.IntegerField(max_length=12, null=True)