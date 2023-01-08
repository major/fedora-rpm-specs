%global pypi_name managesieve

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Accessing a Sieve-Server for managing Sieve scripts
License:        Python and GPLv3
URL:            https://managesieve.readthedocs.io/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python3-devel

# Test Requirements
#BuildRequires:  python3-pytest-runner
BuildRequires:  python3-pytest

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

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files managesieve


%check
#%%{python3} setup.py test
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%{_bindir}/sieveshell

%changelog
* Fri Jan 6 2023 Steve Traylen <steve.traylen@cern.ch> - 0.7.1-1
- Update to 0.7.1
- LICENSE file now included in release
- Migrate to pyproject macros

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
