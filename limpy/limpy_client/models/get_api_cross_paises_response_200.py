from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiCrossPaisesResponse200")


@_attrs_define
class GetApiCrossPaisesResponse200:
    """
    Attributes:
        id_pais (Union[Unset, float]): Código do Pais
        nome_pais (Union[Unset, str]): Nome do País
        codigo_iso (Union[Unset, str]): Código ISO do País 3166-1
        sigla3dig (Union[Unset, str]): Sigla do País com 3 Caracteres
        sigla2dig (Union[Unset, str]): Sigla do País com 2 Caracteres
        outros_nomes (Union[Unset, str]): Outros Nomes reconhecidos do País
        ddi (Union[Unset, float]): Código de Discagem Direta Internacional do País
        path_bandeira (Union[Unset, str]): URL da imagem da bandeira do país
    """

    id_pais: Union[Unset, float] = UNSET
    nome_pais: Union[Unset, str] = UNSET
    codigo_iso: Union[Unset, str] = UNSET
    sigla3dig: Union[Unset, str] = UNSET
    sigla2dig: Union[Unset, str] = UNSET
    outros_nomes: Union[Unset, str] = UNSET
    ddi: Union[Unset, float] = UNSET
    path_bandeira: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id_pais = self.id_pais

        nome_pais = self.nome_pais

        codigo_iso = self.codigo_iso

        sigla3dig = self.sigla3dig

        sigla2dig = self.sigla2dig

        outros_nomes = self.outros_nomes

        ddi = self.ddi

        path_bandeira = self.path_bandeira

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id_pais is not UNSET:
            field_dict["idPais"] = id_pais
        if nome_pais is not UNSET:
            field_dict["nomePais"] = nome_pais
        if codigo_iso is not UNSET:
            field_dict["codigoISO"] = codigo_iso
        if sigla3dig is not UNSET:
            field_dict["sigla3dig"] = sigla3dig
        if sigla2dig is not UNSET:
            field_dict["sigla2dig"] = sigla2dig
        if outros_nomes is not UNSET:
            field_dict["outrosNomes"] = outros_nomes
        if ddi is not UNSET:
            field_dict["ddi"] = ddi
        if path_bandeira is not UNSET:
            field_dict["pathBandeira"] = path_bandeira

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id_pais = d.pop("idPais", UNSET)

        nome_pais = d.pop("nomePais", UNSET)

        codigo_iso = d.pop("codigoISO", UNSET)

        sigla3dig = d.pop("sigla3dig", UNSET)

        sigla2dig = d.pop("sigla2dig", UNSET)

        outros_nomes = d.pop("outrosNomes", UNSET)

        ddi = d.pop("ddi", UNSET)

        path_bandeira = d.pop("pathBandeira", UNSET)

        get_api_cross_paises_response_200 = cls(
            id_pais=id_pais,
            nome_pais=nome_pais,
            codigo_iso=codigo_iso,
            sigla3dig=sigla3dig,
            sigla2dig=sigla2dig,
            outros_nomes=outros_nomes,
            ddi=ddi,
            path_bandeira=path_bandeira,
        )

        get_api_cross_paises_response_200.additional_properties = d
        return get_api_cross_paises_response_200

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
