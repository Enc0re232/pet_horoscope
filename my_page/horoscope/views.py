from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


zodiac_dict = {
    'aries': ' Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}


def index(request):
    zodiacs = list(zodiac_dict)
    # f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': {},
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sing_zodiac(request, sign_zodiac: str):
    global zodiac_dict
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'sign_name': description.split()[0],
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sing_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
