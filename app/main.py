from telegram.ext import (
    ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters, CallbackQueryHandler
)
from config import BOT_TOKEN

from handlers.set_profile_handlers import (
    set_profile_start, weight_handler, height_handler, age_handler,
    activity_handler, city_handler, gender_handler
)
from handlers.set_profile_handlers import WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, GENDER

from handlers.user_profile_handlers import view_profile_handler, delete_profile_handler, update_goals_handler

from handlers.common_handlers import start_handler
from strings import (
    CREATE_PROFILE_BUTTON_LABEL, SHOW_PROFILE_BUTTON_LABEL,
    DELETE_PROFILE_BUTTON_LABEL, EDIT_PROFILE_BUTTON_LABEL,
    UPDATE_GOALS_BUTTON_LABEL
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
                MessageHandler(filters.TEXT & ~filters.COMMAND, weight_handler),
            ],
            HEIGHT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, height_handler),
            ],
            AGE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, age_handler),
            ],
            ACTIVITY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, activity_handler),
            ],
            CITY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, city_handler),
            ],
            GENDER: [
                CallbackQueryHandler(gender_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, gender_handler),
            ]
        },
        fallbacks=[
            CommandHandler("start", start_handler),
        ],
        allow_reentry=True
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

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(set_profile_handler)
    app.add_handler(user_profile_handler)
    app.run_polling()


if __name__ == "__main__":
    main()
