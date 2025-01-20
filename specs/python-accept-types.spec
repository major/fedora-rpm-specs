%global pypi_name accept-types
%global pypi_version 0.4.1
%global commit cb2531768689478737e4a8454def6a60575424e3
%global shortcommit %(c=%{commit}; echo ${c:0:12})
%global owner tim_heap

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        13%{?dist}
Summary:        Use the correct accept type for an HTTP request
License:        MIT
URL:            https://bitbucket.org/%{owner}/%{name}
# The pypi source has the test suite stripped out :/
Source0:        %{URL}/get/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global desc \
accept-types helps your application respond to a HTTP request in a way \
that a client prefers.  The Accept header of an HTTP request informs the \
server which MIME types the client is expecting back from this request, \
with weighting to indicate the most prefered. If your server can respond \
in multiple formats (e.g.: JSON, XML, HTML), the client can easily tell \
your server which is the prefered format without resorting to hacks like \
'&amp;format=json' on the end of query strings.

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{owner}-%{name}-%{shortcommit}
%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%check
%tox

%install
%pyproject_install
%pyproject_save_files accept_types

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.1-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.11

* Tue Mar 15 2022 Paul Wouters <paul.wouters@aiven.io> - 0.4.1-3
- Resolves: rhbz#2050434 python-accept-types
- Fix license, description and summary, cleanup BuildRequires:

* Mon Feb 07 2022 Paul Wouters <paul.wouters@aiven.io> - 0.4.1-2
- Use latest python macros

* Thu Feb 03 2022 Paul Wouters <paul.wouters@aiven.io> - 0.4.1-1
- Initial package.
