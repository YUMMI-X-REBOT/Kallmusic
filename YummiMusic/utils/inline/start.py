from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐀𝐝𝐝 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩✦",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="☆𝐇𝐞𝐥𝐩☆", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆𝐆𝐫𝐨𝐮𝐩☆", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="☆𝐂𝐡𝐚𝐧𝐧𝐞𝐥☆", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐎𝐰𝐧𝐞𝐫✦", user_id=OWNER
            )
        ],
     ]
    return buttons
