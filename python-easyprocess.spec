%global pypi_name EasyProcess
%global dist_name %{py_dist_name %{pypi_name}}

Name:           python-%{dist_name}
Version:        0.3
Release:        6%{?dist}
Summary:        Easy to use Python subprocess interface

License:        BSD
URL:            https://github.com/ponty/EasyProcess
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
# For Tests
BuildRequires:  iputils
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-timeout}
BuildRequires:  %{py3_dist six}

%global _description %{expand:
EasyProcess is an easy to use python subprocess interface.}

%description %_description

%package -n     python3-%{dist_name}
Summary:        %{summary}

Requires:       %{py3_dist py}
%description -n python3-%{dist_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Avoid circular dependency with PyVirtualDisplay
rm -f tests/test_fast/test_deadlock.py

%build
%py3_build

%install
%py3_install

%check
%pytest


%files -n python3-%{dist_name}
%doc README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{dist_name}/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3-2
- Rebuilt for Python 3.10

* Sat Feb 13 2021 Scott Talbert <swt@techie.net> - 0.3-1
- Initial package
