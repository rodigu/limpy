from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostApiAuthBody")


@_attrs_define
class PostApiAuthBody:
    """
    Example:
        {'usuario': 'usuario', 'senha': 'senha'}

    Attributes:
        usuario (str): Seu Usuário
        senha (str): Sua Senha
    """

    usuario: str
    senha: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usuario = self.usuario

        senha = self.senha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "usuario": usuario,
                "senha": senha,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usuario = d.pop("usuario")

        senha = d.pop("senha")

        post_api_auth_body = cls(
            usuario=usuario,
            senha=senha,
        )

        post_api_auth_body.additional_properties = d
        return post_api_auth_body

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
