# Applied Python HW 2

Telegram-бот для расчёта нормы воды, калорий и трекинга активности

Построен на базе библиотеки python-telegram-bot. 
В качестве бд используется postgres.

> Бота можно найти по имени @applied_python_hw_2_bot

## Функционал

Опишите основные функции вашего проекта. Например:

- **Регистрация профиля**: Пользователь может создать и в любой момент отредактировать свой профиль.
- **Отслеживание питания**: Возможность добавлять и отслеживать потребление пищи.
- **Отслеживание тренировок**: Возможность добавлять и отслеживать физическую активность. Предлагается выбрать тип тренировки из предложенных вариантов. Функционал легко расширяемый.
- **Графики**: Генерация графиков для визуализации данных за последние 7 дней.


```
Вся информация сохраняется в базу данных postgresql.

Бот и БД задеплоены на timeweb.cloud 

Для работы с температурой используется API openweathermap.org.

Для работы с продуктами используется API openfoodfacts
```

С формулами для расчёта нормы воды, калорий и трекинга активности можно ознакомиться в файле
[goals_service.py](https://github.com/dmsezv/applied_python_hw_2/blob/main/app/services/goals_service.py)

> [!IMPORTANT]
> В качестве дополнительного функционала используется кеширование данных об уже полученных продуктах.

## Демонстрация функционала

1. Работа с профилем пользователя. Редактирование и обновление данных.
   
![scrcast](https://github.com/dmsezv/applied_python_hw_2/blob/main/steps/step_1.gif)

2. Работа со статистикой. Добавление продуктов и тренировок. Расчеты.

![scrcast](https://github.com/dmsezv/applied_python_hw_2/blob/main/steps/step_2.gif)

3. Генерация графиков

![scrcast](https://github.com/dmsezv/applied_python_hw_2/blob/main/steps/step_3.gif)


> [!NOTE]
> Проект упакован в docker контейнер и запущен на сервере. База данных так же развернута.
