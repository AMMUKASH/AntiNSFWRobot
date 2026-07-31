from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
👋 **Hello {mention}!**

🛡 **Welcome to Anti NSFW Robot**

• Detects NSFW Photos & Media
• Automatic Moderation
• Fast & Reliable Protection
• Easy to Setup

➕ Add me to your group and give me admin permissions to start protecting your community.
"""

@Client.on_message(filters.command(["start", "help", "repo", "source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText.format(
            mention=m.from_user.mention if m.from_user else "User"
        ),
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(
                        "➕ Add Me",
                        url="https://t.me/YOUR_BOT_USERNAME?startgroup=true"
                    )
                ],
                [
                    t.InlineKeyboardButton(
                        "👑 σωɴєʀ",
                        url="https://t.me/CoderNova"
                    ),
                    t.InlineKeyboardButton(
                        "💬 ꜱυᴩᴩσʀᴛ",
                        url="https://t.me/+BTg9b8Xw9lhkMWUx"
                    )
                ],
                [
                    t.InlineKeyboardButton(
                        "📢 ᴜᴩᴅαтє",
                        url="https://t.me/NovaBot_Support"
                    ),
                    t.InlineKeyboardButton(
                        "⭐ ѕσυʀᴄє",
                        url="https://t.me/Nova_coder"
                    )
                ],
                [
                    t.InlineKeyboardButton(
                        "📚 Help Guide",
                        callback_data="help"
                    )
                ]
            ]
        )
    )
