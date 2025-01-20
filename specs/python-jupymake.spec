# Upstream does not release tarballs.  Instead the code is copied directly
# into the polymake distribution.  Therefore, we check out the code from git.
%global commit  a6987c8bb455c172e80eed7b5b62a7c13bf85815
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20231204

Name:           python-jupymake
Version:        0.9
Release:        34.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Python wrapper for the polymake shell

License:        GPL-2.0-or-later
URL:            https://github.com/polymake/JuPyMake
VCS:            git:%{url}.git
Source:         %{url}/archive/%{commit}/JuPyMake-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libnormaliz-devel
BuildRequires:  polymake
BuildRequires:  python3-devel

# Polymake is not available on 32-bit platforms.
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _description %{expand:
This package provides a basic interface to call polymake from python.
It is meant to be used in the Jupyter interface for polymake.}

%description %_description

%package     -n python3-jupymake
Summary:        Python wrapper for the polymake shell
Requires:       polymake%{?_isa}

%description -n python3-jupymake %_description

%prep
%autosetup -n JuPyMake-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l JuPyMake

%check
%pyproject_check_import

%files -n python3-jupymake -f %{pyproject_files}
%doc README README.md example.py

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-34.20231204.a6987c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 24 2024 Jerry James <loganjerry@gmail.com> - 0.9-33.20231204.a6987c8
- Rebuild for polymake 4.13

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-32.20231204.a6987c8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Jerry James <loganjerry@gmail.com> - 0.9-31.20231204.a6987c8
- Rebuild for polymake 4.12

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.9-30.20231204.a6987c8
- Rebuilt for Python 3.13

* Fri Feb 23 2024 Jerry James <loganjerry@gmail.com> - 0.9-29.20231204.a6987c8
- Switch to new git repository

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-28.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-27.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-26.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9-25.20190509.031cc3a
- Rebuilt for Python 3.12

* Mon Jun 12 2023 Jerry James <loganjerry@gmail.com> - 0.9-24.20190509.031cc3a
- Rebuild for polymake 4.10

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.9-23.20190509.031cc3a
- Dynamically generate BuildRequires.

* Wed Feb  1 2023 Jerry James <loganjerry@gmail.com> - 0.9-23.20190509.031cc3a
- Rebuild for polymake 4.9

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-22.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Jerry James <loganjerry@gmail.com> - 0.9-21.20190509.031cc3a
- Rebuild for polymake 4.8

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.9-20.20190509.031cc3a
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-20.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jerry James <loganjerry@gmail.com> - 0.9-19.20190509.031cc3a
- Rebuild for polymake 4.7
- Do not build on 32-bit platforms due to unavailability of polymake

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9-18.20190509.031cc3a
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-17.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Jerry James <loganjerry@gmail.com> - 0.9-16.20190509.031cc3a
- Rebuild for polymake 4.6

* Thu Oct  7 2021 Jerry James <loganjerry@gmail.com> - 0.9-15.20190509.031cc3a
- Rebuild for polymake 4.5
- Modernize the python macros

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-14.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 0.9-13.20190509.031cc3a
- Rebuild for polymake 4.4

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9-12.20190509.031cc3a
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-11.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 17 2020 Jerry James <loganjerry@gmail.com> - 0.9-10.20190509.031cc3a
- Rebuild for polymake 4.3

* Wed Sep 30 2020 Jerry James <loganjerry@gmail.com> - 0.9-9.20190509.031cc3a
- Rebuild for normaliz 3.8.9

* Mon Sep 28 2020 Jerry James <loganjerry@gmail.com> - 0.9-8.20190509.031cc3a
- Rebuild for polymake 4.2

* Mon Aug 31 2020 Jerry James <loganjerry@gmail.com> - 0.9-7.20190509.031cc3a
- Rebuild for normaliz 3.8.8

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jerry James <loganjerry@gmail.com> - 0.9-5.20190509.031cc3a
- Rebuild for polymake 4.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9-4.20190509.031cc3a
- Rebuilt for Python 3.9

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.9-3.20190509.031cc3a
- Rebuild for polymake 4.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2.20190509.031cc3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 0.9-1.20190509.031cc3a
- Initial RPM
