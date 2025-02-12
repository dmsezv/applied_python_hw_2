from telegram import InlineKeyboardButton
from strings import (
    CREATE_PROFILE_BUTTON_LABEL, SHOW_PROFILE_BUTTON_LABEL, DELETE_PROFILE_BUTTON_LABEL,
    GENDER_MAN, GENDER_WOMAN, SKIP_BUTTON_LABEL, EDIT_PROFILE_BUTTON_LABEL, UPDATE_GOALS_BUTTON_LABEL,
    YES_BUTTON_LABEL, NO_BUTTON_LABEL
)

CREATE_PROFILE_BUTTON = [[CREATE_PROFILE_BUTTON_LABEL]]

MAIN_MENU_BUTTONS = [
    [SHOW_PROFILE_BUTTON_LABEL, UPDATE_GOALS_BUTTON_LABEL],
    [EDIT_PROFILE_BUTTON_LABEL, DELETE_PROFILE_BUTTON_LABEL]
]

MAN_WOMAN_INLINE_BUTTONS = [
    [
        InlineKeyboardButton(GENDER_MAN, callback_data="M"),
        InlineKeyboardButton(GENDER_WOMAN, callback_data="F")
    ]
]

SKIP_INLINE_BUTTON = [
    [
        InlineKeyboardButton(SKIP_BUTTON_LABEL, callback_data="skip")
    ]
]

YES_NO_INLINE_BUTTON = [
    [
        InlineKeyboardButton(YES_BUTTON_LABEL, callback_data="yes"),
        InlineKeyboardButton(NO_BUTTON_LABEL, callback_data="no")
    ]
]
