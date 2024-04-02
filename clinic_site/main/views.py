from datetime import timedelta, datetime
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Doctor, Patient, Appointment, News


def index(request):
    news = News.objects.order_by('-id')[:10]
    return render(request, 'main/index.html', {'title': 'Главная страница и новости', 'news': news})


def about(request):
    return render(request, 'main/about.html')


def doctors(request):
    doctors_list = Doctor.objects.all()
    return render(request, 'main/doctors.html', {'title': 'Наши специалисты', 'врачи': doctors_list})


@login_required
def appoint(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        doc_name = request.POST.get('doc_name')
        appointment_time = request.POST.get('appointment_time')

        # Проверяем, связан ли текущий пользователь с пациентом
        try:
            patient = request.user.patient
        except Patient.DoesNotExist:
            messages.error(request, 'Вы должны быть зарегистрированы как пациент для записи на прием!')
            return redirect('appoint')

        # Получаем объект врача
        try:
            doctor = Doctor.objects.get(full_name=doc_name)
        except Doctor.DoesNotExist:
            messages.error(request, 'Выбранный врач не найден!')
            return redirect('appoint')

        # Создаем запись на прием
        appointment = Appointment(doctor=doctor, patient=patient, appointment_time=appointment_time)
        appointment.save()

        messages.success(request, 'Вы успешно записаны на прием!')

        return redirect('appoint')

    # Если метод запроса не POST, просто отображаем форму

    # Создаем список времен приема с промежутком в полчаса
    start_time = datetime.strptime('08:00', '%H:%M')
    end_time = datetime.strptime('18:00', '%H:%M')
    delta = timedelta(minutes=30)
    appointment_times = []
    current_time = start_time
    while current_time < end_time:
        appointment_times.append(current_time.strftime('%H:%M'))
        current_time += delta

    # Получаем список всех врачей
    doctors = Doctor.objects.all()

    return render(request, 'main/appoint.html', {'doctors': doctors, 'appointment_times': appointment_times})

def services(request):
    return render(request, 'main/services.html')
