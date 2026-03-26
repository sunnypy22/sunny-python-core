# Advanced Quiz - Modules and Packages
1. What is the purpose of `__all__` in `__init__.py`?
2. Explain the difference between absolute and relative imports.
3. What happens when you run `import package`? (role of __init__.py)
4. How can you create a package that can be installed using pip?
5. What is the recommended way to import modules in large projects?

**Answers**:
1. Controls what gets imported with `from package import *`
2. Absolute: from root, Relative: using . and .. (inside package)
3. It executes the code inside __init__.py
4. By creating proper package structure with setup.py or pyproject.toml
5. Use explicit imports (`import module` or `from module import specific`)
