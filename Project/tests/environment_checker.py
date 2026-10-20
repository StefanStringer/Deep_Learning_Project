#!/usr/bin/env python3
"""
Environment consistency check for Deep_Learning_Project.

Usage:
    python tests/environment_checker.py

Exit code 0 = everything matches, 1 = at least one FAIL.

Every member should run this once after setup and paste the output
into the group chat. So we all start at the same point.
"""

from __future__ import annotations

import platform
import sys
from importlib import metadata

# --------------------------------------------------------------- expectations
# This can be changed if we need to take a different version, I just run on 3.13 currently.
PYTHON_EXPECTED = (3, 13)

REQUIRED_PACKAGES = {
    # name: (minimum, maximum_or_None)   -- maximum is exclusive
    "torch":       ("2.3.0",  "2.10.0"),
    "torchvision": ("0.18.0", "0.25.0"),
    "numpy":       ("1.26.0", "2.2.0"),
    "pandas":      ("2.1.0",  None),
    "scipy":       ("1.12.0", None),
    "matplotlib":  ("3.9.0",  None),
    "wandb":       ("0.16.0", None),
    "tensorboard": ("2.15.0", None),
    "tqdm":        ("4.66.0", None),
}

PASS, WARN, FAIL = "PASS", "WARN", "FAIL"


# ------------------------------------------------------------------- helpers
def _parse(version: str) -> tuple[int, int, int]:
    """Turn '2.9.0+cu126' into (2, 9, 0). Good enough for our purposes."""
    core = version.split("+")[0].split("-")[0]
    nums: list[int] = []
    for chunk in core.split(".")[:3]:
        digits = ""
        for ch in chunk:
            if ch.isdigit():
                digits += ch
            else:
                break
        nums.append(int(digits) if digits else 0)
    while len(nums) < 3:
        nums.append(0)
    return (nums[0], nums[1], nums[2])


def _in_range(version: str, lo: str, hi: str | None) -> bool:
    v = _parse(version)
    ok = v >= _parse(lo)
    if hi is not None:
        ok = ok and v < _parse(hi)
    return ok


def _add(results: list, status: str, label: str, detail: str) -> None:
    results.append((status, label, detail))


# -------------------------------------------------------------------- checks
def check_python(results: list) -> None:
    got = sys.version_info[:2]
    if got == PYTHON_EXPECTED:
        _add(results, PASS, "Python", platform.python_version())
    else:
        _add(
            results,
            FAIL,
            "Python",
            f"{platform.python_version()} "
            f"(expected {PYTHON_EXPECTED[0]}.{PYTHON_EXPECTED[1]}.x)",
        )


def check_packages(results: list) -> None:
    for name, (lo, hi) in REQUIRED_PACKAGES.items():
        try:
            version = metadata.version(name)
        except metadata.PackageNotFoundError:
            _add(results, FAIL, name, "NOT INSTALLED")
            continue

        if _in_range(version, lo, hi):
            _add(results, PASS, name, version)
        else:
            bound = f">={lo}" + (f",<{hi}" if hi else "")
            _add(results, FAIL, name, f"{version}  (requires {bound})")


def check_hardware(results: list):
    """Returns the torch module if it imported, else None."""
    try:
        import torch
    except ImportError:
        _add(results, FAIL, "torch import", "could not import torch")
        return None

    _add(results, PASS, "CUDA build", torch.version.cuda or "CPU-only build")

    if not torch.cuda.is_available():
        _add(results, FAIL, "CUDA", "torch.cuda.is_available() is False")
        return torch

    _add(results, PASS, "GPU", torch.cuda.get_device_name(0))

    try:
        a = torch.randn(512, 512, device="cuda")
        b = torch.randn(512, 512, device="cuda")
        c = a @ b
        torch.cuda.synchronize()
        _add(results, PASS, "GPU matmul", f"ok (sum={float(c.sum()):.3f})")
    except Exception as exc:  # driver mismatch or something
        _add(results, FAIL, "GPU matmul", repr(exc))

    return torch


def fingerprint(torch_mod) -> str | None:
    """
    Seeded random draw, printed so members can compare across machines.
    Small differences are NORMAL (different CPU/GPU/BLAS). Large ones mean
    something is genuinely different about the install.
    """
    if torch_mod is None:
        return None
    torch_mod.manual_seed(0)
    x = torch_mod.randn(1000)
    return f"{float(x.sum()):.6f}"


# ---------------------------------------------------------------------- main
def main() -> int:
    results: list = []

    check_python(results)
    check_packages(results)
    torch_mod = check_hardware(results)
    fp = fingerprint(torch_mod)

    width = max(len(label) for _, label, _ in results) + 2

    print()
    print("=" * 62)
    print(" Deep_Learning_Project - environment check")
    print("=" * 62)
    print(f" Platform : {platform.platform()}")
    print(f" Machine  : {platform.machine()}  ({platform.processor() or 'unknown CPU'})")
    print("-" * 62)

    for status, label, detail in results:
        print(f" [{status}] {label:<{width}}{detail}")

    if fp is not None:
        print("-" * 62)
        print(f" Fingerprint (seeded randn sum): {fp}")
        print(" Method to see where we, as a group, deviate. Hopefully minimal.")

    n_fail = sum(1 for s, _, _ in results if s == FAIL)
    n_warn = sum(1 for s, _, _ in results if s == WARN)

    print("-" * 62)
    if n_fail:
        print(f" RESULT: {n_fail} FAIL, {n_warn} WARN  -> fix before continuing")
    else:
        print(f" RESULT: all {len(results)} checks passed  -> environment OK")
    print("=" * 62)
    print()

    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())