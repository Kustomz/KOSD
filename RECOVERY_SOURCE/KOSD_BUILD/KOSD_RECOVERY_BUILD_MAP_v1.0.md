# KOSD RECOVERY BUILD MAP

Version: 1.0
Status: DRAFT / BUILD CHECKPOINT
Source: Kustomz Project Recovery v1.5

## Purpose

This document defines the first bridge from the Kustomz Project Recovery state into the KOS Distribution (KOSD) build.

Recovery is the source for the currently established Kustomz project state. Existing KOSD files are treated as prior implementation material to migrate where they remain consistent with recovery.

This is a build map, not a release.

## Governing Principles

- Recovery establishes the project state to be carried forward.
- KOSD implementation must preserve locked decisions and stable IDs.
- Existing valid KOSD material is migrated rather than blindly recreated.
- Recovery items marked REVIEW are not silently promoted to LOCKED.
- Missing information remains missing.
- A KOSD module is not authoritative merely because it has been created.
- Released KOSD modules are governed by the KOSD release process.

## Phase 1 — KOSD Core

The documented KOSD roadmap identifies these Core modules:

- KOS-MANIFEST
- KOS-CORE-001
- KOS-INDEX-001
- STD-001
- MODULE-TEMPLATE
- KOS-RELEASE
- CHANGELOG

## First Build Order

1. Establish KOSD Core directory and module naming.
2. Migrate/validate the existing Core module set.
3. Build the KOSD registry/index from the recovered project state.
4. Establish the module template and standard metadata.
5. Map Governance and existing CBP material.
6. Map Acquisition/toolchain material, including E-004/E-005.
7. Map Production and existing BP workflows.
8. Build library indexes.
9. Convert approved assets while preserving IDs and relationships.
10. Run validation gates.
11. Prepare a release candidate.
12. Publish only after release criteria are satisfied.

## Important Boundary

The recovery package is not itself the KOSD release.

KOSD must be constructed from the recovered state, but each KOSD module still requires its own validation and status.
