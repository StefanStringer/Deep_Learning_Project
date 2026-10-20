# Deep_Learning_Project

GitHub repo for Deep Learning course project.
**Project Title:** Vision-Language-Action (VLA) Model for some control, maybe robotic (EDIT when known)

## Group Members
Please add your name and details here when joining the repo.

| Name | Discord Handle | 
| :--- | :--- | 
| Stefan Stringer | ChickenSandwhichKing |
| Mikkel Møllebro | Makrel |

## Project Overview
We are developing a Vision-Language-Action (VLA) model capable of translating visual inputs (images/video frames) and natural language instructions into actionable control signals for simulated environments (e.g., robotic arm manipulation or autonomous vehicle navigation).

The model will be trained using:
1.  **Supervised Learning:** On a dataset of ....... (Insert when known)

## Problem Statement
Current robotic systems often struggle with generalisation to new tasks or environments. By combining computer vision (to perceive the world) and NLP (to understand high-level goals), we aim to create a policy that can execute complex, multi-step tasks based on simple textual commands.
*   **Goal:** Minimise task failure rate and maximise the smoothness.
*   **Success Metric:** Percentage of successful task completions in simulation and smoothness score of control outputs.

## Dataset
Details regarding the data source and preprocessing will be documented here.


## Model Architecture
We will utilize **PyTorch** as our primary framework.



# Project Setup Guide: Vision-Language-Action (VLA) Model

This guide outlines the exact steps to set up a unified development environment for our group project. Everyone must use the same stack (WSL2 + Ubuntu 3.13 + NVIDIA CUDA) to ensure reproducibility.

## Python Installation

The project targets **Python 3.13**.

```bash
# Update and refresh the package index 
sudo apt update
sudo apt install -y software-properties-common

# Add python repository
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Install Python 3.13, venv support, dev headers, and build tools
sudo apt install -y python3.13 python3.13-venv python3.13-dev build-essential git

# Confirm the version
python3.13 --version
```

## Virtual Environment Setup

An isolated environment keeps project dependencies separate from system Python and guarantees everyone resolves the same versions.

### Create the virtual environment

```bash
python3.13 -m venv venv
```

### Activate it

```bash
source venv/bin/activate
```

Your prompt should now show the `(venv)` prefix seeen below:

```
(venv) user@machine:~/vla-project$
```

> **Every new terminal session** requires re-activation:
> ```bash
> source venv/bin/activate
> ```
> To leave the environment: `deactivate`

---

##  Install Project Dependencies

### Install requirements

Do this once you have created the environment, so that everything here is the same as everyone elses! This is the whole point.
```bash
pip install -r requirements.txt
```

Make sure pip is upgraded and everything, as environment will be very bare bones.
```bash
pip install --upgrade pip
```

### Install PyTorch with the right CUDA build

If `requirements.txt` does not pin a CUDA-specific PyTorch build, install it explicitly. Pick the command matching your driver from the official selector at **pytorch.org/get-started/locally**, then re-run the requirements install so nothing is downgraded:

```bash
# Example shape only — use the exact command from the PyTorch selector
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126

# Then reconcile with the rest of the pinned deps
pip install -r requirements.txt
```

Confirm the GPU is visible to PyTorch:

```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

---

## Environment Verification

Run the bundled sanity check. It validates the interpreter version, confirms the virtual environment is active, imports every critical package, and probes CUDA.

```bash
python check_environment.py
```
