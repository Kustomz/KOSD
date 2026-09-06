# KOSD CSR2 Direct Acquisition Model

**Status:** LOCKED
**Scope:** CSR2 APK and OBB acquisition
**Effective:** 2026-09-06

## Locked Directory Model

Each acquired CSR2 version is represented by one version directory under `ACQUISITION`.

```text
ACQUISITION/<version>/
├── base.apk
└── com.naturalmotion.customstreetracer2/
    ├── main.obb
    └── patch.obb
```

`base.apk` is a sibling of the Android package directory. It is **not** stored inside `com.naturalmotion.customstreetracer2/`.

Only OBB files that actually exist for that release are present.

## APK Acquisition

- APKs are acquired as complete files.
- Termux is the preferred upload path.
- Manual file splitting is not required while the APK remains below GitHub's regular Git individual-file limit.
- The APK workflow validates the complete file, records its SHA-256, and maintains Current + Previous released APK retention.
- If a future APK reaches the regular Git individual-file limit, the APK acquisition path will be migrated to Git LFS rather than introducing manual chunk splitting.

## OBB Acquisition

- OBBs are acquired as complete files.
- OBBs are stored with Git LFS.
- Manual `.001/.002/.003` splitting is not required for the direct acquisition model.
- Termux may push the complete OBB files directly to GitHub LFS.
- The OBB ingestion workflow validates and promotes the files to the canonical game-version tree:

```text
RESEARCH/CSR2/GAME_VERSIONS/<version>/
├── MAIN_OBB/
│   └── main.obb
└── PATCH_OBB/
    └── patch.obb
```

- Current + Previous game versions are retained; older OBB data is purged after successful ingestion.

## Source-of-Truth Rule

The direct acquired files are transport/source inputs. Canonical OBB research artifacts remain under `RESEARCH/CSR2/GAME_VERSIONS/<version>/` and are stored with Git LFS.

The complete APK remains available under `ACQUISITION/RELEASED_APK/` subject to Current + Previous retention.

## Locked Principle

KOSD does not require manual file splitting merely to accommodate a browser-upload limitation. Large-file handling is delegated to Git LFS where required.
