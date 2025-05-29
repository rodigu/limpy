import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_api_ec_clientes_response_200_termos_item import GetApiEcClientesResponse200TermosItem


T = TypeVar("T", bound="GetApiEcClientesResponse200")


@_attrs_define
class GetApiEcClientesResponse200:
    """
    Attributes:
        codigo (Union[Unset, float]): Código do Cliente
        nome (Union[Unset, str]): Nome do Cliente
        email (Union[Unset, str]): E-mail do Cliente
        bloqueado (Union[Unset, bool]): Cliente Bloqueado
        grupo_usuarios (Union[Unset, str]): Grupo de Usuários do Cliente
        tipo_documento (Union[Unset, str]): Tipo de documento do cliente
        documento (Union[Unset, str]): Número do documento do cliente
        data_nasc (Union[Unset, datetime.date]): Data de nascimento do cliente
        telefone (Union[Unset, str]): Número de telefone do cliente
        nome_empresa_tur (Union[None, Unset, str]): Nome da empresa do cliente no setor de turismo
        segmento_tur (Union[None, Unset, str]): Segmento de turismo do cliente
        codigo_postal (Union[None, Unset, str]): Código postal do cliente
        pais (Union[None, Unset, int]): Código do país do cliente
        estado (Union[None, Unset, str]): Estado do cliente
        municipio (Union[None, Unset, str]): Município do cliente
        bairro (Union[None, Unset, str]): Bairro do cliente
        endereco (Union[None, Unset, str]): Endereço do cliente
        numero (Union[None, Unset, str]): Número do endereço do cliente
        data_hora_cadastro (Union[None, Unset, datetime.datetime]): Data e hora de cadastro do cliente
        data_hora_alteracao (Union[None, Unset, datetime.datetime]): Data e hora da última alteração no cliente
        termos (Union[Unset, list['GetApiEcClientesResponse200TermosItem']]): Lista de Termos
    """

    codigo: Union[Unset, float] = UNSET
    nome: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    bloqueado: Union[Unset, bool] = UNSET
    grupo_usuarios: Union[Unset, str] = UNSET
    tipo_documento: Union[Unset, str] = UNSET
    documento: Union[Unset, str] = UNSET
    data_nasc: Union[Unset, datetime.date] = UNSET
    telefone: Union[Unset, str] = UNSET
    nome_empresa_tur: Union[None, Unset, str] = UNSET
    segmento_tur: Union[None, Unset, str] = UNSET
    codigo_postal: Union[None, Unset, str] = UNSET
    pais: Union[None, Unset, int] = UNSET
    estado: Union[None, Unset, str] = UNSET
    municipio: Union[None, Unset, str] = UNSET
    bairro: Union[None, Unset, str] = UNSET
    endereco: Union[None, Unset, str] = UNSET
    numero: Union[None, Unset, str] = UNSET
    data_hora_cadastro: Union[None, Unset, datetime.datetime] = UNSET
    data_hora_alteracao: Union[None, Unset, datetime.datetime] = UNSET
    termos: Union[Unset, list["GetApiEcClientesResponse200TermosItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        codigo = self.codigo

        nome = self.nome

        email = self.email

        bloqueado = self.bloqueado

        grupo_usuarios = self.grupo_usuarios

        tipo_documento = self.tipo_documento

        documento = self.documento

        data_nasc: Union[Unset, str] = UNSET
        if not isinstance(self.data_nasc, Unset):
            data_nasc = self.data_nasc.isoformat()

        telefone = self.telefone

        nome_empresa_tur: Union[None, Unset, str]
        if isinstance(self.nome_empresa_tur, Unset):
            nome_empresa_tur = UNSET
        else:
            nome_empresa_tur = self.nome_empresa_tur

        segmento_tur: Union[None, Unset, str]
        if isinstance(self.segmento_tur, Unset):
            segmento_tur = UNSET
        else:
            segmento_tur = self.segmento_tur

        codigo_postal: Union[None, Unset, str]
        if isinstance(self.codigo_postal, Unset):
            codigo_postal = UNSET
        else:
            codigo_postal = self.codigo_postal

        pais: Union[None, Unset, int]
        if isinstance(self.pais, Unset):
            pais = UNSET
        else:
            pais = self.pais

        estado: Union[None, Unset, str]
        if isinstance(self.estado, Unset):
            estado = UNSET
        else:
            estado = self.estado

        municipio: Union[None, Unset, str]
        if isinstance(self.municipio, Unset):
            municipio = UNSET
        else:
            municipio = self.municipio

        bairro: Union[None, Unset, str]
        if isinstance(self.bairro, Unset):
            bairro = UNSET
        else:
            bairro = self.bairro

        endereco: Union[None, Unset, str]
        if isinstance(self.endereco, Unset):
            endereco = UNSET
        else:
            endereco = self.endereco

        numero: Union[None, Unset, str]
        if isinstance(self.numero, Unset):
            numero = UNSET
        else:
            numero = self.numero

        data_hora_cadastro: Union[None, Unset, str]
        if isinstance(self.data_hora_cadastro, Unset):
            data_hora_cadastro = UNSET
        elif isinstance(self.data_hora_cadastro, datetime.datetime):
            data_hora_cadastro = self.data_hora_cadastro.isoformat()
        else:
            data_hora_cadastro = self.data_hora_cadastro

        data_hora_alteracao: Union[None, Unset, str]
        if isinstance(self.data_hora_alteracao, Unset):
            data_hora_alteracao = UNSET
        elif isinstance(self.data_hora_alteracao, datetime.datetime):
            data_hora_alteracao = self.data_hora_alteracao.isoformat()
        else:
            data_hora_alteracao = self.data_hora_alteracao

        termos: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.termos, Unset):
            termos = []
            for termos_item_data in self.termos:
                termos_item = termos_item_data.to_dict()
                termos.append(termos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if nome is not UNSET:
            field_dict["nome"] = nome
        if email is not UNSET:
            field_dict["email"] = email
        if bloqueado is not UNSET:
            field_dict["bloqueado"] = bloqueado
        if grupo_usuarios is not UNSET:
            field_dict["grupo_usuarios"] = grupo_usuarios
        if tipo_documento is not UNSET:
            field_dict["tipo_documento"] = tipo_documento
        if documento is not UNSET:
            field_dict["documento"] = documento
        if data_nasc is not UNSET:
            field_dict["data_nasc"] = data_nasc
        if telefone is not UNSET:
            field_dict["telefone"] = telefone
        if nome_empresa_tur is not UNSET:
            field_dict["nome_empresa_tur"] = nome_empresa_tur
        if segmento_tur is not UNSET:
            field_dict["segmento_tur"] = segmento_tur
        if codigo_postal is not UNSET:
            field_dict["codigo_postal"] = codigo_postal
        if pais is not UNSET:
            field_dict["pais"] = pais
        if estado is not UNSET:
            field_dict["estado"] = estado
        if municipio is not UNSET:
            field_dict["municipio"] = municipio
        if bairro is not UNSET:
            field_dict["bairro"] = bairro
        if endereco is not UNSET:
            field_dict["endereco"] = endereco
        if numero is not UNSET:
            field_dict["numero"] = numero
        if data_hora_cadastro is not UNSET:
            field_dict["data_hora_cadastro"] = data_hora_cadastro
        if data_hora_alteracao is not UNSET:
            field_dict["data_hora_alteracao"] = data_hora_alteracao
        if termos is not UNSET:
            field_dict["termos"] = termos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_api_ec_clientes_response_200_termos_item import GetApiEcClientesResponse200TermosItem

        d = dict(src_dict)
        codigo = d.pop("codigo", UNSET)

        nome = d.pop("nome", UNSET)

        email = d.pop("email", UNSET)

        bloqueado = d.pop("bloqueado", UNSET)

        grupo_usuarios = d.pop("grupo_usuarios", UNSET)

        tipo_documento = d.pop("tipo_documento", UNSET)

        documento = d.pop("documento", UNSET)

        _data_nasc = d.pop("data_nasc", UNSET)
        data_nasc: Union[Unset, datetime.date]
        if isinstance(_data_nasc, Unset):
            data_nasc = UNSET
        else:
            data_nasc = isoparse(_data_nasc).date()

        telefone = d.pop("telefone", UNSET)

        def _parse_nome_empresa_tur(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nome_empresa_tur = _parse_nome_empresa_tur(d.pop("nome_empresa_tur", UNSET))

        def _parse_segmento_tur(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        segmento_tur = _parse_segmento_tur(d.pop("segmento_tur", UNSET))

        def _parse_codigo_postal(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        codigo_postal = _parse_codigo_postal(d.pop("codigo_postal", UNSET))

        def _parse_pais(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pais = _parse_pais(d.pop("pais", UNSET))

        def _parse_estado(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        estado = _parse_estado(d.pop("estado", UNSET))

        def _parse_municipio(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        municipio = _parse_municipio(d.pop("municipio", UNSET))

        def _parse_bairro(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bairro = _parse_bairro(d.pop("bairro", UNSET))

        def _parse_endereco(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        endereco = _parse_endereco(d.pop("endereco", UNSET))

        def _parse_numero(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        numero = _parse_numero(d.pop("numero", UNSET))

        def _parse_data_hora_cadastro(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_hora_cadastro_type_0 = isoparse(data)

                return data_hora_cadastro_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        data_hora_cadastro = _parse_data_hora_cadastro(d.pop("data_hora_cadastro", UNSET))

        def _parse_data_hora_alteracao(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_hora_alteracao_type_0 = isoparse(data)

                return data_hora_alteracao_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        data_hora_alteracao = _parse_data_hora_alteracao(d.pop("data_hora_alteracao", UNSET))

        termos = []
        _termos = d.pop("termos", UNSET)
        for termos_item_data in _termos or []:
            termos_item = GetApiEcClientesResponse200TermosItem.from_dict(termos_item_data)

            termos.append(termos_item)

        get_api_ec_clientes_response_200 = cls(
            codigo=codigo,
            nome=nome,
            email=email,
            bloqueado=bloqueado,
            grupo_usuarios=grupo_usuarios,
            tipo_documento=tipo_documento,
            documento=documento,
            data_nasc=data_nasc,
            telefone=telefone,
            nome_empresa_tur=nome_empresa_tur,
            segmento_tur=segmento_tur,
            codigo_postal=codigo_postal,
            pais=pais,
            estado=estado,
            municipio=municipio,
            bairro=bairro,
            endereco=endereco,
            numero=numero,
            data_hora_cadastro=data_hora_cadastro,
            data_hora_alteracao=data_hora_alteracao,
            termos=termos,
        )

        get_api_ec_clientes_response_200.additional_properties = d
        return get_api_ec_clientes_response_200

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
