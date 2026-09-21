"""Normalize messy human-name strings into a consistent display form.

Name lists pulled from CSV exports, scraped pages, or old databases tend to
arrive in whatever case someone typed them in: ALL CAPS, all lowercase, extra
internal whitespace, non-breaking spaces copied from a web page, and so on.
This module turns that mess into a single predictable casing so the rest of
a pipeline (matching, deduping, display) can rely on it.

It is deliberately narrow: it fixes casing and whitespace, knows about a
handful of common patterns (Mc-, apostrophes, hyphenated names, lowercase
particles like "van" or "de la"), reorders simple "Last, First" input, and
strips a small set of common titles and suffixes (Dr., Jr., III). It does
not guess nicknames or middle names - see the README for what's out of
scope.
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

# Leading title, stripped once from the start of the string ("Dr. John
# Smith" -> "John Smith"). Only one is stripped - "Dr. Prof. Smith" is rare
# enough not to bother with.
_TITLE_RE = re.compile(r"^(dr|mr|mrs|ms|miss|prof|rev)\.?\s+", re.IGNORECASE)

# Trailing generational or professional suffix, with an optional leading
# comma ("John Smith, Jr." and "John Smith Jr." both work). Applied
# repeatedly so "John Smith Jr., PhD" loses both.
_SUFFIX_RE = re.compile(r"[,\s]+(jr|sr|ii|iii|iv|v|vi|phd|md|esq)\.?$", re.IGNORECASE)


def normalize_name(raw):
    """Return `raw` with whitespace collapsed, casing fixed, titles/suffixes
    stripped, and "Last, First" input reordered to "First Last".

    Empty or None input returns "". Non-breaking spaces (as seen in text
    copy-pasted from web pages) are treated like regular spaces.
    """
    if raw is None:
        return ""
    text = raw.replace(_NBSP, " ")
    text = _WHITESPACE_RE.sub(" ", text).strip()
    if not text:
        return ""
    text = _TITLE_RE.sub("", text)
    text = _strip_suffixes(text)
    text = _reorder_last_first(text)
    if not text:
        return ""
    return " ".join(_format_token(token) for token in text.split(" "))


def _strip_suffixes(text):
    while True:
        stripped = _SUFFIX_RE.sub("", text)
        if stripped == text:
            return text
        text = stripped


def _reorder_last_first(text):
    # Only handle the unambiguous case: exactly one comma splitting the
    # string into two non-empty halves. Suffixes are stripped before this
    # runs, so a remaining second comma is genuinely ambiguous - leave it
    # alone rather than guess.
    if text.count(",") != 1:
        return text
    last, first = text.split(",", 1)
    last = last.strip()
    first = first.strip()
    if not last or not first:
        return text
    return f"{first} {last}"


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
