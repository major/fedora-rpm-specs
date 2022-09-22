%global srcname %(echo %{name} | sed 's/^python-//')
Name:           python-fqdn
Version:        1.5.1
Release:        6%{?dist}
Summary:        Validates fully-qualified domain names against RFC 1123
BuildArch:      noarch
License:        MPLv2.0
URL:            https://github.com/ypcrts/fqdn
Source0:        %pypi_source
# Missing in pypi tar ball release, present at github :(
Source1:        test_fqdn.py

%global _description %{expand:
Validates fully-qualified domain names against RFC 1123, so that they
are acceptable to modern browsers.}
%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
mkdir tests/
touch tests/__init__.py
cp %{SOURCE1} tests/
%pytest

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Paul Wouters <paul.wouters@aiven.io> - 1.5.1-2
- Initial package
