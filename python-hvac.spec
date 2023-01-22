%global pypi_name hvac

Name:           python-%{pypi_name}
Version:        0.11.2
Release:        4%{?dist}
Summary:        HashiCorp Vault API client for Python

License:        ASL 2.0
URL:            https://github.com/hvac/hvac
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package provides a Python API client for HashiCorp Vault.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        HashiCorp Vault API client for Python 3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Extra dependency is not mandatory but quite useful
## Making this EPEL8 compatible...
Recommends:     python%{python3_version}dist(pyhcl) >= 0.3.10

%description -n python%{python3_pkgversion}-%{pypi_name}
This package provides a Python API client for HashiCorp Vault.

This is for Python 3.

%prep
%autosetup -n %{pypi_name}-%{version}
%if 0%{?el8}
# Lower dependency to requests 2.20+ for EL8
sed -e "s/requests>=2.21.0/requests>=2.20.0/" -i setup.py
%endif

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.11.2-2
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.7-2
- Rebuilt for Python 3.10

* Fri Feb 05 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.10.7-1
- Update to 0.10.7

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 18:27:43 EDT 2019 Neal Gompa <ngompa@datto.com> - 0.9.5-1
- Initial packaging for Fedora (RH#1765350)
