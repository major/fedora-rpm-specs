
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global modname cliff

%global common_desc \
cliff is a framework for building command line programs. It uses setuptools \
entry points to provide subcommands, output formatters, and other \
extensions. \
\
Documentation for cliff is hosted on readthedocs.org at \
http://readthedocs.org/docs/cliff/en/latest/

%global common_desc_tests This package contains tests for the python cliff library.

Name:             python-%{modname}
Version:          4.2.0
Release:          2%{?dist}
Summary:          Command Line Interface Formulation Framework

Group:            Development/Libraries
License:          ASL 2.0
URL:              https://pypi.io/pypi/cliff
Source0:          https://pypi.io/packages/source/c/cliff/cliff-%{version}.tar.gz

BuildArch:        noarch

%package -n python3-%{modname}
Summary:          Command Line Interface Formulation Framework
%{?python_provide:%python_provide python3-%{modname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-prettytable
BuildRequires:    python3-stevedore
BuildRequires:    python3-cmd2 >= 0.8.0
BuildRequires:    python3-autopage
BuildRequires:    python3-importlib-metadata

Requires:         python3-prettytable
Requires:         python3-stevedore >= 2.0.1
Requires:         python3-cmd2 >= 1.0.0
Requires:         python3-yaml >= 3.12
Requires:         python3-autopage >= 0.4.0
Requires:         python3-importlib-metadata >= 4.4

%description -n python3-%{modname}
%{common_desc}

%package -n python3-%{modname}-tests
Summary:          Command Line Interface Formulation Framework
%{?python_provide:%python_provide python3-%{modname}-tests}

# Required for the test suite
BuildRequires:    bash
BuildRequires:    which
BuildRequires:    python3-subunit
BuildRequires:    python3-testtools
BuildRequires:    python3-testscenarios
BuildRequires:    python3-docutils
BuildRequires:    python3-PyYAML

Requires:         python3-%{modname} = %{version}-%{release}
Requires:         bash
Requires:         which
Requires:         python3-subunit
Requires:         python3-testtools
Requires:         python3-testscenarios
Requires:         python3-PyYAML

%description -n python3-%{modname}-tests
%{common_desc_tests}

%description
%{common_desc}

%prep
%setup -q -n %{modname}-%{upstream_version}
rm -rf {test-,}requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

%build
%{py3_build}

%install
%{py3_install}

%check
PYTHON=python3 python3 setup.py test

%files -n python3-%{modname}
%license LICENSE
%doc doc/ README.rst ChangeLog AUTHORS CONTRIBUTING.rst
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-*.egg-info
%exclude %{python3_sitelib}/%{modname}/tests

%files -n python3-%{modname}-tests
%{python3_sitelib}/%{modname}/tests

%changelog
* Tue Jun 06 2023 Joel Capitao <jcapitao@redhat.com> 4.2.0-2
- Remove mock and testrepository BR

* Fri Apr 21 2023 Karolina Kula <kkula@redhat.com> 4.2.0-1
- Update to upstream version 4.2.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 4.0.0-2
- Fix missing importlib_metadata runtime dependency

* Sun Sep 18 2022 Kevin Fenzi <kevin@scrye.com> - 4.0.0-1
- Update to 4.0.0. Fixes rhbz#2117683

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.10.1-3
- Rebuilt for pyparsing-3.0.9

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 3.10.1-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 3.10.1-1
- Update to upstream version 3.10.1

* Thu Jan 27 2022 Joel Capitao <jcapitao@redhat.com> - 3.10.0-3
- Requires autopage to fix F36/FTBFS

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 Kevin Fenzi <kevin@scrye.com> - 3.10.0-1
- Update to 3.10.0. Fixes rhbz#2026719

* Sat Nov 06 2021 Kevin Fenzi <kevin@scrye.com> - 3.9.0-1
- Update to 3.9.1. Fixes rhbz#1997441

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Kevin Fenzi <kevin@scrye.com> - 3.8.0-1
- Update to 3.8.0. Fixes rhbz#1965278

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.0-2
- Rebuilt for Python 3.10

* Thu Feb 18 2021 Kevin Fenzi <kevin@scrye.com> - 3.7.0-1
- Update to 3.7.0. Fixes rhbz#1929150

* Thu Jan 28 2021 Kevin Fenzi <kevin@scrye.com> - 3.6.0-1
- Update to 3.6.0. Fixes rhbz#1917619

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Kevin Fenzi <kevin@scrye.com> - 3.5.0-1
- Update to 3.5.0. Fixes rhbz#1896811

* Sun Sep 27 2020 Kevin Fenzi <kevin@scrye.com> - 3.4.0-1
- Update to 3.4.0. Fixes #1783966

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Joel Capitao <jcapitao@redhat.com> 3.1.0-1
- Update to upstream version 3.1.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.16.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Alfredo Moralejo <amoralej@redhat.com> 2.16.0-2
- Update to upstream version 2.16.0

* Sun Oct 06 2019 Kevin Fenzi <kevin@scrye.com> - 2.16.0-1
- Update to 2.16.0. Fixes bug #1749959

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.15.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.15.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Kevin Fenzi <kevin@scrye.com> - 2.15.0-1
- Update to 2.15.0. Fixed bug #1686683

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 2.14.1-1
- Update to 2.14.1

