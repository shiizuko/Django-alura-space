from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# ORM -- tradução entre o banco de dados e o python puro

class Photography(models.Model):
    CATEGORY_OPTIONS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]
    # Colunas
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150,null=False, blank=False)
    category = models.CharField(max_length=100,  choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=True)
    date_picture = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
        to = User,
        on_delete=models.SET_NULL,
        null = True,
        blank = False,
        related_name= "user",
        )

# Boa prática
def __str__(self):
    return self.name