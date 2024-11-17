from django.db import models

# Create your models here.
#Category	Age	Sex	ALB	ALP	ALT	AST	BIL	CHE	CHOL	CREA	GGT	PROT
class Heptities(models.Model):
    Category=models.CharField(max_length=90)
    Age=models.IntegerField()
    Sex=models.CharField(max_length=500)
    ALB=models.IntegerField()
    ALP=models.IntegerField()
    ALT=models.IntegerField()
    AST=models.IntegerField()
    BIL=models.IntegerField()
    CHE=models.IntegerField()
    CHOL=models.IntegerField()
    CREA=models.IntegerField()
    GGT=models.IntegerField()
    PROT=models.IntegerField()




