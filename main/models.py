from django.db import models

class News_model_total(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images')
    CATEGORIES = (
        ('N', 'Nowosc'),
        ('P', 'Polityka'),
        ('S', 'Sport'),
        ('B', 'Biznes'),
        ('I', 'Inne'),
    )
    category = models.CharField(max_length=1, choices=CATEGORIES ,default="N")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('main.News_model_total', related_name='comments', on_delete=models.CASCADE, null=True)   #CIEKAWE
    autor = models.CharField(max_length=200)
    tekst = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tekst
