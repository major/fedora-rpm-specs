%global common_description %{expand:
The Trio project's goal is to produce a production-quality, permissively
licensed, async/await-native I/O library for Python.  Like all async libraries,
its main purpose is to help you write programs that do multiple things at the
same time with parallelized I/O.  A web spider that wants to fetch lots of
pages in parallel, a web server that needs to juggle lots of downloads and
websocket connections at the same time, a process supervisor monitoring
multiple subprocesses... that sort of thing.  Compared to other libraries, Trio
attempts to distinguish itself with an obsessive focus on usability and
correctness.  Concurrency is complicated; we try to make it easy to get things
right.}


Name:           python-trio
Version:        0.22.0
Release:        4%{?dist}
Summary:        A friendly Python library for async concurrency and I/O
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/trio
Source:         %pypi_source trio

# remove async_generator as dependency
# https://github.com/python-trio/trio/pull/2478
# trivially removed test-requirements.in changes (file missing in sdist)
Patch:          2478.patch

BuildArch:      noarch


%description %{common_description}


%package -n python3-trio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%description -n python3-trio %{common_description}


%prep
%autosetup -p 1 -n trio-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files trio


%check
# TODO investigate test_nursery_cancel_doesnt_create_cyclic_garbage failure
%pytest trio/_core/tests -k "not test_nursery_cancel_doesnt_create_cyclic_garbage"


%files -n python3-trio -f %{pyproject_files}
%doc README.rst


%changelog
* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 0.22.0-4
- Rebuilt for Python 3.12

* Sat Jul 01 2023 Miro Hrončok <mhroncok@redhat.com> - 0.22.0-3
- Remove async_generator as dependency

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Carl George <carl@george.computer> - 0.22.0-1
- Update to 0.22.0, resolves rhbz#2094511

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.20.0-4
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Miro Hrončok <mhroncok@redhat.com> - 0.20.0-3
- Add fix for Python 3.11
- Fixes: rhbz#2049632

* Thu Mar 03 2022 Carl George <carl@george.computer> - 0.20.0-1
- Latest upstream rhbz#2056578

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 24 2021 Carl George <carl@george.computer> - 0.19.0-1
- Latest upstream rhbz#1972135

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18.0^20210519gitd883dbe-4
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18.0^20210519gitd883dbe-3
- Bootstrap for Python 3.10

* Mon May 17 2021 Tomas Hrnciar <thrnciar@redhat.com> - 0.18.0-2
- Backport upstream fixes to bring compatibility with Python 3.10

* Tue Feb 09 2021 Joel Capitao <jcapitao@redhat.com> - 0.18.0-1
- Latest upstream rhbz#1879061

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 06 2020 Carl George <carl@george.computer> - 0.16.0-1
- Latest upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Carl George <carl@george.computer> - 0.15.1-1
- Latest upstream rhbz#1828266

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Carl George <carl@george.computer> - 0.13.0-1
- Latest upstream rhbz#1742425

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Carl George <carl@george.computer> - 0.11.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Carl George <carl@george.computer> - 0.7.0-1
- Initial package
