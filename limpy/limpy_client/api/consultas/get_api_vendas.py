from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_vendas_body import GetApiVendasBody
from ...models.get_api_vendas_response_200 import GetApiVendasResponse200
from ...models.get_api_vendas_response_400 import GetApiVendasResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GetApiVendasBody,
    authorization: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/vendas",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetApiVendasResponse200, GetApiVendasResponse400]]:
    if response.status_code == 200:
        response_200 = GetApiVendasResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetApiVendasResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetApiVendasResponse200, GetApiVendasResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetApiVendasBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiVendasResponse200, GetApiVendasResponse400]]:
    """Listagem de vendas

     Rota destinada a retornar as vendas realizadas a qualquer estabelecimento que o seu usuário tenha
    permissão de visualização.

    Args:
        authorization (Union[Unset, str]):
        body (GetApiVendasBody):  Example: {'localizador': 'localizador', 'dataVendaInit':
            'dataVendaInit', 'dataVendaFim': 'dataVendaFim', 'dataVisitaInit': 'dataVisitaInit',
            'dataVisitaFim': 'dataVisitaFim', 'dataCancelamentoInit': 'dataCancelamentoInit',
            'dataCancelamentoFim': 'dataCancelamentoFim', 'dataUtilizacaoInit': 'dataUtilizacaoInit',
            'dataUtilizacaoFim': 'dataUtilizacaoFim', 'statusArray': 'statusArray', 'idOrigem':
            'idOrigem', 'nomeOrEmail': 'nomeOrEmail', 'estabelecOrig': 'estabelecOrig',
            'estabelecDest': 'estabelecDest', 'bilhetes': 'bilhetes', 'codClienteEc': 'codClienteEc',
            'modoPagArray': 'modoPagArray', 'nsuIdAutorizacao': 'nsuIdAutorizacao', 'locaisEmbarque':
            'locaisEmbarque'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiVendasResponse200, GetApiVendasResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetApiVendasBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiVendasResponse200, GetApiVendasResponse400]]:
    """Listagem de vendas

     Rota destinada a retornar as vendas realizadas a qualquer estabelecimento que o seu usuário tenha
    permissão de visualização.

    Args:
        authorization (Union[Unset, str]):
        body (GetApiVendasBody):  Example: {'localizador': 'localizador', 'dataVendaInit':
            'dataVendaInit', 'dataVendaFim': 'dataVendaFim', 'dataVisitaInit': 'dataVisitaInit',
            'dataVisitaFim': 'dataVisitaFim', 'dataCancelamentoInit': 'dataCancelamentoInit',
            'dataCancelamentoFim': 'dataCancelamentoFim', 'dataUtilizacaoInit': 'dataUtilizacaoInit',
            'dataUtilizacaoFim': 'dataUtilizacaoFim', 'statusArray': 'statusArray', 'idOrigem':
            'idOrigem', 'nomeOrEmail': 'nomeOrEmail', 'estabelecOrig': 'estabelecOrig',
            'estabelecDest': 'estabelecDest', 'bilhetes': 'bilhetes', 'codClienteEc': 'codClienteEc',
            'modoPagArray': 'modoPagArray', 'nsuIdAutorizacao': 'nsuIdAutorizacao', 'locaisEmbarque':
            'locaisEmbarque'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiVendasResponse200, GetApiVendasResponse400]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetApiVendasBody,
    authorization: Union[Unset, str] = UNSET,
) -> Response[Union[GetApiVendasResponse200, GetApiVendasResponse400]]:
    """Listagem de vendas

     Rota destinada a retornar as vendas realizadas a qualquer estabelecimento que o seu usuário tenha
    permissão de visualização.

    Args:
        authorization (Union[Unset, str]):
        body (GetApiVendasBody):  Example: {'localizador': 'localizador', 'dataVendaInit':
            'dataVendaInit', 'dataVendaFim': 'dataVendaFim', 'dataVisitaInit': 'dataVisitaInit',
            'dataVisitaFim': 'dataVisitaFim', 'dataCancelamentoInit': 'dataCancelamentoInit',
            'dataCancelamentoFim': 'dataCancelamentoFim', 'dataUtilizacaoInit': 'dataUtilizacaoInit',
            'dataUtilizacaoFim': 'dataUtilizacaoFim', 'statusArray': 'statusArray', 'idOrigem':
            'idOrigem', 'nomeOrEmail': 'nomeOrEmail', 'estabelecOrig': 'estabelecOrig',
            'estabelecDest': 'estabelecDest', 'bilhetes': 'bilhetes', 'codClienteEc': 'codClienteEc',
            'modoPagArray': 'modoPagArray', 'nsuIdAutorizacao': 'nsuIdAutorizacao', 'locaisEmbarque':
            'locaisEmbarque'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetApiVendasResponse200, GetApiVendasResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GetApiVendasBody,
    authorization: Union[Unset, str] = UNSET,
) -> Optional[Union[GetApiVendasResponse200, GetApiVendasResponse400]]:
    """Listagem de vendas

     Rota destinada a retornar as vendas realizadas a qualquer estabelecimento que o seu usuário tenha
    permissão de visualização.

    Args:
        authorization (Union[Unset, str]):
        body (GetApiVendasBody):  Example: {'localizador': 'localizador', 'dataVendaInit':
            'dataVendaInit', 'dataVendaFim': 'dataVendaFim', 'dataVisitaInit': 'dataVisitaInit',
            'dataVisitaFim': 'dataVisitaFim', 'dataCancelamentoInit': 'dataCancelamentoInit',
            'dataCancelamentoFim': 'dataCancelamentoFim', 'dataUtilizacaoInit': 'dataUtilizacaoInit',
            'dataUtilizacaoFim': 'dataUtilizacaoFim', 'statusArray': 'statusArray', 'idOrigem':
            'idOrigem', 'nomeOrEmail': 'nomeOrEmail', 'estabelecOrig': 'estabelecOrig',
            'estabelecDest': 'estabelecDest', 'bilhetes': 'bilhetes', 'codClienteEc': 'codClienteEc',
            'modoPagArray': 'modoPagArray', 'nsuIdAutorizacao': 'nsuIdAutorizacao', 'locaisEmbarque':
            'locaisEmbarque'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetApiVendasResponse200, GetApiVendasResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
