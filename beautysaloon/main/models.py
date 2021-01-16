from django.db import models

from django.contrib.postgres.validators import (MinValueValidator, MaxValueValidator)


class Status(models.Model):
    status_name = models.CharField('Статус', max_length=80, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.status_name


class Services(models.Model):
    service = models.CharField('Типы услуг', max_length=80, unique=True, default='')

    class Meta:
        verbose_name = "Тип услуги"
        verbose_name_plural = "Тип услуги"

    def __str__(self):
        return self.service


class Visits(models.Model):
    visit_number = models.IntegerField('Номер визита', validators=[MinValueValidator(0)])
    service_name = models.CharField('услуга', max_length=70)
    fio_client = models.CharField('ФИО клиента', max_length=70)
    fio_staff = models.CharField('ФИО сотрудника', max_length=70)
    price = models.IntegerField('Цена', validators=[MinValueValidator(1)], default=1)

    class Meta:
        verbose_name = "Визиты"
        verbose_name_plural = "Визиты"

    def __str__(self):
        return self.service_name


class Client(models.Model):
    clientcode = models.IntegerField('Код клиента', validators=[MinValueValidator(1), MaxValueValidator(9999999)])
    clientname = models.CharField('ФИО', max_length=250)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return str(self.clientcode)


class Products(models.Model):
    title = models.CharField('Название', max_length=60)
    description = models.TextField('Описание товара', blank=True)
    price = models.IntegerField('Цена, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title


class Sale(models.Model):
    products = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продукт'
    )
    salecode = models.IntegerField('Код услуги', validators=[MinValueValidator(1), MaxValueValidator(9999999)],
                                   unique=True)
    salesumm = models.IntegerField('Cтоимость, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return str(self.salecode)


class Post(models.Model):
    postcode = models.IntegerField('Код должности', validators=[MinValueValidator(1), MaxValueValidator(9999)])
    postname = models.CharField('Название должности', max_length=250)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.postname


class Salerman(models.Model):
    salercode = models.IntegerField('Код работника', validators=[MinValueValidator(1), MaxValueValidator(9999999)])
    salername = models.CharField('ФИО', max_length=250)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Должность'
    )
    cash = models.IntegerField('Заработная плата, руб.', validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"

    def __str__(self):
        return self.salername


class SaleCheck(models.Model):
    salerman = models.ForeignKey(
        Salerman,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продавец'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Клиент'
    )
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Продажа'
    )
    salecheckcode = models.IntegerField('Код чека', validators=[MinValueValidator(1), MaxValueValidator(9999999)],
                                        unique=True)
    salechecksumm = models.IntegerField('Сумма чека, руб.',
                                        validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"

    def __str__(self):
        return str(self.salecheckcode)

class Discount(models.Model):
    discountcode = models.IntegerField('Код акции', validators=[MinValueValidator(1), MaxValueValidator(9999999)],
                                        unique=True)
    discountname = models.CharField('Название акции', max_length=250)
    description = models.TextField('Описание акции', blank=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return str(self.discountcode)
