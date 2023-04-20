from django.db import models

# ORM -- tradução entre o banco de dados e o python puro

class Photography(models.Model):
    # Colunas
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.CharField(max_length=100,null=False, blank=False)

# Boa prática
def __str__(self):
    return f"Photography [name={self.name}]"