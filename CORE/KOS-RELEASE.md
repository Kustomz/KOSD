# KOS-RELEASE

**Version:** 2.0.0 (Draft)
**Status:** Draft

## Purpose

Defines the controlled release process for KOSD.

## Release Principle

A KOSD build is not a release merely because files have been created or assembled.

A release requires validation of the applicable modules and confirmation that the release contents are internally consistent with the current authoritative KOS/project state.

## Release States

- DRAFT — work in progress; not authoritative as a release.
- VALIDATION — release candidate undergoing validation.
- RELEASED — validated KOSD distribution.
- SUPERSEDED — a released version replaced by a later released version.
- ARCHIVED — retained historical release.

## Release Requirements

Before a KOSD build is released:

1. Required modules are present.
2. Stable IDs are preserved.
3. Locked content has not been silently altered.
4. Module versions and statuses are explicit.
5. Applicable dependencies and relationships are present.
6. Recovery/project-state conflicts have been identified and resolved.
7. Validation checks have passed.
8. Release contents are recorded.
9. A release version is assigned.
10. The release is recorded in the changelog.

## Recovery Relationship

KOSD is built from the recovered Kustomz project state.

Recovery items marked REVIEW must not be silently treated as authoritative without the applicable project decision.

## Release Integrity

A release should include a machine-readable or otherwise auditable record of its included modules and their versions.

Checksums may be used to establish file integrity.

## Rollback / Historical Preservation

Previously released KOSD versions must remain identifiable and recoverable. A new release must not destroy the ability to reproduce or inspect a prior release.

## Current Build Boundary

The current KOSD v2.0.0 work is a Draft build.

It is NOT a released KOSD distribution.

## Kustomz Decision

_Not yet reviewed._

## Master Promotion

Not yet promoted.
