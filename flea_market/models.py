from django.db import models
from django.contrib.postgres.fields import JSONField


class TestUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SectionProduction(models.Model):
    CATEGORY = 'CAT'
    SUBCATEGORY = 'SUBCAT'
    TYPE_CATEGORY = (
        (CATEGORY, 'Категория'),
        (SUBCATEGORY, 'Подкатегория'),
    )
    number_section = models.PositiveSmallIntegerField(default=0)
    type_category = models.CharField(max_length=10, choices=TYPE_CATEGORY, default=CATEGORY)
    name = models.CharField(max_length=150)
    category = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type_category + ', ' + self.name + ', num: ' + str(self.number_section) + ' Parent cat: ' + str(self.category)


class Ad(models.Model):
    user = models.ForeignKey(TestUser, on_delete=models.CASCADE)
    category = models.ForeignKey(SectionProduction, on_delete=models.CASCADE)
    name_product = models.CharField(max_length=250)
    production_year = models.DateField(auto_now_add=True)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_product


class Comment(models.Model):
    text_comment = models.TextField()
    user = models.ForeignKey(TestUser, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_comment

