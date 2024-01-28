%global common_description %{expand:
Curio is a library of building blocks for performing concurrent I/O and common
system programming tasks such as launching subprocesses, working with files,
and farming work out to thread and process pools.  It uses Python coroutines
and the explicit async/await syntax introduced in Python 3.5.  Its programming
model is based on cooperative multitasking and existing programming
abstractions such as threads, sockets, files, subprocesses, locks, and queues.
You'll find it to be small, fast, and fun.  Curio has no third-party
dependencies and does not use the standard asyncio module.  Most users will
probably find it to be a bit too-low level--it's probably best to think of it
as a library for building libraries.  Although you might not use it directly,
many of its ideas have influenced other libraries with similar functionality.}


Name:           python-curio
Version:        1.6
Release:        7%{?dist}
Summary:        Building blocks for performing concurrent I/O
License:        BSD
URL:            https://github.com/dabeaz/curio
Source:         %{pypi_source curio}
# https://github.com/dabeaz/curio/issues/361
Patch:          0001-Python-3.12-compatibility.patch
BuildArch:      noarch


%description %{common_description}


%package -n python3-curio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}


%description -n python3-curio %{common_description}


%prep
%autosetup -n curio-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files curio


%check
%pytest --verbose -m 'not internet'


%files -n python3-curio -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Carl George <carl@george.computer> - 1.6-5
- Add patch for Python 3.12 compatibility, resolves rhbz#2174408

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Carl George <carl@george.computer> - 1.6-1
- Update to 1.6, resolves rhbz#2137578

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5-6
- Rebuilt for Python 3.11

* Thu Jan 27 2022 Carl George <carl@george.computer> - 1.5-5
- Convert to pyproject macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 1.5-1
- Update to 1.5 (rhbz#1821534)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 05 2020 Yatin Karel <ykarel@redhat.com> - 1.4-1
- Update to 1.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Carl George <carl@george.computer> - 1.1-1
- Latest upstream
- Add patch0 to skip tests that require internet

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Carl George <carl@george.computer> - 0.9-1
- Initial package
