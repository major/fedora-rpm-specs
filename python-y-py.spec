Name:           python-y-py
Version:        0.6.0
Release:        %autorelease
Summary:        Python bindings for the Y-CRDT built from yrs (Rust)
# SPDX
License:        MIT
URL:            https://github.com/y-crdt/ypy
Source:         %{pypi_source y_py}

# Switch to pyo3 0.19.2
Patch:          https://github.com/y-crdt/ypy/pull/138.patch

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
# Apache-2.0: pyo3 v0.19.2
# Apache-2.0: pyo3-ffi v0.19.2
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: getrandom v0.1.16
# MIT OR Apache-2.0: libc v0.2.147
# MIT OR Apache-2.0: lock_api v0.4.10
# MIT OR Apache-2.0: parking_lot v0.12.1
# MIT OR Apache-2.0: parking_lot_core v0.9.8
# MIT OR Apache-2.0: ppv-lite86 v0.2.17
# MIT OR Apache-2.0: rand v0.7.3
# MIT OR Apache-2.0: rand_chacha v0.2.2
# MIT OR Apache-2.0: rand_core v0.5.1
# MIT OR Apache-2.0: scopeguard v1.2.0
# MIT OR Apache-2.0: smallstr v0.2.0
# MIT OR Apache-2.0: smallvec v1.11.0
# MIT OR Apache-2.0: thiserror v1.0.47
# MIT OR Apache-2.0: unindent v0.1.11
# MIT: lib0 v0.12.2
# MIT: memoffset v0.9.0
# MIT: yrs v0.12.2
License: MIT AND (MIT OR Apache-2.0) AND Apache-2.0

%description -n python3-y-py %_description


%prep
%autosetup -p1 -n y_py-%{version}
# Fedora has maturin 1.0.0 which is pretty much compatible with 0.14;
# we relax the upper bound entirely -- if it builds, it's probably OK.
sed -i 's/maturin>=0.14,<0.15/maturin>=0.14/' pyproject.toml
%cargo_prep


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
%autochangelog
