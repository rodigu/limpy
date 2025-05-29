from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_vendas_venda_pagamentos_id_venda_response_200 import (
    GetApiVendasVendaPagamentosIdVendaResponse200,
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
        "url": f"/api/vendas/venda/pagamentos/{id_venda}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetApiVendasVendaPagamentosIdVendaResponse200]:
    if response.status_code == 200:
        response_200 = GetApiVendasVendaPagamentosIdVendaResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetApiVendasVendaPagamentosIdVendaResponse200]:
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
) -> Response[GetApiVendasVendaPagamentosIdVendaResponse200]:
    r"""Consultar pagamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    ## Descrição do retorno

    | Chave | Tipo | Descrição |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `valor` | number | Valor de um Item da venda |
    | `cartao_bandeira` | string | Bandeira Do Cartão Utilizado na Venda |
    | `parcela` | number | Número de Parcelas que foi escolhido na hora do Pagamento |
    | `cartao_autorizacao` | number | Código de Autorização do Cartão |
    | `cartao_nsu` | number | Código NSU do Cartão |
    | `cartao_terminal_nsu` | number | Código do Terminal NSU do Cartão |
    | `b_comprovante` | string | Armazena Objeto enviado para adquirente, e o retorno da mesma |
    | `cartao_bin` | number | São os seis primeiros números do cartão |
    | `cartao_quatro_ult` | number | Útimos quatro dígitos do Cartão que foi usado na Compra |
    | `ip_comprador` | number | IP da Máquina de quem realizou a compra |
    | `cartao_tipo` | string | Tipo do Crtão utilizado na Compra |
    | `forma_pag` | number | Forma de Pagamento Utilizado |
    | `data_hora_autorizacao` | string | Data e Hora que o Pagamento foi autorizado na
    Adquirente(Cartão) ou no Banco(PIX) |
    | `ambiente` | string | Ambiente que foi realizado a compra (\"H\": Homologação, \"P\": Produção) |
    | `nome_adquirente` | string | Nome da Adquierente do Pagamento |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaPagamentosIdVendaResponse200]
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
) -> Optional[GetApiVendasVendaPagamentosIdVendaResponse200]:
    r"""Consultar pagamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    ## Descrição do retorno

    | Chave | Tipo | Descrição |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `valor` | number | Valor de um Item da venda |
    | `cartao_bandeira` | string | Bandeira Do Cartão Utilizado na Venda |
    | `parcela` | number | Número de Parcelas que foi escolhido na hora do Pagamento |
    | `cartao_autorizacao` | number | Código de Autorização do Cartão |
    | `cartao_nsu` | number | Código NSU do Cartão |
    | `cartao_terminal_nsu` | number | Código do Terminal NSU do Cartão |
    | `b_comprovante` | string | Armazena Objeto enviado para adquirente, e o retorno da mesma |
    | `cartao_bin` | number | São os seis primeiros números do cartão |
    | `cartao_quatro_ult` | number | Útimos quatro dígitos do Cartão que foi usado na Compra |
    | `ip_comprador` | number | IP da Máquina de quem realizou a compra |
    | `cartao_tipo` | string | Tipo do Crtão utilizado na Compra |
    | `forma_pag` | number | Forma de Pagamento Utilizado |
    | `data_hora_autorizacao` | string | Data e Hora que o Pagamento foi autorizado na
    Adquirente(Cartão) ou no Banco(PIX) |
    | `ambiente` | string | Ambiente que foi realizado a compra (\"H\": Homologação, \"P\": Produção) |
    | `nome_adquirente` | string | Nome da Adquierente do Pagamento |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaPagamentosIdVendaResponse200
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
) -> Response[GetApiVendasVendaPagamentosIdVendaResponse200]:
    r"""Consultar pagamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    ## Descrição do retorno

    | Chave | Tipo | Descrição |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `valor` | number | Valor de um Item da venda |
    | `cartao_bandeira` | string | Bandeira Do Cartão Utilizado na Venda |
    | `parcela` | number | Número de Parcelas que foi escolhido na hora do Pagamento |
    | `cartao_autorizacao` | number | Código de Autorização do Cartão |
    | `cartao_nsu` | number | Código NSU do Cartão |
    | `cartao_terminal_nsu` | number | Código do Terminal NSU do Cartão |
    | `b_comprovante` | string | Armazena Objeto enviado para adquirente, e o retorno da mesma |
    | `cartao_bin` | number | São os seis primeiros números do cartão |
    | `cartao_quatro_ult` | number | Útimos quatro dígitos do Cartão que foi usado na Compra |
    | `ip_comprador` | number | IP da Máquina de quem realizou a compra |
    | `cartao_tipo` | string | Tipo do Crtão utilizado na Compra |
    | `forma_pag` | number | Forma de Pagamento Utilizado |
    | `data_hora_autorizacao` | string | Data e Hora que o Pagamento foi autorizado na
    Adquirente(Cartão) ou no Banco(PIX) |
    | `ambiente` | string | Ambiente que foi realizado a compra (\"H\": Homologação, \"P\": Produção) |
    | `nome_adquirente` | string | Nome da Adquierente do Pagamento |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaPagamentosIdVendaResponse200]
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
) -> Optional[GetApiVendasVendaPagamentosIdVendaResponse200]:
    r"""Consultar pagamentos da venda

     Rota destinada a buscar informações sobre o cancelamento de uma venda.

    ## Descrição do retorno

    | Chave | Tipo | Descrição |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `valor` | number | Valor de um Item da venda |
    | `cartao_bandeira` | string | Bandeira Do Cartão Utilizado na Venda |
    | `parcela` | number | Número de Parcelas que foi escolhido na hora do Pagamento |
    | `cartao_autorizacao` | number | Código de Autorização do Cartão |
    | `cartao_nsu` | number | Código NSU do Cartão |
    | `cartao_terminal_nsu` | number | Código do Terminal NSU do Cartão |
    | `b_comprovante` | string | Armazena Objeto enviado para adquirente, e o retorno da mesma |
    | `cartao_bin` | number | São os seis primeiros números do cartão |
    | `cartao_quatro_ult` | number | Útimos quatro dígitos do Cartão que foi usado na Compra |
    | `ip_comprador` | number | IP da Máquina de quem realizou a compra |
    | `cartao_tipo` | string | Tipo do Crtão utilizado na Compra |
    | `forma_pag` | number | Forma de Pagamento Utilizado |
    | `data_hora_autorizacao` | string | Data e Hora que o Pagamento foi autorizado na
    Adquirente(Cartão) ou no Banco(PIX) |
    | `ambiente` | string | Ambiente que foi realizado a compra (\"H\": Homologação, \"P\": Produção) |
    | `nome_adquirente` | string | Nome da Adquierente do Pagamento |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaPagamentosIdVendaResponse200
    """

    return (
        await asyncio_detailed(
            id_venda=id_venda,
            client=client,
            authorization=authorization,
        )
    ).parsed
