# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1

Name:           python-pydantic-core
Version:        2.16.2
Release:        1%{?dist}
Summary:        Core validation logic for pydantic written in rust

License:        MIT
URL:            https://github.com/pydantic/pydantic-core
Source:         %{url}/archive/v%{version}/pydantic-core-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  rust-packaging
BuildRequires:  tomcli >= 0.3.0
%if %{with tests}
BuildRequires:  %{py3_dist dirty-equals}
BuildRequires:  %{py3_dist hypothesis}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytz}
%endif


%global _description %{expand:
The pydantic-core project provides the core validation logic for pydantic
written in Rust.}

%description %_description


%package -n python3-pydantic-core
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0 (duplicate)
# MIT OR Apache-2.0 OR Zlib
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT (duplicate)
License:        %{shrink:
                (MIT OR Apache-2.0)
                AND Unicode-DFS-2016
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND (Apache-2.0 OR BSL-1.0)
                AND MIT
                AND (MIT OR Apache-2.0 OR zlib)
                AND (Unlicense OR MIT)
                }

%description -n python3-pydantic-core %_description


%prep
%autosetup -p1 -n pydantic-core-%{version}

# Remove unused Cargo config that contains buildflags for Darwin
rm -v .cargo/config.toml

# Delete pytest adopts. We don't care about benchmarking or coverage.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.addopts'
# Remove pytest timeout config. pytest-timeout is not needed for downstream tests.
tomcli-set pyproject.toml del 'tool.pytest.ini_options.timeout'

%cargo_prep

# Remove Windows-only dependencies
tomcli-set Cargo.toml del 'dependencies.python3-dll-a'
tomcli-set Cargo.toml lists delitem 'dependencies.pyo3.features' 'generate-import-lib'
# Do not strip binaries. We want useful debuginfo.
tomcli-set Cargo.toml del 'profile.release.strip'


%generate_buildrequires
%pyproject_buildrequires
%cargo_generate_buildrequires


%build
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

export RUSTFLAGS="%{build_rustflags}"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pydantic_core


%check
%pyproject_check_import
%if %{with tests}
%pytest --ignore=tests/benchmarks
%endif


%files -n python3-pydantic-core -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSES.dependencies


%changelog
* Mon Feb 05 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.16.2-1
- Update to 2.16.2.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 23 2023 Maxwell G <maxwell@gtmx.me> - 2.14.6-1
- Update to 2.14.6.

* Sat Nov 25 2023 Maxwell G <maxwell@gtmx.me> - 2.14.5-1
- Update to 2.14.5.

* Fri Sep 29 2023 Maxwell G <maxwell@gtmx.me> - 2.10.1-1
- Update to 2.10.1.

* Mon Jun 05 2023 Maxwell G <maxwell@gtmx.me> - 2.6.3-1
- Initial package. Closes rhbz#2238117.
