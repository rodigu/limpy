from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_vendas_venda_itens_id_venda_response_200 import GetApiVendasVendaItensIdVendaResponse200
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
        "url": f"/api/vendas/venda/itens/{id_venda}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetApiVendasVendaItensIdVendaResponse200]:
    if response.status_code == 200:
        response_200 = GetApiVendasVendaItensIdVendaResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetApiVendasVendaItensIdVendaResponse200]:
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
) -> Response[GetApiVendasVendaItensIdVendaResponse200]:
    r"""Consulta de itens de uma venda

     Rota com o objectivo de retornar dados dos ingressos de uma venda, juntamente com as receitas de
    cada um.

    ## Dados do retorno

    | Atributo | Tipo | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | Código da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `uf` | string | Estado escolhido pelo titular da reserva |
    | `pais` | number | Código do país escolhido pelo titular da reserva |
    | `desc_pais` | strin | Nome do país escolhido pelo titular da reserva |
    | `bilhete` | number | Código do bilhete |
    | `nome_bilhete` | string | Nome do Bilhete |
    | `controle_disponibilidade` | string | Caractere que define o tipo de controle de disponibilidade
    do item: \"H\" - Horários, \"V\" - Vagas, \"M\" - Mapa de Assentos |
    | `venda_sem_data_visita` | string | Define se a venda foi realizada sem data de visita escolhida -
    \"S\"/\"N\" |
    | `texto_impressao` | string | Texto para a impressão do ingresso |
    | `texto_impressao_horario` | string | Texto para a impressão do ingresso |
    | `texto_hora_vis_voucher` | string | Texto para a impressão - refentente à disponibilidade |
    | `texto_data_vis_voucher` | string | Texto para a impressão - refentente à data de visita |
    | `texto_embarque_voucher` | string | Texto para a impressão - refentente ao local de embarque |
    | `texto_sessao_imp` | string | Texto para a impressão - refentente à sessão |
    | `texto_vagao` | string | Texto para a impressão - refentente ao vagão |
    | `texto_poltrona` | string | Texto para a impressão - refentente à poltrona |
    | `permite_visualizar_ingressos` | booelan | Parâmetro que verifica se é permitido a visualização de
    Ingressos |
    | `texto_motivo_nao_ver_ing_ec` | string | Texto explicando o motivo de não ser possível visualizar
    o ingresso |
    | `mostra_horario_final` | string | Define se o bilhete irá informar o horário final |
    | `imprime_valor_tick` | booelan | Parâmetro que verifica se Imprime o Valor no Tick |
    | `utiliza_qrcode` | boolean | Se o ingresso utiliza qrcode ou não |
    | `categoria` | number | Código da categoria |
    | `nome_categoria` | string | Nome da categoria |
    | `privativo` | boolean | Define se a categoria é do tipo privativo |
    | `imagem_categoria` | string | Imagem referente à categoria |
    | `operacao` | number | Código da operação |
    | `cancelado` | boolean | Define se o item foi cancelado ou não |
    | `cancelamentos_codigo` | number Array | Código dos cancelamentos relacionados ao item |
    | `data_hora_pedido_canc` | string | Data e Hora do Pedido de Cancelamento |
    | `quantidade` | number | Quantidade de ingressos |
    | `vlr_total` | number | Valor total do item (contém descontos de cupom) |
    | `vlr_unitario` | number | Valor unitário do ingresso (valor bruto) |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `atrativo_nome` | string | Nome do visitante |
    | `atrativo_doc` | string | Documento do visitante |
    | `atrativo_email` | string | E-mail do visitante |
    | `atrativo_convenio` | string | Código do visitante |
    | `observacao_convenio` | string | Texto de Observações do Convênio |
    | `nome_convenio` | string | Nome do convênio do visitante |
    | `atrativo_data_nasc` | string | Data de nascimento do visitante |
    | `lb_int_tipo_venda` | string | ?? |
    | `contrib_fundo` | boolean | Se foi escolhido contribuir com o Fundo do ingresso |
    | `morador_tipo_doc` | string | Tipo do documento do morador local |
    | `qr_code_exp` | string | QRcode do item |
    | `card_id` | number |  |
    | `descricao_venda` | string | Descrição da venda |
    | `dados_incompletos` | boolean | Define se na hora da reserva, os dados dos visitantes não foram
    preenchidos |
    | `local_de_apanhe` | number | Código do local de apanhe |
    | `local_de_apanhe_nome` | string | Nome do local de apanhe |
    | `local_de_apanhe_endereco` | string | Endereço do local de apanhe |
    | `data_visita` | string | Data de visita (primeiro entre receitas) |
    | `data_visita_final` | string | Data de visita final entre as receitas |
    | `dias_para_alterar_visitantes` | number | Dias limite antes da data de visita para alterar os
    dados dos visitantes |
    | `integracao_carteiras_digital` | string | Verifica se está habilitado Integração com Carteiras
    Digitais |
    | `permite_info_visitante_depois` | booelan | Parâmetro que Ativa/Desativa a opção de preencher os
    dados do Visitante após finalizar a compra |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `remarca_visitante` | boolean | Verifica se o bilhete permite alterar dados do visitante na
    remarcação |
    | `remarca_data_visita` | boolean | Verifica se o bilhete permite alterar data de visita na
    remarcação |
    | `remarca_hora_visita` | boolean | Verifica se o bilhete permite alterar horário da visita na
    remarcação |
    | `receitas[]` | Object Array | Lista de Receitas disponíveis para o Item |
    | `receitas[].codigo` | number | ID da Venda |
    | `receitas[].sequencia` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].tipo_receita` | number | Código da receita |
    | `receitas[].preco` | number | Preço Definido para o Produto na Receita determinada |
    | `receitas[].preco_bruto` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].prog_horario` | number | Código da Programação de Horários para o Item na receita
    informada |
    | `receitas[].prog_seq` | number | Sequencia do Horário na Programação de Horários para o Item na
    receita informada |
    | `receitas[].lb_vou_idvenda` | string | ID da venda na bilheteria |
    | `receitas[].lb_vou_datahora` | string | Data e Hora da venda na bilheteria |
    | `receitas[].estabelec` | string | Nome do Estabelecimento |
    | `receitas[].versao` | number | Versão do cadastro do estabelecimento em relação à integração com a
    bilheteria |
    | `receitas[].estabelec_dest` | number | Estabelecimento de Destino do Item |
    | `receitas[].id_produto` | number | ID Do Item |
    | `receitas[].data_visita` | date | Data de visita (primeiro entre receitas) |
    | `receitas[].data_visita_final` | date | Data de visita final entre as receitas |
    | `receitas[].hoje_entre_visitas` | date | Se a data atual está entre a data de visita inicial e
    final |
    | `receitas[].horario_str` | string | Descrição do horário ou vaga |
    | `receitas[].local_embarque` | number | Código do Local de Embarque |
    | `receitas[].local_embarque_nome` | string | Nome do Local de Embarque |
    | `receitas[].local_embarque_desc` | string | Descrição sobre o Local de Embarque |
    | `receitas[].sessao` | number | Código da Sessão |
    | `receitas[].sessao_nome` | string | Nome Da Sessão |
    | `receitas[].placa` | string |  |
    | `receitas[].poltrona` | string |  |
    | `receitas[].mostra_horario_final` | string | Verifica se Mostra o Horário Final |
    | `receitas[].credenciado` | number | Código do Credenciado Cadastrado |
    | `receitas[].credenciado_nome` | string | Nome do Credenciado Cadastrado |
    | `receitas[].credenciado_cpf` | number | CPF do Credenciado Cadastrado |
    | `receitas[]idioma_escolhido` | string | Idioma Escolhido |
    | `receitas[].habilita_vendas_dias_corridos` | boolean | Parâmetro para geração de QrCode para a
    quantidade determinada de dias após o dia escolhido para a visita |
    | `receitas[].evento` | boolean | Parâmetro que verifica se o Item é para um Evento |
    | `receitas[].data_hora_utilizacao` | string | Data e Hora da Utilização do Item |
    | `receitas[].leituras[]` | Object Array |  |
    | `receitas[].leituras[].sequencia` | number | Sequência do item |
    | `receitas[].leituras[].seq` | number | Sequência da receita |
    | `receitas[].leituras[].seq_leitura` | number | Sequência da leitura |
    | `receitas[].leituras[].usu_data_hora` | string | Data e Hora da leitura <br>Formato: **YYYY-MM-DD
    HH:mm** |
    | `receitas[].leituras[].uso_terminal` | string | Identificador do terminal da leitura  |
    | `receitas[].tem_leitura_hoje` | boolean | Parâmetro que identifica se Possui Leituras disponíveis
    para o dia atual |
    | `receitas[].horario_str_formatado` | string | Horário escolhido para a Data de Visita já formatado
    |
    | `receitasAgrupadas[]` | Object Array | Lista de Receitas Agrupadas disponíveis para o Item |
    | `receitasAgrupadas[].tipo_receita` | number | ID da Venda |
    | `receitasAgrupadas[].receita` | string | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].data_visita` | date | Código da receita |
    | `receitasAgrupadas[].data_visita_final` | date | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].credenciado` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_nome` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_desc` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].sessao` | number | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].sessao_nome` | string | Nome da Sessão |
    | `receitasAgrupadas[].poltrona` | number | Código da Poltrona |
    | `receitasAgrupadas[].placa` | string |  |
    | `receitasAgrupadas[].horario_str` | string | Horário da Receita em string |
    | `receitasAgrupadas[].data_hora_utilizacao` | string | Data e Hora de Utilização do Item |
    | `receitasAgrupadas[].leituras[]` | Array | Array de Leituras feitas no Item |
    | `tem_leitura_hoje` | string | Verifica se Há Leituras Disponíveis para a Data atual |
    | `qnt_receitas` | string | Quantidade de Receitas No Item |
    | `qnt_receitas_lidas` | string | Quantidade de Receitas Lidas |
    | `qnt_receitas_utilizadas` | string | Quantidade de Receitas Utilizadas |
    | `local_embarque` | string | Código do Local de Embarque |
    | `desc_local_embarque` | string | Descrição do Local de Embarque |
    | `temporada` | string | Código da Temporada |
    | `temporada_nome` | string | Nome da Temporada |
    | `horario_str` | string | Horário em formato de String |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaItensIdVendaResponse200]
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
) -> Optional[GetApiVendasVendaItensIdVendaResponse200]:
    r"""Consulta de itens de uma venda

     Rota com o objectivo de retornar dados dos ingressos de uma venda, juntamente com as receitas de
    cada um.

    ## Dados do retorno

    | Atributo | Tipo | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | Código da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `uf` | string | Estado escolhido pelo titular da reserva |
    | `pais` | number | Código do país escolhido pelo titular da reserva |
    | `desc_pais` | strin | Nome do país escolhido pelo titular da reserva |
    | `bilhete` | number | Código do bilhete |
    | `nome_bilhete` | string | Nome do Bilhete |
    | `controle_disponibilidade` | string | Caractere que define o tipo de controle de disponibilidade
    do item: \"H\" - Horários, \"V\" - Vagas, \"M\" - Mapa de Assentos |
    | `venda_sem_data_visita` | string | Define se a venda foi realizada sem data de visita escolhida -
    \"S\"/\"N\" |
    | `texto_impressao` | string | Texto para a impressão do ingresso |
    | `texto_impressao_horario` | string | Texto para a impressão do ingresso |
    | `texto_hora_vis_voucher` | string | Texto para a impressão - refentente à disponibilidade |
    | `texto_data_vis_voucher` | string | Texto para a impressão - refentente à data de visita |
    | `texto_embarque_voucher` | string | Texto para a impressão - refentente ao local de embarque |
    | `texto_sessao_imp` | string | Texto para a impressão - refentente à sessão |
    | `texto_vagao` | string | Texto para a impressão - refentente ao vagão |
    | `texto_poltrona` | string | Texto para a impressão - refentente à poltrona |
    | `permite_visualizar_ingressos` | booelan | Parâmetro que verifica se é permitido a visualização de
    Ingressos |
    | `texto_motivo_nao_ver_ing_ec` | string | Texto explicando o motivo de não ser possível visualizar
    o ingresso |
    | `mostra_horario_final` | string | Define se o bilhete irá informar o horário final |
    | `imprime_valor_tick` | booelan | Parâmetro que verifica se Imprime o Valor no Tick |
    | `utiliza_qrcode` | boolean | Se o ingresso utiliza qrcode ou não |
    | `categoria` | number | Código da categoria |
    | `nome_categoria` | string | Nome da categoria |
    | `privativo` | boolean | Define se a categoria é do tipo privativo |
    | `imagem_categoria` | string | Imagem referente à categoria |
    | `operacao` | number | Código da operação |
    | `cancelado` | boolean | Define se o item foi cancelado ou não |
    | `cancelamentos_codigo` | number Array | Código dos cancelamentos relacionados ao item |
    | `data_hora_pedido_canc` | string | Data e Hora do Pedido de Cancelamento |
    | `quantidade` | number | Quantidade de ingressos |
    | `vlr_total` | number | Valor total do item (contém descontos de cupom) |
    | `vlr_unitario` | number | Valor unitário do ingresso (valor bruto) |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `atrativo_nome` | string | Nome do visitante |
    | `atrativo_doc` | string | Documento do visitante |
    | `atrativo_email` | string | E-mail do visitante |
    | `atrativo_convenio` | string | Código do visitante |
    | `observacao_convenio` | string | Texto de Observações do Convênio |
    | `nome_convenio` | string | Nome do convênio do visitante |
    | `atrativo_data_nasc` | string | Data de nascimento do visitante |
    | `lb_int_tipo_venda` | string | ?? |
    | `contrib_fundo` | boolean | Se foi escolhido contribuir com o Fundo do ingresso |
    | `morador_tipo_doc` | string | Tipo do documento do morador local |
    | `qr_code_exp` | string | QRcode do item |
    | `card_id` | number |  |
    | `descricao_venda` | string | Descrição da venda |
    | `dados_incompletos` | boolean | Define se na hora da reserva, os dados dos visitantes não foram
    preenchidos |
    | `local_de_apanhe` | number | Código do local de apanhe |
    | `local_de_apanhe_nome` | string | Nome do local de apanhe |
    | `local_de_apanhe_endereco` | string | Endereço do local de apanhe |
    | `data_visita` | string | Data de visita (primeiro entre receitas) |
    | `data_visita_final` | string | Data de visita final entre as receitas |
    | `dias_para_alterar_visitantes` | number | Dias limite antes da data de visita para alterar os
    dados dos visitantes |
    | `integracao_carteiras_digital` | string | Verifica se está habilitado Integração com Carteiras
    Digitais |
    | `permite_info_visitante_depois` | booelan | Parâmetro que Ativa/Desativa a opção de preencher os
    dados do Visitante após finalizar a compra |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `remarca_visitante` | boolean | Verifica se o bilhete permite alterar dados do visitante na
    remarcação |
    | `remarca_data_visita` | boolean | Verifica se o bilhete permite alterar data de visita na
    remarcação |
    | `remarca_hora_visita` | boolean | Verifica se o bilhete permite alterar horário da visita na
    remarcação |
    | `receitas[]` | Object Array | Lista de Receitas disponíveis para o Item |
    | `receitas[].codigo` | number | ID da Venda |
    | `receitas[].sequencia` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].tipo_receita` | number | Código da receita |
    | `receitas[].preco` | number | Preço Definido para o Produto na Receita determinada |
    | `receitas[].preco_bruto` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].prog_horario` | number | Código da Programação de Horários para o Item na receita
    informada |
    | `receitas[].prog_seq` | number | Sequencia do Horário na Programação de Horários para o Item na
    receita informada |
    | `receitas[].lb_vou_idvenda` | string | ID da venda na bilheteria |
    | `receitas[].lb_vou_datahora` | string | Data e Hora da venda na bilheteria |
    | `receitas[].estabelec` | string | Nome do Estabelecimento |
    | `receitas[].versao` | number | Versão do cadastro do estabelecimento em relação à integração com a
    bilheteria |
    | `receitas[].estabelec_dest` | number | Estabelecimento de Destino do Item |
    | `receitas[].id_produto` | number | ID Do Item |
    | `receitas[].data_visita` | date | Data de visita (primeiro entre receitas) |
    | `receitas[].data_visita_final` | date | Data de visita final entre as receitas |
    | `receitas[].hoje_entre_visitas` | date | Se a data atual está entre a data de visita inicial e
    final |
    | `receitas[].horario_str` | string | Descrição do horário ou vaga |
    | `receitas[].local_embarque` | number | Código do Local de Embarque |
    | `receitas[].local_embarque_nome` | string | Nome do Local de Embarque |
    | `receitas[].local_embarque_desc` | string | Descrição sobre o Local de Embarque |
    | `receitas[].sessao` | number | Código da Sessão |
    | `receitas[].sessao_nome` | string | Nome Da Sessão |
    | `receitas[].placa` | string |  |
    | `receitas[].poltrona` | string |  |
    | `receitas[].mostra_horario_final` | string | Verifica se Mostra o Horário Final |
    | `receitas[].credenciado` | number | Código do Credenciado Cadastrado |
    | `receitas[].credenciado_nome` | string | Nome do Credenciado Cadastrado |
    | `receitas[].credenciado_cpf` | number | CPF do Credenciado Cadastrado |
    | `receitas[]idioma_escolhido` | string | Idioma Escolhido |
    | `receitas[].habilita_vendas_dias_corridos` | boolean | Parâmetro para geração de QrCode para a
    quantidade determinada de dias após o dia escolhido para a visita |
    | `receitas[].evento` | boolean | Parâmetro que verifica se o Item é para um Evento |
    | `receitas[].data_hora_utilizacao` | string | Data e Hora da Utilização do Item |
    | `receitas[].leituras[]` | Object Array |  |
    | `receitas[].leituras[].sequencia` | number | Sequência do item |
    | `receitas[].leituras[].seq` | number | Sequência da receita |
    | `receitas[].leituras[].seq_leitura` | number | Sequência da leitura |
    | `receitas[].leituras[].usu_data_hora` | string | Data e Hora da leitura <br>Formato: **YYYY-MM-DD
    HH:mm** |
    | `receitas[].leituras[].uso_terminal` | string | Identificador do terminal da leitura  |
    | `receitas[].tem_leitura_hoje` | boolean | Parâmetro que identifica se Possui Leituras disponíveis
    para o dia atual |
    | `receitas[].horario_str_formatado` | string | Horário escolhido para a Data de Visita já formatado
    |
    | `receitasAgrupadas[]` | Object Array | Lista de Receitas Agrupadas disponíveis para o Item |
    | `receitasAgrupadas[].tipo_receita` | number | ID da Venda |
    | `receitasAgrupadas[].receita` | string | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].data_visita` | date | Código da receita |
    | `receitasAgrupadas[].data_visita_final` | date | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].credenciado` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_nome` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_desc` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].sessao` | number | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].sessao_nome` | string | Nome da Sessão |
    | `receitasAgrupadas[].poltrona` | number | Código da Poltrona |
    | `receitasAgrupadas[].placa` | string |  |
    | `receitasAgrupadas[].horario_str` | string | Horário da Receita em string |
    | `receitasAgrupadas[].data_hora_utilizacao` | string | Data e Hora de Utilização do Item |
    | `receitasAgrupadas[].leituras[]` | Array | Array de Leituras feitas no Item |
    | `tem_leitura_hoje` | string | Verifica se Há Leituras Disponíveis para a Data atual |
    | `qnt_receitas` | string | Quantidade de Receitas No Item |
    | `qnt_receitas_lidas` | string | Quantidade de Receitas Lidas |
    | `qnt_receitas_utilizadas` | string | Quantidade de Receitas Utilizadas |
    | `local_embarque` | string | Código do Local de Embarque |
    | `desc_local_embarque` | string | Descrição do Local de Embarque |
    | `temporada` | string | Código da Temporada |
    | `temporada_nome` | string | Nome da Temporada |
    | `horario_str` | string | Horário em formato de String |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaItensIdVendaResponse200
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
) -> Response[GetApiVendasVendaItensIdVendaResponse200]:
    r"""Consulta de itens de uma venda

     Rota com o objectivo de retornar dados dos ingressos de uma venda, juntamente com as receitas de
    cada um.

    ## Dados do retorno

    | Atributo | Tipo | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | Código da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `uf` | string | Estado escolhido pelo titular da reserva |
    | `pais` | number | Código do país escolhido pelo titular da reserva |
    | `desc_pais` | strin | Nome do país escolhido pelo titular da reserva |
    | `bilhete` | number | Código do bilhete |
    | `nome_bilhete` | string | Nome do Bilhete |
    | `controle_disponibilidade` | string | Caractere que define o tipo de controle de disponibilidade
    do item: \"H\" - Horários, \"V\" - Vagas, \"M\" - Mapa de Assentos |
    | `venda_sem_data_visita` | string | Define se a venda foi realizada sem data de visita escolhida -
    \"S\"/\"N\" |
    | `texto_impressao` | string | Texto para a impressão do ingresso |
    | `texto_impressao_horario` | string | Texto para a impressão do ingresso |
    | `texto_hora_vis_voucher` | string | Texto para a impressão - refentente à disponibilidade |
    | `texto_data_vis_voucher` | string | Texto para a impressão - refentente à data de visita |
    | `texto_embarque_voucher` | string | Texto para a impressão - refentente ao local de embarque |
    | `texto_sessao_imp` | string | Texto para a impressão - refentente à sessão |
    | `texto_vagao` | string | Texto para a impressão - refentente ao vagão |
    | `texto_poltrona` | string | Texto para a impressão - refentente à poltrona |
    | `permite_visualizar_ingressos` | booelan | Parâmetro que verifica se é permitido a visualização de
    Ingressos |
    | `texto_motivo_nao_ver_ing_ec` | string | Texto explicando o motivo de não ser possível visualizar
    o ingresso |
    | `mostra_horario_final` | string | Define se o bilhete irá informar o horário final |
    | `imprime_valor_tick` | booelan | Parâmetro que verifica se Imprime o Valor no Tick |
    | `utiliza_qrcode` | boolean | Se o ingresso utiliza qrcode ou não |
    | `categoria` | number | Código da categoria |
    | `nome_categoria` | string | Nome da categoria |
    | `privativo` | boolean | Define se a categoria é do tipo privativo |
    | `imagem_categoria` | string | Imagem referente à categoria |
    | `operacao` | number | Código da operação |
    | `cancelado` | boolean | Define se o item foi cancelado ou não |
    | `cancelamentos_codigo` | number Array | Código dos cancelamentos relacionados ao item |
    | `data_hora_pedido_canc` | string | Data e Hora do Pedido de Cancelamento |
    | `quantidade` | number | Quantidade de ingressos |
    | `vlr_total` | number | Valor total do item (contém descontos de cupom) |
    | `vlr_unitario` | number | Valor unitário do ingresso (valor bruto) |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `atrativo_nome` | string | Nome do visitante |
    | `atrativo_doc` | string | Documento do visitante |
    | `atrativo_email` | string | E-mail do visitante |
    | `atrativo_convenio` | string | Código do visitante |
    | `observacao_convenio` | string | Texto de Observações do Convênio |
    | `nome_convenio` | string | Nome do convênio do visitante |
    | `atrativo_data_nasc` | string | Data de nascimento do visitante |
    | `lb_int_tipo_venda` | string | ?? |
    | `contrib_fundo` | boolean | Se foi escolhido contribuir com o Fundo do ingresso |
    | `morador_tipo_doc` | string | Tipo do documento do morador local |
    | `qr_code_exp` | string | QRcode do item |
    | `card_id` | number |  |
    | `descricao_venda` | string | Descrição da venda |
    | `dados_incompletos` | boolean | Define se na hora da reserva, os dados dos visitantes não foram
    preenchidos |
    | `local_de_apanhe` | number | Código do local de apanhe |
    | `local_de_apanhe_nome` | string | Nome do local de apanhe |
    | `local_de_apanhe_endereco` | string | Endereço do local de apanhe |
    | `data_visita` | string | Data de visita (primeiro entre receitas) |
    | `data_visita_final` | string | Data de visita final entre as receitas |
    | `dias_para_alterar_visitantes` | number | Dias limite antes da data de visita para alterar os
    dados dos visitantes |
    | `integracao_carteiras_digital` | string | Verifica se está habilitado Integração com Carteiras
    Digitais |
    | `permite_info_visitante_depois` | booelan | Parâmetro que Ativa/Desativa a opção de preencher os
    dados do Visitante após finalizar a compra |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `remarca_visitante` | boolean | Verifica se o bilhete permite alterar dados do visitante na
    remarcação |
    | `remarca_data_visita` | boolean | Verifica se o bilhete permite alterar data de visita na
    remarcação |
    | `remarca_hora_visita` | boolean | Verifica se o bilhete permite alterar horário da visita na
    remarcação |
    | `receitas[]` | Object Array | Lista de Receitas disponíveis para o Item |
    | `receitas[].codigo` | number | ID da Venda |
    | `receitas[].sequencia` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].tipo_receita` | number | Código da receita |
    | `receitas[].preco` | number | Preço Definido para o Produto na Receita determinada |
    | `receitas[].preco_bruto` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].prog_horario` | number | Código da Programação de Horários para o Item na receita
    informada |
    | `receitas[].prog_seq` | number | Sequencia do Horário na Programação de Horários para o Item na
    receita informada |
    | `receitas[].lb_vou_idvenda` | string | ID da venda na bilheteria |
    | `receitas[].lb_vou_datahora` | string | Data e Hora da venda na bilheteria |
    | `receitas[].estabelec` | string | Nome do Estabelecimento |
    | `receitas[].versao` | number | Versão do cadastro do estabelecimento em relação à integração com a
    bilheteria |
    | `receitas[].estabelec_dest` | number | Estabelecimento de Destino do Item |
    | `receitas[].id_produto` | number | ID Do Item |
    | `receitas[].data_visita` | date | Data de visita (primeiro entre receitas) |
    | `receitas[].data_visita_final` | date | Data de visita final entre as receitas |
    | `receitas[].hoje_entre_visitas` | date | Se a data atual está entre a data de visita inicial e
    final |
    | `receitas[].horario_str` | string | Descrição do horário ou vaga |
    | `receitas[].local_embarque` | number | Código do Local de Embarque |
    | `receitas[].local_embarque_nome` | string | Nome do Local de Embarque |
    | `receitas[].local_embarque_desc` | string | Descrição sobre o Local de Embarque |
    | `receitas[].sessao` | number | Código da Sessão |
    | `receitas[].sessao_nome` | string | Nome Da Sessão |
    | `receitas[].placa` | string |  |
    | `receitas[].poltrona` | string |  |
    | `receitas[].mostra_horario_final` | string | Verifica se Mostra o Horário Final |
    | `receitas[].credenciado` | number | Código do Credenciado Cadastrado |
    | `receitas[].credenciado_nome` | string | Nome do Credenciado Cadastrado |
    | `receitas[].credenciado_cpf` | number | CPF do Credenciado Cadastrado |
    | `receitas[]idioma_escolhido` | string | Idioma Escolhido |
    | `receitas[].habilita_vendas_dias_corridos` | boolean | Parâmetro para geração de QrCode para a
    quantidade determinada de dias após o dia escolhido para a visita |
    | `receitas[].evento` | boolean | Parâmetro que verifica se o Item é para um Evento |
    | `receitas[].data_hora_utilizacao` | string | Data e Hora da Utilização do Item |
    | `receitas[].leituras[]` | Object Array |  |
    | `receitas[].leituras[].sequencia` | number | Sequência do item |
    | `receitas[].leituras[].seq` | number | Sequência da receita |
    | `receitas[].leituras[].seq_leitura` | number | Sequência da leitura |
    | `receitas[].leituras[].usu_data_hora` | string | Data e Hora da leitura <br>Formato: **YYYY-MM-DD
    HH:mm** |
    | `receitas[].leituras[].uso_terminal` | string | Identificador do terminal da leitura  |
    | `receitas[].tem_leitura_hoje` | boolean | Parâmetro que identifica se Possui Leituras disponíveis
    para o dia atual |
    | `receitas[].horario_str_formatado` | string | Horário escolhido para a Data de Visita já formatado
    |
    | `receitasAgrupadas[]` | Object Array | Lista de Receitas Agrupadas disponíveis para o Item |
    | `receitasAgrupadas[].tipo_receita` | number | ID da Venda |
    | `receitasAgrupadas[].receita` | string | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].data_visita` | date | Código da receita |
    | `receitasAgrupadas[].data_visita_final` | date | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].credenciado` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_nome` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_desc` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].sessao` | number | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].sessao_nome` | string | Nome da Sessão |
    | `receitasAgrupadas[].poltrona` | number | Código da Poltrona |
    | `receitasAgrupadas[].placa` | string |  |
    | `receitasAgrupadas[].horario_str` | string | Horário da Receita em string |
    | `receitasAgrupadas[].data_hora_utilizacao` | string | Data e Hora de Utilização do Item |
    | `receitasAgrupadas[].leituras[]` | Array | Array de Leituras feitas no Item |
    | `tem_leitura_hoje` | string | Verifica se Há Leituras Disponíveis para a Data atual |
    | `qnt_receitas` | string | Quantidade de Receitas No Item |
    | `qnt_receitas_lidas` | string | Quantidade de Receitas Lidas |
    | `qnt_receitas_utilizadas` | string | Quantidade de Receitas Utilizadas |
    | `local_embarque` | string | Código do Local de Embarque |
    | `desc_local_embarque` | string | Descrição do Local de Embarque |
    | `temporada` | string | Código da Temporada |
    | `temporada_nome` | string | Nome da Temporada |
    | `horario_str` | string | Horário em formato de String |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiVendasVendaItensIdVendaResponse200]
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
) -> Optional[GetApiVendasVendaItensIdVendaResponse200]:
    r"""Consulta de itens de uma venda

     Rota com o objectivo de retornar dados dos ingressos de uma venda, juntamente com as receitas de
    cada um.

    ## Dados do retorno

    | Atributo | Tipo | **Descrição** |
    | --- | --- | --- |
    | `codigo` | number | Código da venda |
    | `sequencia` | number | Código sequencial do item da venda |
    | `uf` | string | Estado escolhido pelo titular da reserva |
    | `pais` | number | Código do país escolhido pelo titular da reserva |
    | `desc_pais` | strin | Nome do país escolhido pelo titular da reserva |
    | `bilhete` | number | Código do bilhete |
    | `nome_bilhete` | string | Nome do Bilhete |
    | `controle_disponibilidade` | string | Caractere que define o tipo de controle de disponibilidade
    do item: \"H\" - Horários, \"V\" - Vagas, \"M\" - Mapa de Assentos |
    | `venda_sem_data_visita` | string | Define se a venda foi realizada sem data de visita escolhida -
    \"S\"/\"N\" |
    | `texto_impressao` | string | Texto para a impressão do ingresso |
    | `texto_impressao_horario` | string | Texto para a impressão do ingresso |
    | `texto_hora_vis_voucher` | string | Texto para a impressão - refentente à disponibilidade |
    | `texto_data_vis_voucher` | string | Texto para a impressão - refentente à data de visita |
    | `texto_embarque_voucher` | string | Texto para a impressão - refentente ao local de embarque |
    | `texto_sessao_imp` | string | Texto para a impressão - refentente à sessão |
    | `texto_vagao` | string | Texto para a impressão - refentente ao vagão |
    | `texto_poltrona` | string | Texto para a impressão - refentente à poltrona |
    | `permite_visualizar_ingressos` | booelan | Parâmetro que verifica se é permitido a visualização de
    Ingressos |
    | `texto_motivo_nao_ver_ing_ec` | string | Texto explicando o motivo de não ser possível visualizar
    o ingresso |
    | `mostra_horario_final` | string | Define se o bilhete irá informar o horário final |
    | `imprime_valor_tick` | booelan | Parâmetro que verifica se Imprime o Valor no Tick |
    | `utiliza_qrcode` | boolean | Se o ingresso utiliza qrcode ou não |
    | `categoria` | number | Código da categoria |
    | `nome_categoria` | string | Nome da categoria |
    | `privativo` | boolean | Define se a categoria é do tipo privativo |
    | `imagem_categoria` | string | Imagem referente à categoria |
    | `operacao` | number | Código da operação |
    | `cancelado` | boolean | Define se o item foi cancelado ou não |
    | `cancelamentos_codigo` | number Array | Código dos cancelamentos relacionados ao item |
    | `data_hora_pedido_canc` | string | Data e Hora do Pedido de Cancelamento |
    | `quantidade` | number | Quantidade de ingressos |
    | `vlr_total` | number | Valor total do item (contém descontos de cupom) |
    | `vlr_unitario` | number | Valor unitário do ingresso (valor bruto) |
    | `id_cupom_desc` | string | Código unitário do cupom de desconto aplicado na venda |
    | `cupom_desc` | string | Cupom de desconto aplicado na venda |
    | `atrativo_nome` | string | Nome do visitante |
    | `atrativo_doc` | string | Documento do visitante |
    | `atrativo_email` | string | E-mail do visitante |
    | `atrativo_convenio` | string | Código do visitante |
    | `observacao_convenio` | string | Texto de Observações do Convênio |
    | `nome_convenio` | string | Nome do convênio do visitante |
    | `atrativo_data_nasc` | string | Data de nascimento do visitante |
    | `lb_int_tipo_venda` | string | ?? |
    | `contrib_fundo` | boolean | Se foi escolhido contribuir com o Fundo do ingresso |
    | `morador_tipo_doc` | string | Tipo do documento do morador local |
    | `qr_code_exp` | string | QRcode do item |
    | `card_id` | number |  |
    | `descricao_venda` | string | Descrição da venda |
    | `dados_incompletos` | boolean | Define se na hora da reserva, os dados dos visitantes não foram
    preenchidos |
    | `local_de_apanhe` | number | Código do local de apanhe |
    | `local_de_apanhe_nome` | string | Nome do local de apanhe |
    | `local_de_apanhe_endereco` | string | Endereço do local de apanhe |
    | `data_visita` | string | Data de visita (primeiro entre receitas) |
    | `data_visita_final` | string | Data de visita final entre as receitas |
    | `dias_para_alterar_visitantes` | number | Dias limite antes da data de visita para alterar os
    dados dos visitantes |
    | `integracao_carteiras_digital` | string | Verifica se está habilitado Integração com Carteiras
    Digitais |
    | `permite_info_visitante_depois` | booelan | Parâmetro que Ativa/Desativa a opção de preencher os
    dados do Visitante após finalizar a compra |
    | `reserva_suspeita` | boolean | Informa que a venda é suspeita |
    | `remarca_visitante` | boolean | Verifica se o bilhete permite alterar dados do visitante na
    remarcação |
    | `remarca_data_visita` | boolean | Verifica se o bilhete permite alterar data de visita na
    remarcação |
    | `remarca_hora_visita` | boolean | Verifica se o bilhete permite alterar horário da visita na
    remarcação |
    | `receitas[]` | Object Array | Lista de Receitas disponíveis para o Item |
    | `receitas[].codigo` | number | ID da Venda |
    | `receitas[].sequencia` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].tipo_receita` | number | Código da receita |
    | `receitas[].preco` | number | Preço Definido para o Produto na Receita determinada |
    | `receitas[].preco_bruto` | number | Primeiro código da temporada entre as receitas |
    | `receitas[].prog_horario` | number | Código da Programação de Horários para o Item na receita
    informada |
    | `receitas[].prog_seq` | number | Sequencia do Horário na Programação de Horários para o Item na
    receita informada |
    | `receitas[].lb_vou_idvenda` | string | ID da venda na bilheteria |
    | `receitas[].lb_vou_datahora` | string | Data e Hora da venda na bilheteria |
    | `receitas[].estabelec` | string | Nome do Estabelecimento |
    | `receitas[].versao` | number | Versão do cadastro do estabelecimento em relação à integração com a
    bilheteria |
    | `receitas[].estabelec_dest` | number | Estabelecimento de Destino do Item |
    | `receitas[].id_produto` | number | ID Do Item |
    | `receitas[].data_visita` | date | Data de visita (primeiro entre receitas) |
    | `receitas[].data_visita_final` | date | Data de visita final entre as receitas |
    | `receitas[].hoje_entre_visitas` | date | Se a data atual está entre a data de visita inicial e
    final |
    | `receitas[].horario_str` | string | Descrição do horário ou vaga |
    | `receitas[].local_embarque` | number | Código do Local de Embarque |
    | `receitas[].local_embarque_nome` | string | Nome do Local de Embarque |
    | `receitas[].local_embarque_desc` | string | Descrição sobre o Local de Embarque |
    | `receitas[].sessao` | number | Código da Sessão |
    | `receitas[].sessao_nome` | string | Nome Da Sessão |
    | `receitas[].placa` | string |  |
    | `receitas[].poltrona` | string |  |
    | `receitas[].mostra_horario_final` | string | Verifica se Mostra o Horário Final |
    | `receitas[].credenciado` | number | Código do Credenciado Cadastrado |
    | `receitas[].credenciado_nome` | string | Nome do Credenciado Cadastrado |
    | `receitas[].credenciado_cpf` | number | CPF do Credenciado Cadastrado |
    | `receitas[]idioma_escolhido` | string | Idioma Escolhido |
    | `receitas[].habilita_vendas_dias_corridos` | boolean | Parâmetro para geração de QrCode para a
    quantidade determinada de dias após o dia escolhido para a visita |
    | `receitas[].evento` | boolean | Parâmetro que verifica se o Item é para um Evento |
    | `receitas[].data_hora_utilizacao` | string | Data e Hora da Utilização do Item |
    | `receitas[].leituras[]` | Object Array |  |
    | `receitas[].leituras[].sequencia` | number | Sequência do item |
    | `receitas[].leituras[].seq` | number | Sequência da receita |
    | `receitas[].leituras[].seq_leitura` | number | Sequência da leitura |
    | `receitas[].leituras[].usu_data_hora` | string | Data e Hora da leitura <br>Formato: **YYYY-MM-DD
    HH:mm** |
    | `receitas[].leituras[].uso_terminal` | string | Identificador do terminal da leitura  |
    | `receitas[].tem_leitura_hoje` | boolean | Parâmetro que identifica se Possui Leituras disponíveis
    para o dia atual |
    | `receitas[].horario_str_formatado` | string | Horário escolhido para a Data de Visita já formatado
    |
    | `receitasAgrupadas[]` | Object Array | Lista de Receitas Agrupadas disponíveis para o Item |
    | `receitasAgrupadas[].tipo_receita` | number | ID da Venda |
    | `receitasAgrupadas[].receita` | string | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].data_visita` | date | Código da receita |
    | `receitasAgrupadas[].data_visita_final` | date | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].credenciado` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque` | number | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_nome` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].local_embarque_desc` | string | Primeiro código da temporada entre as
    receitasAgrupadas |
    | `receitasAgrupadas[].sessao` | number | Primeiro código da temporada entre as receitasAgrupadas |
    | `receitasAgrupadas[].sessao_nome` | string | Nome da Sessão |
    | `receitasAgrupadas[].poltrona` | number | Código da Poltrona |
    | `receitasAgrupadas[].placa` | string |  |
    | `receitasAgrupadas[].horario_str` | string | Horário da Receita em string |
    | `receitasAgrupadas[].data_hora_utilizacao` | string | Data e Hora de Utilização do Item |
    | `receitasAgrupadas[].leituras[]` | Array | Array de Leituras feitas no Item |
    | `tem_leitura_hoje` | string | Verifica se Há Leituras Disponíveis para a Data atual |
    | `qnt_receitas` | string | Quantidade de Receitas No Item |
    | `qnt_receitas_lidas` | string | Quantidade de Receitas Lidas |
    | `qnt_receitas_utilizadas` | string | Quantidade de Receitas Utilizadas |
    | `local_embarque` | string | Código do Local de Embarque |
    | `desc_local_embarque` | string | Descrição do Local de Embarque |
    | `temporada` | string | Código da Temporada |
    | `temporada_nome` | string | Nome da Temporada |
    | `horario_str` | string | Horário em formato de String |

    Args:
        id_venda (float):
        authorization (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiVendasVendaItensIdVendaResponse200
    """

    return (
        await asyncio_detailed(
            id_venda=id_venda,
            client=client,
            authorization=authorization,
        )
    ).parsed
