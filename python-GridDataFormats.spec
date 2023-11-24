# main package is archful to run tests everywhere but produces noarch packages
%global debug_package %{nil}
%global pname GridDataFormats
%bcond_without check

%global commit be6132ac13041390a880061e4e873044b6c29573
%global date 20200812
%global shortcommit %(c=%{commit}; echo ${c:0:7})


%global desc \
GridDataFormats provides the Python package 'gridData'. It contains a class \
('Grid') to handle data on a regular grid --- basically NumPy n-dimensional \
arrays. It supports reading from and writing to some common formats (such as \
OpenDX).

Name: python-%{pname}
Version: 1.0.2
Release: 1%{?dist}
Summary: Read and write data on regular grids in Python
License: LGPL-3.0-or-later
URL: https://github.com/orbeckst/GridDataFormats
Source0: https://github.com/MDAnalysis/GridDataFormats/archive/%{version}/%{pname}-%{version}.tar.gz

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildArch: noarch
Requires: python3-numpy
Recommends: python3-scipy
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-numpy
BuildRequires: python3-versioneer
%if %{with check}
BuildRequires: python3-mrcfile
BuildRequires: python3-pytest
BuildRequires: python3-pytest-xdist
BuildRequires: python3-scipy
BuildRequires: python3-six
BuildRequires: python3-tempdir
%endif
%{?python_provide:%python_provide python3-%{pname}}

%description -n python3-%{pname}
%{desc}

%prep
%setup -q -n %{pname}-%{version}
rm versioneer.py

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
pytest-3 -v --numprocesses=auto ./gridData/tests
%endif

%files -n python3-%{pname}
%license COPYING.LESSER
%doc AUTHORS README.rst
%{python3_sitelib}/%{pname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/gridData

%changelog
* Wed Nov 22 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.0.2-1
- update to 1.0.2 (resolves rhbz#2245479)
- use SPDX identifier in License: field

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Dominik Mierzejewski <dominik@greysector.net> - 1.0.1-6
- fix build with Python 3.12 by removing bundled old versioneer module

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.11

* Sun May 29 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> - 1.0.1-1
- update to 1.0.1 (#2056400)
- run tests on all arches

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.4.20200812gitbe6132a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20200812gitbe6132a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.0-0.2.20200812gitbe6132a
- Rebuilt for Python 3.10

* Tue Jun 01 2021 Dominik Mierzejewski <dominik@greysector.net> 0.6.0-0.1.20200820gitbe6132a
- update to git be6132a (fixes test_resample_factor test failure rhbz#1917369)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Dominik Mierzejewski <dominik@greysector.net> 0.5.0-1
- update to 0.5.0 (#1696989)
- use pythonX_version macros
- upstream switched to pytest for testing
- run tests in parallel

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-4
- Subpackage python2-GridDataFormats has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-2
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Dominik Mierzejewski <dominik@greysector.net> 0.4.0-1
- update to 0.4.0 (#1535726)
- fix build on 32-bit arches
- drop RHEL5 stuff
- use standard bcond for enabling/disabling tests

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Dominik Mierzejewski <dominik@greysector.net> 0.3.3-1
- update to 0.3.3 (#1336061)
- use current python2 module requirements specification
- drop no longer relevant Obsoletes:

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.2-2
- enable tests (python2/3-tempdir is in Fedora now)

* Sat Dec 12 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.2-1
- update to 0.3.2 (#1289547)
- works without scipy now, so make it a soft dependency
- prepare to enable tests (depends on python2/3-tempdir)

* Wed Dec 09 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.1-1
- update to 0.3.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 24 2015 Dominik Mierzejewski <dominik@greysector.net> 0.3.0-1
- update to 0.3.0
- add python3 subpackage and update to current Python packaging guidelines

* Fri Jul 10 2015 Dominik Mierzejewski <dominik@greysector.net> 0.2.5-1
- update to 0.2.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 Dominik Mierzejewski <dominik@greysector.net> 0.2.4-1
- initial build
