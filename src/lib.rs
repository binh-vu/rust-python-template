use pyo3::prelude::*;

/// square of a number
#[pyfunction]
fn square(x: f64) -> f64 {
    x * x
}

#[pymodule]
fn rust_python_template(py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(square, m)?)?;
    Ok(())
}
