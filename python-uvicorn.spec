# what it's called on pypi
%global srcname uvicorn
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Uvicorn is a lightning-fast ASGI server implementation, using uvloop and
httptools.  Until recently Python has lacked a minimal low-level
server/application interface for asyncio frameworks.  The ASGI specification
fills this gap, and means we are now able to start building a common set of
tooling usable across all asyncio frameworks.  Uvicorn currently supports
HTTP/1.1 and WebSockets.  Support for HTTP/2 is planned.}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        0.15.0
Release:        4%{?dist}
Summary:        The lightning-fast ASGI server
License:        BSD
URL:            https://www.uvicorn.org
# PyPI tarball doesn't have tests
Source0:        https://github.com/encode/uvicorn/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest pytest-mock requests trustme httpx pytest-asyncio}
# from minimal requirements
BuildRequires:  %{py3_dist asgiref click h11}
# from extra requirements
BuildRequires:  %{py3_dist websockets wsproto httptools uvloop watchgod python-dotenv pyyaml}
%endif
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{pkgname} -i %{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info standard}


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%pytest --verbose -W 'default::DeprecationWarning'
%endif


%files -n python3-%{pkgname}
%license LICENSE.md
%doc README.md
%{_bindir}/uvicorn
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 0.15.0-3
- Do not treat a DeprecationWarning in the tests as an error (fix RHBZ#2099139)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 10 2021 Tomas Hrnciar - 0.15.0-1
- Update to 0.15.0
- Fixes: rhbz#1966531

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 23 2021 Lumír Balhar <lbalhar@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.13.4-2
- Rebuilt for Python 3.10

* Sat Mar 20 2021 Carl George <carl@george.computer> - 0.13.4-1
- Latest upstream
- Fixes: rhbz#1940231

* Fri Feb 05 2021 Carl George <carl@george.computer> - 0.13.3-1
- Latest upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Carl George <carl@george.computer> - 0.12.2-1
- Latest upstream
- Add uvicorn[standard] subpackage

* Tue Aug 18 2020 Carl George <carl@george.computer> - 0.11.8-1
- Latest upstream

* Thu Jun 04 2020 Carl George <carl@george.computer> - 0.11.5-1
- Initial package
