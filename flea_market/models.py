from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfileImg(models.Model):
    photo = models.ImageField(upload_to='user')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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


class Location(models.Model):
    # check on correct name
    REGION = 'REGION'
    CITY = 'CITY'
    name = models.CharField(max_length=25)
    type_region = models.CharField(max_length=6, default=REGION)
    number_region = models.PositiveSmallIntegerField(null=True)
    region = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "name: {}, type region: {}, number region: {}, region object: {} |*|"\
            .format(self.name, self.type_region, self.number_region, self.region)


class Ad(models.Model):
    SALE = 'SALE'
    BUY = 'BUY'
    EXCHANGE = 'EXCHANGE'
    SERVICE = 'SERVICE'
    RENT = 'RENT'
    CLOSED = 'CLOSED'
    TYPE_DEAL = (
        (SALE, 'Продам'),
        (BUY, 'Куплю'),
        (EXCHANGE, 'Обменяю'),
        (SERVICE, 'Услуга'),
        (RENT, 'Оренда'),
        (CLOSED, 'Закрыто'),
    )
    type_deal = models.CharField(max_length=8, choices=TYPE_DEAL, default=SALE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(SectionProduction, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #check on correct name
    publication_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    upped_date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.name_product


class AdImage(models.Model):
    photo = models.ImageField(upload_to='ad')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class CommonInfo(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class Bookmark(CommonInfo):
    pass


class Comment(CommonInfo):
    text_comment = models.TextField()

    def __str__(self):
        return self.text_comment


class CommentImage(models.Model):
    photo = models.ImageField(upload_to='comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Complaint(CommonInfo):
    ILLEGAL = 'ILLEGAL'
    AD = 'AD'
    NOT_THAT = 'NOT THAT'
    OTHER = 'OTHER'
    CHOICE_COMPLAINT = (
        (ILLEGAL, 'Сообщение содержит ссылки на незаконные или пиратские программы.'),
        (AD, 'Сообщение имеет единственной целью рекламу сайтов, программ или других продуктов, товаров, услуг и пр.'),
        (NOT_THAT, 'Сообщение не относится к обсуждаемой теме.'),
        (OTHER, 'Причина обжалования не относится ни к одной из перечисленных, используйте поле дополнительной информации.'),
    )
    cause = models.CharField(max_length=8, choices=CHOICE_COMPLAINT, default=ILLEGAL)
    text_complaint = models.TextField()
