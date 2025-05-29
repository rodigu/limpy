from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_vendas_venda_cancelamentos_id_venda_response_200 import (
    GetApiVendasVendaCancelamentosIdVendaResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id_venda: float,
    *,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/vendas/venda/cancelamentos/{id_venda}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetApiVendasVendaCancelamentosIdVendaResponse200]:
    if response.status_code == 200:
        response_200 = GetApiVendasVendaCancelamentosIdVendaResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetApiVendasVendaCancelamentosIdVendaResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id_venda: float,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Response[GetApiVendasVendaCancelamentosIdVendaResponse200]:
    """Consultar cancelamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaCancelamentosIdVendaResponse200]
    """

    kwargs = _get_kwargs(
        id_venda=id_venda,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id_venda: float,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[GetApiVendasVendaCancelamentosIdVendaResponse200]:
    """Consultar cancelamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaCancelamentosIdVendaResponse200
    """

    return sync_detailed(
        id_venda=id_venda,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    id_venda: float,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Response[GetApiVendasVendaCancelamentosIdVendaResponse200]:
    """Consultar cancelamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaCancelamentosIdVendaResponse200]
    """

    kwargs = _get_kwargs(
        id_venda=id_venda,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id_venda: float,
    *,
    client: AuthenticatedClient,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[GetApiVendasVendaCancelamentosIdVendaResponse200]:
    """Consultar cancelamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaCancelamentosIdVendaResponse200
    """

    return (
        await asyncio_detailed(
            id_venda=id_venda,
            client=client,
            authorization=authorization,
        )
    ).parsed
