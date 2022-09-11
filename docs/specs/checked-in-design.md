# Checked-in design docs

Consider setting up a process for design proposals via checked-in Markdown files
which are reviewed just like source code.

For inspiration / reference, see:

- [.NET designs](https://github.com/dotnet/designs)
- [C\# language design](https://github.com/dotnet/csharplang)
- [Kubernetes enhancements](https://github.com/kubernetes/enhancements/)
- [PyTorch RFCs](https://github.com/pytorch/rfcs/)

Checked in design docs should include snippets of code that would work after
the design is implemented:

```python
from modern_python_package import inner_method

big_number = 42

cool_variable = inner_method("short string", big_number)
```

:point_right: Use emoji to call attention to a specific point. :point_left:
