"""Tiny sandbox app used for Collie validation."""

from urllib.parse import urlsplit


def normalize_timeout(timeout):
    """Return timeout as a positive float or None."""
    if timeout is None:
        return None
    value = float(timeout)
    if value <= 0:
        raise ValueError("timeout must be positive")
    return value


def path_url(url: str) -> str:
    """Return path and query used by the sandbox request layer."""
    parsed = urlsplit(url)
    path = parsed.path or "/"
    if parsed.query:
        return f"{path}?{parsed.query}"
    return path


def route_operation_id(path: str, method: str) -> str:
    cleaned = path.strip("/").replace("/", "_") or "root"
    return f"{method.lower()}_{cleaned}"
