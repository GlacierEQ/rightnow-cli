#!/usr/bin/env python
"""
RightNow CLI - CUDA Kernel Optimizer
Part of the RightNow AI Code Editor ecosystem

Multi-Agent System with Session Management

Clean UX - suppress warnings before anything else.
"""

# Suppress warnings BEFORE any imports for clean output
import warnings
import os

warnings.filterwarnings('ignore')
os.environ['PYTHONWARNINGS'] = 'ignore'

if __name__ == "__main__":
    from rightnow_cli.cli_minimal import main
    main()
