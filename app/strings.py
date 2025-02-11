# flake8: noqa
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
CITY_TEXT_SAVED = "Город сохранен: {city}\nВыберите ваш пол:"
CITY_TYPE_ERROR = "Пожалуйста, введите название города"

GENDER_TEXT = "Выберите ваш пол:"
GENDER_TEXT_SAVED = "Пол сохранен: {gender}\nВведите вашу цель калорий (или нажмите кнопку пропустить для автоматического расчета):"
GENDER_TYPE_ERROR = "Пожалуйста, выберите мужской или женский пол"
GENDER_MAN = "Мужской"
GENDER_WOMAN = "Женский"

CALORIES_TEXT = "Введите вашу цель калорий (или нажмите кнопку пропустить для автоматического расчета):"
CALORIES_TEXT_SAVED = "Цель калорий сохранена: {calories}\nВведите ваш пол:"
CALORIES_ZERO_ERROR = "Цель калорий должна быть больше 0"
CALORIES_TYPE_ERROR = "Пожалуйста, введите числовое значение цели калорий или оставьте пустым для автоматического расчета"

PROFILE_UPDATED = "Отлично! Ваш профиль обновлен!"
PROFILE_ERROR = "Произошла ошибка при сохранении профиля. Пожалуйста, попробуйте еще раз."
CANCEL_MESSAGE = "Операция отменена."
BACK_NOT_POSSIBLE = "Вы не можете вернуться назад."
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
    "📊 Прогресс:\n"
    "Вода:\n"
    "- Выпито: {water_consumed} мл из {water_goal} мл.\n"
    "- Осталось: {water_goal - water_consumed} мл.\n\n"
    "Калории:\n"
    "- Потреблено: {calories_consumed} ккал из {calories_goal} ккал.\n"
    "- Сожжено: {calories_burned} ккал.\n"
    "- Баланс: {balance} ккал."
)

# Button strings
START_BUTTON = "Создать профиль"
BACK_BUTTON = "Назад"
CANCEL_BUTTON = "Отмена"
