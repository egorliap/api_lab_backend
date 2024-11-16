import json
from os import getenv

from aiohttp import ClientSession
from dotenv import load_dotenv

load_dotenv()


class Exchanger:
    base_exchanger_url = f"https://v6.exchangerate-api.com/v6/{getenv('ER_API_KEY')}/"

    @classmethod
    async def get_conversion_rates(cls, session: ClientSession, currency: str):

        response = await session.get(
            cls.base_exchanger_url + f"latest/{currency.upper()}"
        )
        if response.status == 200:
            response_content = await response.read()
            return response_content
        else:
            error_content = await response.text()
            error_type = json.loads(error_content).get("error-type", -1)
            raise Exception(error_type)

    @classmethod
    async def get_pair_conversion(
        cls,
        session: ClientSession,
        curr_from: str,
        curr_to: str,
        amount: float = 1,
    ):

        response = await session.get(
            cls.base_exchanger_url
            + f"pair/{curr_from.upper()}/{curr_to.upper()}/{amount}"
        )
        if response.status == 200:
            response_content = await response.read()
            return response_content
        else:
            error_content = await response.text()
            error_type = json.loads(error_content).get("error-type", -1)
            raise Exception(error_type)
