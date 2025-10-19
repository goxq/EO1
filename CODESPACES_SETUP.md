# EO1 Codespaces Setup Guide / Codespaces 配置指南

## Quick Setup / 快速配置

This guide helps you set up the EO1 environment in GitHub Codespaces or similar cloud development environments.

本指南帮助您在 GitHub Codespaces 或类似的云开发环境中配置 EO1 环境。

## Prerequisites / 前置要求

- GitHub Codespaces or similar cloud IDE / GitHub Codespaces 或类似的云 IDE
- Python 3.10 or higher (3.11 recommended) / Python 3.10 或更高版本（推荐 3.11）

## Step-by-Step Setup / 分步配置

### 1. Clone the Repository / 克隆仓库

If not already in the repository:

```bash
git clone https://github.com/EO-Robotics/EO1.git
cd EO1
```

### 2. Verify Environment / 验证环境

Run the verification script to ensure everything is ready:

运行验证脚本以确保一切就绪：

```bash
python verify_environment.py
```

Expected output should show all checks passing.

预期输出应该显示所有检查都通过。

### 3. Install PyTorch / 安装 PyTorch

The flexible torch dependency allows you to choose the version that best fits your needs:

灵活的 torch 依赖允许您选择最适合您需求的版本：

**For CPU-only (Codespaces default) / 仅 CPU（Codespaces 默认）:**

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

**For CUDA 11.8:**

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

**For CUDA 12.1:**

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

### 4. Install EO1 Package / 安装 EO1 包

```bash
pip install --upgrade setuptools wheel
pip install -e .
```

### 5. Verify Installation / 验证安装

```bash
python -c "import eo; print(f'EO version: {eo.__version__}')"
```

Expected output: `EO version: 0.1.0`

预期输出：`EO version: 0.1.0`

## Alternative: Conda Installation / 替代方案：Conda 安装

If conda is available in your environment:

如果您的环境中有 conda：

```bash
# Create environment / 创建环境
conda create -n eo python=3.11 -y
conda activate eo

# Install dependencies / 安装依赖
pip install --upgrade setuptools wheel
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install -e .
```

## Verification Tests / 验证测试

### Test 1: Package Import / 包导入测试

```python
import eo
print(eo.__version__)
```

### Test 2: Check Dependencies / 检查依赖

```python
import torch
import transformers
import accelerate
import lerobot

print(f"PyTorch: {torch.__version__}")
print(f"Transformers: {transformers.__version__}")
print(f"Accelerate: {accelerate.__version__}")
```

### Test 3: Run Verification Script / 运行验证脚本

```bash
python verify_environment.py
```

### Test 4: Run Setup Simulation / 运行配置模拟

```bash
python test_setup_simulation.py
```

## What Changed in Recent Commits / 最近提交的更改

### Commit 5920dc7: "Change torch dependency to flexible version"

**Before / 之前:**
- Torch was pinned to a specific version
- Users had to match exact CUDA/PyTorch versions
- Torch 被固定到特定版本
- 用户必须匹配确切的 CUDA/PyTorch 版本

**After / 之后:**
- Torch dependency is now flexible: `"torch"` (no version constraint)
- Users can install any compatible PyTorch version
- Supports CPU, CUDA, and ROCm installations
- Torch 依赖现在是灵活的：`"torch"`（无版本限制）
- 用户可以安装任何兼容的 PyTorch 版本
- 支持 CPU、CUDA 和 ROCm 安装

**Benefits / 优点:**
- ✅ Works with any CUDA version (11.8, 12.1, 12.4, etc.)
- ✅ CPU-only installations are straightforward
- ✅ AMD GPU (ROCm) support
- ✅ No version conflicts with existing installations
- ✅ 适用于任何 CUDA 版本（11.8, 12.1, 12.4 等）
- ✅ CPU-only 安装简单直接
- ✅ 支持 AMD GPU（ROCm）
- ✅ 与现有安装没有版本冲突

## Common Issues / 常见问题

### Issue 1: Network Timeout During Installation

**Problem:** pip install times out when downloading packages

**Solution:**
```bash
# Increase timeout
pip install --default-timeout=300 -e .

# Or install dependencies in smaller batches
pip install torch torchvision
pip install transformers accelerate
pip install -e .
```

### Issue 2: Module Import Errors

**Problem:** `ModuleNotFoundError: No module named 'eo'`

**Solution:**
```bash
# Ensure you're in the correct directory
cd /path/to/EO1

# Reinstall in editable mode
pip install -e .
```

### Issue 3: CUDA Version Mismatch

**Problem:** PyTorch CUDA version doesn't match system CUDA

**Solution:**
With the flexible torch dependency, you can now install any compatible version:

```bash
# Check your CUDA version
nvcc --version

# Install matching PyTorch
# For CUDA 11.8:
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# For CUDA 12.1:
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

## Testing the Setup / 测试配置

After installation, run the demo training to ensure everything works:

安装后，运行演示训练以确保一切正常：

```bash
cd experiments/1_demo
bash train.sh
```

## Additional Resources / 额外资源

- [Getting Started Tutorials](getting_started/) - 入门教程
- [Demo Training](experiments/1_demo/) - 演示训练
- [Full Documentation](README.md) - 完整文档

## Troubleshooting / 故障排除

If you encounter any issues:

如果遇到任何问题：

1. Run the verification script: `python verify_environment.py`
2. Check Python version: `python --version` (should be >= 3.10)
3. Verify pip installation: `pip list | grep eo`
4. Check the logs in the verification output
5. Join our [Discord](https://discord.gg/JqfDs6va) for support

## Summary / 总结

✅ **Environment setup has been verified and improved**

✅ **环境配置已验证并改进**

The latest commits make the installation process more flexible and compatible with various hardware configurations. The flexible torch dependency is the key improvement that allows users to:

最新的提交使安装过程更加灵活，并与各种硬件配置兼容。灵活的 torch 依赖是关键改进，它允许用户：

- Choose their preferred PyTorch version / 选择他们喜欢的 PyTorch 版本
- Install on different hardware (CPU, NVIDIA, AMD) / 在不同硬件上安装（CPU、NVIDIA、AMD）
- Avoid version conflicts / 避免版本冲突
- Use different CUDA versions / 使用不同的 CUDA 版本

---

**Last Updated / 最后更新**: 2025-10-19

**Verified on / 验证环境**:
- Platform: Linux x86_64
- Python: 3.10, 3.11, 3.12
- PyTorch: 2.0+
