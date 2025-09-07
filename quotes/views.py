from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
import random
from .models import Quote


def index(request):
    # Получаем все цитаты
    quotes = list(Quote.objects.all())

    # Если нет цитат — показываем пустую страницу
    if not quotes:
        return render(request, 'quotes/index.html', {'quote': None})

    # Выбираем случайную с учётом веса
    quote = random.choices(quotes, weights=[q.weight for q in quotes])[0]

    # Увеличиваем счётчик просмотров
    quote.view_count += 1
    quote.save()

    return render(request, 'quotes/index.html', {'quote': quote})


def like(request, quote_id):
    try:
        quote = Quote.objects.get(id=quote_id)
        quote.likes += 1
        quote.save()
    except Quote.DoesNotExist:
        pass
    return redirect('quotes:index')


def dislike(request, quote_id):
    try:
        quote = Quote.objects.get(id=quote_id)
        quote.dislikes += 1
        quote.save()
    except Quote.DoesNotExist:
        pass
    return redirect('quotes:index')


def top_quotes(request):
    quotes = Quote.objects.all().order_by('-likes')[:10]
    return render(request, 'quotes/top.html', {'quotes': quotes})
