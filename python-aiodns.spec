# set upstream name variable
%global srcname aiodns


Name:           python-aiodns
Version:        3.0.0
Release:        8%{?dist}
Summary:        Simple DNS resolver for asyncio

License:        MIT
URL:            https://github.com/saghul/aiodns
Source0:        https://github.com/saghul/%{srcname}/archive/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pycares
# for tests
#BuildRequires:  python3-pytest

%description
aiodns provides a simple way for doing asynchronous DNS resolutions
with a synchronous looking interface by using pycares.



%package     -n python3-%{srcname}
Summary:        Simple DNS resolver for asyncio
BuildArch:      noarch
Requires:       python3-pycares
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
aiodns provides a simple way for doing asynchronous DNS resolutions
with a synchronous looking interface by using pycares.



%prep
%autosetup -n %{srcname}-%{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
# no tests to run with pytest: Disabling.



%files -n python3-%{srcname}
%license LICENSE
%doc README.rst ChangeLog
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}/



%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 3.0.0-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.0-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 9 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0
- Remove Patch0 (Backport from upstream commit: 28111210)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-9
- Rebuilt for Python 3.10

* Sun Feb 14 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-8
- Replace glob with %%{python3_version} in %%files section

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-6
- Add Patch0 to fix epel8 installation package
  Backport from upstream commit: 28111210

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-1
- Bump version to 2.0.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.1-5
- Subpackage python2-aiodns has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.7

* Wed Apr 18 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.1.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Apr  4 2018 Matthieu Saulnier <fantom@fedoraproject.org> - 1.1.1-1
- Initial package
