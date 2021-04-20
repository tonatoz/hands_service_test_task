from aiohttp import ClientSession
from asyncio import get_event_loop, create_task, gather
from loguru import logger
from bs4 import BeautifulSoup
import re
import time


async def fetch(session: ClientSession, url: str) -> str:
    resp = await session.get(url)
    return await resp.text()


async def parse(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    texts = soup.findAll(text=True)
    return [t.strip() for t in texts]


def find_phone_nubmer(text):
    phone = re.match(
        "^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$",
        text,
    )
    if phone:
        clean_phone = list(re.sub("[^0-9]", "", phone.group()))
        clean_phone[0] = "8"  # if +7 - change to 8, if 8 - it's good
        return "".join(clean_phone)


async def process(session: ClientSession, url: str) -> tuple[str, list[str]]:
    try:
        html = await fetch(session, url)
        texts = await parse(html)
        phones = [find_phone_nubmer(t) for t in texts]
        return url, list(filter(lambda x: x, phones))
    except Exception as e:
        logger.warning(e)
        return []


async def main(urls: list[str]):
    async with ClientSession() as session:
        start = time.time()
        tasks = [create_task(process(session, url)) for url in urls]
        results = await gather(*tasks)
        # logger.info(f"Result: {results}")
        logger.info(f"Time elapsed: {time.time() - start} ")


if __name__ == "__main__":
    loop = get_event_loop()
    try:
        organizations = ["https://masterdel.ru/", "https://repetitors.info/"] * 100
        loop.run_until_complete(main(organizations))
    except:
        logger.exception("Error")
