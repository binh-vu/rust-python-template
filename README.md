# rust-python-template

Project template for creating a Python library with Rust extensions. It uses PyO3 with two building options: maturine (default) and setuptools-rust.

If you have more than one Rust extensions (libraries), use setuptools-rust. Otherwise, you can stay with maturine. Checkout their documentations for more information.

To run cargo test: `cargo test --no-default-features`
