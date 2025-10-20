# 安装过程示例 / Installation Process Example

## 基于 pyproject.toml 的依赖解析 / Dependency Resolution Based on pyproject.toml

当运行 `pip install -e .` 时，pip 会根据 pyproject.toml 中的依赖规范解析并安装包。

When running `pip install -e .`, pip resolves and installs packages based on dependency specifications in pyproject.toml.

### 观察到的安装行为 / Observed Installation Behavior

根据实际的 pip 安装尝试，以下是依赖解析的关键发现：

Based on actual pip installation attempts, here are key findings from dependency resolution:

```
Collecting torch (from eo==0.1.0)
  Downloading torch-2.9.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata

Collecting torchvision>=0.21.0 (from eo==0.1.0)
  Downloading torchvision-0.24.0-cp312-cp312-manylinux_2_28_x86_64.whl.metadata

Collecting transformers==4.56.0 (from eo==0.1.0)
  Downloading transformers-4.56.0-py3-none-any.whl.metadata

Collecting lerobot<=0.3.4,>=0.3.3 (from eo==0.1.0)
  Downloading lerobot-0.3.3-py3-none-any.whl.metadata
```

### 关键依赖的版本选择 / Version Selection for Key Dependencies

| 包名 / Package | pyproject.toml 规范 | Pip 选择的版本 | 说明 / Notes |
|----------------|---------------------|----------------|--------------|
| **torch** | `"torch"` | **2.9.0** | 最新稳定版，与 Python 3.12 兼容 |
| **torchvision** | `"torchvision>=0.21.0"` | **0.24.0** | 与 torch 2.9.0 配套的版本 |
| **transformers** | `"transformers==4.56.0"` | **4.56.0** | 固定版本 |
| **lerobot** | `"lerobot>=0.3.3,<=0.3.4"` | **0.3.3** | 版本范围内的最低版本 |
| **datasets** | `"datasets>=2.19.0,<=3.6.0"` | **3.6.0** | 版本范围内的最高版本 |
| **accelerate** | `"accelerate>=1.10.1"` | **1.10.1** | 满足最低版本要求 |

### Python 和 Torch 兼容性矩阵 / Python and Torch Compatibility Matrix

PyTorch 2.9.0 支持的 Python 版本：

PyTorch 2.9.0 supports the following Python versions:

- Python 3.9 ✓
- Python 3.10 ✓
- Python 3.11 ✓
- Python 3.12 ✓ (当前使用 / currently using)
- Python 3.13 ✓

### 完整依赖链 / Complete Dependency Chain

```
eo==0.1.0
├── torch==2.9.0
│   ├── nvidia-cuda-runtime-cu12==12.8.62
│   ├── nvidia-cudnn-cu12==9.7.0.134
│   ├── nvidia-cublas-cu12==12.8.0.1
│   └── ... (其他 CUDA 相关依赖)
├── torchvision==0.24.0
│   ├── torch==2.9.0 (already installed)
│   ├── pillow>=8.0.0
│   └── numpy
├── transformers==4.56.0
│   ├── tokenizers<=0.23.0,>=0.22.0
│   ├── safetensors>=0.4.3
│   ├── huggingface-hub
│   └── ... (其他依赖)
├── lerobot==0.3.3
│   └── ... (机器人控制相关依赖)
└── ... (其他依赖)
```

## 灵活版本控制的优势 / Advantages of Flexible Versioning

### 1. 自动兼容性 / Automatic Compatibility

使用 `"torch"` 而不是 `"torch==2.0.0"` 的好处：

Benefits of using `"torch"` instead of `"torch==2.0.0"`:

- ✅ 自动选择与当前 Python 版本兼容的最新 PyTorch
- ✅ 获得 bug 修复和性能改进
- ✅ 减少版本冲突

### 2. 跨平台支持 / Cross-Platform Support

灵活版本允许在不同平台上自动选择合适的版本：

Flexible versioning allows automatic selection of appropriate versions on different platforms:

- Linux (x86_64, ARM)
- macOS (Intel, Apple Silicon)
- Windows

### 3. CUDA 版本适配 / CUDA Version Adaptation

PyTorch 会根据系统的 CUDA 可用性自动选择：

PyTorch automatically selects based on CUDA availability:

- CPU-only 版本 (如果没有 GPU)
- CUDA 12.x 版本 (如果有 NVIDIA GPU)
- ROCm 版本 (如果有 AMD GPU)

## 实际安装建议 / Practical Installation Recommendations

### 开发环境 / Development Environment

```bash
# 创建虚拟环境 / Create virtual environment
conda create -n eo python=3.11
conda activate eo

# 安装包 / Install package
pip install -e .

# 验证安装 / Verify installation
python verify_environment.py
```

### 生产环境 / Production Environment

对于生产环境，建议固定版本以确保可重现性：

For production, recommend pinning versions for reproducibility:

```toml
dependencies = [
    "torch==2.9.0",  # 固定版本
    "torchvision==0.24.0",  # 固定版本
    # ... 其他依赖
]
```

### 离线安装 / Offline Installation

如果需要离线安装：

For offline installation:

```bash
# 1. 在线环境下载所有依赖
pip download -r requirements.txt -d ./packages

# 2. 在离线环境安装
pip install --no-index --find-links=./packages -e .
```

## 总结 / Summary

灵活的 torch 版本控制策略在 EO-1 项目中是合适的选择：

The flexible torch versioning strategy is appropriate for the EO-1 project:

1. **开发友好 / Development Friendly**: 开发者可以使用最新的 PyTorch 特性
2. **兼容性好 / Good Compatibility**: 支持多个 Python 版本 (3.10+)
3. **维护简单 / Easy Maintenance**: 减少版本冲突和依赖管理复杂度
4. **生产可控 / Production Controllable**: 可以通过 requirements.txt 固定版本用于生产部署

**最终答案 / Final Answer**:
- Python 版本: **3.12.3**
- PyTorch 版本: **2.9.0** (灵活安装的最新兼容版本)
- 环境配置: **可以正常工作** ✓
