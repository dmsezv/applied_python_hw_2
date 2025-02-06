from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler, CallbackQueryHandler
from strings import (
    WEIGHT_TEXT, WEIGHT_TEXT_SAVED, WEIGHT_TYPE_ERROR, WEIGHT_ZERO_ERROR,
    HEIGHT_TEXT, HEIGHT_TEXT_SAVED, HEIGHT_TYPE_ERROR, HEIGHT_ZERO_ERROR,
    AGE_TEXT, AGE_TEXT_SAVED, AGE_TYPE_ERROR, AGE_ZERO_ERROR,
    ACTIVITY_TEXT, ACTIVITY_TEXT_SAVED, ACTIVITY_TYPE_ERROR, ACTIVITY_ZERO_ERROR,
    CITY_TEXT, CITY_TEXT_SAVED, CITY_TYPE_ERROR,
    CALORIES_TEXT, CALORIES_TEXT_SAVED, CALORIES_TYPE_ERROR, CALORIES_ZERO_ERROR,
    PROFILE_UPDATED, PROFILE_ERROR,
    HELLO_TEXT,
    GENDER_TEXT, GENDER_TEXT_SAVED, GENDER_TYPE_ERROR,
    GENDER_MAN, GENDER_WOMAN
)
from services.user_service import UserService

WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, CALORIES, GENDER = range(7)

man_woman_buttons = [
    [
        InlineKeyboardButton(GENDER_MAN, callback_data="M"),
        InlineKeyboardButton(GENDER_WOMAN, callback_data="F")
    ]
]

skip_button = [
    [
        InlineKeyboardButton("Пропустить", callback_data="skip")
    ]
]


async def set_profile_start(update: Update, context: CallbackContext) -> int:
    username = update.message.from_user.username
    context.user_data["username"] = username
    message = f"{HELLO_TEXT.format(username=username)}\n\n{WEIGHT_TEXT}"
    await update.message.reply_text(message)
    context.user_data["current_state"] = WEIGHT
    return WEIGHT


async def weight_handler(update: Update, context: CallbackContext) -> int:
    try:
        weight = float(update.message.text)
        if weight <= 0:
            await update.message.reply_text(WEIGHT_ZERO_ERROR)
            return WEIGHT
    except ValueError:
        await update.message.reply_text(WEIGHT_TYPE_ERROR)
        return WEIGHT

    context.user_data["weight"] = update.message.text
    await update.message.reply_text(WEIGHT_TEXT_SAVED.format(weight=update.message.text))
    context.user_data["current_state"] = HEIGHT
    return HEIGHT


async def height_handler(update: Update, context: CallbackContext) -> int:
    try:
        height = float(update.message.text)
        if height <= 0:
            await update.message.reply_text(HEIGHT_ZERO_ERROR)
            return HEIGHT
    except ValueError:
        await update.message.reply_text(HEIGHT_TYPE_ERROR)
        return HEIGHT

    context.user_data["height"] = update.message.text
    await update.message.reply_text(HEIGHT_TEXT_SAVED.format(height=update.message.text))
    context.user_data["current_state"] = AGE
    return AGE


async def age_handler(update: Update, context: CallbackContext) -> int:
    try:
        age = float(update.message.text)
        if age <= 0:
            await update.message.reply_text(AGE_ZERO_ERROR)
            return AGE
    except ValueError:
        await update.message.reply_text(AGE_TYPE_ERROR)
        return AGE

    context.user_data["age"] = update.message.text
    await update.message.reply_text(AGE_TEXT_SAVED.format(age=update.message.text))
    context.user_data["current_state"] = ACTIVITY
    return ACTIVITY


async def activity_handler(update: Update, context: CallbackContext) -> int:
    try:
        activity = float(update.message.text)
        if activity <= 0:
            await update.message.reply_text(ACTIVITY_ZERO_ERROR)
            return ACTIVITY
    except ValueError:
        await update.message.reply_text(ACTIVITY_TYPE_ERROR)
        return ACTIVITY

    context.user_data["activity"] = update.message.text
    await update.message.reply_text(ACTIVITY_TEXT_SAVED.format(activity=update.message.text))
    context.user_data["current_state"] = CITY
    return CITY


async def city_handler(update: Update, context: CallbackContext) -> int:
    try:
        city = update.message.text
        if not city:
            await update.message.reply_text(CITY_TYPE_ERROR)
            return CITY
    except ValueError:
        await update.message.reply_text(CITY_TYPE_ERROR)
        return CITY

    context.user_data["city"] = update.message.text
    keyboard = man_woman_buttons
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(CITY_TEXT_SAVED.format(city=update.message.text), reply_markup=reply_markup)
    context.user_data["current_state"] = GENDER
    return GENDER


async def gender_handler(update: Update, context: CallbackContext) -> int:
    if update.callback_query:
        query = update.callback_query
        await query.answer()

        if query.data == "M":
            context.user_data["gender"] = "M"
        elif query.data == "F":
            context.user_data["gender"] = "F"
        else:
            keyboard = man_woman_buttons
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.reply_text(GENDER_TYPE_ERROR, reply_markup=reply_markup)
            return GENDER

        keyboard = skip_button
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            GENDER_TEXT_SAVED.format(
                gender=GENDER_MAN if query.data == "M" else GENDER_WOMAN
            ),
            reply_markup=reply_markup
        )
    else:
        keyboard = man_woman_buttons
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(GENDER_TYPE_ERROR, reply_markup=reply_markup)
        return GENDER

    context.user_data["current_state"] = CALORIES
    return CALORIES


async def calories_handler(update: Update, context: CallbackContext) -> int:
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        context.user_data["calories"] = None
    else:
        try:
            calories = float(update.message.text)
            if calories <= 0:
                await update.message.reply_text(CALORIES_ZERO_ERROR)
                return CALORIES
            context.user_data["calories"] = calories
        except ValueError:
            await update.message.reply_text(CALORIES_TYPE_ERROR)
        return CALORIES

    user = UserService().create_user(
        username=context.user_data["username"],
        weight=context.user_data["weight"],
        height=context.user_data["height"],
        age=context.user_data["age"],
        activity=context.user_data["activity"],
        city=context.user_data["city"], 
        calories=context.user_data["calories"],
        gender=context.user_data["gender"]
    )

    if user is None:
        if update.callback_query:
            await update.callback_query.message.reply_text(PROFILE_ERROR)
        else:
            await update.message.reply_text(PROFILE_ERROR)
        return CALORIES

    if update.callback_query:
        await update.callback_query.message.reply_text(PROFILE_UPDATED)
    else:
        await update.message.reply_text(PROFILE_UPDATED)

    # Добавляем кнопки "Посмотреть профиль" и "Удалить профиль"
    profile_buttons = [
        [InlineKeyboardButton("Посмотреть профиль", callback_data="view_profile")],
        [InlineKeyboardButton("Удалить профиль", callback_data="delete_profile")]
    ]
    reply_markup = InlineKeyboardMarkup(profile_buttons)
    if update.callback_query:
        await update.callback_query.message.reply_text("Выберите действие:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

    context.user_data.clear()
    return ConversationHandler.END
