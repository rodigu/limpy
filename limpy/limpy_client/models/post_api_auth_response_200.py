from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_api_auth_response_200_parceiros_item import PostApiAuthResponse200ParceirosItem


T = TypeVar("T", bound="PostApiAuthResponse200")


@_attrs_define
class PostApiAuthResponse200:
    """
    Attributes:
        codigo (Union[Unset, float]): Código unitário do usuário em questão
        nivel (Union[Unset, float]): Nível de Permissões do Usuário
        nome (Union[Unset, str]): Nome do usuário
        usuario (Union[Unset, str]): Seu Usuário
        token (Union[Unset, str]): Token para Autenticação
        parceiros (Union[Unset, list['PostApiAuthResponse200ParceirosItem']]): Lista de parceiros que o usuário pode
            realizar requisições de integração
    """

    codigo: Union[Unset, float] = UNSET
    nivel: Union[Unset, float] = UNSET
    nome: Union[Unset, str] = UNSET
    usuario: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    parceiros: Union[Unset, list["PostApiAuthResponse200ParceirosItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codigo = self.codigo

        nivel = self.nivel

        nome = self.nome

        usuario = self.usuario

        token = self.token

        parceiros: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parceiros, Unset):
            parceiros = []
            for parceiros_item_data in self.parceiros:
                parceiros_item = parceiros_item_data.to_dict()
                parceiros.append(parceiros_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if nivel is not UNSET:
            field_dict["nivel"] = nivel
        if nome is not UNSET:
            field_dict["nome"] = nome
        if usuario is not UNSET:
            field_dict["usuario"] = usuario
        if token is not UNSET:
            field_dict["token"] = token
        if parceiros is not UNSET:
            field_dict["parceiros"] = parceiros

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_api_auth_response_200_parceiros_item import PostApiAuthResponse200ParceirosItem

        d = dict(src_dict)
        codigo = d.pop("codigo", UNSET)

        nivel = d.pop("nivel", UNSET)

        nome = d.pop("nome", UNSET)

        usuario = d.pop("usuario", UNSET)

        token = d.pop("token", UNSET)

        parceiros = []
        _parceiros = d.pop("parceiros", UNSET)
        for parceiros_item_data in _parceiros or []:
            parceiros_item = PostApiAuthResponse200ParceirosItem.from_dict(parceiros_item_data)

            parceiros.append(parceiros_item)

        post_api_auth_response_200 = cls(
            codigo=codigo,
            nivel=nivel,
            nome=nome,
            usuario=usuario,
            token=token,
            parceiros=parceiros,
        )

        post_api_auth_response_200.additional_properties = d
        return post_api_auth_response_200

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
