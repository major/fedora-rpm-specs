%global pypi_name wsaccel

Name:           python-%{pypi_name}
Version:        0.6.6
Release:        2%{?dist}
Summary:        Accelerator for ws4py and AutobahnPython

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
# Use GitHub archive to get Cython sources
Source0:        https://github.com/methane/wsaccel/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# License is not yet included in the 0.6.2 tag
Source1:        https://github.com/methane/wsaccel/blob/master/LICENSE
# Tests from the 0.6.2 tag don't work, get them from master instead.
SOURCE2:        https://raw.githubusercontent.com/methane/wsaccel/master/tests/test_4.py

%description
* WSAccell is WebSocket accelerator for AutobahnPython, ws4py and Tornado.
* WSAccell replaces per-byte process in them with Cython version.
* AutobahnPython beginning with version 0.6 automatically uses WSAccell if
  available.


%package -n     python3-%{pypi_name}
Summary:        Accelerator for ws4py and AutobahnPython
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-Cython
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
* WSAccell is WebSocket accelerator for AutobahnPython, ws4py and Tornado.
* WSAccell replaces per-byte process in them with Cython version.
* AutobahnPython beginning with version 0.6 automatically uses WSAccell if
  available.


%prep
%setup -qn %{pypi_name}-%{version}
cp -a %{SOURCE1} .
cp -a %{SOURCE2} tests/


%build
%py3_build


%install
%py3_install


# Fix permission
chmod 755 %{buildroot}%{python3_sitearch}/%{pypi_name}/*.so


%check
PYTHONPATH="$(echo build/lib.linux-%{_arch}-cpython-%{python3_version_nodots} | sed s/i386/i686/)" py.test-%{python3_version} tests


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitearch}/%{pypi_name}/


%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Julien Enselme <jujens@jujens.eu> - 0.6.6-1
- Update to 0.6.6

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.4-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Julien Enselme <jujens@jujens.eu> - 0.6.4-1
- Update to 0.6.4

* Fri Aug 12 2022 Julien Enselme <jujens@jujeuns.eu> - 0.6.3-8
- Rebuild to update Python bytecode files (#2113662)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.3-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 14:52:34 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-22
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-20
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 23 2019 Julien Enselme <jujens@jujens.eu> - 0.6.2-17
- Remove Python 2 subpackage.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-9
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.6.2-7
- Rebuilt for python 3.5

* Tue Aug 4 2015 Julien Enselme <jujens@jujens.eu> - 0.6.2-6
- Correct %%check section so tests pass on arm

* Fri Jul 31 2015 Julien Enseme <jujens@jujens.eu> - 0.6.2-5
- Fix tests in mock
- Use %%py2_build, %%py3build, %%py2_install and %%py2_install
- Make a python2 subpackage

* Thu Jul 30 2015 Julien Enselme <jujens@jujens.eu> - 0.6.2-4
- Add provides for python2-snappy
- Remove usage of python2 and python3 dirs

* Fri Jul 24 2015 Julien Enselme <jujens@jujens.eu> - 0.6.2-3
- Remove %%py3dir macro
- Add CFLAGS in %%build

* Sun Jul 19 2015 Julien Enselme <jujens@jujens.eu> - 0.6.2-2
- Add licence
- Launch tests

* Sat Jul 18 2015 Julien Enselme <jujens@jujens.eu> - 0.6.2-1
- Initial packaging
