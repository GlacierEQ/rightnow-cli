"""Setup configuration for RightNow CLI."""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="rightnow-cli",
    version="1.0.0",
    author="Jaber",
    author_email="jaber@rightnowai.co",
    description="GPU-Native AI Code Editor for CUDA optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RightNow-AI/rightnow-cli",
    project_urls={
        "Bug Tracker": "https://github.com/RightNow-AI/rightnow-cli/issues",
        "Documentation": "https://github.com/RightNow-AI/rightnow-cli#readme",
        "Source Code": "https://github.com/RightNow-AI/rightnow-cli",
        "Twitter": "https://twitter.com/rightnowai_co",
    },
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "rightnow=rightnow_cli:main",
            "rightnow-cli=rightnow_cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "rightnow_cli": [
            "config/templates/*.json",
            "ui/themes/*.json",
        ],
    },
    keywords=[
        "cuda",
        "gpu",
        "ai",
        "code-editor",
        "optimization",
        "nvidia",
        "development-tools",
        "machine-learning",
        "deep-learning",
        "parallel-computing",
        "openrouter",
        "llm",
    ],
)