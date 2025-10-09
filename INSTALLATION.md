# Installation Guide

RightNow CLI can be installed using various methods depending on your platform and preferences.

## Quick Install

### 🐧 Linux / macOS

```bash
# Using curl (recommended)
curl -sSL https://raw.githubusercontent.com/RightNow-AI/rightnow-cli/main/install.sh | bash

# Or using pip
pip install rightnow-cli
```

### 🪟 Windows

```powershell
# Using PowerShell (run as Administrator)
irm https://raw.githubusercontent.com/RightNow-AI/rightnow-cli/main/install.ps1 | iex

# Or using pip
pip install rightnow-cli
```

## Prerequisites

### Required
- **Python 3.9+** - [Download Python](https://python.org)
- **OpenRouter API Key** - [Get Free API Key](https://openrouter.ai) (30 seconds, no credit card)

### Optional (for GPU acceleration)
- **NVIDIA GPU** - Any CUDA-capable GPU
- **CUDA Toolkit 11.0+** - [Download CUDA](https://developer.nvidia.com/cuda-downloads)
- **cuDNN** - [Download cuDNN](https://developer.nvidia.com/cudnn)

## Installation Methods

### Method 1: Install via pip (Recommended)

The simplest way to install RightNow CLI:

```bash
# Install from PyPI
pip install rightnow-cli

# Or install with user flag (no admin required)
pip install --user rightnow-cli

# Upgrade to latest version
pip install --upgrade rightnow-cli
```

### Method 2: Install from Source

For the latest development version:

```bash
# Clone the repository
git clone https://github.com/RightNow-AI/rightnow-cli.git
cd rightnow-cli

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Method 3: Install in Virtual Environment

For an isolated installation:

```bash
# Create virtual environment
python -m venv rightnow-env

# Activate environment
# On Linux/macOS:
source rightnow-env/bin/activate
# On Windows:
rightnow-env\Scripts\activate

# Install RightNow CLI
pip install rightnow-cli
```

### Method 4: Using Docker (Coming Soon)

```bash
# Pull the Docker image
docker pull rightnowai/rightnow-cli

# Run the container
docker run -it rightnowai/rightnow-cli
```

## Platform-Specific Instructions

### Ubuntu/Debian

```bash
# Install Python and pip
sudo apt update
sudo apt install python3 python3-pip

# Install CUDA (optional)
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt update
sudo apt install cuda

# Install RightNow CLI
pip install rightnow-cli
```

### Fedora/RHEL/CentOS

```bash
# Install Python and pip
sudo dnf install python3 python3-pip

# Install RightNow CLI
pip install rightnow-cli
```

### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Install RightNow CLI
pip3 install rightnow-cli
```

### Windows

#### Option 1: Using Windows Package Manager

```powershell
# Install Python
winget install Python.Python.3.11

# Install RightNow CLI
pip install rightnow-cli
```

#### Option 2: Manual Installation

1. Download Python from [python.org](https://python.org)
2. During installation, check "Add Python to PATH"
3. Open Command Prompt or PowerShell
4. Run: `pip install rightnow-cli`

## Post-Installation Setup

### 1. Verify Installation

```bash
# Check if RightNow is installed
rightnow --version

# Get help
rightnow --help
```

### 2. Configure API Key

When you first run RightNow, you'll be prompted to enter your OpenRouter API key:

```bash
# Start RightNow CLI
rightnow

# You'll see:
# ============================================================
# Welcome to RightNow CLI!
# ============================================================
#
# API Key Setup Required
#
# Quick Setup:
# 1. Open: https://openrouter.ai
# 2. Click 'Sign Up' (use Google/GitHub for instant access)
# 3. Copy your API key from the dashboard
```

### 3. Test GPU Support (Optional)

```bash
# In RightNow CLI, use the /gpu command
/gpu

# You should see your GPU status if CUDA is properly installed
```

## Environment Variables

You can configure RightNow using environment variables:

```bash
# Set API key (alternative to interactive setup)
export OPENROUTER_API_KEY="your-api-key-here"

# Set default model
export RIGHTNOW_MODEL="google/gemini-2.0-flash-thinking-exp:free"

# Set working directory
export RIGHTNOW_WORKDIR="/path/to/cuda/projects"
```

## Troubleshooting

### Command Not Found

If `rightnow` command is not found after installation:

**Linux/macOS:**
```bash
# Add to PATH in ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Reload shell configuration
source ~/.bashrc  # or source ~/.zshrc
```

**Windows:**
```powershell
# Add Python Scripts to PATH
$env:PATH += ";$env:APPDATA\Python\Python311\Scripts"

# Or reinstall with admin privileges
pip uninstall rightnow-cli
pip install rightnow-cli --user
```

### Permission Denied

If you get permission errors:

```bash
# Use --user flag
pip install --user rightnow-cli

# Or use sudo (not recommended)
sudo pip install rightnow-cli
```

### SSL Certificate Error

If you encounter SSL errors:

```bash
# Upgrade certificates
pip install --upgrade certifi

# Or use trusted host
pip install --trusted-host pypi.org rightnow-cli
```

### CUDA Not Detected

If GPU/CUDA is not detected:

1. Verify NVIDIA drivers: `nvidia-smi`
2. Check CUDA installation: `nvcc --version`
3. Ensure CUDA is in PATH:
   ```bash
   export PATH=/usr/local/cuda/bin:$PATH
   export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
   ```

## Uninstallation

To remove RightNow CLI:

```bash
# Uninstall via pip
pip uninstall rightnow-cli

# Remove configuration files (optional)
rm -rf ~/.rightnow-cli
```

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/RightNow-AI/rightnow-cli/issues)
- **Documentation**: [Full documentation](https://github.com/RightNow-AI/rightnow-cli#readme)
- **Twitter**: [@rightnowai_co](https://twitter.com/rightnowai_co)
- **Email**: jaber@rightnowai.co

## Next Steps

1. Get your [free API key from OpenRouter](https://openrouter.ai)
2. Run `rightnow` to start the CLI
3. Try creating a simple CUDA kernel: "Create a vector addition kernel"
4. Explore commands with `/help`

Happy CUDA coding! 🚀