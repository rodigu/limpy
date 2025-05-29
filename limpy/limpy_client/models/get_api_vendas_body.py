from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiVendasBody")


@_attrs_define
class GetApiVendasBody:
    """
    Example:
        {'localizador': 'localizador', 'dataVendaInit': 'dataVendaInit', 'dataVendaFim': 'dataVendaFim',
            'dataVisitaInit': 'dataVisitaInit', 'dataVisitaFim': 'dataVisitaFim', 'dataCancelamentoInit':
            'dataCancelamentoInit', 'dataCancelamentoFim': 'dataCancelamentoFim', 'dataUtilizacaoInit':
            'dataUtilizacaoInit', 'dataUtilizacaoFim': 'dataUtilizacaoFim', 'statusArray': 'statusArray', 'idOrigem':
            'idOrigem', 'nomeOrEmail': 'nomeOrEmail', 'estabelecOrig': 'estabelecOrig', 'estabelecDest': 'estabelecDest',
            'bilhetes': 'bilhetes', 'codClienteEc': 'codClienteEc', 'modoPagArray': 'modoPagArray', 'nsuIdAutorizacao':
            'nsuIdAutorizacao', 'locaisEmbarque': 'locaisEmbarque'}

    Attributes:
        localizador (Union[Unset, str]): Código único da venda
        data_venda_init (Union[Unset, str]): Data início para pesquisa
        data_venda_fim (Union[Unset, str]): Data final para pesquisa
        data_visita_init (Union[Unset, str]): Filtro de vendas agendadas para o mesmo dia ou após essa data
        data_visita_fim (Union[Unset, str]): Filtro de vendas agendadas para o mesmo dia ou antes essa data
        data_cancelamento_init (Union[Unset, str]): Filtro de vendas com itens cancelados para o mesmo dia ou após essa
            data
        data_cancelamento_fim (Union[Unset, str]): Filtro de vendas com itens cancelados para o mesmo dia ou antes essa
            data
        data_utilizacao_init (Union[Unset, str]): Filtro de vendas utilizadas para o mesmo dia ou antes essa data
        data_utilizacao_fim (Union[Unset, str]): Filtro de vendas utilizadas para o mesmo dia ou após essa data
        status_array (Union[Unset, list[str]]): Status da venda
        id_origem (Union[Unset, float]): Código da venda no estabelecimento de origem da venda
        nome_or_email (Union[Unset, str]): Nome ou E-mail do titular da compra
        estabelec_orig (Union[Unset, float]): Código do estabelecimento de venda
        estabelec_dest (Union[Unset, float]): Código do estabelecimento de destino(Bilheteria)
        bilhetes (Union[Unset, str]): Códigos dos bilhetes a serem filtrados(separados por vírgula)
        cod_cliente_ec (Union[Unset, float]): Código do cliente final que realizou a compra
        modo_pag_array (Union[Unset, str]): Número ou lista de modo de pagamento(separados por vírgula)
        nsu_id_autorizacao (Union[Unset, str]): ID Autorização devolvido pela adquirente de pagamento
        locais_embarque (Union[Unset, str]): Número ou lista de local de embarque(separados por vírgula
    """

    localizador: Union[Unset, str] = UNSET
    data_venda_init: Union[Unset, str] = UNSET
    data_venda_fim: Union[Unset, str] = UNSET
    data_visita_init: Union[Unset, str] = UNSET
    data_visita_fim: Union[Unset, str] = UNSET
    data_cancelamento_init: Union[Unset, str] = UNSET
    data_cancelamento_fim: Union[Unset, str] = UNSET
    data_utilizacao_init: Union[Unset, str] = UNSET
    data_utilizacao_fim: Union[Unset, str] = UNSET
    status_array: Union[Unset, list[str]] = UNSET
    id_origem: Union[Unset, float] = UNSET
    nome_or_email: Union[Unset, str] = UNSET
    estabelec_orig: Union[Unset, float] = UNSET
    estabelec_dest: Union[Unset, float] = UNSET
    bilhetes: Union[Unset, str] = UNSET
    cod_cliente_ec: Union[Unset, float] = UNSET
    modo_pag_array: Union[Unset, str] = UNSET
    nsu_id_autorizacao: Union[Unset, str] = UNSET
    locais_embarque: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        localizador = self.localizador

        data_venda_init = self.data_venda_init

        data_venda_fim = self.data_venda_fim

        data_visita_init = self.data_visita_init

        data_visita_fim = self.data_visita_fim

        data_cancelamento_init = self.data_cancelamento_init

        data_cancelamento_fim = self.data_cancelamento_fim

        data_utilizacao_init = self.data_utilizacao_init

        data_utilizacao_fim = self.data_utilizacao_fim

        status_array: Union[Unset, list[str]] = UNSET
        if not isinstance(self.status_array, Unset):
            status_array = self.status_array

        id_origem = self.id_origem

        nome_or_email = self.nome_or_email

        estabelec_orig = self.estabelec_orig

        estabelec_dest = self.estabelec_dest

        bilhetes = self.bilhetes

        cod_cliente_ec = self.cod_cliente_ec

        modo_pag_array = self.modo_pag_array

        nsu_id_autorizacao = self.nsu_id_autorizacao

        locais_embarque = self.locais_embarque

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localizador is not UNSET:
            field_dict["localizador"] = localizador
        if data_venda_init is not UNSET:
            field_dict["dataVendaInit"] = data_venda_init
        if data_venda_fim is not UNSET:
            field_dict["dataVendaFim"] = data_venda_fim
        if data_visita_init is not UNSET:
            field_dict["dataVisitaInit"] = data_visita_init
        if data_visita_fim is not UNSET:
            field_dict["dataVisitaFim"] = data_visita_fim
        if data_cancelamento_init is not UNSET:
            field_dict["dataCancelamentoInit"] = data_cancelamento_init
        if data_cancelamento_fim is not UNSET:
            field_dict["dataCancelamentoFim"] = data_cancelamento_fim
        if data_utilizacao_init is not UNSET:
            field_dict["dataUtilizacaoInit"] = data_utilizacao_init
        if data_utilizacao_fim is not UNSET:
            field_dict["dataUtilizacaoFim"] = data_utilizacao_fim
        if status_array is not UNSET:
            field_dict["statusArray"] = status_array
        if id_origem is not UNSET:
            field_dict["idOrigem"] = id_origem
        if nome_or_email is not UNSET:
            field_dict["nomeOrEmail"] = nome_or_email
        if estabelec_orig is not UNSET:
            field_dict["estabelecOrig"] = estabelec_orig
        if estabelec_dest is not UNSET:
            field_dict["estabelecDest"] = estabelec_dest
        if bilhetes is not UNSET:
            field_dict["bilhetes"] = bilhetes
        if cod_cliente_ec is not UNSET:
            field_dict["codClienteEc"] = cod_cliente_ec
        if modo_pag_array is not UNSET:
            field_dict["modoPagArray"] = modo_pag_array
        if nsu_id_autorizacao is not UNSET:
            field_dict["nsuIdAutorizacao"] = nsu_id_autorizacao
        if locais_embarque is not UNSET:
            field_dict["locaisEmbarque"] = locais_embarque

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        localizador = d.pop("localizador", UNSET)

        data_venda_init = d.pop("dataVendaInit", UNSET)

        data_venda_fim = d.pop("dataVendaFim", UNSET)

        data_visita_init = d.pop("dataVisitaInit", UNSET)

        data_visita_fim = d.pop("dataVisitaFim", UNSET)

        data_cancelamento_init = d.pop("dataCancelamentoInit", UNSET)

        data_cancelamento_fim = d.pop("dataCancelamentoFim", UNSET)

        data_utilizacao_init = d.pop("dataUtilizacaoInit", UNSET)

        data_utilizacao_fim = d.pop("dataUtilizacaoFim", UNSET)

        status_array = cast(list[str], d.pop("statusArray", UNSET))

        id_origem = d.pop("idOrigem", UNSET)

        nome_or_email = d.pop("nomeOrEmail", UNSET)

        estabelec_orig = d.pop("estabelecOrig", UNSET)

        estabelec_dest = d.pop("estabelecDest", UNSET)

        bilhetes = d.pop("bilhetes", UNSET)

        cod_cliente_ec = d.pop("codClienteEc", UNSET)

        modo_pag_array = d.pop("modoPagArray", UNSET)

        nsu_id_autorizacao = d.pop("nsuIdAutorizacao", UNSET)

        locais_embarque = d.pop("locaisEmbarque", UNSET)

        get_api_vendas_body = cls(
            localizador=localizador,
            data_venda_init=data_venda_init,
            data_venda_fim=data_venda_fim,
            data_visita_init=data_visita_init,
            data_visita_fim=data_visita_fim,
            data_cancelamento_init=data_cancelamento_init,
            data_cancelamento_fim=data_cancelamento_fim,
            data_utilizacao_init=data_utilizacao_init,
            data_utilizacao_fim=data_utilizacao_fim,
            status_array=status_array,
            id_origem=id_origem,
            nome_or_email=nome_or_email,
            estabelec_orig=estabelec_orig,
            estabelec_dest=estabelec_dest,
            bilhetes=bilhetes,
            cod_cliente_ec=cod_cliente_ec,
            modo_pag_array=modo_pag_array,
            nsu_id_autorizacao=nsu_id_autorizacao,
            locais_embarque=locais_embarque,
        )

        get_api_vendas_body.additional_properties = d
        return get_api_vendas_body

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
