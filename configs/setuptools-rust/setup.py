from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rust_python_template",
    version="0.1.2",
    rust_extensions=[RustExtension("rust_python_template.rust_python_template", binding=Binding.PyO3)],
    packages=["rust_python_template"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)