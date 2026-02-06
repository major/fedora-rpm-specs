Name:           python-fastuuid
Version:        0.14.0
Release:        %autorelease
Summary:        Python bindings to Rust's UUID library

# main package is BSD-3-Clause
# from LICENSE.dependencies
# Apache-2.0 OR MIT: atomic v0.6.1 
# Apache-2.0 OR MIT: uuid v1.19.0
# BSD-2-Clause OR Apache-2.0 OR MIT: zerocopy v0.8.31
# BSD-3-Clause: sha1_smol v1.0.1
# BSD3: fastuuid v0.14.0
# MIT OR Apache-2.0: block-buffer v0.10.4
# MIT OR Apache-2.0: cfg-if v1.0.4
# MIT OR Apache-2.0: crypto-common v0.1.7
# MIT OR Apache-2.0: digest v0.10.7
# MIT OR Apache-2.0: getrandom v0.2.16
# MIT OR Apache-2.0: getrandom v0.3.4
# MIT OR Apache-2.0: libc v0.2.180
# MIT OR Apache-2.0: md-5 v0.10.6
# MIT OR Apache-2.0: once_cell v1.21.3
# MIT OR Apache-2.0: ppv-lite86 v0.2.21
# MIT OR Apache-2.0: pyo3 v0.26.0
# MIT OR Apache-2.0: pyo3-ffi v0.26.0
# MIT OR Apache-2.0: rand v0.8.5
# MIT OR Apache-2.0: rand_chacha v0.3.1
# MIT OR Apache-2.0: rand_core v0.6.4
# MIT OR Apache-2.0: typenum v1.19.0
# MIT OR Apache-2.0: unindent v0.2.4
# MIT: generic-array v0.14.9
# MIT: memoffset v0.9.1
# Zlib OR Apache-2.0 OR MIT: bytemuck v1.24.0
License:        %{shrink:
        BSD-3-Clause AND
        (Apache-2.0 OR MIT) AND
        (BSD-2-Clause OR Apache-2.0 OR MIT) AND
        BSD-3-Clause AND
        (MIT OR Apache-2.0) AND
        MIT AND
        (Zlib OR Apache-2.0 OR MIT)
}

URL:            https://github.com/thedrow/fastuuid/
Source:         %{pypi_source fastuuid}

BuildSystem:    pyproject
BuildOption(install):  -l fastuuid

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
FastUUID is a library which provides CPython bindings to Rust's UUID library.

The provided API is exactly as Python's builtin UUID class. The supported UUID
versions are v1, v3, v4, v5, and v7.}

%description %_description

%package -n     python3-fastuuid
Summary:        %{summary}

%description -n python3-fastuuid %_description

%generate_buildrequires -a
%cargo_generate_buildrequires

%prep -a
%cargo_prep

%build -a
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%check
%pyproject_check_import

%files -n python3-fastuuid -f %{pyproject_files}
%license LICENSE
%license LICENSE.dependencies
%doc README.rst

%changelog
%autochangelog
