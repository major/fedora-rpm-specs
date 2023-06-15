%global pypi_name subarulink

Name:           python-%{pypi_name}
Version:        0.3.11
Release:        9%{?dist}
Summary:        Python package to interact with Subaru Starlink Remote Services API

License:        ASL 2.0
URL:            https://github.com/G-Two/subarulink
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python package for interacting with the Subaru Starlink remote
vehicle services API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python package for interacting with the Subaru Starlink remote
vehicle services API.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
# https://github.com/G-Two/subarulink/pull/31
#%%license LICENSE
%doc README.md
%{_bindir}/subarulink
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.11-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.11-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.11-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.11-1
- Update to latest upstream release 0.3.11

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.6-1
- Update to latest upstream release 0.3.6

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Initial package for Fedora