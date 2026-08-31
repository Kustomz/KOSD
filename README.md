# KOSD

Kustomz Operating System Distribution (KOSD).

## Current State

**Version:** 2.0.0 (Draft)
**State:** Initial repository setup / build checkpoint

KOSD is being constructed from the Kustomz Project Recovery state. The recovery package is the source of current project-state context; existing KOSD implementation material is migrated only where it remains consistent with recovery.

## Build Principles

- Preserve locked decisions and stable IDs.
- Do not silently promote REVIEW recovery items to authoritative status.
- Do not invent missing information.
- Keep draft, validation, release, and historical states distinguishable.
- Treat this repository as the version-controlled home of KOSD.

## Initial Core

The initial Core migration sequence is:

1. KOS-MANIFEST
2. KOS-CORE-001
3. KOS-INDEX-001
4. STD-001
5. MODULE-TEMPLATE
6. KOS-RELEASE
7. CHANGELOG

The Core set is currently assembled as a draft checkpoint and has not been released.
