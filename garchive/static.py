# Copyright 2023 iiPython
# Copy of Blacksheep's static handlers with added authentication

# Modules
import os
from typing import Optional, Awaitable, Callable, Set
from .identity import match_ip

# Blacksheep hell
from blacksheep.messages import Request, Response
from blacksheep.server.routing import Route, Router
from blacksheep.exceptions import NotFound, Unauthorized
from blacksheep.server.files import validate_source_path, get_default_extensions
from blacksheep.server.files.dynamic import (
    get_static_files_route, unquote, get_response_for_resource_path, get_resource_file_content
)
from blacksheep.server.application import FilesHandler

# Utilities
def get_client_ip(request: Request) -> str:
    cf = request.headers.get_first(b"CF-Connecting-IP")
    if cf is not None:
        cf = cf.decode()

    if not (cf or "").strip():
        return request.client_ip

    return cf

# Handlers
def get_files_route_handler(
    files_handler: FilesHandler,
    source_folder_name: str,
    discovery: bool,
    cache_time: int,
    extensions: Set[str],
    root_path: str,
    index_document: Optional[str],
    fallback_document: Optional[str],
) -> Callable[[Request], Awaitable[Response]]:
    files_list_html = get_resource_file_content("fileslist.html")
    source_folder_full_path = os.path.abspath(str(source_folder_name))

    async def static_files_handler(request: Request) -> Response:
        assert request.route_values is not None, "Expects a route pattern with star *"
        tail = unquote(request.route_values.get("tail", "")).lstrip("/")
        if tail.replace("../", "").split("/")[-1] == "download.zip":
            if not match_ip(get_client_ip(request)):
                raise Unauthorized

        try:
            return get_response_for_resource_path(
                request,
                tail,
                files_list_html,
                source_folder_name,
                files_handler,
                source_folder_full_path,
                discovery,
                cache_time,
                extensions,
                root_path,
                index_document,
            )
        except NotFound:
            if fallback_document is None:
                raise

            return get_response_for_resource_path(
                request,
                fallback_document,
                files_list_html,
                source_folder_name,
                files_handler,
                source_folder_full_path,
                discovery,
                cache_time,
                extensions,
                root_path,
                None,
            )

    return static_files_handler

def serve_files_dynamic(
    router: Router,
    files_handler: FilesHandler,
    source_folder: str,
    *,
    discovery: bool,
    cache_time: int,
    extensions: Optional[Set[str]],
    root_path: str,
    index_document: Optional[str],
    fallback_document: Optional[str],
    anonymous_access: bool = True,
) -> None:
    validate_source_path(source_folder)

    if not extensions:
        extensions = get_default_extensions()

    handler = get_files_route_handler(
        files_handler,
        str(source_folder),
        bool(discovery),
        int(cache_time),
        set(extensions),
        root_path,
        index_document,
        fallback_document,
    )

    handler.allow_anonymous = True
    route = Route(
        get_static_files_route(root_path),
        handler,
    )
    router.add_route("GET", route)
    router.add_route("HEAD", route)
