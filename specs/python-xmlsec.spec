%global srcname xmlsec

Name:           python-%{srcname}
Version:        1.3.14
Release:        3%{?dist}
Summary:        Python bindings for the XML Security Library

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/x/%{srcname}/%{srcname}-%{version}.tar.gz

# Explicitly cast the pointer type in PyXmlSec_ClearReplacedNodes
# Fixes build with -Wincompatible-pointer-types
Patch:          https://github.com/xmlsec/python-xmlsec/pull/325.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  libxml2-devel >= 2.9.1
BuildRequires:  xmlsec1-devel >= 1.2.33
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  libtool-ltdl-devel

%description
%{summary}.


%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.33
Requires: xmlsec1-openssl


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/xmlsec*.so
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}-%{version}.dist-info/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 20 2024 Martin Kutlak <mkfedora@outlook.com> - 1.3.14-1
- Update to upstream version 1.3.14 rhbz#2273502 rhbz#2261617
- Fix build with -Wincompatible-pointer-types PR#5

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.3.13-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.3.13-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 12 2022 Martin Kutlak <mkfedora@outlook.com> - 1.3.13-1
- Update to upstream version 1.3.13 (rhbz#2120027)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.12-2
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Martin Kutlak <mkfedora@outlook.com> - 1.3.12-1
- Add buildrequire for xmlsec1-openssl-devel
- Update to upstream version 1.3.12
- Fix build (#2039340)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Martin Kutlak <mkfedora@outlook.com> - 1.3.9-1
- Update to 1.3.9 (#1892839)

* Mon Sep 21 2020 Lumír Balhar <lbalhar@redhat.com> - 1.3.8-3
- Fix FTBFS

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 1 2020 Martin Kutlak <mkfedora@outlook.com> - 1.3.8-1
- Update spec file
- Update to 1.3.8 (#1838368)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-10
- Rebuilt for Python 3.9

* Wed Feb 12 2020 Ken Dreyer <kdreyer@redhat.com> - 1.3.3-9
- pkgconfig is only a build-time dependency (rhbz#1789152)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.3-1
- Initial package.
