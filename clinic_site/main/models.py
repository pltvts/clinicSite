from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()

    def __str__(self):
        return f"Appointment: {self.appointment_time}, Doctor: {self.doctor.full_name}, Patient: {self.patient.full_name}"

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    date = models.CharField('Дата', max_length=50)
    news = models.TextField('Новость', max_length=1000)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'