from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiCrossCepCEPResponse200")


@_attrs_define
class GetApiCrossCepCEPResponse200:
    """
    Attributes:
        cep (Union[Unset, str]): CEP que foi informado Example: 85503-380.
        cidade (Union[Unset, str]): Cidade ao qual o CEP é pertencente Example: Pato Branco.
        logradouro (Union[Unset, str]): Endereço ao qual o CEP é pertencente Example: Avenida Elisa Rosa Colla Padoan.
        bairro (Union[Unset, str]): Bairro ao qual o CEP é pertencente Example: Fraron.
        uf (Union[Unset, str]): Unidade Federativa da cidade da qual o CEP é pertencente Example: PR.
        ibge (Union[Unset, int]): Código IBGE da localidade Example: 4118501.
    """

    cep: Union[Unset, str] = UNSET
    cidade: Union[Unset, str] = UNSET
    logradouro: Union[Unset, str] = UNSET
    bairro: Union[Unset, str] = UNSET
    uf: Union[Unset, str] = UNSET
    ibge: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cep = self.cep

        cidade = self.cidade

        logradouro = self.logradouro

        bairro = self.bairro

        uf = self.uf

        ibge = self.ibge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cep is not UNSET:
            field_dict["cep"] = cep
        if cidade is not UNSET:
            field_dict["cidade"] = cidade
        if logradouro is not UNSET:
            field_dict["logradouro"] = logradouro
        if bairro is not UNSET:
            field_dict["bairro"] = bairro
        if uf is not UNSET:
            field_dict["uf"] = uf
        if ibge is not UNSET:
            field_dict["ibge"] = ibge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cep = d.pop("cep", UNSET)

        cidade = d.pop("cidade", UNSET)

        logradouro = d.pop("logradouro", UNSET)

        bairro = d.pop("bairro", UNSET)

        uf = d.pop("uf", UNSET)

        ibge = d.pop("ibge", UNSET)

        get_api_cross_cep_cep_response_200 = cls(
            cep=cep,
            cidade=cidade,
            logradouro=logradouro,
            bairro=bairro,
            uf=uf,
            ibge=ibge,
        )

        get_api_cross_cep_cep_response_200.additional_properties = d
        return get_api_cross_cep_cep_response_200

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
