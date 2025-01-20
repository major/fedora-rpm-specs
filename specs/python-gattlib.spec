%global modname gattlib

Name:               python-gattlib
Version:            0.20210616
Release:            15%{?dist}
Summary:            Library to access Bluetooth LE devices

License:            Apache-2.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
# main package under ASL 2.0
# src/bluez under GPLv2+ and LGPLv2+
URL:                https://github.com/oscaracena/pygattlib
Source0:            https://files.pythonhosted.org/packages/source/g/%{modname}/%{modname}-%{version}.tar.gz
Source1:	    COPYING
Patch0:             py313.patch

BuildRequires:      gcc-c++

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      boost-python%{python3_pkgversion}-devel
BuildRequires:      glib2-devel
BuildRequires:      bluez-libs-devel

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -n %{modname}-%{version} -p1
cp %{S:1} .

find . -type f | xargs chmod -x

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python%{python3_pkgversion}-%{modname}
%license COPYING
%{python3_sitearch}/gattlib*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 14 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.20210616-14
- Modernize packaging.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.20210616-12
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.20210616-9
- Rebuilt for Boost 1.83

* Tue Nov 21 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.20210616-8
- Patch for Python 3.13

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.20210616-6
- Rebuilt for Python 3.12

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.20210616-5
- migrated to SPDX license

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.20210616-4
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20210616-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.20210616-1
- 0.20210616

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.20201113-10
- Rebuilt for Python 3.11

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.20201113-9
- Rebuilt for Boost 1.78

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20201113-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.20201113-7
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20201113-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.20201113-5
- Rebuilt for Python 3.10

* Wed Mar 03 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.20201113-4
- Patch for deadlock issue.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20201113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.20201113-2
- Rebuilt for Boost 1.75

* Fri Nov 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20201113-1
- 0.20201113

* Tue Sep 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200929-1
- 0.20200929

* Fri Sep 25 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200925-1
- 0.20200925

* Tue Sep 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200915-1
- 0.20200915

* Mon Sep 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200914-1
- 0.20200914

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20200122-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 0.20200122-3
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.20200122-2
- Rebuilt for Python 3.9

* Wed Jan 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200122-1
- 0.20200122

* Tue Jan 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200121-1
- 0.20200121

* Fri Jan 17 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20200117-1.post3
- 0.2020017.post3

* Sat Nov 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.20150805-12
- Drop Python 2.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.20150805-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.20180805-9
- Update patch to fix 3.8 FTBFS.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Jonathan Wakely <jwakely@redhat.com> - 0.20150805-7
- Patch for Boost.Python library names in Boost 1.69.0

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.20150805-7
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.20150805-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20150805-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.20150805-3
- Rebuilt for Boost 1.66

* Tue Dec 12 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.20150805-2
- License clarification.

* Mon Dec 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.20150805-1
- Add license file, fix URL, explain patch.

* Mon Dec 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.20150805-0
- Initial package.
