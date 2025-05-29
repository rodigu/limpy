import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiEcClientesResponse200TermosItem")


@_attrs_define
class GetApiEcClientesResponse200TermosItem:
    """
    Attributes:
        codigo (Union[Unset, float]): Código do Termo
        nome (Union[Unset, str]): Nome do Termo
        data_hora_aceite_termo (Union[Unset, datetime.datetime]): Nome do Termo
    """

    codigo: Union[Unset, float] = UNSET
    nome: Union[Unset, str] = UNSET
    data_hora_aceite_termo: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codigo = self.codigo

        nome = self.nome

        data_hora_aceite_termo: Union[Unset, str] = UNSET
        if not isinstance(self.data_hora_aceite_termo, Unset):
            data_hora_aceite_termo = self.data_hora_aceite_termo.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if nome is not UNSET:
            field_dict["nome"] = nome
        if data_hora_aceite_termo is not UNSET:
            field_dict["data_hora_aceite_termo"] = data_hora_aceite_termo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        codigo = d.pop("codigo", UNSET)

        nome = d.pop("nome", UNSET)

        _data_hora_aceite_termo = d.pop("data_hora_aceite_termo", UNSET)
        data_hora_aceite_termo: Union[Unset, datetime.datetime]
        if isinstance(_data_hora_aceite_termo, Unset):
            data_hora_aceite_termo = UNSET
        else:
            data_hora_aceite_termo = isoparse(_data_hora_aceite_termo)

        get_api_ec_clientes_response_200_termos_item = cls(
            codigo=codigo,
            nome=nome,
            data_hora_aceite_termo=data_hora_aceite_termo,
        )

        get_api_ec_clientes_response_200_termos_item.additional_properties = d
        return get_api_ec_clientes_response_200_termos_item

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
