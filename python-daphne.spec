%global srcname daphne
%global common_description %{expand:
Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP,
developed to power Django Channels.  It supports automatic negotiation of
protocols; there is no need for URL prefixing to determine WebSocket endpoints
versus HTTP endpoints.}

%bcond_without  tests


Name:           python-%{srcname}
Version:        3.0.2
Release:        4%{?dist}
Summary:        Django ASGI (HTTP/WebSocket) server
License:        BSD
URL:            https://github.com/django/daphne
# PyPI tarball doesn't have tests
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# downstream-only patch
Patch:          0001-Fedora-dependency-adjustments.patch
BuildArch:      noarch
BuildRequires:  python3-devel


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname} twisted


%check
%if %{with tests}
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.txt
%{_bindir}/daphne


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Python Maint <python-maint@redhat.com> - 3.0.2-2
- Rebuilt for Python 3.11

* Wed Apr 20 2022 Carl George <carl@george.computer> - 3.0.2-1
- Latest upstream (resolves: rhbz#1947130)
- Convert to pyproject macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.1-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 3.0.1-1
- Update to 3.0.1 (rhbz#1892469)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Carl George <carl@george.computer> - 2.5.0-1
- Initial package
