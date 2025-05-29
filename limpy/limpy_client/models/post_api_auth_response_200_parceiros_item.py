from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiAuthResponse200ParceirosItem")


@_attrs_define
class PostApiAuthResponse200ParceirosItem:
    """
    Attributes:
        idparceiro (Union[Unset, float]): Código do parceiro
        nomeparceiro (Union[Unset, str]): Nome do parceiro
    """

    idparceiro: Union[Unset, float] = UNSET
    nomeparceiro: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idparceiro = self.idparceiro

        nomeparceiro = self.nomeparceiro

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idparceiro is not UNSET:
            field_dict["idparceiro"] = idparceiro
        if nomeparceiro is not UNSET:
            field_dict["nomeparceiro"] = nomeparceiro

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idparceiro = d.pop("idparceiro", UNSET)

        nomeparceiro = d.pop("nomeparceiro", UNSET)

        post_api_auth_response_200_parceiros_item = cls(
            idparceiro=idparceiro,
            nomeparceiro=nomeparceiro,
        )

        post_api_auth_response_200_parceiros_item.additional_properties = d
        return post_api_auth_response_200_parceiros_item

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
