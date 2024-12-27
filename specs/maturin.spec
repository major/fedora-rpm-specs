%bcond_without check

Name:           maturin
Version:        1.7.4
Release:        %autorelease
Summary:        Build and publish Rust crates as Python packages
SourceLicense:  MIT OR Apache-2.0

%global pypi_version %(echo %{version} | tr -d "~")

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-3.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR BSD-2-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MIT-0 OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        0BSD AND Apache-2.0 AND Apache-2.0 WITH LLVM-exception AND BSD-3-Clause AND MIT AND MPL-2.0 AND Unicode-3.0 AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSD-2-Clause) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT-0 OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/PyO3/maturin
Source0:        %{pypi_source maturin %{pypi_version}}

# * disable features with missing dependencies:
#   - cross (support for cross compiling with zig / xwin)
#   - upload (support for uploading wheels to PyPI)
# * drop unused test dependencies
Patch:          0001-drop-unavailable-features-and-unused-dev-dependencie.patch

# * drop incompatible arguments from setuptools_rust cargo invocations
Patch:          0002-drop-incompatible-cargo-flags-from-setuptools_rust.patch

# * drop #!/usr/bin/env python3 shebang from maturin/__init__.py
Patch:          0003-remove-shebang-from-non-executable-__init__.py-file.patch

# * Update goblin to 0.9: https://github.com/PyO3/maturin/pull/2284
Patch:          0004-Update-goblin-to-0.9.patch

# * Update base64 from 0.21 to 0.22 and itertools from 0.12 to 0.13:
#   https://github.com/PyO3/maturin/pull/2404
Patch:          0005-Bump-base64-from-0.21-to-0.22-and-itertools-from-0.1.patch

BuildRequires:  cargo-rpm-macros >= 24
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
%cargo_generate_buildrequires -f schemars

%build
export RUSTFLAGS="%{build_rustflags}"
%pyproject_wheel

# write license summary and breakdown
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files maturin

# generate and install shell completions
target/rpm/maturin completions bash > maturin.bash
target/rpm/maturin completions fish > maturin.fish
target/rpm/maturin completions zsh > _maturin

install -Dpm 0644 maturin.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 maturin.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _maturin -t %{buildroot}/%{zsh_completions_dir}

%if %{with check}
%check
# * skip a test that fails with Rust 1.74+
# * skip tests for which fixtures are not included in published sources
%cargo_test -- -- --skip build_context::test::test_macosx_deployment_target --skip build_options::test::test_find_bridge --skip metadata::test::test_implicit_readme --skip metadata::test::test_merge_metadata_from_pyproject --skip pyproject_toml::tests::test_warn_missing_maturin_version
%endif

%files -f %{pyproject_files}
%license license-apache
%license license-mit
%license LICENSE.dependencies
%doc README.md
%doc Changelog.md

%{_bindir}/maturin

%{bash_completions_dir}/maturin.bash
%{fish_completions_dir}/maturin.fish
%{zsh_completions_dir}/_maturin

%changelog
%autochangelog
