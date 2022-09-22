%global srcname pytest-virtualenv
%global sum Virtualenv fixture for py.test

Name:           python-%{srcname}
Version:        1.7.0
Release:        15%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# needed for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-shutil
BuildRequires:  python3-pytest-fixture-config
BuildRequires:  python3-path
BuildRequires:  python3-virtualenv

%description
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
# The requirements are missing from upstream metadata:
Requires:       python3-path python3-setuptools

%description -n python3-%{srcname}
Create a Python virtual environment in your test that cleans up on teardown.
The fixture has utility methods to install packages and list what's installed.

%prep
%autosetup -n %{srcname}-%{version}
# Upstream pins pytest to older than 4.0.0 until they finish cleaning up deprecications. 
# However, we have no choice and all the tests do pass fine, so we unpin here.
sed -i -e 's|pytest<4.0.0|pytest|' setup.py

# This is not needed when building from the sdist
sed -i -e '/setuptools-git/d' common_setup.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.md CHANGES.md
%{python3_sitelib}/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.7.0-14
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-9
- Slim down the requirements

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-2
- Drop python2. Fixes bug #1723591

* Sun Jun 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-1
- Update to 1.7.0. Fixes bug #1714450

* Sun Apr 14 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0. Fixes bug #1697357

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-9
- Use sys.executable -m virtualenv (fixup repeated usage)

* Thu Aug 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-8
- Use sys.executable -m virtualenv

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.11-6
- Rebuilt for Python 3.7

* Wed Mar 14 2018 Tomas Orsava <torsava@redhat.com> - 1.2.11-5
- Add detection of the virtualenv-3 and virtualenv-X.Y executables

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 18 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-3
- Fix up Requires to pull in things it needs to function

* Sun Sep 10 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-2
- Added BuildRequires for tests

* Tue Aug 15 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.11-1
- Initial version. 
