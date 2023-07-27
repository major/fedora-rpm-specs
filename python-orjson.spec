# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT.html
# Copyright (c) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (c) Fedora Project Authors

# Specfile compatability: EPEL >= 9 or Fedora >= 37 and RPM >= 4.16

%bcond tests 1

Name:           python-orjson
Version:        3.9.2
Release:        2%{?dist}
Summary:        Fast, correct Python JSON library

License:        Apache-2.0 OR MIT
URL:            https://github.com/ijl/orjson
Source:         %{pypi_source orjson}

# Compatibility with Python 3.12
Patch:          https://github.com/ijl/orjson/pull/408.patch

# Ineligble for upstreaming
Patch:          Remove-unstable-simd-feature.patch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest-forked}
BuildRequires:  rust-packaging


%global _description %{expand:
orjosn is a fast, correct Python JSON library supporting dataclasses,
datetimes, and numpy}


%description %{_description}

%package -n     python3-orjson
Summary:        %{summary}
# (Apache-2.0 OR MIT) AND BSD-3-Clause
# Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# MIT
License:        %{shrink:
                (Apache-2.0 OR MIT) AND
                BSD-3-Clause AND
                Apache-2.0 AND
                (Apache-2.0 OR BSL-1.0) AND
                MIT
                }


%description -n python3-orjson %{_description}


%prep
%autosetup -p1 -n orjson-%{version}

# Remove bundled rust crates
rm -r include/cargo .cargo/config.toml
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
# --forked: protect the pytest process against test segfaults
%pytest --forked
%endif


%files -n python3-orjson -f %{pyproject_files}
%license LICENSE-MIT LICENSE-APACHE LICENSES.dependencies
%doc README.md


%changelog
* Tue Jul 25 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.9.2-2
- Backport patch to add PyType_GetDict for Python 3.12
- Fixes: rhbz#2220383

* Fri Jul 21 2023 Maxwell G <maxwell@gtmx.me> - 3.9.2-1
- Update to 3.9.2. Fixes rhbz#2211703.

* Fri Jul 21 2023 Maxwell G <maxwell@gtmx.me> - 3.8.14-1
- Update to 3.8.14.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 3.8.12-2
- Rebuilt for Python 3.12

* Thu May 18 2023 Maxwell G <maxwell@gtmx.me> - 3.8.12-1
- Update to 3.8.12.
- Use maturin as a build system when available

* Fri May 5 2023 Maxwell G <maxwell@gtmx.me> - 3.8.11-1
- Update to 3.8.11. Fixes rhbz#2193468.

* Wed Apr 12 2023 Maxwell G <maxwell@gtmx.me> - 3.8.10-1
- Initial package (rhbz#2184237).
