%global pypi_name textfsm

Name:           python-%{pypi_name}
Version:        1.1.2
Release:        1%{?dist}
Summary:        Python module for parsing semi-structured text into python tables

License:        ASL 2.0
URL:            https://github.com/google/textfsm
Source0:        https://github.com/google/textfsm/archive/v%{version}.tar.gz
BuildArch:      noarch

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3-future
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
Requires:       python3-future
Requires:       python3-six

%description -n python3-%{pypi_name}
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING
%exclude %{python3_sitelib}/testdata
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/textfsm

%changelog
* Tue Jul 26 2022 Joel Capitao <jcapitao@redhat.com> - 1.1.2-1
- Update to upstream version 1.1.2 (#1697095)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.10

* Mon Feb 22 2021 Javier Peña <jpena@redhat.com> - 1.1.0-1
- Update to upstream version 1.1.0 (#1931302)
- Remove python2 subpackage
- Enable unit tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Javier Peña <jpena@redhat.com> - 0.3.2-6
- Switch sources to use GitHub release
- Disable unit tests until they are present in the tarball

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 01 2018 Javier Peña <jpena@redhat.com> - 0.3.2-4
- Removed Python 2 package from Fedora 30+ (bz#1634614)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-2
- Rebuilt for Python 3.7

* Fri Mar 16 2018 Javier Peña <jpena@redhat.com> - 0.3.2-1
- Initial package.
