%global pypi_name archinfo

Name:           python-%{pypi_name}
Version:        9.2.136
Release:        2%{?dist}
Summary:        Collection of classes that contain architecture-specific information

License:        LicenseRef-Callaway-BSD
URL:            https://github.com/angr/archinfo
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
archinfo is a collection of classes that contain architecture-specific
information. It is useful for cross-architecture tools.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.136-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.136-1
- Update to latest upstream release (closes rhbz#2336199)

* Wed Jan 01 2025 W. Michael Petullo <mike@flyn.org> - 9.2.135-1
- Update to latest upstream release (closes rhbz#2331808)

* Fri Nov 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.130-1
- Update to latest upstream release (closes rhbz#2327327)

* Wed Nov 13 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.128-1
- Update to latest upstream release (closes rhbz#2323901)

* Tue Oct 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.126-1
- Update to latest upstream release (closes rhbz#2322509)

* Sat Oct 26 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.125-1
- Update to latest upstream release (closes rhbz#2321110)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.124-1
- Update to latest upstream release (closes rhbz#2321110)

* Wed Oct 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.123-1
- Update to latest upstream release (closes rhbz#2318836)

* Tue Oct 08 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.122-1
- Update to latest upstream release (closes rhbz#2317136)

* Tue Oct 01 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.120-1
- Update to latest upstream release (closes rhbz#2315977)

* Thu Sep 26 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.119-1
- Update to new upstream version (closes rhbz#2314473)

* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.118-1
- Update to new upstream version (closes rhbz#2312979)

* Tue Sep 17 2024 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.117-1
- Update to new upstream version (closes rhbz#2174147)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 9.2.39-8
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 9.2.39-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 9.2.39-2
- Rebuilt for Python 3.12

* Tue Feb 21 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.39-1
- Update to latest upstream release 9.2.39

* Sat Feb 11 2023 Fabian Affolter <mail@fabian-affolter.ch> - 9.2.38-1
- Update to latest upstream release 9.2.38 (closes rhbz#1999769)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.9572-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.9572-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 9.0.9572-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.9572-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.9572-1
- Update to latest upstream release 9.0.9572 (rhbz#1960062)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6885-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 9.0.6885-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6885-1
- Update to latest upstream release 9.0.6885 (#1931981)

* Mon Apr 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6852-1
- Update to latest upstream release 9.0.6852 (#1931981)

* Tue Mar 02 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.6136-1
- Update to latest upstream release 9.0.6136 (#1931981)

* Tue Feb 16 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5903-1
- Update to latest upstream release 9.0.5903 (#1920601)

* Fri Feb 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5811-1
- Update to latest upstream release 9.0.5811 (#1920601)

* Tue Feb 09 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5739-1
- Update to latest upstream release 9.0.5739 (#1920601)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.5450-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5450-1
- Update to latest upstream release 9.0.5450 (#1905651)

* Fri Jan 08 2021 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5327-1
- Update to latest upstream release 9.0.5327 (#1905651)

* Sun Dec 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5171-1
- Update to latest upstream release 9.0.5171 (#1905651)

* Fri Dec 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5034-1
- Update to new upstream release 9.0.5034 (#1905651)

* Wed Dec 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.5002-1
- Update to new upstream release 9.0.5002 (#1905651)

* Wed Nov 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4885-1
- Update to new upstream release 9.0.4885 (#1901694)

* Thu Oct 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4663-1
- Update to new upstream release 9.0.4663 (#1891946)

* Fri Oct 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4495-1
- Update to new upstream release 9.0.4495 (#1880178)

* Fri Sep 25 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4446-1
- Update to new upstream release 9.0.4446 (#1880178)

* Wed Sep 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 9.0.4378-1
- Update to new upstream release 9.0.4378 (#1880178)

* Tue Jul 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.27-1
- Update to new upstream release 8.20.7.27 (#1858194)

* Fri Jul 17 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.7.6-1
- Update to new upstream release 8.20.7.6 (#1858194)

* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.8-1
- Update to latest upstream release 8.20.6.8

* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.6.1-1
- Update to new upstream release 8.20.6.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 8.20.1.7-2
- Rebuilt for Python 3.9

* Fri Feb 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 8.20.1.7-1
- Initial package for Fedora
