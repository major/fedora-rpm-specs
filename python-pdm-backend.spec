Name:           python-pdm-backend
Version:        2.1.6
Release:        1%{?dist}
Summary:        The build backend used by PDM that supports latest packaging standards
License:        MIT
URL:            https://github.com/pdm-project/pdm-backend
Source:         %{pypi_source pdm_backend}
# Unbundles vendored dependencies and drops
# validate_pyproject entirely. For context, see
# https://bugzilla.redhat.com/show_bug.cgi?id=2179101
Patch:          unbundle-vendored-deps.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-packaging
BuildRequires:  python3-tomli-w
BuildRequires:  python3-pyproject-metadata
# Test-only deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  python3-editables
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools


%global _description %{expand:
The build backend used by PDM that supports latest packaging standards.}


%description %_description

%package -n     python3-pdm-backend
Summary:        %{summary}
Requires:       python3-packaging
Requires:       python3-tomli-w
Requires:       python3-pyproject-metadata

%description -n python3-pdm-backend %_description


%prep
%autosetup -p1 -n pdm_backend-%{version}
rm -rv src/pdm/backend/_vendor


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pdm


%check
%pytest


%files -n python3-pdm-backend -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Wed Sep 06 2023 Lumír Balhar <lbalhar@redhat.com> - 2.1.6-1
- Update to 2.1.6 (rhbz#2235604)

* Wed Aug 09 2023 Lumír Balhar <lbalhar@redhat.com> - 2.1.5-1
- Update to 2.1.5 (rhbz#2230229)

* Wed Aug 02 2023 Lumír Balhar <lbalhar@redhat.com> - 2.1.4-1
- Update to 2.1.4 (rhbz#2213464)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.7-2
- Rebuilt for Python 3.12

* Mon May 15 2023 Lumír Balhar <lbalhar@redhat.com> - 2.0.7-1
- Update to 2.0.7 (rhbz#2203716)
- SPDX license

* Wed Apr 26 2023 Lumír Balhar <lbalhar@redhat.com> - 2.0.6-1
- Update to 2.0.6 (rhbz#2185582)

* Mon Mar 20 2023 Lumír Balhar <lbalhar@redhat.com> - 2.0.5-1
- Initial package