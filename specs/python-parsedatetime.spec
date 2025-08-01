%{?python_enable_dependency_generator}
%global realname parsedatetime

%bcond_without tests

Name:           python-%{realname}
Version:        2.6
Release:        18%{?dist}
Summary:        Parse human-readable date/time strings in Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/bear/%{realname}
Source0:        https://github.com/bear/%{realname}/archive/v%{version}.tar.gz#/%{realname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description
parsedatetime is a python module that can parse human-readable date/time\
strings.


%package -n python3-%{realname}
Summary:        Parse human-readable date/time strings in Python
%{?python_provide:%python_provide python3-%{realname}}

%description -n python3-%{realname}
parsedatetime is a python module that can parse human-readable date/time
strings.

%prep
%autosetup -n %{realname}-%{version}


%build
%py3_build


%install
%py3_install
# It makes no sense to ship all these tests in the package
# just use them during the build
rm -rf %{buildroot}%{python3_sitelib}/%{realname}/tests

%check
%if %{with tests}
py.test-3 -x tests/*.py
%endif

%files -n python3-%{realname}
%license LICENSE.txt
%doc AUTHORS.txt CHANGES.txt README.rst
%{python3_sitelib}/%{realname}
%{python3_sitelib}/%{realname}*.egg-info

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.6-17
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.6-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.6-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.6-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Michele Baldessari <michele@acksyn.org> - 2.6-1
- New upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 2.5-1
- update to new upstream version 2.5 (#1773846)

* Thu Nov 21 2019 Felix Schwarz <fschwarz@fedoraproject.org> 2.4-16
- add "tests" define to run tests manually without changing the spec file

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-11
- Enable python dependency generator

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4-10
- Remove Python 2 subpackage and epydoc documentation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4-8
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4-7
- Fix BuildRequires to require the tox command and not the python2 module

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.4-6
- Escape macros in %%changelog

* Wed Feb 07 2018 Eli Young <elyscape@gmail.com> - 2.4-5
- Declare missing dependency on python-future
- Update package on EPEL7

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.4-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4-3
- Python 2 binary package renamed to python2-parsedatetime
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 14 2017 Michele Baldessari <michele@acksyn.org> - 2.4-1
- New upstream release

* Mon Mar 13 2017 Michele Baldessari <michele@acksyn.org> - 2.3-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Michele Baldessari <michele@acksyn.org> - 2.2-2
- Disable %%check for the time being as not all requirements are packaged

* Tue Jan 24 2017 Michele Baldessari <michele@acksyn.org> - 2.2-1
- New upstream

* Tue Dec 27 2016 Michele Baldessari <michele@acksyn.org> - 2.1-4
- Fix python3.6 build

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Mar 10 2016 Michele Baldessari <michele@acksyn.org> - 2.1-1
- New upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 02 2015 Michele Baldessari <michele@acksyn.org> - 1.5-1
- New upstream (BZ#1238670)
* Mon Jun 22 2015 Michele Baldessari <michele@acksyn.org> - 1.4-2
- Fix python --> python2 macros
* Thu Jun 04 2015 Michele Baldessari <michele@acksyn.org> - 1.4-1
- Initial packaging
