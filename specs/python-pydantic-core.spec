# Copyright (C) 2023 Maxwell G <maxwell@gtmx.me>
# Copyright (C) Fedora Project Authors
# SPDX-License-Identifier: MIT
# License text: https://spdx.org/licenses/MIT

%bcond tests 1
# Optional integration tests (no effect if tests are disabled)
%bcond numpy_tests 1
%bcond pandas_tests 1
# - No python-inline-snapshot on Fedora 40 (dependencies are too old)
# - No python-inline-snapshot in EPEL10 (blocked by python-black)
%bcond inline_snapshot_tests %{expr:%{undefined fc40} && %{undefined el10}}

Name:           python-pydantic-core
Version:        2.27.2
Release:        3%{?dist}
Summary:        Core validation logic for pydantic written in rust

License:        MIT
URL:            https://github.com/pydantic/pydantic-core
Source:         %{url}/archive/v%{version}/pydantic-core-%{version}.tar.gz

# Downstream-only: allow an older version of idna
#
# The many new dependencies of idna 1.x mean it will take some time to update.
Patch:          0001-Downstream-only-allow-an-older-version-of-idna.patch

BuildRequires:  python3-devel
BuildRequires:  rust-packaging
BuildRequires:  tomcli >= 0.3.0
%if %{with tests}
BuildRequires:  %{py3_dist dirty-equals}
%if %{with inline_snapshot_tests}
BuildRequires:  %{py3_dist inline-snapshot}
%endif
%if %{with numpy_tests}
BuildRequires:  %{py3_dist numpy}
%endif
BuildRequires:  %{py3_dist hypothesis}
%if %{with pandas_tests}
%ifnarch %{ix86}
BuildRequires:  %{py3_dist pandas}
%endif
%endif
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
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
ignore="${ignore-} --ignore=tests/benchmarks"
%if %{without inline_snapshot_tests}
ignore="${ignore-} --ignore=tests/validators/test_allow_partial.py"
%endif
%pytest ${ignore-} -rs
%endif


%files -n python3-pydantic-core -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSES.dependencies


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.27.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.27.2-2
- Omit snapshot tests on EPEL10

* Wed Dec 18 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.27.2-1
- Update to 2.27.2

* Sat Nov 23 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.27.1-1
- Update to 2.27.1

* Thu Sep 26 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.23.4-2
- Fix automatic provides on Python extension due to SONAME

* Wed Sep 18 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.23.4-1
- Update to 2.23.4

* Tue Sep 10 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.23.3-1
- Update to 2.23.3

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.20.1-1
- Update to 2.20.1

* Tue Jun 25 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.20.0-1
- Update to 2.20.0

* Sat Jun 15 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.18.4-3
- Rebuilt with rust-jiter 0.4.2

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.18.4-2
- Rebuilt for Python 3.13

* Wed Jun 05 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.18.4-1
- Update to 2.18.4

* Wed May 29 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.18.3-1
- Update to 2.18.3

* Fri May 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.18.2-2
- Rebuild with Rust 1.78 to fix incomplete debuginfo and backtraces

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.18.2-1
- Update to 2.18.2

* Sat Apr 13 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.18.1-1
- Update to 2.18.1

* Sat Feb 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.16.3-1
- Update to 2.16.3.

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
