from django.db import models

# Create your models here.

# class AbstractTable(models.Model):
#    title = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(to='Category', on_delete = models.CASCADE) # с помощью кавычек как ссылка бедт! и будет ссылаться! гно только если в этом файле! а если в дугом файле то путь<!
    

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

