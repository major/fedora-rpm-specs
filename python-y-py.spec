Name:           python-y-py
Version:        0.6.0
Release:        1%{?dist}
Summary:        Python bindings for the Y-CRDT built from yrs (Rust)
License:        MIT
URL:            https://github.com/y-crdt/ypy
Source:         %{pypi_source y_py}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  rust-packaging

%global _description %{expand:
Ypy is a Python binding for Y-CRDT. 
It provides distributed data types that
enable real-time collaboration between devices.}


%description %_description

%package -n     python3-y-py
Summary:        %{summary}
# Statically linked deps and their licenses.
# When updating, check the generated LICENSE.dependencies file.
#
# python-y-py code is MIT
# Apache-2.0: pyo3 v0.16.6
# Apache-2.0: pyo3-ffi v0.16.6
# MIT OR Apache-2.0: cfg-if v0.1.10
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: getrandom v0.1.15
# MIT OR Apache-2.0: libc v0.2.139
# MIT OR Apache-2.0: lock_api v0.4.9
# MIT OR Apache-2.0: parking_lot v0.12.1
# MIT OR Apache-2.0: parking_lot_core v0.9.5
# MIT OR Apache-2.0: ppv-lite86 v0.2.17
# MIT OR Apache-2.0: rand v0.7.3
# MIT OR Apache-2.0: rand_chacha v0.2.2
# MIT OR Apache-2.0: rand_core v0.5.1
# MIT OR Apache-2.0: scopeguard v1.1.0
# MIT OR Apache-2.0: smallstr v0.2.0
# MIT OR Apache-2.0: smallvec v1.10.0
# MIT OR Apache-2.0: thiserror v1.0.37
# MIT OR Apache-2.0: unindent v0.1.11
# MIT: lib0 v0.12.2
# MIT: yrs v0.12.2
License: MIT AND (MIT OR Apache-2.0) AND Apache-2.0

%description -n python3-y-py %_description


%prep
%autosetup -p1 -n y_py-%{version}
%cargo_prep
# Porting from maturin to setuptools_rust
# This is far from perfect but because maturin (a popular
# build backend for Rust packages) is not yet available
# in Fedora, we have to use setuptools-rust instead
# which requires multiple changes in metadata.

cat << EOF > MANIFEST.in
include Cargo.toml
recursive-include src *
EOF

cat << EOF > pyproject.toml
[build-system]
requires = ["setuptools", "wheel", "setuptools-rust"]
EOF

cat << EOF > setup.cfg
[metadata]
name = y-py
version = %{version}
license = MIT
url = %{url}
long_description = file: README.md
long_description_content_type = text/markdown

[options]
zip_safe = False
include_package_data = True
EOF

cat << EOF > setup.py
import sys

from setuptools import setup
from setuptools_rust import RustExtension

setup(
    rust_extensions=[RustExtension("y_py", args=["--offline"])],
)
EOF

%generate_buildrequires
%cargo_generate_buildrequires
%pyproject_buildrequires


%build
export RUSTFLAGS="%build_rustflags"
%pyproject_wheel
%{cargo_license} > LICENSE.dependencies


%install
%pyproject_install
%pyproject_save_files y_py


%check
%pytest


%files -n python3-y-py -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE.dependencies


%changelog
* Thu Feb 23 2023 Lumír Balhar <lbalhar@redhat.com> - 0.6.0-1
- Update to 0.6.0 (rhbz#2171402)

* Thu Dec 15 2022 Lumír Balhar <lbalhar@redhat.com> - 0.5.5-1
- Initial package