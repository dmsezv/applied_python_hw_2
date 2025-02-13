# flake8: noqa

#Commond strings
YES_BUTTON_LABEL = "Да"
NO_BUTTON_LABEL = "Нет"
WHATS_NEXT_TEXT = "Что делаем дальше?"
USER_NOT_FOUND_TEXT = "❌ Пользователь не найден. Пожалуйста, установите профиль с помощью команды /set_profile"
DATE_TEXT = "Дата"

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
CITY_ERROR = "❌ Не удалось получить температуру в городе. Пожалуйста, попробуйте еще раз."
CITY_WEATHER_IN_PROGRESS = "Получение температуры в {city}..."
CITY_WEATHER_SUCCESS = "Температура в {city} сегодня: {temperature}°C"

GENDER_TEXT = "Выберите ваш пол:"
GENDER_TEXT_SAVED = "Пол сохранен: {gender}"
GENDER_TYPE_ERROR = "Пожалуйста, выберите мужской или женский пол"
GENDER_MAN = "Мужской"
GENDER_WOMAN = "Женский"

PROFILE_UPDATED = """✅ Отлично! Я сохранил Ваши данные и рассчитал суточные цели:\nКалории: {calories_goal} ккал\nВода: {water_goal} мл.
\nОбратите внимание, что на цели влияет текущая температура в городе (Сегодня в {city} {temperature}°C).\nНажимайте кнопку "Обновить цели", чтобы пересчитать их с учетом текущей температуры."""
PROFILE_ERROR = "❌ Произошла ошибка при сохранении профиля. Пожалуйста, попробуйте еще раз."
PROFILE_NOT_FOUND = "❌ Профиль не найден. Пожалуйста, установите профиль с помощью команды /set_profile"
PROFILE_DELETED = "✅ Профиль удален."
PROFILE_DELETE_ERROR = "❌ Произошла ошибка при удалении профиля. Пожалуйста, попробуйте еще раз."
PROFILE_SAVING_IN_PROGRESS = "Сохранение профиля и расчет целей..."
PROFILE_VIEW = """Ваш профиль:
\n💪 Вес: {weight} кг
\n📐 Рост: {height} см
\n🪪 Возраст: {age}
\n👫 Пол: {gender}
\n🏃‍♂️ Активность: {activity} минут в день
\n🏙 Город: {city}
\n🥗 Цель калорий: {calories_goal} ккал
\n💧 Цель воды: {water_goal} мл"""

UPDATE_GOALS_TEXT = "Обновление дневной нормы воды и калорий..."
UPDATE_GOALS_SUCCESS = "Цели успешно обновлены.\nДневная норма воды: {water_goal} мл\nДневная норма калорий: {calories_goal} ккал"
UPDATE_GOALS_ERROR = "Произошла ошибка при обновлении целей. Пожалуйста, попробуйте еще раз."

# Log strings
STATISTICS_TEXT = "Выберите что вы хотите посмотреть"

FOOD_GET_TEXT = "Введите название продукта который вы съели:"
FOOD_FOUND_TEXT = "✅ Продукт найден!\n{product_name} — {calories_per_100g} ккал на 100 г.\nДобавляем в статистику?"
FOOD_NOT_FOUND_TEXT = "❌ Не удалось найти продукт. Пожалуйста, попробуйте еще раз."
FOOD_ADD_TEXT = "✅ Продукт добавлен в статистику."
FOOD_NOT_ADDED_TEXT = "❌ Продукт не добавлен в статистику."
FOOD_NOT_ADDED_ERROR_TEXT = "❌ Произошла ошибка при добавлении продукта в статистику. Пожалуйста, попробуйте еще раз."
FOOD_WEIGHT_TEXT = "Сколько грамм вы съели?"
FOOD_ZERO_ERROR = "Количество грамм должно быть больше 0"
FOOD_TYPE_ERROR = "Пожалуйста, введите числовое значение количества грамм"

WORKOUT_GET_TEXT = "Выберите тип тренировки:"
WORKOUT_MINUTES_TEXT = "Сколько минут вы тренировались?"
WORKOUT_ADD_TEXT = "✅ Тренировка учтена в статистике.\n🔥 Сожжено {calories_burned} ккал.\n💦 Не забудьте восполнить воду ({water_needed} мл).\n"
WORKOUT_NOT_ADDED_ERROR_TEXT = "❌ Произошла ошибка при добавлении тренировки в статистику. Пожалуйста, попробуйте еще раз."
WORKOUT_ZERO_ERROR = "Количество минут должно быть больше 0"
WORKOUT_TYPE_ERROR = "Пожалуйста, введите числовое значение количества минут"

WATER_GET_TEXT = "Сколько воды вы выпили?\nВведите количество воды в миллилитрах:"
WATER_ADD_TEXT = "✅ Вода учтена в статистике.\n💦 Выпито: {water_needed} мл.\n"
WATER_NOT_ADDED_ERROR_TEXT = "❌ Произошла ошибка при добавлении воды в статистику. Пожалуйста, попробуйте еще раз."
WATER_ZERO_ERROR = "Количество воды должно быть больше 0"
WATER_TYPE_ERROR = "Пожалуйста, введите числовое значение количества воды"

GRAPHICS_IN_PROGRESS_TEXT = "Подождите, пожалуйста, мне нужно время чтобы сгенерировать график..."
GRAPHICS_ERROR_TEXT = "❌ Произошла ошибка при генерации графика. Пожалуйста, попробуйте еще раз."
CHECK_PROGRESS = (
    "📊 Прогресс за сегодня ({date}):\n\n"
    "Вода:\n"
    "- Выпито: {water} мл из {water_goal} мл.\n"
    "- Осталось: {water_left} мл.\n\n"
    "Калории:\n"
    "- Потреблено: {food} ккал из {calories_goal} ккал.\n"
    "- Сожжено: {workout} ккал.\n"
    "- Баланс: {food_left} ккал."
)
CHECK_PROGRESS_ERROR = "Не удалось получить статистику за сегодня. Пожалуйста, попробуйте еще раз."
CALORIES_GRAPHICS_TEXT = "График потребления калорий за последнюю неделю"
WATER_GRAPHICS_TEXT = "График потребления воды за последнюю неделю"
WATER_GRAPHICS_TEXT_Y_AXIS = "Вода(мл)"
CALORIES_GRAPHICS_TEXT_Y_AXIS = "Калории(ккал)"
WATER_GRAPHICS_GOAL_TEXT = "Цель воды"
CALORIES_GRAPHICS_GOAL_TEXT = "Цель калорий"

# Button strings
CREATE_PROFILE_BUTTON_LABEL = "Создать профиль"
BACK_BUTTON_LABEL = "Назад"
CANCEL_BUTTON_LABEL = "Отмена"
SHOW_PROFILE_BUTTON_LABEL = "Посмотреть профиль"
EDIT_PROFILE_BUTTON_LABEL = "Редактировать профиль"
DELETE_PROFILE_BUTTON_LABEL = "Удалить профиль"
SKIP_BUTTON_LABEL = "Пропустить"
UPDATE_GOALS_BUTTON_LABEL = "Обновить цели"

LOG_WATER_BUTTON_LABEL = "💧 Попил"
LOG_FOOD_BUTTON_LABEL = "🍌 Поел"
LOG_WORKOUT_BUTTON_LABEL = "🏃‍♂️ Потренировался"
DAILY_STATISTICS_BUTTON_LABEL = "📊 Дневная статистика"
STATISTICS_BUTTON_LABEL = "Статистика"
GRAPHICS_BUTTON_LABEL = "🚀 Твой график за неделю"

RUN_BUTTON_LABEL = "🏃‍♂️ Бег"
CYCLE_BUTTON_LABEL = "🚴‍♂️ Велосипед"
SWIM_BUTTON_LABEL = "🏊‍♂️ Плавание"
PLANK_BUTTON_LABEL = "🧘‍♂️ Планка"
GYM_BUTTON_LABEL = "🏋️‍♂️ Тренажерный зал"
KLIMBING_BUTTON_LABEL = "🧗‍♂️ Скалы"
