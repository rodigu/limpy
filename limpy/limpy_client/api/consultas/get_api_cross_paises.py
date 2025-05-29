from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_cross_paises_response_200 import GetApiCrossPaisesResponse200
from ...models.get_api_cross_paises_response_400 import GetApiCrossPaisesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cross/paises",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]:
    if response.status_code == 200:
        response_200 = GetApiCrossPaisesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetApiCrossPaisesResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]:
    """Consulta de Países

     Rota destinada a retornar a Lista de Países para preenchimento da informação para Integração da
    Reserva

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]:
    """Consulta de Países

     Rota destinada a retornar a Lista de Países para preenchimento da informação para Integração da
    Reserva

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]:
    """Consulta de Países

     Rota destinada a retornar a Lista de Países para preenchimento da informação para Integração da
    Reserva

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]]:
    """Consulta de Países

     Rota destinada a retornar a Lista de Países para preenchimento da informação para Integração da
    Reserva

    Args:
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiCrossPaisesResponse200, GetApiCrossPaisesResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
