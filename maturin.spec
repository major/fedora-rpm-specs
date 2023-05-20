%bcond_without check

Name:           maturin
Version:        1.0.0~b7
Release:        %autorelease
Summary:        Build and publish Rust crates as Python packages
SourceLicense:  MIT OR Apache-2.0

%global pypi_version %(echo %{version} | tr -d "~")

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# CC0-1.0 OR MIT-0 OR Apache-2.0
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        0BSD AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND MIT AND MPL-2.0 AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSD-2-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (CC0-1.0 OR MIT-0 OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/PyO3/maturin
Source0:        %{pypi_source maturin %{pypi_version}}

# * disable all optional features for now: they are not needed for building RPM
#   packages, but they pull in lots of additional dependencies
# * drop unused test dependencies
Patch:          0001-disable-all-optional-features-and-drop-unused-test-d.patch

# * drop incompatible arguments from setuptools_rust cargo invocations
Patch:          0002-drop-incompatible-cargo-flags-from-setuptools_rust.patch

# * drop #!/usr/bin/env python3 shebang from maturin/__init__.py
Patch:          0003-remove-shebang-from-non-executable-__init__.py-file.patch

BuildRequires:  rust-packaging >= 23
BuildRequires:  python3-devel

%py_provides python3-maturin

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%prep
%autosetup -n maturin-%{pypi_version} -p1
%cargo_prep

%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires

%build
export RUSTFLAGS="%{build_rustflags}"
%pyproject_wheel
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files maturin

%if %{with check}
%check
# * skip tests for which fixtures are not included in published sources
%cargo_test -- -- --skip build_options::test::test_find_bridge --skip metadata::test::test_implicit_readme --skip metadata::test::test_merge_metadata_from_pyproject --skip pyproject_toml::tests::test_warn_missing_maturin_version
%endif

%files -f %{pyproject_files}
%license license-apache
%license license-mit
%license LICENSE.dependencies
%doc README.md
%doc Changelog.md
%{_bindir}/maturin

%changelog
%autochangelog
