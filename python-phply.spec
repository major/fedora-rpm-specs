%global pypi_name phply
%global author viraptor

Name:           python-%{pypi_name}
Version:        1.2.5
Release:        5%{?dist}
Summary:        PHP parser written in Python using PLY 

License:        BSD-3-Clause
URL:            https://github.com/%{author}/%{pypi_name}
Source0:        https://github.com/%{author}/%{pypi_name}/archive/refs/tags/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-ply

%description
phply is a parser for the PHP programming language written using PLY.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
phply is a parser for the PHP programming language written using PLY

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%py3_check_import %{pypi_name}

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.md
%license LICENSE
%{_bindir}/phplex
%{_bindir}/phpparse
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.5-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Sudip Shil <sshil@redhat.com> - 1.2.5-3
- spec file updated

* Wed Nov 23 2022 Sudip Shil <sshil@redhat.com> - 1.2.5-2
- spec file updated

* Fri Nov 18 2022 Sudip Shil <sshil@redhat.com> - 1.2.5-1
- New rpm package submission for Fedora
