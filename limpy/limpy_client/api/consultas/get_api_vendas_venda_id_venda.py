from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_vendas_venda_id_venda_response_200 import GetApiVendasVendaIdVendaResponse200
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
        "url": f"/api/vendas/venda/{id_venda}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetApiVendasVendaIdVendaResponse200]:
    if response.status_code == 200:
        response_200 = GetApiVendasVendaIdVendaResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetApiVendasVendaIdVendaResponse200]:
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
) -> Response[GetApiVendasVendaIdVendaResponse200]:
    r"""Listagem de uma Venda em específico

     Rota destinada a buscar informações de uma venda.

    ## Descrição do retorno

    | **Chave** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `localizador` | string | ID único da venda com prefixo |
    | `data_hora` | string | Data e hora do registro da venda formatada |
    | `status` | string | Caractere identificador do status da venda |
    | `total_liquido` | number | Valor total da venda |
    | `data_hora_inc` | Date | Data e hora do registro da venda UTC |
    | `usuario_logado` | number | Código do usuário do CARD que realizou a reserva |
    | `usuario_logado_nome` | string | Nome do usuário do CARD que realizou a reserva |
    | `usuario_venda` | string | Nome do usuário do E-commerce que realizou a reserva |
    | `codigo_promocional` | string | Código promocional que foi aplicado para a venda |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `local_venda` | string | Nome do estabelecimento que realizou a venda |
    | `pedido_canc_portal` | string | Parâmetro define se o estabelecimento de venda permite realizar
    pedido de cancelamento |
    | `intervalo_tempo_pagamento` | number | Parâmetro que define quanto tempo o usuário tem para
    realizar o pagamento da reserva. Só é permitido em estabelecimentos do tipo AGÊNCIA e E-COMMERCE |
    | `nome_local_venda` | string | Nome do usuário do CARD referente ao estabelecimento de venda |
    | `tick_codigo` | number | Código unitário do cadastro do Tick Ingressos |
    | `tick_nome` | string | Nome do cadastro do Tick Ingressos |
    | `tick_codigo_nome` | string | Código e nome do cadastro do Tick Ingressos |
    | `tick_terminal` | string | Código do terminal que realizou a reserva |
    | `tick_terminal_descricao` | string | Descrição do terminal que realizou a reserva |
    | `cod_local_venda` | number | Código do estabelecimento que realizou a venda |
    | `ponto_venda` | string | URL do e-commerce que realizou a venda |
    | `idorigem` | string | ID da venda no estabelecimento de origem |
    | `origem_venda` | string | Origem da inserção da reserva |
    | `campanha_venda` | string | Campanha da reserva |
    | `nome_titular` | string | Nome do titular da venda |
    | `email_titular` | string | E-mail do titular da venda |
    | `fone_titular` | string | Telefone do titular da venda |
    | `doc_titular` | string | Documento do titular da venda |
    | `nascimento_titular` | string | Data de nascimento do titular da venda formatada |
    | `idioma` | string | Idioma da venda (\"PT\", \"EN\", \"ES\") |
    | `pedido_de_cancelamento` | boolean | Se a venda tem algum item com pedido de cancelamento |
    | `ec_origem` | number | Código do e-commerce que realizou a reserva |
    | `idioma` | string | Idioma da reserva |
    | `ip_comprador` | string | IP do dispositivo do comprador |
    | `pedido_de_cancelamento` | boolean | Informa se a reserva tem algum item com pedido de
    cancelamento |
    | `ec_usuario_f` | number | Código identificador do cliente final do e-commerce |
    | `login_ec_usuario_f` | string | Login do cliente final do e-commerce |
    | `email_ec_usuario_f` | string | E-mail do cliente final do e-commerce |
    | `nome_ec_usuario_f` | string | Nome do cliente final do e-commerce |
    | `documento_ec_usuario_f` | string | Documento do cliente final do e-commerce |
    | `inc_ec_usuario_f` | string | Data de inclusão do cadastro do cliente final do e-commerce |
    | `alt_ec_usuario_f` | string | Data de última alteração do cadastro do cliente final do e-commerce
    |
    | `ec_origem_ec_usuario_f_criacao` | number | Código do usuário do local de venda onde o cliente
    final se registrou, ou seja, em qual e-commerce |
    | `codigo_postal_f` | number | Código postal do usuário que realizou a compra |
    | `bairro_f` | string | Nome do Bairro do usuário que realizou a compra |
    | `municipio_f` | string | Cidade do usuário que realizou a compra |
    | `numero_f` | number | Número do Endereço do usuário que realizou a compra |
    | `endereco_f` | string | Endereço do usuário que realizou a compra |
    | `ibge_f` | number | Código do IBGE da cidade do usuário que realizou a compra |
    | `pais_f` | number | Código do País do usuário que realizou a compra |
    | `desc_pais_f` | string | Descrição do País do usuário que realizou a compra |
    | `estado_f` | string | Estado do usuário do usuário que realizou a compra |
    | `ec_origem_ec_usuario_f` | number | Código do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `nome_usuario_criacao` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `ec_origem_ec_usuario_f_nome` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `quantidade` | number | Quantidade de itens da venda |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `payment_id_pix` | string | Código unitário do pix gerado para pagamento da venda |
    | `qrcode_pix` | string | QRCode do pix gerado para pagamento da venda |
    | `status_pix` | string | Status do pix de pagamento da venda |
    | `data` | string | Data da venda formatada - DD/MM/YYYY |
    | `hora` | string | Hora da venda formatada - HH:mm:ss |
    | `usuario_logado_cod_nome` | string | Código do usuário do CARD que realizou a reserva e Nome do
    usuário do CARD que realizou a reserva |
    | `siglaIdioma` | string | Sigla do Idioma que foi realizado a compra |
    | `status_desc` | string | Label referente ao status da venda  <br>R - Reservado (Sem Pagamento)
    <br>X - Inutilizada (Não confirmou o Pagamento)  <br>A - Aprovada  <br>C - Cancelada (Estorno) |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaIdVendaResponse200]
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
) -> Optional[GetApiVendasVendaIdVendaResponse200]:
    r"""Listagem de uma Venda em específico

     Rota destinada a buscar informações de uma venda.

    ## Descrição do retorno

    | **Chave** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `localizador` | string | ID único da venda com prefixo |
    | `data_hora` | string | Data e hora do registro da venda formatada |
    | `status` | string | Caractere identificador do status da venda |
    | `total_liquido` | number | Valor total da venda |
    | `data_hora_inc` | Date | Data e hora do registro da venda UTC |
    | `usuario_logado` | number | Código do usuário do CARD que realizou a reserva |
    | `usuario_logado_nome` | string | Nome do usuário do CARD que realizou a reserva |
    | `usuario_venda` | string | Nome do usuário do E-commerce que realizou a reserva |
    | `codigo_promocional` | string | Código promocional que foi aplicado para a venda |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `local_venda` | string | Nome do estabelecimento que realizou a venda |
    | `pedido_canc_portal` | string | Parâmetro define se o estabelecimento de venda permite realizar
    pedido de cancelamento |
    | `intervalo_tempo_pagamento` | number | Parâmetro que define quanto tempo o usuário tem para
    realizar o pagamento da reserva. Só é permitido em estabelecimentos do tipo AGÊNCIA e E-COMMERCE |
    | `nome_local_venda` | string | Nome do usuário do CARD referente ao estabelecimento de venda |
    | `tick_codigo` | number | Código unitário do cadastro do Tick Ingressos |
    | `tick_nome` | string | Nome do cadastro do Tick Ingressos |
    | `tick_codigo_nome` | string | Código e nome do cadastro do Tick Ingressos |
    | `tick_terminal` | string | Código do terminal que realizou a reserva |
    | `tick_terminal_descricao` | string | Descrição do terminal que realizou a reserva |
    | `cod_local_venda` | number | Código do estabelecimento que realizou a venda |
    | `ponto_venda` | string | URL do e-commerce que realizou a venda |
    | `idorigem` | string | ID da venda no estabelecimento de origem |
    | `origem_venda` | string | Origem da inserção da reserva |
    | `campanha_venda` | string | Campanha da reserva |
    | `nome_titular` | string | Nome do titular da venda |
    | `email_titular` | string | E-mail do titular da venda |
    | `fone_titular` | string | Telefone do titular da venda |
    | `doc_titular` | string | Documento do titular da venda |
    | `nascimento_titular` | string | Data de nascimento do titular da venda formatada |
    | `idioma` | string | Idioma da venda (\"PT\", \"EN\", \"ES\") |
    | `pedido_de_cancelamento` | boolean | Se a venda tem algum item com pedido de cancelamento |
    | `ec_origem` | number | Código do e-commerce que realizou a reserva |
    | `idioma` | string | Idioma da reserva |
    | `ip_comprador` | string | IP do dispositivo do comprador |
    | `pedido_de_cancelamento` | boolean | Informa se a reserva tem algum item com pedido de
    cancelamento |
    | `ec_usuario_f` | number | Código identificador do cliente final do e-commerce |
    | `login_ec_usuario_f` | string | Login do cliente final do e-commerce |
    | `email_ec_usuario_f` | string | E-mail do cliente final do e-commerce |
    | `nome_ec_usuario_f` | string | Nome do cliente final do e-commerce |
    | `documento_ec_usuario_f` | string | Documento do cliente final do e-commerce |
    | `inc_ec_usuario_f` | string | Data de inclusão do cadastro do cliente final do e-commerce |
    | `alt_ec_usuario_f` | string | Data de última alteração do cadastro do cliente final do e-commerce
    |
    | `ec_origem_ec_usuario_f_criacao` | number | Código do usuário do local de venda onde o cliente
    final se registrou, ou seja, em qual e-commerce |
    | `codigo_postal_f` | number | Código postal do usuário que realizou a compra |
    | `bairro_f` | string | Nome do Bairro do usuário que realizou a compra |
    | `municipio_f` | string | Cidade do usuário que realizou a compra |
    | `numero_f` | number | Número do Endereço do usuário que realizou a compra |
    | `endereco_f` | string | Endereço do usuário que realizou a compra |
    | `ibge_f` | number | Código do IBGE da cidade do usuário que realizou a compra |
    | `pais_f` | number | Código do País do usuário que realizou a compra |
    | `desc_pais_f` | string | Descrição do País do usuário que realizou a compra |
    | `estado_f` | string | Estado do usuário do usuário que realizou a compra |
    | `ec_origem_ec_usuario_f` | number | Código do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `nome_usuario_criacao` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `ec_origem_ec_usuario_f_nome` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `quantidade` | number | Quantidade de itens da venda |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `payment_id_pix` | string | Código unitário do pix gerado para pagamento da venda |
    | `qrcode_pix` | string | QRCode do pix gerado para pagamento da venda |
    | `status_pix` | string | Status do pix de pagamento da venda |
    | `data` | string | Data da venda formatada - DD/MM/YYYY |
    | `hora` | string | Hora da venda formatada - HH:mm:ss |
    | `usuario_logado_cod_nome` | string | Código do usuário do CARD que realizou a reserva e Nome do
    usuário do CARD que realizou a reserva |
    | `siglaIdioma` | string | Sigla do Idioma que foi realizado a compra |
    | `status_desc` | string | Label referente ao status da venda  <br>R - Reservado (Sem Pagamento)
    <br>X - Inutilizada (Não confirmou o Pagamento)  <br>A - Aprovada  <br>C - Cancelada (Estorno) |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaIdVendaResponse200
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
) -> Response[GetApiVendasVendaIdVendaResponse200]:
    r"""Listagem de uma Venda em específico

     Rota destinada a buscar informações de uma venda.

    ## Descrição do retorno

    | **Chave** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `localizador` | string | ID único da venda com prefixo |
    | `data_hora` | string | Data e hora do registro da venda formatada |
    | `status` | string | Caractere identificador do status da venda |
    | `total_liquido` | number | Valor total da venda |
    | `data_hora_inc` | Date | Data e hora do registro da venda UTC |
    | `usuario_logado` | number | Código do usuário do CARD que realizou a reserva |
    | `usuario_logado_nome` | string | Nome do usuário do CARD que realizou a reserva |
    | `usuario_venda` | string | Nome do usuário do E-commerce que realizou a reserva |
    | `codigo_promocional` | string | Código promocional que foi aplicado para a venda |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `local_venda` | string | Nome do estabelecimento que realizou a venda |
    | `pedido_canc_portal` | string | Parâmetro define se o estabelecimento de venda permite realizar
    pedido de cancelamento |
    | `intervalo_tempo_pagamento` | number | Parâmetro que define quanto tempo o usuário tem para
    realizar o pagamento da reserva. Só é permitido em estabelecimentos do tipo AGÊNCIA e E-COMMERCE |
    | `nome_local_venda` | string | Nome do usuário do CARD referente ao estabelecimento de venda |
    | `tick_codigo` | number | Código unitário do cadastro do Tick Ingressos |
    | `tick_nome` | string | Nome do cadastro do Tick Ingressos |
    | `tick_codigo_nome` | string | Código e nome do cadastro do Tick Ingressos |
    | `tick_terminal` | string | Código do terminal que realizou a reserva |
    | `tick_terminal_descricao` | string | Descrição do terminal que realizou a reserva |
    | `cod_local_venda` | number | Código do estabelecimento que realizou a venda |
    | `ponto_venda` | string | URL do e-commerce que realizou a venda |
    | `idorigem` | string | ID da venda no estabelecimento de origem |
    | `origem_venda` | string | Origem da inserção da reserva |
    | `campanha_venda` | string | Campanha da reserva |
    | `nome_titular` | string | Nome do titular da venda |
    | `email_titular` | string | E-mail do titular da venda |
    | `fone_titular` | string | Telefone do titular da venda |
    | `doc_titular` | string | Documento do titular da venda |
    | `nascimento_titular` | string | Data de nascimento do titular da venda formatada |
    | `idioma` | string | Idioma da venda (\"PT\", \"EN\", \"ES\") |
    | `pedido_de_cancelamento` | boolean | Se a venda tem algum item com pedido de cancelamento |
    | `ec_origem` | number | Código do e-commerce que realizou a reserva |
    | `idioma` | string | Idioma da reserva |
    | `ip_comprador` | string | IP do dispositivo do comprador |
    | `pedido_de_cancelamento` | boolean | Informa se a reserva tem algum item com pedido de
    cancelamento |
    | `ec_usuario_f` | number | Código identificador do cliente final do e-commerce |
    | `login_ec_usuario_f` | string | Login do cliente final do e-commerce |
    | `email_ec_usuario_f` | string | E-mail do cliente final do e-commerce |
    | `nome_ec_usuario_f` | string | Nome do cliente final do e-commerce |
    | `documento_ec_usuario_f` | string | Documento do cliente final do e-commerce |
    | `inc_ec_usuario_f` | string | Data de inclusão do cadastro do cliente final do e-commerce |
    | `alt_ec_usuario_f` | string | Data de última alteração do cadastro do cliente final do e-commerce
    |
    | `ec_origem_ec_usuario_f_criacao` | number | Código do usuário do local de venda onde o cliente
    final se registrou, ou seja, em qual e-commerce |
    | `codigo_postal_f` | number | Código postal do usuário que realizou a compra |
    | `bairro_f` | string | Nome do Bairro do usuário que realizou a compra |
    | `municipio_f` | string | Cidade do usuário que realizou a compra |
    | `numero_f` | number | Número do Endereço do usuário que realizou a compra |
    | `endereco_f` | string | Endereço do usuário que realizou a compra |
    | `ibge_f` | number | Código do IBGE da cidade do usuário que realizou a compra |
    | `pais_f` | number | Código do País do usuário que realizou a compra |
    | `desc_pais_f` | string | Descrição do País do usuário que realizou a compra |
    | `estado_f` | string | Estado do usuário do usuário que realizou a compra |
    | `ec_origem_ec_usuario_f` | number | Código do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `nome_usuario_criacao` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `ec_origem_ec_usuario_f_nome` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `quantidade` | number | Quantidade de itens da venda |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `payment_id_pix` | string | Código unitário do pix gerado para pagamento da venda |
    | `qrcode_pix` | string | QRCode do pix gerado para pagamento da venda |
    | `status_pix` | string | Status do pix de pagamento da venda |
    | `data` | string | Data da venda formatada - DD/MM/YYYY |
    | `hora` | string | Hora da venda formatada - HH:mm:ss |
    | `usuario_logado_cod_nome` | string | Código do usuário do CARD que realizou a reserva e Nome do
    usuário do CARD que realizou a reserva |
    | `siglaIdioma` | string | Sigla do Idioma que foi realizado a compra |
    | `status_desc` | string | Label referente ao status da venda  <br>R - Reservado (Sem Pagamento)
    <br>X - Inutilizada (Não confirmou o Pagamento)  <br>A - Aprovada  <br>C - Cancelada (Estorno) |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaIdVendaResponse200]
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
) -> Optional[GetApiVendasVendaIdVendaResponse200]:
    r"""Listagem de uma Venda em específico

     Rota destinada a buscar informações de uma venda.

    ## Descrição do retorno

    | **Chave** | **Tipo** | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | ID único da venda |
    | `localizador` | string | ID único da venda com prefixo |
    | `data_hora` | string | Data e hora do registro da venda formatada |
    | `status` | string | Caractere identificador do status da venda |
    | `total_liquido` | number | Valor total da venda |
    | `data_hora_inc` | Date | Data e hora do registro da venda UTC |
    | `usuario_logado` | number | Código do usuário do CARD que realizou a reserva |
    | `usuario_logado_nome` | string | Nome do usuário do CARD que realizou a reserva |
    | `usuario_venda` | string | Nome do usuário do E-commerce que realizou a reserva |
    | `codigo_promocional` | string | Código promocional que foi aplicado para a venda |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `local_venda` | string | Nome do estabelecimento que realizou a venda |
    | `pedido_canc_portal` | string | Parâmetro define se o estabelecimento de venda permite realizar
    pedido de cancelamento |
    | `intervalo_tempo_pagamento` | number | Parâmetro que define quanto tempo o usuário tem para
    realizar o pagamento da reserva. Só é permitido em estabelecimentos do tipo AGÊNCIA e E-COMMERCE |
    | `nome_local_venda` | string | Nome do usuário do CARD referente ao estabelecimento de venda |
    | `tick_codigo` | number | Código unitário do cadastro do Tick Ingressos |
    | `tick_nome` | string | Nome do cadastro do Tick Ingressos |
    | `tick_codigo_nome` | string | Código e nome do cadastro do Tick Ingressos |
    | `tick_terminal` | string | Código do terminal que realizou a reserva |
    | `tick_terminal_descricao` | string | Descrição do terminal que realizou a reserva |
    | `cod_local_venda` | number | Código do estabelecimento que realizou a venda |
    | `ponto_venda` | string | URL do e-commerce que realizou a venda |
    | `idorigem` | string | ID da venda no estabelecimento de origem |
    | `origem_venda` | string | Origem da inserção da reserva |
    | `campanha_venda` | string | Campanha da reserva |
    | `nome_titular` | string | Nome do titular da venda |
    | `email_titular` | string | E-mail do titular da venda |
    | `fone_titular` | string | Telefone do titular da venda |
    | `doc_titular` | string | Documento do titular da venda |
    | `nascimento_titular` | string | Data de nascimento do titular da venda formatada |
    | `idioma` | string | Idioma da venda (\"PT\", \"EN\", \"ES\") |
    | `pedido_de_cancelamento` | boolean | Se a venda tem algum item com pedido de cancelamento |
    | `ec_origem` | number | Código do e-commerce que realizou a reserva |
    | `idioma` | string | Idioma da reserva |
    | `ip_comprador` | string | IP do dispositivo do comprador |
    | `pedido_de_cancelamento` | boolean | Informa se a reserva tem algum item com pedido de
    cancelamento |
    | `ec_usuario_f` | number | Código identificador do cliente final do e-commerce |
    | `login_ec_usuario_f` | string | Login do cliente final do e-commerce |
    | `email_ec_usuario_f` | string | E-mail do cliente final do e-commerce |
    | `nome_ec_usuario_f` | string | Nome do cliente final do e-commerce |
    | `documento_ec_usuario_f` | string | Documento do cliente final do e-commerce |
    | `inc_ec_usuario_f` | string | Data de inclusão do cadastro do cliente final do e-commerce |
    | `alt_ec_usuario_f` | string | Data de última alteração do cadastro do cliente final do e-commerce
    |
    | `ec_origem_ec_usuario_f_criacao` | number | Código do usuário do local de venda onde o cliente
    final se registrou, ou seja, em qual e-commerce |
    | `codigo_postal_f` | number | Código postal do usuário que realizou a compra |
    | `bairro_f` | string | Nome do Bairro do usuário que realizou a compra |
    | `municipio_f` | string | Cidade do usuário que realizou a compra |
    | `numero_f` | number | Número do Endereço do usuário que realizou a compra |
    | `endereco_f` | string | Endereço do usuário que realizou a compra |
    | `ibge_f` | number | Código do IBGE da cidade do usuário que realizou a compra |
    | `pais_f` | number | Código do País do usuário que realizou a compra |
    | `desc_pais_f` | string | Descrição do País do usuário que realizou a compra |
    | `estado_f` | string | Estado do usuário do usuário que realizou a compra |
    | `ec_origem_ec_usuario_f` | number | Código do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `nome_usuario_criacao` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `ec_origem_ec_usuario_f_nome` | string | Nome do usuário do local de venda onde o cliente final se
    registrou, ou seja, em qual e-commerce |
    | `quantidade` | number | Quantidade de itens da venda |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `payment_id_pix` | string | Código unitário do pix gerado para pagamento da venda |
    | `qrcode_pix` | string | QRCode do pix gerado para pagamento da venda |
    | `status_pix` | string | Status do pix de pagamento da venda |
    | `data` | string | Data da venda formatada - DD/MM/YYYY |
    | `hora` | string | Hora da venda formatada - HH:mm:ss |
    | `usuario_logado_cod_nome` | string | Código do usuário do CARD que realizou a reserva e Nome do
    usuário do CARD que realizou a reserva |
    | `siglaIdioma` | string | Sigla do Idioma que foi realizado a compra |
    | `status_desc` | string | Label referente ao status da venda  <br>R - Reservado (Sem Pagamento)
    <br>X - Inutilizada (Não confirmou o Pagamento)  <br>A - Aprovada  <br>C - Cancelada (Estorno) |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaIdVendaResponse200
    """

    return (
        await asyncio_detailed(
            id_venda=id_venda,
            client=client,
            authorization=authorization,
        )
    ).parsed
