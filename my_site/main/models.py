from django.db import models

# Create your models here.
class Table(models.Model):
    title=models.CharField("Название", max_length=50)
    text=models.TextField("Текст")
    
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name="Фильм"
        verbose_name_plural="Фильм"