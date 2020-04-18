# from django.db import models
#
#
# class TestUser(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#
# class Ad(models.Model):
#     user = models.ForeignKey(TestUser, on_delete=models.CASCADE)
#     name_product = models.CharField(max_length=250)
#     category = models.CharField(max_length=100)
#     production_year = models.DateField(auto_now_add=True)
#     description = models.TextField()
#     publication_date = models.DateTimeField(auto_now_add=True)
#     change_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name_product
#
#
# class Comment(models.Model):
#     text_comment = models.TextField()
#     user = models.ForeignKey(TestUser, on_delete=models.CASCADE)
#     ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.text_comment
