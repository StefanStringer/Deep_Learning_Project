# SmolVLA Robotic Manipulation Pipeline (ManiSkill3 + LeRobot)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C.svg)](https://pytorch.org/)

An end-to-end Vision-Language-Action (VLA) manipulation pipeline fine-tuning **SmolVLA** (500M parameters) on **ManiSkill3 PickCube-v1** using **HuggingFace LeRobot**. Based on https://github.com/Aditya-1711/vla-manipulation.git

---

## 📌 Features

Todo

---

## 🛠️ Installation

```bash
# Clone repository
git https://github.com/StefanStringer/Deep_Learning_Project.git
cd Deep_Learning_Project

# Install core dependencies
pip install "numpy>=2.0.0,<2.3.0"
pip install "lerobot[dataset]" av wandb num2words
pip install --no-deps mani_skill
pip install pytorch_kinematics_ms arm_pytorch_utilities nvidia-ml-py
pip install gymnasium h5py trimesh transforms3d pandas sapien dacite GitPython tyro
```

---

## 🚀 Usage

### Environment Debug
If it shows "ImportError: pytorch_kinematics_ms not installed. Install with pip install pytorch_kinematics_ms", run:
```
python -m pip install --force-reinstall --no-deps --no-cache-dir pytorch-kinematics-ms==0.7.3
```

### 1. Prepare Data
```bash
cd Deep_Learning_Project
python -m data_collection.collect_demos
python -m data_collection.dataset_convert
```

### 2. Fine-Tuning SmolVLA Policy
You can run run_train.sh simply, or:

```bash
lerobot-train \
  --policy.path=lerobot/smolvla_base \
  --policy.push_to_hub=false \
  --dataset.repo_id=local/pick_cube_rebalanced \
  --dataset.root="./data/lerobot_pick_cube" \
  '--rename_map={"observation.image": "observation.images.camera1"}' \
  --output_dir="./checkpoints/smolvla_pickcube_60ep_8k" \
  --batch_size=4 \
  --optimizer.lr=1e-4 \
  --steps=8000 \
  --save_freq=1000 \
  --log_freq=20 \
  --wandb.enable=false
```

### 3. Single Episode Diagnostic Rollout
You can run run_eval_seed1000.sh simply, or:
```bash
python evaluation/eval_seed1000_full_trace.py
```

### 4. Complete 35-Seed Benchmark Evaluation
```bash
python evaluation/eval_full_matrix.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
