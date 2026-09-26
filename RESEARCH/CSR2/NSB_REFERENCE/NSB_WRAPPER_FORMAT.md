# NSB Wrapper Format — Byte-Verified (2026-09-26)

## Pipeline

```
GZIP (magic 1f 8b at byte 0)
  → wrapper/header line
  → newline (\n)
  → JSON payload
```

Verified via raw bytes of `nsb_0_uzjh.bin` (game 6.7.0, 636 top-level keys).
Decompressed: 4,236,248 bytes. Header is inside the gzip, before the JSON.

## Wrapper Structure

```
<major-version>-ver-<40-char-hex>
```

Observed:
- `6-ver-3a39f08a3563f907cf6f95eb57eb4d5871af1c6e` (game 6.7.0)
- `3-ver-<40 hex>` (older saves)

The 40-character value is lowercase hex. The version prefix tracks the game major version.

## Status

| Component | Status |
|-----------|--------|
| GZIP outer layer | Verified |
| Wrapper inside GZIP | Verified |
| Wrapper before JSON, separated by newline | Verified |
| Versioned prefix (`<major>-ver-`) | Verified |
| 40-char hex value | Verified |
| `3-ver-` / `6-ver-` variation | Observed |
| When/why the version prefix changed | Open |
| Export filename behavior (imported name ignored) | Unverified (write-path) |
| Wrapper is JSON metadata | False — ruled out |

## Retired

The shorthand "NSB = bare 40-char value + newline + JSON" is retired.
NSB carries a version prefix. Do not use the old form.

## Note

This is a research/spec finding, not a KOSD governance decision.
It becomes a locked implementation behavior only via CORE/DECISIONS.md.
