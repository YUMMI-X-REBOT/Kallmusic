from YummiMusic.core.bot import YummiX
from YummiMusic.core.dir import dirr
from YummiMusic.core.userbot import Userbot
from YummiMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER


dirr()

dbb()

heroku()

sudo()

# Clients
app = YummiX()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
