from sqlalchemy.ext.asyncio import AsyncSession
from database.orm_query import orm_get_banner
from aiogram.types import InputMediaPhoto
from database.orm_query import orm_get_banner
from keyboards.inline import get_user_main_btns


async def main_menu(session, level, menu_name):
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)
    kbds = get_user_main_btns(level=level)

    return image, kbds



async def get_menu_content(
        session: AsyncSession,
        level: int,
        menu_name: str,
):
    if level == 0:
        return await main_menu(session, level, menu_name)