#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default="26796802", cast=int)
    API_HASH = config("API_HASH", default="b8cc96196eb105c33d8ce193e5efff5c")
    BOT_TOKEN = config("BOT_TOKEN", default="6590624540:AAGOkHMG-k4ykdex2pz3LOOE6CGMZIU-c7s")

    # Database Credentials

    REDIS_URI = config("REDIS_URI", default="redis://default:34957c0584804a6cb1fdc9b4fd9fc4ee@thorough-shrimp-40797.kv.vercel-storage.com:40797")
    REDIS_PASS = config("REDIS_PASSWORD", default="AZ9dASQgM2VhODk1OTMtOGQzMy00ZWE0LWI4MGUtZmZlOTViN2M4YzdjMzQ5NTdjMDU4NDgwNGE2Y2IxZmRjOWI0ZmQ5ZmM0ZWU")

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default="-1001946276932", cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default="-1001939871276", cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1001292557562", cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", cast=int)
    OWNER = config("OWNER", default="1474271232", cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/04571fee511dd2a0f48b6.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
