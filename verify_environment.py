#!/usr/bin/env python3
"""
Environment Verification Script
This script verifies the environment setup and reports installed versions.
"""

import sys
import platform


def check_python_version():
    """Check Python version."""
    print("=" * 60)
    print("Python Environment Check")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Python Executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.machine()}")
    print()
    
    version_info = sys.version_info
    required_major = 3
    required_minor = 10
    
    if version_info.major >= required_major and version_info.minor >= required_minor:
        print(f"✓ Python version check PASSED (requires >= 3.10)")
        return True
    else:
        print(f"✗ Python version check FAILED (requires >= 3.10)")
        return False


def check_torch_installation():
    """Check if PyTorch is installed and report version."""
    print("=" * 60)
    print("PyTorch Installation Check")
    print("=" * 60)
    
    try:
        import torch
        print(f"✓ PyTorch is installed")
        print(f"  Version: {torch.__version__}")
        print(f"  CUDA Available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"  CUDA Version: {torch.version.cuda}")
            print(f"  GPU Device: {torch.cuda.get_device_name(0)}")
        print()
        return True
    except ImportError:
        print("✗ PyTorch is NOT installed")
        print("  To install: pip install torch")
        print()
        return False


def check_torchvision_installation():
    """Check if torchvision is installed and report version."""
    print("=" * 60)
    print("TorchVision Installation Check")
    print("=" * 60)
    
    try:
        import torchvision
        print(f"✓ TorchVision is installed")
        print(f"  Version: {torchvision.__version__}")
        print()
        return True
    except ImportError:
        print("✗ TorchVision is NOT installed")
        print("  To install: pip install torchvision")
        print()
        return False


def check_key_dependencies():
    """Check other key dependencies."""
    print("=" * 60)
    print("Key Dependencies Check")
    print("=" * 60)
    
    dependencies = [
        ("transformers", "transformers"),
        ("datasets", "datasets"),
        ("lerobot", "lerobot"),
        ("accelerate", "accelerate"),
        ("einops", "einops"),
        ("wandb", "wandb"),
    ]
    
    results = {}
    for package_name, import_name in dependencies:
        try:
            module = __import__(import_name)
            version = getattr(module, "__version__", "unknown")
            print(f"✓ {package_name}: {version}")
            results[package_name] = True
        except ImportError:
            print(f"✗ {package_name}: NOT installed")
            results[package_name] = False
    
    print()
    return results


def check_eo_package():
    """Check if eo package is installed."""
    print("=" * 60)
    print("EO Package Check")
    print("=" * 60)
    
    try:
        import eo
        print(f"✓ eo package is installed")
        # Try to get version if available
        version = getattr(eo, "__version__", "development")
        print(f"  Version: {version}")
        print()
        return True
    except ImportError:
        print("✗ eo package is NOT installed")
        print("  To install: pip install -e .")
        print()
        return False


def verify_dependency_config():
    """Verify the dependency configuration from pyproject.toml."""
    print("=" * 60)
    print("Dependency Configuration Verification")
    print("=" * 60)
    
    try:
        import tomllib
    except ImportError:
        try:
            import tomli as tomllib
        except ImportError:
            print("✗ Cannot read pyproject.toml (tomllib/tomli not available)")
            print()
            return False
    
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
        
        project = config.get("project", {})
        dependencies = project.get("dependencies", [])
        
        print("Key dependency specifications from pyproject.toml:")
        for dep in dependencies:
            if any(pkg in dep.lower() for pkg in ["torch", "python", "transform", "lerobot"]):
                print(f"  - {dep}")
        
        print(f"\nPython requirement: {project.get('requires-python', 'not specified')}")
        print()
        return True
    except Exception as e:
        print(f"✗ Error reading pyproject.toml: {e}")
        print()
        return False


def main():
    """Main verification function."""
    print("\n" + "=" * 60)
    print("EO-1 Environment Verification")
    print("=" * 60)
    print()
    
    results = {
        "Python": check_python_version(),
        "PyTorch": check_torch_installation(),
        "TorchVision": check_torchvision_installation(),
        "EO Package": check_eo_package(),
    }
    
    check_key_dependencies()
    verify_dependency_config()
    
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    for component, status in results.items():
        status_str = "✓ PASS" if status else "✗ FAIL"
        print(f"{component}: {status_str}")
    
    print()
    all_pass = all(results.values())
    if all_pass:
        print("✓ All critical components are installed and verified!")
    else:
        print("✗ Some components are missing. Please install missing dependencies.")
        print("\nTo install all dependencies, run:")
        print("  pip install -e .")
    
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
