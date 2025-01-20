
%global pypi_name pydyf

Name:           python-pydyf
Version:        0.11.0
Release:        3%{?dist}
Summary:        Low-level PDF creator
# The test suite is released under the AGPL but we are not shipping any test
# code in the "binary" (noarch) RPM so we can just use the 3-clause BSD.
License:        BSD-3-Clause
URL:            https://www.courtbouillon.org/pydyf
Source0:        %{pypi_source}
# remove some dependency/pytest options which are mostly useful for developers
# (e.g. style checks) but may cause unnecessary issues for distro-level testing
Patch0:         %{name}-no-developer-testing-options.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
# used as "build-backend" in pyproject.toml but not detected by Fedora's
# macros to generate build requirements
BuildRequires:  python3dist(flit-core)
# test suite calls the "gs" binary to verify outputs, not detectable by
# Fedora's macros
BuildRequires:  ghostscript


%description
pydyf is a low-level PDF generator written in Python and based on PDF
specification 1.7.


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
pydyf is a low-level PDF generator written in Python and based on PDF
specification 1.7.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x test


%build
%pyproject_wheel


%install
%pyproject_install


%check
%pytest

%files -n  python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.11.0-1
- update to 0.11.0

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.13

* Tue Apr 30 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.10.0-1
- update to 0.10.0

* Mon Feb 26 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.9.0-1
- update to 0.9.0

* Thu Jan 25 2024 Felix Schwarz <fschwarz@fedoraproject.org> - 0.8.0-3
- use just flit-core as build dependency

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 05 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 0.8.0-1
- update to 0.8.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 0.7.0-1
- update to 0.7.0

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.12

* Fri Apr 14 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 0.6.0-2
- SPDX migration

* Wed Mar 29 2023 Felix Schwarz <fschwarz@fedoraproject.org> - 0.6.0-1
- update to 0.6.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 12 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 0.5.0-1
- update to 0.5.0

* Mon Sep 19 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 0.3.0-1
- update to 0.3.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 0.2.0-1
- update to 0.2.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.0.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 01 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 0.0.3-1
- update to 0.0.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.2-3
- Rebuilt for Python 3.10

* Sun Apr 18 2021 Felix Schwarz <fschwarz@fedoraproject.org> 0.0.2-2
- updated according to review comments

* Sun Apr 18 2021 Felix Schwarz <fschwarz@fedoraproject.org> 0.0.2-1
- initial package

