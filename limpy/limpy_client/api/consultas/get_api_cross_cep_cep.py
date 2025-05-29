from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_cross_cep_cep_response_200 import GetApiCrossCepCEPResponse200
from ...models.get_api_cross_cep_cep_response_400 import GetApiCrossCepCEPResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    content_type: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(content_type, Unset):
        headers["Content-Type"] = content_type

    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cross/cep/CEP",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]:
    if response.status_code == 200:
        response_200 = GetApiCrossCepCEPResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetApiCrossCepCEPResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content_type: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]:
    """Consulta de CEP

     Retorna o endereço de acordo com o CEP utilizado.

    Args:
        content_type (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    content_type: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]:
    """Consulta de CEP

     Retorna o endereço de acordo com o CEP utilizado.

    Args:
        content_type (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]
    """

    return sync_detailed(
        client=client,
        content_type=content_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    content_type: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]:
    """Consulta de CEP

     Retorna o endereço de acordo com o CEP utilizado.

    Args:
        content_type (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]
    """

    kwargs = _get_kwargs(
        content_type=content_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    content_type: Union[Unset, str] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]]:
    """Consulta de CEP

     Retorna o endereço de acordo com o CEP utilizado.

    Args:
        content_type (Union[Unset, str]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiCrossCepCEPResponse200, GetApiCrossCepCEPResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            content_type=content_type,
            authorization=authorization,
        )
    ).parsed
