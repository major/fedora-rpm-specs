Name:           python-fastuuid
Version:        0.14.0
Release:        %autorelease
Summary:        Python bindings to Rust's UUID library

# main package is BSD-3-Clause; statically-linked Rust dependencies are, from
# the output of %%{cargo_license_summary}:
#
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# BSD-3-Clause
# MIT
# MIT OR Apache-2.0
# Zlib OR Apache-2.0 OR MIT
License:        %{shrink:
        BSD-3-Clause AND
        (Apache-2.0 OR MIT) AND
        (BSD-2-Clause OR Apache-2.0 OR MIT) AND
        BSD-3-Clause AND
        MIT AND
        (Zlib OR Apache-2.0 OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/thedrow/fastuuid/
Source:         %{pypi_source fastuuid}

# Adapt for `uuid::Context` renaming in v1.23
# https://github.com/fastuuid/fastuuid/pull/66
# Avoids a warning.
Patch:          %{url}/pull/66.patch
# Update Pyo3 from 0.26 to 0.29
# https://github.com/fastuuid/fastuuid/pull/67
# Fixes RUSTSEC-2026-0176 and RUSTSEC-2026-0177.
Patch:          %{url}/pull/67.patch
# Fix invalid SPDX in license metadata
# https://github.com/fastuuid/fastuuid/pull/68
# Fixes RUSTSEC-2026-0176 and RUSTSEC-2026-0177.
Patch:          %{url}/pull/68.patch

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
