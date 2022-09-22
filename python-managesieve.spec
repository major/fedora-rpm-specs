%global pypi_name managesieve

Name:           python-%{pypi_name}
Version:        0.6
Release:        10%{?dist}
Summary:        Accessing a Sieve-Server for managing Sieve scripts
License:        Python and GPLv3
URL:            https://managesieve.readthedocs.io/
Source0:        %pypi_source
# Source1 may be removed in future, read https://gitlab.com/htgoebel/managesieve/-/issues/4
Source1:        LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner

%description
This module allows accessing a Sieve-Server for managing Sieve scripts there.
It is accompanied by a simple yet functional user application ‘sieveshell’.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module allows accessing a Sieve-Server for managing Sieve scripts there.
It is accompanied by a simple yet functional user application ‘sieveshell’.

%prep
%autosetup -n %{pypi_name}-%{version}
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{_bindir}/sieveshell
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 18 2020 Steve Traylen <steve.traylen@cern.ch> - 0.6-4
- Include LICENSE file

* Fri Nov 13 2020 Germano Massullo <germano.massullo@gmail.com> - 0.6-3
- rearranged %%check section
- added LICENSE file

* Wed Nov 11 2020 Steve Traylen <steve.traylen@cern.ch> - 0.6-2
- BR for pytest-runner for tests

* Thu Oct 29 2020 Steve Traylen <steve.traylen@cern.ch> - 0.6-1
- Initial release
