# Python Environments & Package Management

> **Scope:** How to create environments and install packages using
> **Miniforge (conda)**, **Anaconda (conda)**, and **pip + venv**

---

## 1. Core Idea: Environments

*   An **environment** is an isolated Python setup.
*   Each environment has:

    *   Its own Python interpreter
    *   Its own installed packages
*   Purpose:

    *   Avoid dependency conflicts
    *   Protect system Python
    *   Allow multiple projects with different requirements

---

## 2. Two Environment Systems

### 2.1 Conda-based

*   Miniforge
*   Anaconda
*   Uses **conda** as:

    *   Environment manager
    *   Package manager

### 2.2 pip-based

*   Python built-in `venv`
*   Uses **pip** for package installation

---

## 3. Miniforge (Conda Environments)

Miniforge is a lightweight conda distribution.

### 3.1 Verify conda installation

```bash
conda --version
```

---

### 3.2 Create a conda environment

```bash
conda create -n myenv python=3.11
```

*   `-n myenv` → environment name
*   `python=3.11` → specific Python version

---

### 3.3 Activate environment

```bash
conda activate myenv
```

*   Environment name appears in terminal prompt

---

### 3.4 Install packages (recommended)

```bash
conda install numpy pandas matplotlib
```

*   Handles Python and system-level dependencies
*   Preferred for scientific and data libraries

---

### 3.5 Use pip inside conda (only if needed)

```bash
pip install requests
```

*   Use only when package is not available via conda

---

### 3.6 Deactivate environment

```bash
conda deactivate
```

---

### 3.7 List conda environments

```bash
conda env list
```

---

## 4. Anaconda (Conda Environments)

Anaconda uses the **same conda commands** as Miniforge.

### 4.1 Create environment

```bash
conda create -n anaconda_env python=3.10
```

---

### 4.2 Activate environment

```bash
conda activate anaconda_env
```

---

### 4.3 Install packages

```bash
conda install scikit-learn seaborn
```

---

### 4.4 Deactivate environment

```bash
conda deactivate
```

### 4.5 Delete environment

```bash
conda env remove -n anaconda_env
```
---

## 5. pip + venv (Python Built-in)

Used for lightweight projects such as web and backend development.

---

### 5.1 Create virtual environment

```bash
python -m venv venv
```

*   Creates a `venv/` directory
*   Contains its own Python and `site-packages`

---

### 5.2 Activate virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

venv/
  bin/
    python
    pip
  lib/
    site-packages

### 5.3 Install packages using pip

```bash
python -m pip install flask django requests
```

*   Recommended over `pip install`
*   Ensures correct Python–pip pairing

---

### 5.4 Deactivate virtual environment

```bash
deactivate
```

---

## 6. pip vs conda (Usage Rules)

*   In **conda environments**:

    *   Prefer `conda install`
    *   Use `pip` only if necessary
*   In **venv environments**:

    *   Use `pip` only

---

## 7. Environment Activation Rules

*   Packages are installed **only in the active environment**
*   Always:

    1.  Activate environment
    2.  Install packages
    3.  Run code
    4.  Deactivate when done

---

## 8. Jupyter Notebook & Environments

*   Jupyter uses a **kernel**
*   Kernel = Python interpreter from an environment
*   Packages must be installed in the same environment as the kernel

---

## 9. Common Package Locations

*   Each environment has its own:

    *   Python executable
    *   `site-packages` directory
*   Installing a package in one environment does not make it available in others

---

## 10. Best Practices Summary

*   Never install packages globally
*   Always use environments
*   Match editor / terminal / Jupyter to the same environment
*   Use `python -m pip` for safety
*   Deactivate environments after use

---

## 11. Understanding uv

> uv is a very fast Python package manager and environment manager built in Rust.
> It is popular because:
  - Extremely fast (much faster than pip)
  - Deterministic (reliable dependency resolution)
  - Works with requirements.txt and pyproject.toml

---

## 12. Understanding structure of pyproject.toml

```toml
[project]
name = "myapp"
version = "0.1.0"

dependencies = [
    "fastapi",
    "uvicorn",
    "requests"
]
```

> To install everything use **uv sync**