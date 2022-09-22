%global srcname wsproto
%global common_description %{expand:
wsproto is a pure-Python implementation of a WebSocket protocol stack.  It is
written from the ground up to be embeddable in whatever program you choose to
use, ensuring that you can communicate via WebSockets, as defined in RFC6455,
regardless of your programming paradigm.

wsproto does not provide a parsing layer, a network layer, or any rules about
concurrency.  Instead, it is a purely in-memory solution, defined in terms of
data actions and WebSocket frames.  RFC6455 and Compression Extensions for
WebSocket via RFC7692 are fully supported.}

%bcond_without  tests


Name:           python-%{srcname}
Version:        1.1.0
Release:        2%{?dist}
Summary:        WebSockets state-machine based protocol implementation
License:        MIT
URL:            https://github.com/python-hyper/wsproto
Source:         %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{with tests}
%pytest --verbose
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CHANGELOG.rst


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream
- Resolves: rhbz#2058965
- Resolves: rhbz#2049630

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.10

* Fri Feb 05 2021 Carl George <carl@george.computer> - 1.0.0-1
- Latest upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Carl George <carl@george.computer> - 0.14.1-1
- Latest upstream

* Mon Feb 25 2019 Carl George <carl@george.computer> - 0.13.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 14 2018 Carl George <carl@george.computer> - 0.12.0-1
- Initial package
