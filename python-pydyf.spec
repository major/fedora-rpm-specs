
%global pypi_name pydyf

Name:           python-pydyf
Version:        0.3.0
Release:        1%{?dist}
Summary:        Low-level PDF creator 
# The test suite is released under the AGPL but we are not shipping any test
# code in the "binary" (noarch) RPM so we can just use the 3-clause BSD.
License:        BSD
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
BuildRequires:  python3-flit
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

