from telegram import Update
from telegram.ext import CallbackContext
from strings import (
    LOG_WATER_SUCCESS, LOG_WATER_ERROR, LOG_FOOD_PROMPT, LOG_FOOD_ERROR,
    LOG_WORKOUT_SUCCESS, LOG_WORKOUT_ERROR, CHECK_PROGRESS
)


async def log_water(update: Update, context: CallbackContext) -> None:
    try:
        amount = int(context.args[0])
        # Здесь можно добавить логику для сохранения количества выпитой воды
        # и расчета оставшегося объема до выполнения нормы
        await update.message.reply_text(LOG_WATER_SUCCESS.format(amount=amount))
    except (IndexError, ValueError):
        await update.message.reply_text(LOG_WATER_ERROR)


async def log_food(update: Update, context: CallbackContext) -> None:
    try:
        product_name = " ".join(context.args)
        # Здесь можно добавить логику для использования API, например, OpenFoodFacts
        # и получения информации о продукте
        # Пример: калорийность продукта
        calories_per_100g = 89  # Это значение можно получить из API
        await update.message.reply_text(
            LOG_FOOD_PROMPT.format(product_name=product_name, calories_per_100g=calories_per_100g)
        )
        # Логика для сохранения калорийности
    except IndexError:
        await update.message.reply_text(LOG_FOOD_ERROR)


async def log_workout(update: Update, context: CallbackContext) -> None:
    try:
        workout_type = context.args[0]
        duration = int(context.args[1])
        # Здесь можно добавить логику для расчета сожженных калорий в зависимости от типа тренировки
        # и времени
        calories_burned = 300  # Примерное значение, можно заменить на расчетное
        water_needed = (duration // 30) * 200  # Дополнительные 200 мл за каждые 30 минут
        await update.message.reply_text(
            LOG_WORKOUT_SUCCESS.format(
                workout_type=workout_type, duration=duration,
                calories_burned=calories_burned, water_needed=water_needed
            )
        )
    except (IndexError, ValueError):
        await update.message.reply_text(LOG_WORKOUT_ERROR)


async def check_progress(update: Update, context: CallbackContext) -> None:
    # Здесь можно добавить логику для получения текущего прогресса по воде и калориям
    water_consumed = 1500  # Примерное значение
    water_goal = 2400  # Примерное значение
    calories_consumed = 1800  # Примерное значение
    calories_goal = 2500  # Примерное значение
    calories_burned = 400  # Примерное значение
    balance = calories_consumed - calories_burned
    await update.message.reply_text(
        CHECK_PROGRESS.format(
            water_consumed=water_consumed, water_goal=water_goal,
            calories_consumed=calories_consumed, calories_goal=calories_goal,
            calories_burned=calories_burned, balance=balance
        )
    )
