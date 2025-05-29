import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiVendasResponse200")


@_attrs_define
class GetApiVendasResponse200:
    """
    Attributes:
        codigo (Union[Unset, float]): Código único da venda em questão
        localizador (Union[Unset, str]): Código único da venda com prefixo
        data_hora (Union[Unset, str]): Data e hora do registro da venda formatada
        idorigem (Union[Unset, str]): Código da venda no estabelecimento de origem
        cod_local_venda (Union[Unset, float]): Código do estabelecimento que realizou a venda
        ponto_venda (Union[Unset, str]): URL do e-commerce que realizou a venda
        local_venda (Union[Unset, str]): Nome do estabelecimento que realizou a venda
        nome_titular (Union[Unset, str]): Nome do titular da venda
        email_titular (Union[Unset, str]): E-mail do titular da venda
        fone_titular (Union[Unset, str]): Telefone do titular da venda
        doc_titular (Union[Unset, str]): Documento do titular da venda
        nascimento_titular (Union[Unset, str]): Data de nascimento do titular da venda formatada
        codigo_promocional (Union[Unset, str]): Código promocional que foi aplicado para a venda
        total_liquido (Union[Unset, float]): Valor total da venda
        idioma (Union[Unset, str]): Idioma da venda ("PT", "EN", "ES")
        data_hora_inc (Union[Unset, datetime.datetime]): Data e hora do registro da venda UTC
        pedido_de_cancelamento (Union[Unset, bool]): Se a venda tem algum item com pedido de cancelamento
        ip_comprador (Union[Unset, str]): IP do dispositivo do comprador
        tag_nao_enviada (Union[Unset, str]): Parâmetro indica se o pagamento foi enviado para o TagManager, quando é
            "null" o pagamento foi enviado. Se for "true", significa que o pagamento ainda não foi enviado para o TagManager
        quantidade (Union[Unset, float]): Quantidade de itens da venda
        importante (Union[Unset, bool]): Quantidade de itens da venda
        tick_nome (Union[Unset, str]): Nome do cadastro do Tick Ingressos
        tick_terminal (Union[Unset, str]): Identificador do dispositivo que roda o aplicativo do Tick Ingressos e
            realizou a venda
        tick_term_descricao (Union[Unset, str]): Descrição do dispositivo que roda o aplicativo do Tick Ingressos e
            realizou a venda
        formas_pag_desc (Union[Unset, list[str]]): Forma(s) de pagamento utilizados na venda
        nome_adquirente (Union[Unset, str]): Nome da adquirente de pagamento
        data (Union[Unset, str]): Data da venda formatada - DD/MM/YYYY
        hora (Union[Unset, str]): Hora da venda formatada - HH:mm:ss
        atrativo_data_nasc (Union[Unset, str]): Data de nascimento do visitante (PRIMEIRO ITEM DA VENDA)
        data_visita (Union[Unset, str]): Data de visita (PRIMEIRO ITEM DA VENDA)
        data_visita_final (Union[Unset, str]): Data de visita final (PRIMEIRO ITEM DA VENDA)
        uso_data_hora (Union[Unset, str]): Data/Hora de utilização (PRIMEIRO ITEM DA VENDA)
        data_hora_canc (Union[Unset, str]): Data/Hora de cancelamento (PRIMEIRO ITEM DA VENDA)
        status_desc (Union[Unset, str]): Descrição referente ao status da venda
    """

    codigo: Union[Unset, float] = UNSET
    localizador: Union[Unset, str] = UNSET
    data_hora: Union[Unset, str] = UNSET
    idorigem: Union[Unset, str] = UNSET
    cod_local_venda: Union[Unset, float] = UNSET
    ponto_venda: Union[Unset, str] = UNSET
    local_venda: Union[Unset, str] = UNSET
    nome_titular: Union[Unset, str] = UNSET
    email_titular: Union[Unset, str] = UNSET
    fone_titular: Union[Unset, str] = UNSET
    doc_titular: Union[Unset, str] = UNSET
    nascimento_titular: Union[Unset, str] = UNSET
    codigo_promocional: Union[Unset, str] = UNSET
    total_liquido: Union[Unset, float] = UNSET
    idioma: Union[Unset, str] = UNSET
    data_hora_inc: Union[Unset, datetime.datetime] = UNSET
    pedido_de_cancelamento: Union[Unset, bool] = UNSET
    ip_comprador: Union[Unset, str] = UNSET
    tag_nao_enviada: Union[Unset, str] = UNSET
    quantidade: Union[Unset, float] = UNSET
    importante: Union[Unset, bool] = UNSET
    tick_nome: Union[Unset, str] = UNSET
    tick_terminal: Union[Unset, str] = UNSET
    tick_term_descricao: Union[Unset, str] = UNSET
    formas_pag_desc: Union[Unset, list[str]] = UNSET
    nome_adquirente: Union[Unset, str] = UNSET
    data: Union[Unset, str] = UNSET
    hora: Union[Unset, str] = UNSET
    atrativo_data_nasc: Union[Unset, str] = UNSET
    data_visita: Union[Unset, str] = UNSET
    data_visita_final: Union[Unset, str] = UNSET
    uso_data_hora: Union[Unset, str] = UNSET
    data_hora_canc: Union[Unset, str] = UNSET
    status_desc: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codigo = self.codigo

        localizador = self.localizador

        data_hora = self.data_hora

        idorigem = self.idorigem

        cod_local_venda = self.cod_local_venda

        ponto_venda = self.ponto_venda

        local_venda = self.local_venda

        nome_titular = self.nome_titular

        email_titular = self.email_titular

        fone_titular = self.fone_titular

        doc_titular = self.doc_titular

        nascimento_titular = self.nascimento_titular

        codigo_promocional = self.codigo_promocional

        total_liquido = self.total_liquido

        idioma = self.idioma

        data_hora_inc: Union[Unset, str] = UNSET
        if not isinstance(self.data_hora_inc, Unset):
            data_hora_inc = self.data_hora_inc.isoformat()

        pedido_de_cancelamento = self.pedido_de_cancelamento

        ip_comprador = self.ip_comprador

        tag_nao_enviada = self.tag_nao_enviada

        quantidade = self.quantidade

        importante = self.importante

        tick_nome = self.tick_nome

        tick_terminal = self.tick_terminal

        tick_term_descricao = self.tick_term_descricao

        formas_pag_desc: Union[Unset, list[str]] = UNSET
        if not isinstance(self.formas_pag_desc, Unset):
            formas_pag_desc = self.formas_pag_desc

        nome_adquirente = self.nome_adquirente

        data = self.data

        hora = self.hora

        atrativo_data_nasc = self.atrativo_data_nasc

        data_visita = self.data_visita

        data_visita_final = self.data_visita_final

        uso_data_hora = self.uso_data_hora

        data_hora_canc = self.data_hora_canc

        status_desc = self.status_desc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if localizador is not UNSET:
            field_dict["localizador"] = localizador
        if data_hora is not UNSET:
            field_dict["data_hora"] = data_hora
        if idorigem is not UNSET:
            field_dict["idorigem"] = idorigem
        if cod_local_venda is not UNSET:
            field_dict["cod_local_venda"] = cod_local_venda
        if ponto_venda is not UNSET:
            field_dict["ponto_venda"] = ponto_venda
        if local_venda is not UNSET:
            field_dict["local_venda"] = local_venda
        if nome_titular is not UNSET:
            field_dict["nome_titular"] = nome_titular
        if email_titular is not UNSET:
            field_dict["email_titular"] = email_titular
        if fone_titular is not UNSET:
            field_dict["fone_titular"] = fone_titular
        if doc_titular is not UNSET:
            field_dict["doc_titular"] = doc_titular
        if nascimento_titular is not UNSET:
            field_dict["nascimento_titular"] = nascimento_titular
        if codigo_promocional is not UNSET:
            field_dict["codigo_promocional"] = codigo_promocional
        if total_liquido is not UNSET:
            field_dict["total_liquido"] = total_liquido
        if idioma is not UNSET:
            field_dict["idioma"] = idioma
        if data_hora_inc is not UNSET:
            field_dict["data_hora_inc"] = data_hora_inc
        if pedido_de_cancelamento is not UNSET:
            field_dict["pedido_de_cancelamento"] = pedido_de_cancelamento
        if ip_comprador is not UNSET:
            field_dict["ip_comprador"] = ip_comprador
        if tag_nao_enviada is not UNSET:
            field_dict["tag_nao_enviada"] = tag_nao_enviada
        if quantidade is not UNSET:
            field_dict["quantidade"] = quantidade
        if importante is not UNSET:
            field_dict["importante"] = importante
        if tick_nome is not UNSET:
            field_dict["tick_nome"] = tick_nome
        if tick_terminal is not UNSET:
            field_dict["tick_terminal"] = tick_terminal
        if tick_term_descricao is not UNSET:
            field_dict["tick_term_descricao"] = tick_term_descricao
        if formas_pag_desc is not UNSET:
            field_dict["formas_pag_desc"] = formas_pag_desc
        if nome_adquirente is not UNSET:
            field_dict["nome_adquirente"] = nome_adquirente
        if data is not UNSET:
            field_dict["data"] = data
        if hora is not UNSET:
            field_dict["hora"] = hora
        if atrativo_data_nasc is not UNSET:
            field_dict["atrativo_data_nasc"] = atrativo_data_nasc
        if data_visita is not UNSET:
            field_dict["data_visita"] = data_visita
        if data_visita_final is not UNSET:
            field_dict["data_visita_final"] = data_visita_final
        if uso_data_hora is not UNSET:
            field_dict["uso_data_hora"] = uso_data_hora
        if data_hora_canc is not UNSET:
            field_dict["data_hora_canc"] = data_hora_canc
        if status_desc is not UNSET:
            field_dict["status_desc"] = status_desc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        codigo = d.pop("codigo", UNSET)

        localizador = d.pop("localizador", UNSET)

        data_hora = d.pop("data_hora", UNSET)

        idorigem = d.pop("idorigem", UNSET)

        cod_local_venda = d.pop("cod_local_venda", UNSET)

        ponto_venda = d.pop("ponto_venda", UNSET)

        local_venda = d.pop("local_venda", UNSET)

        nome_titular = d.pop("nome_titular", UNSET)

        email_titular = d.pop("email_titular", UNSET)

        fone_titular = d.pop("fone_titular", UNSET)

        doc_titular = d.pop("doc_titular", UNSET)

        nascimento_titular = d.pop("nascimento_titular", UNSET)

        codigo_promocional = d.pop("codigo_promocional", UNSET)

        total_liquido = d.pop("total_liquido", UNSET)

        idioma = d.pop("idioma", UNSET)

        _data_hora_inc = d.pop("data_hora_inc", UNSET)
        data_hora_inc: Union[Unset, datetime.datetime]
        if isinstance(_data_hora_inc, Unset):
            data_hora_inc = UNSET
        else:
            data_hora_inc = isoparse(_data_hora_inc)

        pedido_de_cancelamento = d.pop("pedido_de_cancelamento", UNSET)

        ip_comprador = d.pop("ip_comprador", UNSET)

        tag_nao_enviada = d.pop("tag_nao_enviada", UNSET)

        quantidade = d.pop("quantidade", UNSET)

        importante = d.pop("importante", UNSET)

        tick_nome = d.pop("tick_nome", UNSET)

        tick_terminal = d.pop("tick_terminal", UNSET)

        tick_term_descricao = d.pop("tick_term_descricao", UNSET)

        formas_pag_desc = cast(list[str], d.pop("formas_pag_desc", UNSET))

        nome_adquirente = d.pop("nome_adquirente", UNSET)

        data = d.pop("data", UNSET)

        hora = d.pop("hora", UNSET)

        atrativo_data_nasc = d.pop("atrativo_data_nasc", UNSET)

        data_visita = d.pop("data_visita", UNSET)

        data_visita_final = d.pop("data_visita_final", UNSET)

        uso_data_hora = d.pop("uso_data_hora", UNSET)

        data_hora_canc = d.pop("data_hora_canc", UNSET)

        status_desc = d.pop("status_desc", UNSET)

        get_api_vendas_response_200 = cls(
            codigo=codigo,
            localizador=localizador,
            data_hora=data_hora,
            idorigem=idorigem,
            cod_local_venda=cod_local_venda,
            ponto_venda=ponto_venda,
            local_venda=local_venda,
            nome_titular=nome_titular,
            email_titular=email_titular,
            fone_titular=fone_titular,
            doc_titular=doc_titular,
            nascimento_titular=nascimento_titular,
            codigo_promocional=codigo_promocional,
            total_liquido=total_liquido,
            idioma=idioma,
            data_hora_inc=data_hora_inc,
            pedido_de_cancelamento=pedido_de_cancelamento,
            ip_comprador=ip_comprador,
            tag_nao_enviada=tag_nao_enviada,
            quantidade=quantidade,
            importante=importante,
            tick_nome=tick_nome,
            tick_terminal=tick_terminal,
            tick_term_descricao=tick_term_descricao,
            formas_pag_desc=formas_pag_desc,
            nome_adquirente=nome_adquirente,
            data=data,
            hora=hora,
            atrativo_data_nasc=atrativo_data_nasc,
            data_visita=data_visita,
            data_visita_final=data_visita_final,
            uso_data_hora=uso_data_hora,
            data_hora_canc=data_hora_canc,
            status_desc=status_desc,
        )

        get_api_vendas_response_200.additional_properties = d
        return get_api_vendas_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
