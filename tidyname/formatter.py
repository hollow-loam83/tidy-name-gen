"""Normalize messy human-name strings into a consistent display form.

Name lists pulled from CSV exports, scraped pages, or old databases tend to
arrive in whatever case someone typed them in: ALL CAPS, all lowercase, extra
internal whitespace, non-breaking spaces copied from a web page, and so on.
This module turns that mess into a single predictable casing so the rest of
a pipeline (matching, deduping, display) can rely on it.

It is deliberately narrow: it fixes casing and whitespace, and knows about
a handful of common patterns (Mc-, apostrophes, hyphenated names, lowercase
particles like "van" or "de la"). It does not try to parse name order,
strip titles, or guess nicknames - see the README for what's out of scope.
"""

import re

_WHITESPACE_RE = re.compile(r"\s+")
_NBSP = "\xa0"

# Particles that conventionally stay lowercase inside a name (van Gogh,
# Lucia de la Cruz). This list covers the common Western European cases
# and is intentionally not exhaustive.
_PARTICLES = frozenset(
    {"de", "del", "della", "der", "den", "di", "du", "la", "le", "van", "von", "bin", "al", "da"}
)


def normalize_name(raw):
    """Return `raw` with whitespace collapsed and casing fixed.

    Empty or None input returns "". Non-breaking spaces (as seen in text
    copy-pasted from web pages) are treated like regular spaces.
    """
    if raw is None:
        return ""
    text = raw.replace(_NBSP, " ")
    text = _WHITESPACE_RE.sub(" ", text).strip()
    if not text:
        return ""
    return " ".join(_format_token(token) for token in text.split(" "))


def _format_token(token):
    if not token:
        return token
    lowered = token.lower()
    if lowered in _PARTICLES:
        return lowered
    if "-" in token:
        return "-".join(_format_token(part) for part in token.split("-"))
    if "'" in token:
        return "'".join(_capitalize(part) for part in token.split("'"))
    return _capitalize(token)


def _capitalize(segment):
    if not segment:
        return segment
    lower = segment.lower()
    # "Mc" is almost always followed by a capital (McDonald, McKenzie).
    # "Mac" is not attempted here - too many surnames (Mack, Macy) would
    # get mangled by a blanket rule.
    if lower.startswith("mc") and len(lower) > 2:
        return "Mc" + lower[2].upper() + lower[3:]
    return lower[0].upper() + lower[1:]
