# Jupyter Notebook Naming Hook

A pre-commit hook to enforce naming conventions for Jupyter notebooks.

## Usage

Add the following to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/evmckinney9/jupyter-notebook-naming-hook
  rev: v0.1.0
  hooks:
    - id: enforce-notebook-naming
```

Run `pre-commit install` to set up the hook.

## Naming Convention

> [!NOTE]  
> This hook is designed to enforce the naming convention consistent with my personal [python project directory](https://github.com/evmckinney9/python-template) structure.

- Developing notebooks should be named like `dev_description.ipynb`.
- Deliverable notebooks should be named like `01_description.ipynb` or `01_description_initials_YYYY-MM-DD.ipynb`.

