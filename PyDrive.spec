%global pkgname PyDrive
%global sum A wrapper library of google-api-python-client for Google Drive API tasks

Name:           PyDrive
Version:        1.3.1
Release:        21%{?dist}
Summary:        %{sum}

License:        ASL 2.0 and BSD
URL:            https://pypi.python.org/pypi/PyDrive
Source0:        https://pypi.python.org/packages/52/e0/0e64788e5dd58ce2d6934549676243dc69d982f198524be9b99e9c2a4fd5/PyDrive-1.3.1.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-oauth2client >= 4.0.0
BuildRequires:  python3-PyYAML >= 3.0
BuildRequires:  python3-google-api-client >= 1.2

%description
An python module which provides a convenient example.

%package -n python3-%{pkgname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{pkgname}}
Requires:   python3-oauth2client >= 4.0.0
Requires:   python3-google-api-client >= 1.2
Requires:   python3-PyYAML >= 3.0

%description -n python3-%{pkgname}
A wrapper library of google-api-python-client for Google Drive API tasks

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module if we are building for several python runtimes
%files -n python3-%{pkgname}
%license LICENSE
%{python3_sitelib}/*

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.3.1-20
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.1-17
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-13
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-10
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-8
- Subpackage python2-PyDrive has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 4 2017 Nick Bebout <nb@fedoraproject.org> - 1.3.1-3
- Add BuildRequires for python2|3-setuptools
* Fri Aug 4 2017 Nick Bebout <nb@fedoraproject.org> - 1.3.1-2
- Update for review issues
* Fri Aug 4 2017 Nick Bebout <nb@fedoraproject.org> - 1.3.1-1
- Initial release
