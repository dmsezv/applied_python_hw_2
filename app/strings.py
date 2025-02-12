# flake8: noqa

# Profile strings
WELCOME_TEXT = "Здравствуйте!\nЯ помогу Вам рассчитать дневные нормы воды и калорий, а также отследить тренировки и питание."
HELLO_TEXT = "Привет, {username}!"

WEIGHT_TEXT = "Введите ваш вес (в кг):"
WEIGHT_TEXT_SAVED = "Вес сохранен: {weight}\nВведите ваш рост (в см):"
WEIGHT_ZERO_ERROR = "Вес должен быть больше 0"
WEIGHT_TYPE_ERROR = "Пожалуйста, введите числовое значение веса"

HEIGHT_TEXT = "Введите ваш рост (в см):"
HEIGHT_TEXT_SAVED = "Рост сохранен: {height}\nВведите ваш возраст:"
HEIGHT_ZERO_ERROR = "Рост должен быть больше 0"
HEIGHT_TYPE_ERROR = "Пожалуйста, введите числовое значение роста"

AGE_TEXT = "Введите ваш возраст:"
AGE_TEXT_SAVED = "Возраст сохранен: {age}\nВведите ваш уровень активности (минуты в день):"
AGE_ZERO_ERROR = "Возраст должен быть больше 0"
AGE_TYPE_ERROR = "Пожалуйста, введите числовое значение возраста"

ACTIVITY_TEXT = "Введите уровень активности (минуты в день):"
ACTIVITY_TEXT_SAVED = "Уровень активности сохранен: {activity}\nВведите ваш город:"
ACTIVITY_ZERO_ERROR = "Уровень активности должен быть больше 0"
ACTIVITY_TYPE_ERROR = "Пожалуйста, введите числовое значение уровня активности"

CITY_TEXT = "Введите ваш город:"
CITY_TEXT_SAVED = "Город сохранен: {city}. Температура сегодня: {temperature}°C\nВыберите ваш пол:"
CITY_TYPE_ERROR = "Пожалуйста, введите название города"
CITY_ERROR = "Не удалось получить температуру в городе. Пожалуйста, попробуйте еще раз."
CITY_WEATHER_IN_PROGRESS = "Получение температуры в {city}..."
CITY_WEATHER_SUCCESS = "Температура в {city} сегодня: {temperature}°C"

GENDER_TEXT = "Выберите ваш пол:"
GENDER_TEXT_SAVED = "Пол сохранен: {gender}"
GENDER_TYPE_ERROR = "Пожалуйста, выберите мужской или женский пол"
GENDER_MAN = "Мужской"
GENDER_WOMAN = "Женский"

PROFILE_UPDATED = """Отлично! Я сохранил Ваши данные и рассчитал суточные цели:\nКалории: {calories_goal} ккал\nВода: {water_goal} мл.
\nОбратите внимание, что на цели влияет текущая температура в городе (Сегодня в {city} {temperature}°C).\nНажимайте кнопку "Обновить цели", чтобы пересчитать их с учетом текущей температуры."""
PROFILE_ERROR = "Произошла ошибка при сохранении профиля. Пожалуйста, попробуйте еще раз."
PROFILE_NOT_FOUND = "Профиль не найден. Пожалуйста, установите профиль с помощью команды /set_profile"
PROFILE_DELETED = "Профиль удален."
PROFILE_DELETE_ERROR = "Произошла ошибка при удалении профиля. Пожалуйста, попробуйте еще раз."
PROFILE_SAVING_IN_PROGRESS = "Сохранение профиля и расчет целей..."
PROFILE_VIEW = """Ваш профиль:
\nВес: {weight} кг
\nРост: {height} см
\nВозраст: {age}
\nПол: {gender}
\nАктивность: {activity} минут в день
\nГород: {city}
\nЦель калорий: {calories_goal} ккал
\nЦель воды: {water_goal} мл"""

UPDATE_GOALS_TEXT = "Обновление дневной нормы воды и калорий..."
UPDATE_GOALS_SUCCESS = "Цели успешно обновлены.\nДневная норма воды: {water_goal} мл\nДневная норма калорий: {calories_goal} ккал"
UPDATE_GOALS_ERROR = "Произошла ошибка при обновлении целей. Пожалуйста, попробуйте еще раз."

# Log strings
LOG_WATER_SUCCESS = "Записано: {amount} мл воды. Осталось: ... мл."
LOG_WATER_ERROR = "Пожалуйста, укажите количество воды в миллилитрах."
LOG_FOOD_PROMPT = "🍌 {product_name} — {calories_per_100g} ккал на 100 г. Сколько грамм вы съели?"
LOG_FOOD_ERROR = "Пожалуйста, укажите название продукта."
LOG_WORKOUT_SUCCESS = (
    "🏃‍♂️ {workout_type} {duration} минут — {calories_burned} ккал. "
    "Дополнительно: выпейте {water_needed} мл воды."
)
LOG_WORKOUT_ERROR = "Пожалуйста, укажите тип тренировки и время в минутах."
CHECK_PROGRESS = (
    "📊 Прогресс за сегодня ({date}):\n"
    "Вода:\n"
    "- Выпито: {water} мл из {water_goal} мл.\n"
    "- Осталось: {water_left} мл.\n\n"
    "Калории:\n"
    "- Потреблено: {food} ккал из {calories_goal} ккал.\n"
    "- Сожжено: {workout} ккал.\n"
    "- Баланс: {food_left} ккал."
)
CHECK_PROGRESS_ERROR = "Не удалось получить статистику за сегодня. Пожалуйста, попробуйте еще раз."
# Button strings
CREATE_PROFILE_BUTTON_LABEL = "Создать профиль"
BACK_BUTTON_LABEL = "Назад"
CANCEL_BUTTON_LABEL = "Отмена"
SHOW_PROFILE_BUTTON_LABEL = "Посмотреть профиль"
EDIT_PROFILE_BUTTON_LABEL = "Редактировать профиль"
DELETE_PROFILE_BUTTON_LABEL = "Удалить профиль"
SKIP_BUTTON_LABEL = "Пропустить"
UPDATE_GOALS_BUTTON_LABEL = "Обновить цели"

LOG_WATER_BUTTON_LABEL = "Попил"
LOG_FOOD_BUTTON_LABEL = "Поел"
LOG_WORKOUT_BUTTON_LABEL = "Потренировался"
DAILY_STATISTICS_BUTTON_LABEL = "Дневная статистика"
