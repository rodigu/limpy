import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_ec_clientes_response_200 import GetApiEcClientesResponse200
from ...models.get_api_ec_clientes_response_400 import GetApiEcClientesResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: Union[Unset, str] = UNSET,
    data_ini_cad: Union[Unset, datetime.datetime] = UNSET,
    data_fim_cad: Union[Unset, datetime.datetime] = UNSET,
    data_ini_alt: Union[Unset, datetime.datetime] = UNSET,
    data_fim_alt: Union[Unset, datetime.datetime] = UNSET,
    termos: Union[Unset, str] = UNSET,
    local_venda: Union[Unset, str] = UNSET,
    data_ini: Union[Unset, datetime.datetime] = UNSET,
    data_fim: Union[Unset, datetime.datetime] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["search"] = search

    json_data_ini_cad: Union[Unset, str] = UNSET
    if not isinstance(data_ini_cad, Unset):
        json_data_ini_cad = data_ini_cad.isoformat()
    params["dataIniCad"] = json_data_ini_cad

    json_data_fim_cad: Union[Unset, str] = UNSET
    if not isinstance(data_fim_cad, Unset):
        json_data_fim_cad = data_fim_cad.isoformat()
    params["dataFimCad"] = json_data_fim_cad

    json_data_ini_alt: Union[Unset, str] = UNSET
    if not isinstance(data_ini_alt, Unset):
        json_data_ini_alt = data_ini_alt.isoformat()
    params["dataIniAlt"] = json_data_ini_alt

    json_data_fim_alt: Union[Unset, str] = UNSET
    if not isinstance(data_fim_alt, Unset):
        json_data_fim_alt = data_fim_alt.isoformat()
    params["dataFimAlt"] = json_data_fim_alt

    params["termos"] = termos

    params["localVenda"] = local_venda

    json_data_ini: Union[Unset, str] = UNSET
    if not isinstance(data_ini, Unset):
        json_data_ini = data_ini.isoformat()
    params["dataIni"] = json_data_ini

    json_data_fim: Union[Unset, str] = UNSET
    if not isinstance(data_fim, Unset):
        json_data_fim = data_fim.isoformat()
    params["dataFim"] = json_data_fim

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ec/clientes",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]:
    if response.status_code == 200:
        response_200 = GetApiEcClientesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetApiEcClientesResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    data_ini_cad: Union[Unset, datetime.datetime] = UNSET,
    data_fim_cad: Union[Unset, datetime.datetime] = UNSET,
    data_ini_alt: Union[Unset, datetime.datetime] = UNSET,
    data_fim_alt: Union[Unset, datetime.datetime] = UNSET,
    termos: Union[Unset, str] = UNSET,
    local_venda: Union[Unset, str] = UNSET,
    data_ini: Union[Unset, datetime.datetime] = UNSET,
    data_fim: Union[Unset, datetime.datetime] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]:
    """Consulta de Clientes

     Rota destinada a retornar a Lista de Clientes

    Args:
        search (Union[Unset, str]):
        data_ini_cad (Union[Unset, datetime.datetime]):
        data_fim_cad (Union[Unset, datetime.datetime]):
        data_ini_alt (Union[Unset, datetime.datetime]):
        data_fim_alt (Union[Unset, datetime.datetime]):
        termos (Union[Unset, str]):
        local_venda (Union[Unset, str]):
        data_ini (Union[Unset, datetime.datetime]):
        data_fim (Union[Unset, datetime.datetime]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]
    """

    kwargs = _get_kwargs(
        search=search,
        data_ini_cad=data_ini_cad,
        data_fim_cad=data_fim_cad,
        data_ini_alt=data_ini_alt,
        data_fim_alt=data_fim_alt,
        termos=termos,
        local_venda=local_venda,
        data_ini=data_ini,
        data_fim=data_fim,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    data_ini_cad: Union[Unset, datetime.datetime] = UNSET,
    data_fim_cad: Union[Unset, datetime.datetime] = UNSET,
    data_ini_alt: Union[Unset, datetime.datetime] = UNSET,
    data_fim_alt: Union[Unset, datetime.datetime] = UNSET,
    termos: Union[Unset, str] = UNSET,
    local_venda: Union[Unset, str] = UNSET,
    data_ini: Union[Unset, datetime.datetime] = UNSET,
    data_fim: Union[Unset, datetime.datetime] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]:
    """Consulta de Clientes

     Rota destinada a retornar a Lista de Clientes

    Args:
        search (Union[Unset, str]):
        data_ini_cad (Union[Unset, datetime.datetime]):
        data_fim_cad (Union[Unset, datetime.datetime]):
        data_ini_alt (Union[Unset, datetime.datetime]):
        data_fim_alt (Union[Unset, datetime.datetime]):
        termos (Union[Unset, str]):
        local_venda (Union[Unset, str]):
        data_ini (Union[Unset, datetime.datetime]):
        data_fim (Union[Unset, datetime.datetime]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]
    """

    return sync_detailed(
        client=client,
        search=search,
        data_ini_cad=data_ini_cad,
        data_fim_cad=data_fim_cad,
        data_ini_alt=data_ini_alt,
        data_fim_alt=data_fim_alt,
        termos=termos,
        local_venda=local_venda,
        data_ini=data_ini,
        data_fim=data_fim,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    data_ini_cad: Union[Unset, datetime.datetime] = UNSET,
    data_fim_cad: Union[Unset, datetime.datetime] = UNSET,
    data_ini_alt: Union[Unset, datetime.datetime] = UNSET,
    data_fim_alt: Union[Unset, datetime.datetime] = UNSET,
    termos: Union[Unset, str] = UNSET,
    local_venda: Union[Unset, str] = UNSET,
    data_ini: Union[Unset, datetime.datetime] = UNSET,
    data_fim: Union[Unset, datetime.datetime] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]:
    """Consulta de Clientes

     Rota destinada a retornar a Lista de Clientes

    Args:
        search (Union[Unset, str]):
        data_ini_cad (Union[Unset, datetime.datetime]):
        data_fim_cad (Union[Unset, datetime.datetime]):
        data_ini_alt (Union[Unset, datetime.datetime]):
        data_fim_alt (Union[Unset, datetime.datetime]):
        termos (Union[Unset, str]):
        local_venda (Union[Unset, str]):
        data_ini (Union[Unset, datetime.datetime]):
        data_fim (Union[Unset, datetime.datetime]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]
    """

    kwargs = _get_kwargs(
        search=search,
        data_ini_cad=data_ini_cad,
        data_fim_cad=data_fim_cad,
        data_ini_alt=data_ini_alt,
        data_fim_alt=data_fim_alt,
        termos=termos,
        local_venda=local_venda,
        data_ini=data_ini,
        data_fim=data_fim,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    search: Union[Unset, str] = UNSET,
    data_ini_cad: Union[Unset, datetime.datetime] = UNSET,
    data_fim_cad: Union[Unset, datetime.datetime] = UNSET,
    data_ini_alt: Union[Unset, datetime.datetime] = UNSET,
    data_fim_alt: Union[Unset, datetime.datetime] = UNSET,
    termos: Union[Unset, str] = UNSET,
    local_venda: Union[Unset, str] = UNSET,
    data_ini: Union[Unset, datetime.datetime] = UNSET,
    data_fim: Union[Unset, datetime.datetime] = UNSET,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]]:
    """Consulta de Clientes

     Rota destinada a retornar a Lista de Clientes

    Args:
        search (Union[Unset, str]):
        data_ini_cad (Union[Unset, datetime.datetime]):
        data_fim_cad (Union[Unset, datetime.datetime]):
        data_ini_alt (Union[Unset, datetime.datetime]):
        data_fim_alt (Union[Unset, datetime.datetime]):
        termos (Union[Unset, str]):
        local_venda (Union[Unset, str]):
        data_ini (Union[Unset, datetime.datetime]):
        data_fim (Union[Unset, datetime.datetime]):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiEcClientesResponse200, GetApiEcClientesResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            data_ini_cad=data_ini_cad,
            data_fim_cad=data_fim_cad,
            data_ini_alt=data_ini_alt,
            data_fim_alt=data_fim_alt,
            termos=termos,
            local_venda=local_venda,
            data_ini=data_ini,
            data_fim=data_fim,
            authorization=authorization,
        )
    ).parsed
