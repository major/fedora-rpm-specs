Name:           python-pydiffx
Version:        1.1
Release:        10%{?dist}
Summary:        Python implementation of the DiffX specification
License:        MIT
URL:            https://diffx.org/pydiffx/
Source:         %{pypi_source pydiffx}

BuildArch:      noarch

BuildRequires:  python3-devel

# https://github.com/beanbaginc/diffx/pull/2
Patch:          add_requirements.patch
# https://github.com/beanbaginc/diffx/issues/4
Patch:          pydiffx-1.1-Fix-Python-3.12-compatibility.patch

%global _description %{expand:
DiffX is a proposed specification for a structured version of Unified
Diffsthat contains metadata, standardized parsing, multi-commit diffs, and
binary diffs, in a format compatible with existing diff parsers.

This module is a reference implementation designed to make it easy to read
and write DiffX files in any Python application.}

%description %_description


%package -n python3-pydiffx
Summary:        %{summary}


%description -n python3-pydiffx %_description


%prep
%autosetup -p1 -n pydiffx-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files pydiffx


%check
%pytest


%files -n python3-pydiffx -f %{pyproject_files}
%doc README.rst
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Aleksei Bavshin <alebastr@fedoraproject.org> - 1.1-5
- Fix Python 3.12 compatibility (rhbz#2175200, rhbz#2220425)
- Verify that the License tag is valid SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Jonathan Wright <jonathan@almalinux.org> - 1.1-1
- Initial package build

