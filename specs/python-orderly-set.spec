%global pypi_name orderly-set
%global pypi_version 5.2.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        4%{?dist}
Summary:        A package containing multiple implementations of Ordered Set
License:        MIT
URL:            https://github.com/seperman/orderly-set
Source0:        https://github.com/seperman/orderly-set/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Required by tests
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest
BuildRequires:  python3-mypy

%description
Orderly Set is a package containing multiple implementations of
Ordered Set.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Orderly Set is a package containing multiple implementations
of Ordered Set.

%prep
%autosetup -n orderly-set-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Tests are not running, see https://github.com/seperman/orderly-set/issues/7
#{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.md
%license MIT-LICENSE
%{python3_sitelib}/orderly_set
%{python3_sitelib}/orderly_set-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Susi Lehtola <susi.lehtola@iki.fi> - 5.2.2-3
- Review fix: switch to GitHub upstream to include license file.

* Thu Sep 12 2024 Susi Lehtola <susi.lehtola@iki.fi> - 5.2.2-2
- Added BR: python3-wheel required by tests.

* Wed Sep 04 2024 Susi Lehtola <susi.lehtola@iki.fi> - 5.2.2-1
- Initial package.
