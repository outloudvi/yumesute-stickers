from io import BytesIO
import os

from PIL import Image
from telegram import Bot, InputSticker
from telegram.constants import StickerFormat

BOT_ID = os.environ["BOT_ID"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
TARGET_SIZE = (512, 484)
CONTROLLER_USERID = os.environ["CONTROLLER_USERID"]
PACK_NAME =  os.environ["PACK_NAME"]

bot = Bot(BOT_TOKEN)


def resize_image(path):
    img = Image.open(path)
    resized_img = img.resize(TARGET_SIZE)
    bio = BytesIO()
    bio.name = 'image.png'
    resized_img.save(bio, 'PNG')
    bio.seek(0)
    return bio


def generate_sticker_set() -> list[InputSticker]:
    lines = open("def2.txt", "r").read().split("\n")
    ret = []
    for i in lines:
        items = i.split(",")
        if len(items) != 3:
            continue
        ret.append(InputSticker(resize_image(f"{items[0]}.png"), items[2]))
    return ret


sticker_set = generate_sticker_set()


async def add_images_to_sticker():
    await bot.create_new_sticker_set(
        CONTROLLER_USERID,
        PACK_NAME,
        "ユメステ Stamps",
        stickers=[sticker_set[0]],
        sticker_format=StickerFormat.STATIC
    )


async def add_other_images_to_sticker():
    for s in sticker_set:
        print("Doing", s)
        await bot.add_sticker_to_set(
            CONTROLLER_USERID,
            PACK_NAME,
            sticker=s
        )

async def main():
    # await add_images_to_sticker()
    print(sticker_set)
    await add_other_images_to_sticker()

main()