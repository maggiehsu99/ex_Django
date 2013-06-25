from django.db import models

class Supply(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    phone=models.IntegerField()


    def __unicode__(self):
        return u'%s %s' % (self.name, self.email)

    class Meta:
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    size = models.CharField(max_length=30)
    detail=models.CharField(max_length=200)
    supply = models.ManyToManyField(Supply)
    buy_date=models.DateField()

    def __unicode__(self):
        return u'%s %s %s' % (self.name, self.detail,self.supply)
    class Meta:
        ordering = ['name']


