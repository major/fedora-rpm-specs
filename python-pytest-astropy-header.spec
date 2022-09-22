%global srcname pytest-astropy-header

Name: python-%{srcname}
Version: 0.2.0
Release: 4%{?dist}
Summary: pytest plugin to add diagnostic info to the header of output

License: BSD
URL: https://www.astropy.org/
Source0: %{pypi_source}

BuildArch: noarch

%global _description %{expand:
This plugin package provides a way to include information about the system, 
Python installation, and select dependencies in the header of the output 
when running pytest. It can be used with packages that are not affiliated 
with the Astropy project, but is optimized for use with 
astropy-related projects.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/pytest_astropy_header
%{python3_sitelib}/pytest_astropy_header-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.2.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Christian Dersch <lupinix@fedoraproject.org> - 0.2.0-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-3
- Rebuilt for Python 3.9

* Mon Feb 17 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.1.2-2
- Do not include all files in python sitelib with wildcard

* Sat Jan 11 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.1.2-1
- initial packaging effort

