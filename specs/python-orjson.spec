# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html
# Copyright (c) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (c) Fedora Project Authors

# Specfile compatability: EPEL >= 9 or Fedora >= 37 and RPM >= 4.16

%bcond tests 1

Name:           python-orjson
Version:        3.10.7
Release:        %autorelease
Summary:        Fast, correct Python JSON library

License:        Apache-2.0 OR MIT
URL:            https://github.com/ijl/orjson
Source:         %{pypi_source orjson}

BuildRequires:  tomcli
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest-forked}
# Upstream restricts these test dependencies to particular Python interpreter
# versions and architectures, but we would like to run the corresponding tests
# everywhere.
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pendulum}
# These are not in tests/requirements.txt, but they enable additional tests
%ifnarch %{ix86}
BuildRequires:  %{py3_dist pandas}
%endif
BuildRequires:  %{py3_dist psutil}
BuildRequires:  rust-packaging


%global _description %{expand:
orjson is a fast, correct Python JSON library supporting dataclasses,
datetimes, and numpy}


%description %{_description}

%package -n     python3-orjson
Summary:        %{summary}
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSL-1.0
# MIT
# MIT OR Apache-2.0 (duplicate)
# Unlicense OR MIT
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                (Apache-2.0 OR BSL-1.0) AND
                BSL-1.0 AND
                MIT AND
                (Unlicense OR MIT)
                }


%description -n python3-orjson %{_description}


%prep
%autosetup -p1 -n orjson-%{version}
%cargo_prep

# Remove unstable features that require rust nightly; the avx512 feature also
# requires the x86_64 architecture
tomcli-set Cargo.toml del 'features.unstable-simd'
tomcli-set Cargo.toml del 'features.avx512'
# Remove no-panic feature
tomcli-set Cargo.toml del 'features.no-panic'
# Remove unwind feature, which is not useful here: the comment above it says
# “Avoid bundling libgcc on musl.”
tomcli-set Cargo.toml del 'features.unwind'
tomcli-set Cargo.toml del 'dependencies.unwinding'
# Remove strict dependencies
sed -Ei 's|(version = ")=|\1|' Cargo.toml
# Remove bundled rust crates
rm -r include/cargo
# Remove bundled yyjson.
rm -rv include/yyjson/

# Remove unpackaged PyPI plugin
sed -i '/pytest-random-order/d' test/requirements.txt



%generate_buildrequires
%pyproject_buildrequires %{?with_tests:test/requirements.txt}
%cargo_generate_buildrequires


%build
export RUSTFLAGS='%{build_rustflags}'
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files orjson


%check
%pyproject_check_import
%if %{with tests}
# --forked: protect the pytest process against test segfaults
# -rs: print the reasons for skipped tests
%pytest --forked -rs
%endif


%files -n python3-orjson -f %{pyproject_files}
%license LICENSE-MIT LICENSE-APACHE LICENSES.dependencies
%doc README.md


%changelog
%autochangelog
