from telegram.ext import (
    ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters, CallbackQueryHandler
)
from config import BOT_TOKEN

from handlers.set_profile_handlers import (
    set_profile_start, weight_handler, height_handler, age_handler,
    activity_handler, city_handler, gender_handler
)
from handlers.user_profile_handlers import view_profile_handler, delete_profile_handler, update_goals_handler
from handlers.statistics_handlers import (
    start_statistics_handler, get_daily_statistics_handler,
    get_workout_handler,
    get_food_handler, set_food_handler, add_food_handler, get_calories_count_handler,
    set_workout_handler, add_workout_handler,
    set_water_handler, add_water_handler,
    get_graphics_handler
)
from handlers.common_handlers import start_handler, main_menu_handler
from states import (
    WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, GENDER,
    FOOD_SET, FOOD_ADD, FOOD_CALORIES_COUNT,
    WORKOUT_SET, WORKOUT_ADD,
    WATER_SET, WATER_ADD
)
from strings import (
    CREATE_PROFILE_BUTTON_LABEL, SHOW_PROFILE_BUTTON_LABEL,
    DELETE_PROFILE_BUTTON_LABEL, EDIT_PROFILE_BUTTON_LABEL,
    UPDATE_GOALS_BUTTON_LABEL, STATISTICS_BUTTON_LABEL, BACK_BUTTON_LABEL,
    DAILY_STATISTICS_BUTTON_LABEL,
    LOG_FOOD_BUTTON_LABEL, LOG_WORKOUT_BUTTON_LABEL, LOG_WATER_BUTTON_LABEL,
    GRAPHICS_BUTTON_LABEL,
    CANCEL_BUTTON_LABEL
)


def main():
    app = ApplicationBuilder() \
        .token(BOT_TOKEN) \
        .read_timeout(10) \
        .write_timeout(10) \
        .build()

    set_profile_handler = ConversationHandler(
        entry_points=[
            CommandHandler("set_profile", set_profile_start),
            MessageHandler(filters.Regex(f"^{CREATE_PROFILE_BUTTON_LABEL}$"), set_profile_start),
            CommandHandler("edit_profile", set_profile_start),
            MessageHandler(filters.Regex(f"^{EDIT_PROFILE_BUTTON_LABEL}$"), set_profile_start),
        ],
        states={
            WEIGHT: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, weight_handler),
            ],
            HEIGHT: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, height_handler),
            ],
            AGE: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, age_handler),
            ],
            ACTIVITY: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, activity_handler),
            ],
            CITY: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, city_handler),
            ],
            GENDER: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_handler),
                CallbackQueryHandler(gender_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, gender_handler),
            ]
        },
        fallbacks=[
            CommandHandler("start", start_handler),
        ],
        allow_reentry=False
    )

    user_profile_handler = ConversationHandler(
        entry_points=[
            CommandHandler("view_profile", view_profile_handler),
            MessageHandler(filters.Regex(f"^{SHOW_PROFILE_BUTTON_LABEL}$"), view_profile_handler),
            CommandHandler("delete_profile", delete_profile_handler),
            MessageHandler(filters.Regex(f"^{DELETE_PROFILE_BUTTON_LABEL}$"), delete_profile_handler),
            CommandHandler("update_goals", update_goals_handler),
            MessageHandler(filters.Regex(f"^{UPDATE_GOALS_BUTTON_LABEL}$"), update_goals_handler)
        ],
        states={},
        fallbacks=[
            CommandHandler("start", start_handler),
        ],
        allow_reentry=False
    )

    statistics_handler = ConversationHandler(
        entry_points=[
            CommandHandler("statistics", start_statistics_handler),
            MessageHandler(filters.Regex(f"^{STATISTICS_BUTTON_LABEL}$"), start_statistics_handler),
            MessageHandler(filters.Regex(f"^{DAILY_STATISTICS_BUTTON_LABEL}$"), get_daily_statistics_handler),
            MessageHandler(filters.Regex(f"^{LOG_FOOD_BUTTON_LABEL}$"), get_food_handler),
            MessageHandler(filters.Regex(f"^{LOG_WATER_BUTTON_LABEL}$"), set_water_handler),
            MessageHandler(filters.Regex(f"^{LOG_WORKOUT_BUTTON_LABEL}$"), get_workout_handler),
            MessageHandler(filters.Regex(f"^{GRAPHICS_BUTTON_LABEL}$"), get_graphics_handler),
            MessageHandler(filters.Regex(f"^{BACK_BUTTON_LABEL}$"), main_menu_handler),
        ],
        states={
            # FOOD
            FOOD_SET: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, set_food_handler),
            ],
            FOOD_ADD: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                CallbackQueryHandler(add_food_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_food_handler),
            ],
            FOOD_CALORIES_COUNT: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_calories_count_handler),
            ],
            # WORKOUT
            WORKOUT_SET: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, set_workout_handler),
            ],
            WORKOUT_ADD: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_workout_handler),
            ],
            # WATER
            WATER_SET: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, set_water_handler),
            ],
            WATER_ADD: [
                MessageHandler(filters.Regex(f"^{CANCEL_BUTTON_LABEL}$"), start_statistics_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, add_water_handler),
            ],
        },
        fallbacks=[
            CommandHandler("start", start_handler),
        ],
        allow_reentry=False
    )
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(set_profile_handler)
    app.add_handler(user_profile_handler)
    app.add_handler(statistics_handler)
    app.run_polling()


if __name__ == "__main__":
    main()
