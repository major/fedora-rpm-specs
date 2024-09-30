%global srcname pika
%global srcurl  https://github.com/%{srcname}/%{srcname}
%global desc \
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that \
tries to stay fairly independent of the underlying network support \
library.

Name:           python-%{srcname}
Version:        1.3.1
Release:        8%{?dist}
Summary:        AMQP 0-9-1 client library for Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{srcurl}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# Python 3 requirements
BuildRequires:  python3-devel
BuildRequires:  python3-twisted
BuildRequires:  python3-tornado

# Documentation requirements
BuildRequires:  python3-sphinx

# Test requirements
BuildRequires:  python3-nose2

%description
%{desc}


%package -n python3-%{srcname}
Summary:        AMQP 0-9-1 client library for Python 3
%{?python_provide:%python_provide python3-%{srcname}}
Recommends:     python3-tornado
Recommends:     python3-twisted

%description -n python3-%{srcname}
%{desc}

This package provides the Python 3 implementation.

%package -n python-%{srcname}-doc
Summary:        Additional API documentation for python-%{srcname}
# There used to be two docs packages, but the API isn't version dependent.
Provides: python3-%{srcname}-doc = %{version}-%{release}
Obsoletes: python2-%{srcname}-doc <= 0.12.0-5
Obsoletes: python3-%{srcname}-doc <= 0.12.0-5

%description -n python-%{srcname}-doc
%{summary}.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# These require a broker and should be run as part of the new CI/CD stuff
rm -rf tests/acceptance
sed -i -e s#tests=tests/unit,tests/acceptance#tests=tests/unit#g nose2.cfg
# don't run code coverage
sed -i 's/with-coverage = 1/with-coverage = 0/g' nose2.cfg

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
sphinx-build -b html -d doctrees docs html


%install
%pyproject_install
%pyproject_save_files pika


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} nose2


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CHANGELOG.md


%files -n python-%{srcname}-doc
%license LICENSE
%doc examples/
%doc html/


%changelog
* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.3.1-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.3.1-2
- Rebuilt for Python 3.12

* Thu Mar 16 2023 Jonathan Wright <jonathan@almalinux.org> - 1.3.1-1
- update to 1.3.1 rhbz#2102470
- modernize spec

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.2.1-2
- Rebuilt for Python 3.11

* Sat May 07 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.2.1-1
- Update to v1.2.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.10

* Fri Feb 05 2021 Jeremy Cline <jcline@redhat.com> - 1.2.0-1
- Update to v1.2.0 (https://github.com/pika/pika/milestone/17?closed=1)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Jeremy Cline <jcline@redhat.com> - 1.1.0-1
- Update to v1.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-6
- Subpackage python2-pika has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 11 2019 Jeremy Cline <jcline@redhat.com> - 1.0.1-3
- Fix the tests for Python 3.8

* Tue May 28 2019 Jeremy Cline <jcline@redhat.com> - 1.0.1-2
- Drop tests for Python 2 as Tornado is going away
- Drop integration test requirements from specfile

* Mon Apr 15 2019 Jeremy Cline <jcline@redhat.com> - 1.0.1-1
- Update to v1.0.1

* Wed Apr 10 2019 Jeremy Cline <jcline@redhat.com> - 1.0.0-1
- Update to v1.0.0
- De-conditionalize specfile
- Build documentation with Python 3
- Simplify check section to only run unit tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 25 2018 Miro Hrončok <mhroncok@redhat.com> - 0.12.0-2
- Rebuilt for Python 3.7

* Thu Jun 21 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.12.0-1
- Upstream 0.12.0
- Fix EPEL conditional

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.2-5
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.11.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Neal Gompa <ngompa13@gmail.com> - 0.11.2-2
- Fix directory ownership of Python module files

* Mon Jan 08 2018 Neal Gompa <ngompa13@gmail.com> - 0.11.2-1
- Upgrade to version 0.11.2
- Disable running tests by default for now as tests are timing out

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Raphael Groner <projects.rg@smart.ms> - 0.10.0-9
- merge changelog

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-8.2
- Rebuild for Python 3.6

* Mon Dec 12 2016 Tuomo Soini <tis@foobar.fi> - 0.10.0-8.1
- Honor %%_smp_ncpus_max setting on testing

* Sat Dec 10 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-7
- enable parallel testing with nose
- enable python-twisted-core and python-tornado on epel
- drop obsolete Group tag

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 10 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-5
- drop some duplications
- validate b0rken tests on epel7

* Sun Jul 03 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.0-4
- add %%check with execution of both unit and acceptance tests
- enable adapters for both tornado and twisted
- generate additional documentation, split into subpackage

* Sun Feb 07 2016 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.0-3
- Fix builds by defining python3_pkgversion if it doesn't exist
- Add missing BRs for py3-other variant (for EPEL 7)

* Sat Feb 06 2016 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.0-2
- Actually make the python 3 bcond work

* Sat Feb 06 2016 Neal Gompa <ngompa13{%}gmail{*}com> - 0.10.0-1
- Upgrade to version 0.10.0
- Refactor to meet current Fedora guidelines
- Add Python 3 subpackage (with EPEL 7 compatibility)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 13 2012 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.9.5-3
- Bump pika release version to fix upgrade path for f17 -> f18

* Sun Feb 26 2012 Daniel Aharon <dan@danielaharon.com> - 0.9.5-2
- Patch pika/adapters/blocking_connection.py

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Apr 3 2011 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.9.5-1
- Upgrade to version 0.9.5

* Sun Mar 6 2011 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.9.4-1
- Upgrade to version 0.9.4

* Sat Feb 19 2011 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.9.3-1
- Upgrade to version 0.9.3

* Sat Oct 2 2010 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.5.2-1
- Initial Package

