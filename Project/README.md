# Deep_Learning_Project

GitHub repo for Deep Learning course project.
**Project Title:** Vision-Language-Action (VLA) Model for some control, maybe robotic (EDIT when known)

## Group Members
Please add your name and details here when joining the repo.

| Name | Discord Handle | 
| :--- | :--- | 
| Stefan Stringer | ChickenSandwhichKing |
| Mikkel Møllebro | Makrel |
| Alf Beedholm | Alf |

## Project Overview
We are developing a Vision-Language-Action (VLA) model capable of translating visual inputs (images/video frames) and natural language instructions into actionable control signals for simulated environments (e.g., robotic arm manipulation or autonomous vehicle navigation).

The model will be trained using:
1.  **Supervised Learning:** On a dataset of ....... (Insert when known)
2.  **Reinforcement learning**

## Problem Statement
Current robotic systems often struggle with generalisation to new tasks or environments. By combining computer vision (to perceive the world) and NLP (to understand high-level goals), we aim to create a policy that can execute complex, multi-step tasks based on simple textual commands.
*   **Goal:** Minimise task failure rate and maximise the smoothness.
*   **Success Metric:** Percentage of successful task completions in simulation and smoothness score of control outputs.

## Dataset
Details regarding the data source and preprocessing will be documented here.


## Model Architecture
We will utilize **PyTorch** as our primary framework.



# Project Setup Guide: Vision-Language-Action (VLA) Model

This guide outlines the exact steps to set up a unified development environment for our group project. Everyone must use the same stack (WSL2 + Ubuntu + Python 3.13 + NVIDIA CUDA) to ensure reproducibility.

We use **uv** to manage the Python interpreter and all dependencies from a single
configuration file, `pyproject.toml`.

---

## Install uv

Run this once per machine:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc        # or: exec $SHELL
uv --version
```

If `uv --version` prints a version number, you are done with this step.

---

## Understand the project configuration

Everything about our environment lives in **`pyproject.toml`** at the repository
root. If anything else is added, it should be added into the toml file as this is
the main point for our environment and what packages/versions are used


## Sync the environment

From the repository root:

```bash
uv sync
```

What happens:

1. uv reads `requires-python` and `.python-version`.
2. It downloads a managed Python 3.13 build if you do not already have one.
3. It creates a virtual environment at `.venv/`.
4. It resolves all dependencies and writes `uv.lock`.
5. It installs the resolved set into `.venv/`.

The first run takes a few minutes because PyTorch is large. Later runs are
near-instant thanks to uv's cache.

---

## Environment Verification

Run the bundled sanity check. It validates the interpreter version, confirms the
virtual environment is active, imports every critical package, and probes CUDA.

```bash
uv run python environment_checker.py
```

Expected output starts with `Python 3.13.x` and ends with a passing report.

**Copy the entire output and post it in the group chat.** This lets us confirm
everyone haws the same environment!

---

## Running code

Every time you start a work session:

```bash
cd ~/vla-project
git pull origin main
uv sync                          # picks up any new dependencies

```

`uv run` executes the command inside `.venv` without activating anything. It also
re-syncs automatically if `pyproject.toml` changed.

## Optional: pinning a specific PyTorch CUDA build

The default Linux wheels on PyPI are already CUDA-enabled, so most people can
skip this. Only do it if `torch.cuda.is_available()` returns `False` after
confirming your GPU is visible via `nvidia-smi`.

```bash
uv sync
uv run python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

Confirm the GPU is visible to PyTorch — you want a version number followed by
`True`.

---

## Fallback: plain pip (only if you cannot use uv)

If you are blocked from installing uv, the older manual route still works.

### Create and activate a virtual environment

```bash
python3.13 -m venv venv
source venv/bin/activate
```

Your prompt should now show the `(venv)` prefix:

```
(venv) user@machine:~/vla-project$
```

> **Every new terminal session** requires re-activation:
> ```bash
> source venv/bin/activate
> ```
> To leave the environment: `deactivate`

### Install dependencies

Upgrade pip first, since a fresh environment is bare bones:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Clean reset

If the environment becomes corrupted:

```bash
rm -rf .venv
uv sync
```

Your code and committed work are untouched — only the environment is rebuilt.

---

## File reference

| File | Purpose |
|---|---|---|
| `pyproject.toml` | Python version + direct dependencies |
| `uv.lock` | Exact resolved versions for reproducibility |
| `.python-version` | Pins the interpreter version |
| `requirements.txt` | Human-readable intent, kept for reference |
| `requirements.lock.txt` | Auto-generated pip export |
| `.venv/` | The virtual environment itself |

**Commit:** `pyproject.toml`, `uv.lock`, `.python-version`
**Ignore:** `.venv/`, `requirements.lock.txt`, `__pycache__/`, `data/`, `checkpoints/`

## Project roadmap
This project will attempt to create a Vision-language-action (VLA) model by first establishing a baseline using an established dataset and later extending the model to a cooking task and later fine-tuning. 

### Phase 0: Establishing baseline
We will establish a baseline for our project by implementing the smolVLA model and achieving better-than-chance-level results for the model outputs when trained on the Maniskill3 Franka `PickCube-v1` dataset. 

### Phase 1: 
Achieving comparable results to similar projects by testing different loss functions and optimisers on the model. This phase will be implemented for all other future phases henceforth. 

### Phase 2: 
Fine-tune the model using the `lerobot/smolVLA` fine-tuning pipeline evaluated on a reduction of loss.

### Phase 3: 
Creating a small dataset based on a cooking task of picking up cooking-relevant items.

### Phase 4: 
Create voice-to-text input for the model.

### Phase 5: 
Initializing the model on a physical robot to evaluate difference between simulated and real-life performance.  

### Phase 6: 
Have the model run on a physical robot manipulator.

### Phase 7: 
Recreate part of the training structure to allow reinforcement learning, which can marginally improve performance of the model. Compare results with longer similar training time on the original data. 
