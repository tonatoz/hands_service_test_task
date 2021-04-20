import re
from aiohttp import ClientSession
from asyncio import get_event_loop, create_task, gather
from bs4 import BeautifulSoup
from loguru import logger


phone_pattern = re.compile(
    r"^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$"
)


async def fetch(session: ClientSession, url: str) -> str:
    resp = await session.get(url)
    return await resp.text()


def fix_format(text) -> str:
    clean_phone = list(re.sub(r"[^0-9]", "", text))
    if len(clean_phone) == 10:
        clean_phone.insert(0, "8")
    elif len(clean_phone) == 7:
        clean_phone = ["8", "4", "9", "5"] + clean_phone
    elif clean_phone[0] == "7":
        clean_phone[0] = "8"
    return "".join(clean_phone)


async def process(session: ClientSession, url: str) -> tuple[str, set[str]]:
    try:
        html = await fetch(session, url)
        texts = BeautifulSoup(html, "lxml").findAll(text=phone_pattern)
        phones = [fix_format(t) for t in texts]
        return (url, set(phones))
    except Exception as e:
        logger.error(e)
        return url, []


async def main(urls: list[str]) -> list[tuple[str, set[str]]]:
    async with ClientSession() as session:
        tasks = [create_task(process(session, url)) for url in urls]
        return await gather(*tasks)


def run(urls: list[str]):
    loop = get_event_loop()
    try:
        return loop.run_until_complete(main(urls))
    except:
        logger.exception("Error")
