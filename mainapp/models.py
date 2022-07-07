from django.db import models

class Dept(models.Model):
    name = models.CharField(verbose_name="название управления", max_length=200)
    chief = models.CharField(verbose_name="ФИО начальника управления", max_length=200)
    description = models.CharField(verbose_name="Краткое описание", max_length=200)

    def __str__(self):
        return self.name

class Workshop(models.Model):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    chief = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Obj(models.Model):
    SERVICE_WORKSHOP_CHOICES = [
        ('aw1', 'цех автоматизации №1'),
        ('aw2', 'цех автоматизации №2'),
        ('aw3', 'цех автоматизации №3'),
        ('aw4', 'цех автоматизации №4'),
        ('mss', 'участок метрологического обеспечения'),
        ('acs', 'участок АСУТП'),
    ]

    OILFIELD_LIST = [
        ('sov1', 'Советское-1'),
        ('sov2', 'Советское-2'),
        ('nizh', 'Нижневартовское'),
        ('polu', 'Полуденное'),
        ('katy', 'Катыльгинское'),
        ('perv', 'Первомайское'),
        ('krap', 'Крапивинское'),
        ('dvur', 'Двуреченское'),
        ('igol', 'Игольское'),

    ]

    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    oilfield = models.CharField(max_length=4, choices=OILFIELD_LIST)
    service_division = models.CharField(max_length=3, choices=SERVICE_WORKSHOP_CHOICES)
    description = models.CharField(max_length=200)

class ProcessPlant(models.Model):

    obj = models.ForeignKey(Obj, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    status = models.BooleanField(default=True, verbose_name='Состояние эксплуатации')
    type = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=200)


class Device(models.Model):
    obj = models.ForeignKey(Obj, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    chief = models.CharField(max_length=200)
    description = models.CharField(max_length=200)