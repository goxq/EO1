#!/usr/bin/env python3
"""
Minimal Demo Script for EO-1 Repository
This demonstrates the repository structure and expected usage without full installation.
"""

import os
import sys


def show_repository_structure():
    """Display the repository structure."""
    print("=" * 60)
    print("EO-1 Repository Structure")
    print("=" * 60)
    print()
    
    structure = {
        "Core Package": "eo/",
        "Model Files": "eo/model/",
        "Data Processing": "eo/data/",
        "Training Scripts": "scripts/",
        "Experiments": "experiments/",
        "Getting Started": "getting_started/",
        "Demo Data": "demo_data/",
        "Tests": "tests/",
        "Documentation": "README.md",
    }
    
    for name, path in structure.items():
        exists = "✓" if os.path.exists(path) else "✗"
        print(f"{exists} {name:20s} : {path}")
    print()


def show_demo_examples():
    """Show available demo examples."""
    print("=" * 60)
    print("Available Demo Examples")
    print("=" * 60)
    print()
    
    demos = {
        "Demo Training": "experiments/1_demo/",
        "Libero Benchmark": "experiments/2_libero/",
        "SimplerEnv": "experiments/3_simpler/",
        "SO101 Tasks": "experiments/4_so101/",
        "WidowX Platform": "experiments/5_widowx/",
        "AgiBot Platform": "experiments/6_agibot/",
        "Franka Platform": "experiments/7_franka/",
        "VLM Evaluation": "experiments/8_vllmeval/",
        "Pre-training": "experiments/9_pretraining/",
    }
    
    for name, path in demos.items():
        if os.path.exists(path):
            print(f"✓ {name:20s} : {path}")
            # List files in demo directory
            try:
                files = [f for f in os.listdir(path) if not f.startswith('.')]
                if files:
                    for f in files[:3]:  # Show first 3 files
                        print(f"    - {f}")
                    if len(files) > 3:
                        print(f"    ... and {len(files) - 3} more")
            except:
                pass
        else:
            print(f"✗ {name:20s} : {path} (not found)")
        print()


def show_usage_example():
    """Show expected usage example."""
    print("=" * 60)
    print("Expected Usage (from README)")
    print("=" * 60)
    print()
    
    usage = '''
# 1. Installation
conda create -n eo python=3.11
conda activate eo
pip install -e .

# 2. Model Inference Example
from transformers import AutoModel, AutoProcessor

processor = AutoProcessor.from_pretrained(
    "IPEC-COMMUNITY/EO-1-3B", 
    trust_remote_code=True
)
model = AutoModel.from_pretrained(
    "IPEC-COMMUNITY/EO-1-3B",
    trust_remote_code=True,
    dtype=torch.bfloat16
).eval().cuda()

# 3. Action Sampling (Robot Control)
batch = {
    "observation.images.image": [img],
    "observation.images.wrist_image": [wrist_img],
    "observation.state": [state],
    "task": ["Pick up a red piece and place it at (0, 2)."]
}
output = processor.select_action(model, batch)
print(output.action)

# 4. Text Generation (Multimodal Reasoning)
messages = [{
    "role": "user",
    "content": [
        {"type": "image", "image": "demo_data/example2.png"},
        {"type": "text", "text": "You are a helpful physical agent..."}
    ]
}]
inputs = processor.apply_chat_template(messages, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=1024)
'''
    print(usage)


def check_pyproject_versions():
    """Check version specifications in pyproject.toml."""
    print("=" * 60)
    print("Version Specifications from pyproject.toml")
    print("=" * 60)
    print()
    
    try:
        with open("pyproject.toml", "r") as f:
            in_deps = False
            for line in f:
                if "[project]" in line or "dependencies = [" in line:
                    in_deps = True
                if in_deps and any(pkg in line.lower() for pkg in 
                                  ["torch", "python", "transform", "lerobot", "dataset"]):
                    print(line.rstrip())
                if in_deps and line.strip() == "]":
                    in_deps = False
    except Exception as e:
        print(f"Error reading pyproject.toml: {e}")
    print()


def show_version_change_info():
    """Show information about the version changes."""
    print("=" * 60)
    print("Version Change Analysis")
    print("=" * 60)
    print()
    
    print("Commit: 5920dc7998d129215803c994c57173d1aa8bdb0a")
    print("Message: Change torch dependency to flexible version")
    print("Date: Wed Oct 15 13:14:20 2025")
    print()
    
    print("Key Change:")
    print("  Before: torch==X.X.X (pinned version)")
    print("  After:  torch (flexible version)")
    print()
    
    print("Impact:")
    print("  ✓ Allows pip to install latest compatible PyTorch version")
    print("  ✓ Better compatibility with different Python versions")
    print("  ✓ Automatic updates to newer PyTorch releases")
    print("  ! May require testing with multiple PyTorch versions")
    print()
    
    print("With Python 3.12.3:")
    print("  Expected torch version: ~2.9.0 (latest compatible)")
    print("  Expected torchvision: ~0.24.0 (matches torch)")
    print()


def main():
    """Main demo function."""
    print()
    print("*" * 60)
    print("EO-1: Embodied Foundation Model")
    print("Minimal Demo Script")
    print("*" * 60)
    print()
    
    show_version_change_info()
    show_repository_structure()
    check_pyproject_versions()
    show_demo_examples()
    show_usage_example()
    
    print("=" * 60)
    print("Next Steps")
    print("=" * 60)
    print()
    print("1. Verify environment: python3 verify_environment.py")
    print("2. Install dependencies: pip install -e .")
    print("3. Run demo training: cd experiments/1_demo && bash train.sh")
    print("4. Try getting started notebooks: jupyter notebook getting_started/")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
