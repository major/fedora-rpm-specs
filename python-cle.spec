%global pypi_name cle

Name:           python-%{pypi_name}
Version:        9.2.39
Release:        2%{?dist}
Summary:        Python interface for analyzing binary formats

License:        BSD
URL:            https://github.com/angr/cle
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
CLE loads binaries and their associated libraries, resolves imports
and provides an abstraction of process memory the same way as if it was
loader by the OS's loader.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
CLE loads binaries and their associated libraries, resolves imports
and provides an abstraction of process memory the same way as if it was
loader by the OS's loader.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files cle

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 9.2.39-2
- Rebuilt for Python 3.12

* Tue Feb 21 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.39-1
- Update to latest upstream release 9.2.39

* Sat Feb 11 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.38-1
- Update to latest upstream release 9.2.38

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Jonathan Wright <jonathan@almalinux.org> - 9.2.32-1
- Update to 9.2.32 rhbz#1999782

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 9.2.31-1
- Update to 9.2.31

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.9572-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 9.0.9572-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.9572-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.9572-1
- Update to latest upstream release 9.0.9572 (rhbz#1960072)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6885-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 9.0.6885-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6885-1
- Update to latest upstream release 9.0.6885 (#1929356)

* Mon Apr 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6852-1
- Update to latest upstream release 9.0.6852 (#1929356)

* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1929356)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1929356)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1905654)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1905654)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905654)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1905654)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905654)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905654)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905654)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901718)

* Fri Nov 06 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4663-1
- New upstream version

* Thu Oct 08 2020 W. Michael Petullo <mike@flyn.org> - 9.0.4495-1
- New upstream version

* Sat Aug 01 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.27-1
- New upstream version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.20.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 W. Michael Petullo <mike@flyn.org> - 8.20.7.6-1
- New upstream version

* Tue Jun 23 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.8-1
- New upstream version

* Sun Jun 14 2020 W. Michael Petullo <mike@flyn.org> - 8.20.6.1-1
- New upstream version
- Drop upstreamed patch

* Thu May 28 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-2
- Add commentary for patch: upstream merge request

* Mon May 25 2020 W. Michael Petullo <mike@flyn.org> - 8.20.1.7-1
- Initial package
