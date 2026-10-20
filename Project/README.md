# Deep_Learning_Project

GitHub repo for Deep Learning course project.
**Project Title:** Vision-Language-Action (VLA) Model for some control, maybe robotic (EDIT when known)

## Group Members
Please add your name and details here when joining the repo.

| Name | Discord Handle | 
| :--- | :--- | 
| Stefan Stringer | ChickenSandwhichKing |
| [Name] | [Discord] |

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



## Installation and Setup

Everyone must run the same stack. Follow these steps exactly, then run the
environment check at the end and post the output in the group chat.

### Prerequisites

| Requirement | Notes |
|---|---|
| WSL2 with Ubuntu | `wsl --install -d Ubuntu` from PowerShell if missing |
| Python 3.13 | `python3.13 --version` |
| NVIDIA GPU + Windows driver | WSL uses the **Windows** driver - do not install a Linux driver inside WSL |
| Git | `git --version` |

Install the Python dev headers once (needed to build some wheels):

```bash
sudo apt update
sudo apt install -y python3.13 python3.13-venv python3.13-dev git