import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiVendasVendaCancelamentosIdVendaResponse200")


@_attrs_define
class GetApiVendasVendaCancelamentosIdVendaResponse200:
    """
    Attributes:
        codigo (Union[Unset, float]): ID único da venda Example: 123456777.
        sequencia (Union[Unset, float]): Código sequencial do item da venda Example: 1.
        usuario_pedido (Union[Unset, float]): Código do Usuário que realizou o pedido de Cancelamento da Venda Example:
            999.
        usuario_pedido_nome (Union[Unset, str]): Nome do Usuário que realizou o pedido de Cancelamento da Venda Example:
            Aquele Usuário Mesmo.
        data_hora_pedido (Union[Unset, datetime.datetime]): Data e Hora em que foi realizado o Pedido Example:
            2024-01-03T17:47:42Z.
        motivo_canc (Union[Unset, str]): Motivo para o Cancelamento da venda Example: AQUI ESTÁ SEU MOTIVO.
        valor_cancelado (Union[Unset, float]): Valor total da venda Example: 0.02.
        usuario_canc (Union[Unset, float]): Código do Usuário que realizou o cancelamento da venda Example: 999.
        usuario_canc_nome (Union[Unset, str]): Nome Cadastrado do Usuário que realizou a venda Example: Aquele Usuário
            Mesmo.
        data_hora_canc (Union[Unset, datetime.datetime]): Data e Hora que foi realizado o cancelamento Example:
            2024-01-03T17:47:42Z.
        b_comprovante_canc (Union[Unset, str]): Comprovante do Cancelamento Example: Comprovante de cancelamento.
        canc_manual (Union[Unset, bool]): Verifica se o Cancelamento foi feito Manualmente
        status (Union[Unset, str]): Caractere identificador do status da venda Example: C.
        b_comprovante_confirm_canc (Union[Unset, str]): Comprovante do Cancelamento da Venda
        data_hora_envio_adquirente (Union[Unset, str]): Data e Hora que foi realizado o envio da Adquirente
    """

    codigo: Union[Unset, float] = UNSET
    sequencia: Union[Unset, float] = UNSET
    usuario_pedido: Union[Unset, float] = UNSET
    usuario_pedido_nome: Union[Unset, str] = UNSET
    data_hora_pedido: Union[Unset, datetime.datetime] = UNSET
    motivo_canc: Union[Unset, str] = UNSET
    valor_cancelado: Union[Unset, float] = UNSET
    usuario_canc: Union[Unset, float] = UNSET
    usuario_canc_nome: Union[Unset, str] = UNSET
    data_hora_canc: Union[Unset, datetime.datetime] = UNSET
    b_comprovante_canc: Union[Unset, str] = UNSET
    canc_manual: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    b_comprovante_confirm_canc: Union[Unset, str] = UNSET
    data_hora_envio_adquirente: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codigo = self.codigo

        sequencia = self.sequencia

        usuario_pedido = self.usuario_pedido

        usuario_pedido_nome = self.usuario_pedido_nome

        data_hora_pedido: Union[Unset, str] = UNSET
        if not isinstance(self.data_hora_pedido, Unset):
            data_hora_pedido = self.data_hora_pedido.isoformat()

        motivo_canc = self.motivo_canc

        valor_cancelado = self.valor_cancelado

        usuario_canc = self.usuario_canc

        usuario_canc_nome = self.usuario_canc_nome

        data_hora_canc: Union[Unset, str] = UNSET
        if not isinstance(self.data_hora_canc, Unset):
            data_hora_canc = self.data_hora_canc.isoformat()

        b_comprovante_canc = self.b_comprovante_canc

        canc_manual = self.canc_manual

        status = self.status

        b_comprovante_confirm_canc = self.b_comprovante_confirm_canc

        data_hora_envio_adquirente = self.data_hora_envio_adquirente

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if sequencia is not UNSET:
            field_dict["sequencia"] = sequencia
        if usuario_pedido is not UNSET:
            field_dict["usuario_pedido"] = usuario_pedido
        if usuario_pedido_nome is not UNSET:
            field_dict["usuario_pedido_nome"] = usuario_pedido_nome
        if data_hora_pedido is not UNSET:
            field_dict["data_hora_pedido"] = data_hora_pedido
        if motivo_canc is not UNSET:
            field_dict["motivo_canc"] = motivo_canc
        if valor_cancelado is not UNSET:
            field_dict["valor_cancelado"] = valor_cancelado
        if usuario_canc is not UNSET:
            field_dict["usuario_canc"] = usuario_canc
        if usuario_canc_nome is not UNSET:
            field_dict["usuario_canc_nome"] = usuario_canc_nome
        if data_hora_canc is not UNSET:
            field_dict["data_hora_canc"] = data_hora_canc
        if b_comprovante_canc is not UNSET:
            field_dict["b_comprovante_canc"] = b_comprovante_canc
        if canc_manual is not UNSET:
            field_dict["canc_manual"] = canc_manual
        if status is not UNSET:
            field_dict["status"] = status
        if b_comprovante_confirm_canc is not UNSET:
            field_dict["b_comprovante_confirm_canc"] = b_comprovante_confirm_canc
        if data_hora_envio_adquirente is not UNSET:
            field_dict["data_hora_envio_adquirente"] = data_hora_envio_adquirente

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        codigo = d.pop("codigo", UNSET)

        sequencia = d.pop("sequencia", UNSET)

        usuario_pedido = d.pop("usuario_pedido", UNSET)

        usuario_pedido_nome = d.pop("usuario_pedido_nome", UNSET)

        _data_hora_pedido = d.pop("data_hora_pedido", UNSET)
        data_hora_pedido: Union[Unset, datetime.datetime]
        if isinstance(_data_hora_pedido, Unset):
            data_hora_pedido = UNSET
        else:
            data_hora_pedido = isoparse(_data_hora_pedido)

        motivo_canc = d.pop("motivo_canc", UNSET)

        valor_cancelado = d.pop("valor_cancelado", UNSET)

        usuario_canc = d.pop("usuario_canc", UNSET)

        usuario_canc_nome = d.pop("usuario_canc_nome", UNSET)

        _data_hora_canc = d.pop("data_hora_canc", UNSET)
        data_hora_canc: Union[Unset, datetime.datetime]
        if isinstance(_data_hora_canc, Unset):
            data_hora_canc = UNSET
        else:
            data_hora_canc = isoparse(_data_hora_canc)

        b_comprovante_canc = d.pop("b_comprovante_canc", UNSET)

        canc_manual = d.pop("canc_manual", UNSET)

        status = d.pop("status", UNSET)

        b_comprovante_confirm_canc = d.pop("b_comprovante_confirm_canc", UNSET)

        data_hora_envio_adquirente = d.pop("data_hora_envio_adquirente", UNSET)

        get_api_vendas_venda_cancelamentos_id_venda_response_200 = cls(
            codigo=codigo,
            sequencia=sequencia,
            usuario_pedido=usuario_pedido,
            usuario_pedido_nome=usuario_pedido_nome,
            data_hora_pedido=data_hora_pedido,
            motivo_canc=motivo_canc,
            valor_cancelado=valor_cancelado,
            usuario_canc=usuario_canc,
            usuario_canc_nome=usuario_canc_nome,
            data_hora_canc=data_hora_canc,
            b_comprovante_canc=b_comprovante_canc,
            canc_manual=canc_manual,
            status=status,
            b_comprovante_confirm_canc=b_comprovante_confirm_canc,
            data_hora_envio_adquirente=data_hora_envio_adquirente,
        )

        get_api_vendas_venda_cancelamentos_id_venda_response_200.additional_properties = d
        return get_api_vendas_venda_cancelamentos_id_venda_response_200

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
