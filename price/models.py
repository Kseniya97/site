from  django.db import models
class Woman(models.Model):
    ycluga=models.CharField(max_length=256, verbose_name='Услуга')
    price=models.CharField(max_length=30,verbose_name='Цена')
    dlinna=models.ForeignKey('Dlinna', blank=True,
null=True, verbose_name='Длинна волос')
    def __str__(self):
        return self.ycluga
    class Meta:
        verbose_name_plural='Женский зал'
class Dlinna(models.Model):
        verbose_name = 'Длинна волос'
        verbose_name_plural = 'Длинна волос'
        Name = models.CharField(max_length=30)
        def __str__(self):
            return '%s (%s)' % (self.Name, self.id)
class Man(models.Model):
    ycluga = models.CharField(max_length=256, verbose_name='Услуга')
    price = models.CharField(max_length=30, verbose_name='Цена')
    dlinna = models.ForeignKey('Dlinna', blank=True,null=True, verbose_name='Длинна волос')
    def __str__(self):
        return '%s (%s)' % (self.ycluga, self.id)
    class Meta:
        verbose_name_plural='Мужской зал'
class Nails(models.Model):
    ycluga = models.CharField(max_length=256, verbose_name='Услуга')
    price = models.CharField(max_length=30, verbose_name='Цена')
    type = models.ForeignKey('Nails_type', blank=True,
null=True, verbose_name='Вид')
    def __str__(self):
        return self.ycluga
    class Meta:
        verbose_name_plural='Ногтевой сервис'
class Nails_type(models.Model):
        verbose_name = 'Вид'
        verbose_name_plural = 'Вид'
        Name = models.CharField(max_length=30)
        def __str__(self):
            return '%s (%s)' % (self.Name, self.id)
class Other(models.Model):
    ycluga = models.CharField(max_length=256, verbose_name='Услуга')
    price = models.CharField(max_length=30, verbose_name='Цена')
    type = models.ForeignKey('Other_type', blank=True,
null=True, verbose_name='Вид')
    def __str__(self):
        return self.ycluga
    class Meta:
        verbose_name_plural='Шугарниг/Наращивание ресниц'
class Other_type(models.Model):
        verbose_name = 'Вид'
        verbose_name_plural = 'Вид'
        Name = models.CharField(max_length=30)
        def __str__(self):
            return '%s (%s)' % (self.Name, self.id)







