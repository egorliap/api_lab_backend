import json

from aiohttp import ClientSession
from fastapi import APIRouter, Depends, HTTPException, Request, Response

from .service import Exchanger
from .schemas import SConversionRates, SPairConversion


router = APIRouter(prefix="/exchange", tags=["Exchange"])


@router.get("/rates/{currency}/")
async def get_conversion_rates(currency) -> SConversionRates:
    try:
        async with ClientSession() as session:
            resp = await Exchanger.get_conversion_rates(session, currency)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    conversion_rates = SConversionRates.model_validate_json(resp)
    return conversion_rates


@router.get("/conversion/{currency_from}/{currency_to}/")
async def get_pair_conversion(
    currency_from, currency_to, amount: float = 1
) -> SPairConversion:
    try:
        async with ClientSession() as session:
            resp = await Exchanger.get_pair_conversion(
                session, currency_from, currency_to, amount
            )
    except Exception as e:
        HTTPException(status_code=404, detail=str(e))
    conversion = SPairConversion.model_validate_json(resp)

    return conversion


def get_favorites_from_cookie(request: Request) -> str:
    favorites = request.cookies.get("favorites")
    return favorites


@router.post("/favorites/", description="Sets a pair of currencies to cookies")
async def set_favorite_pair_conversion(
    response: Response,
    currency_from: str,
    currency_to: str,
    favorites: str = Depends(get_favorites_from_cookie),
):
    if favorites:
        favorites = json.loads(favorites)
    else:
        favorites = []
    new_pair = (currency_from, currency_to)
    if new_pair not in favorites:
        favorites.append(new_pair)

    response.set_cookie(key="favorites", value=json.dumps(favorites))


@router.get("/favorites/", description="Gets all pairs of currencies (added) from cookies")
async def get_favorites(favorites: str = Depends(get_favorites_from_cookie)):
    favorites = []
    if favorites:
        favorites = json.loads(favorites)

    conversions = []
    async with ClientSession() as session:
        for fav in favorites:
            try:
                resp = await Exchanger.get_pair_conversion(session, fav[0], fav[1], 1)
            except Exception:
                continue

            conversions.append(SPairConversion.model_validate_json(resp))

    return conversions
