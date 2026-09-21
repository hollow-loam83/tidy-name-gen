# tidyname

Random name generation is easy. Random names that look consistent are not,
because the source lists are never clean. Pull first/last names from a CSV
export, a scraped page, or an old database dump and you get "MARY", "james",
"O'BRIEN", "van der berg" all mixed together. Feed that straight into a
generator and half your output looks broken.

`tidyname` is a small formatter for that problem, plus a generator built on
top of it. The formatter is the actual point - the generator exists mostly
to prove the formatter is worth having.

## What it fixes

- inconsistent casing (`MARY` / `mary` / `Mary` -> `Mary`)
- extra or repeated whitespace, including non-breaking spaces from web copy-paste
- `Mc` surnames (`MCDONALD` -> `McDonald`)
- apostrophes (`o'brien` -> `O'Brien`)
- hyphenated names (`ST-PIERRE` -> `St-Pierre`)
- lowercase particles (`DE LA CRUZ` -> `de la Cruz`, `VAN DER BERG` -> `van der Berg`)
- "Last, First" input (`SMITH, JOHN` -> `John Smith`)
- common titles and suffixes (`DR. JOHN SMITH` -> `John Smith`, `Smith, John, Jr.` -> `John Smith`)

## What it doesn't do

- guess at nicknames or middle names
- handle non-Latin scripts

These are all things a name formatter *could* grow into, but they need real
decisions about behavior, so they're left out rather than half-implemented.

## Usage

```python
from tidyname import normalize_name

normalize_name("MARY O'BRIEN")        # "Mary O'Brien"
normalize_name("  jean   VAN DYKE  ") # "Jean van Dyke"
normalize_name("mcdonald-smith")      # "McDonald-Smith"
normalize_name("SMITH, JOHN")         # "John Smith"
normalize_name("Dr. John Smith")      # "John Smith"
normalize_name("SMITH, JOHN, JR.")    # "John Smith"
```

```python
from tidyname import RandomNameGenerator

gen = RandomNameGenerator(seed=42)
gen.full_name()        # "Karen McDonald"
gen.many(3)             # ["Sarah van der Berg", "David Lopez", "Mary O'Connor"]
```

`RandomNameGenerator` ships with a real-sized built-in name pool (a few
hundred first and last names, deliberately left messy-cased to double as a
formatter demo) but accepts your own lists:

```python
gen = RandomNameGenerator(
    first_names=["ALICE", "bob"],
    last_names=["MCGUIRE", "o'neill"],
)
```

## Status

First working version. The default name pools are now real-sized, "Last,
First" input is reordered automatically, and common titles/suffixes are
stripped. Still missing: a test suite - see "What it doesn't do" above for
the full list of gaps.

## License

MIT, see LICENSE.
