from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_api_auth_body import PostApiAuthBody
from ...models.post_api_auth_response_200 import PostApiAuthResponse200
from ...models.post_api_auth_response_400 import PostApiAuthResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiAuthBody,
    content_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(content_type, Unset):
        headers["Content-Type"] = content_type

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PostApiAuthResponse200, PostApiAuthResponse400]]:
    if response.status_code == 200:
        response_200 = PostApiAuthResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PostApiAuthResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PostApiAuthResponse200, PostApiAuthResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiAuthBody,
    content_type: Union[Unset, str] = UNSET,
) -> Response[Union[PostApiAuthResponse200, PostApiAuthResponse400]]:
    """Autenticação

     Um único login de integração pode fazer chamadas na API de diversos parceiros, como exemplo, um
    mesmo integrador que faz a integração das vendas de vários e-commerces, cada um de um parceiro
    específico, porém utilizando o mesmo token de autenticação. Mas também é possível realizar a criação
    de um login único para cada parceiro de venda.
    ## Tempo de validade do token
    O token tem tempo de validade indeterminado, somente deixa de ser válido após a senha ser alterada
    ou o parceiro não estiver mais cadastrado.

    Args:
        content_type (Union[Unset, str]):
        body (PostApiAuthBody):  Example: {'usuario': 'usuario', 'senha': 'senha'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiAuthResponse200, PostApiAuthResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
        content_type=content_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiAuthBody,
    content_type: Union[Unset, str] = UNSET,
) -> Optional[Union[PostApiAuthResponse200, PostApiAuthResponse400]]:
    """Autenticação

     Um único login de integração pode fazer chamadas na API de diversos parceiros, como exemplo, um
    mesmo integrador que faz a integração das vendas de vários e-commerces, cada um de um parceiro
    específico, porém utilizando o mesmo token de autenticação. Mas também é possível realizar a criação
    de um login único para cada parceiro de venda.
    ## Tempo de validade do token
    O token tem tempo de validade indeterminado, somente deixa de ser válido após a senha ser alterada
    ou o parceiro não estiver mais cadastrado.

    Args:
        content_type (Union[Unset, str]):
        body (PostApiAuthBody):  Example: {'usuario': 'usuario', 'senha': 'senha'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiAuthResponse200, PostApiAuthResponse400]
    """

    return sync_detailed(
        client=client,
        body=body,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiAuthBody,
    content_type: Union[Unset, str] = UNSET,
) -> Response[Union[PostApiAuthResponse200, PostApiAuthResponse400]]:
    """Autenticação

     Um único login de integração pode fazer chamadas na API de diversos parceiros, como exemplo, um
    mesmo integrador que faz a integração das vendas de vários e-commerces, cada um de um parceiro
    específico, porém utilizando o mesmo token de autenticação. Mas também é possível realizar a criação
    de um login único para cada parceiro de venda.
    ## Tempo de validade do token
    O token tem tempo de validade indeterminado, somente deixa de ser válido após a senha ser alterada
    ou o parceiro não estiver mais cadastrado.

    Args:
        content_type (Union[Unset, str]):
        body (PostApiAuthBody):  Example: {'usuario': 'usuario', 'senha': 'senha'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PostApiAuthResponse200, PostApiAuthResponse400]]
    """

    kwargs = _get_kwargs(
        body=body,
        content_type=content_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostApiAuthBody,
    content_type: Union[Unset, str] = UNSET,
) -> Optional[Union[PostApiAuthResponse200, PostApiAuthResponse400]]:
    """Autenticação

     Um único login de integração pode fazer chamadas na API de diversos parceiros, como exemplo, um
    mesmo integrador que faz a integração das vendas de vários e-commerces, cada um de um parceiro
    específico, porém utilizando o mesmo token de autenticação. Mas também é possível realizar a criação
    de um login único para cada parceiro de venda.
    ## Tempo de validade do token
    O token tem tempo de validade indeterminado, somente deixa de ser válido após a senha ser alterada
    ou o parceiro não estiver mais cadastrado.

    Args:
        content_type (Union[Unset, str]):
        body (PostApiAuthBody):  Example: {'usuario': 'usuario', 'senha': 'senha'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PostApiAuthResponse200, PostApiAuthResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            content_type=content_type,
        )
    ).parsed
