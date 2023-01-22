# Created by pyp2rpm-3.3.7
%global pypi_name unicodedata2
%global pypi_version 14.0.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        7%{?dist}
Summary:        Unicodedata backport updated to the latest Unicode version

License:        Apache-2.0
URL:            http://github.com/fonttools/unicodedata2
Source0:        %{pypi_source}

# https://github.com/fonttools/unicodedata2/pull/54
Patch0:         python-3.11-compatibility.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-randomly)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)

%description
This module provides access to the Unicode Character Database (UCD)
which defines character properties for all Unicode characters. The
data contained in this database is compiled from the UCD version 13.0.0.

The versions of this package match Unicode versions, so unicodedata2==13.0.0
is data from Unicode 13.0.0.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module provides access to the Unicode Character Database (UCD) 
which defines character properties for all Unicode characters. The 
data contained in this database is compiled from the UCD version 13.0.0.

The versions of this package match Unicode versions, so unicodedata2==13.0.0 
is data from Unicode 13.0.0.


%prep
%autosetup -n %{pypi_name}-%{pypi_version} -p1

%build
%py3_build

%install
%py3_install

%check
%pytest -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}%{python3_ext_suffix}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-6
- Update license tag to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 14.0.0-4
- Rebuilt for Python 3.11

* Mon May 16 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-3
- Update as suggested in this package review

* Mon May 16 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-2
- Drop un-necessary packaging lines from SPEC file

* Sun Feb 27 2022 Parag Nemade <pnemade AT redhat DOT com> - 14.0.0-1
- Initial package.
