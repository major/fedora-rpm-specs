# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html
# Copyright (c) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (c) Fedora Project Authors

%bcond tests 1

Name:           python-orjson
Version:        3.8.11
Release:        1%{?dist}
Summary:        Fast, correct Python JSON library

License:        Apache-2.0 OR MIT
URL:            https://github.com/ijl/orjson
Source:         %{pypi_source orjson}
# Ineligble for upstreaming
Patch:          Use-setuptools-rust-instead-of-maturin.patch
# Ineligble for upstreaming
Patch:          Remove-unstable-simd-feature.patch

BuildRequires:  python3-devel
BuildRequires:  rust-packaging


%global _description %{expand:
orjosn is a fast, correct Python JSON library supporting dataclasses,
datetimes, and numpy}


%description %{_description}

%package -n     python3-orjson
Summary:        %{summary}
# Apache-2.0 OR MIT: orjson itself
# (Apache-2.0 OR MIT) AND BSD-3-Clause: encoding_rs v0.8.32
# Apache-2.0 OR BSL-1.0: ryu v1.0.13
# Apache-2.0 OR MIT: bytecount v0.6.3
# Apache-2.0 OR MIT: orjson v3.8.9
# Apache-2.0: pyo3-ffi v0.18.2
# MIT OR Apache-2.0: ahash v0.8.3
# MIT OR Apache-2.0: arrayvec v0.7.2
# MIT OR Apache-2.0: associative-cache v1.0.1
# MIT OR Apache-2.0: beef v0.5.2
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: chrono v0.4.24
# MIT OR Apache-2.0: itoa v1.0.6
# MIT OR Apache-2.0: libc v0.2.140
# MIT OR Apache-2.0: num-integer v0.1.45
# MIT OR Apache-2.0: num-traits v0.2.15
# MIT OR Apache-2.0: once_cell v1.17.1
# MIT OR Apache-2.0: serde v1.0.159
# MIT OR Apache-2.0: serde_json v1.0.95
# MIT OR Apache-2.0: simdutf8 v0.1.4
# MIT OR Apache-2.0: smallvec v1.10.0
# MIT OR Apache-2.0: static_assertions v1.1.0
License:        (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND BSD-3-Clause AND Apache-2.0


%description -n python3-orjson %{_description}


%prep
%autosetup -p1 -n orjson-%{version}

# Replaces @@VERSION@@ placeholder in pyproject.toml with the value of %%version.
%writevars -f pyproject.toml version

%if 0%{?fedora} && 0%{?fedora} <= 36
# Minimal setup.cfg for Fedora 36's old setuptools that doesn't support PEP 621
# (i.e. it doesn't understand metadata in pyproject.toml's [project] table)
cat <<EOF > setup.cfg
[metadata]
name = orjson
version = %{version}

[options]
packages = orjson
EOF
sed -i 's|setuptools>=61.0|setuptools|' pyproject.toml
%endif

# Remove bundled yyjson.
rm -rv include/yyjson/

%cargo_prep


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
%pytest -vv
%endif


%files -n python3-orjson -f %{pyproject_files}
%license LICENSE-MIT LICENSE-APACHE LICENSES.dependencies
%doc README.md


%changelog
* Fri May 5 2023 Maxwell G <maxwell@gtmx.me> - 3.8.11-1
- Update to 3.8.11. Fixes rhbz#2193468.

* Wed Apr 12 2023 Maxwell G <maxwell@gtmx.me> - 3.8.10-1
- Initial package (rhbz#2184237).
