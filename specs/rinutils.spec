%define debug_package %{nil}
%global basen rinutils

Name: %{basen}
Version: 0.10.3
%global basenver %{basen}-%{version}
Release: 3%{dist}
License: MIT
Source:  https://github.com/shlomif/rinutils/releases/download/%{version}/%{basenver}.tar.xz
URL: https://github.com/shlomif/rinutils/
Summary: Shlomi Fish's gnu11 C Library of Random headers
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: perl-devel
BuildRequires: python3

%description
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%package devel
Summary: Shlomi Fish's gnu11 C Library of Random headers (development package)
Provides: %{basen}-static = %{version}-%{release}

%description devel
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%prep
%setup -q -n %{basenver}

%build
%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DWITH_TEST_SUITE=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.asciidoc NEWS.asciidoc
%{_includedir}/%{basen}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/Rinutils/*.cmake

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Shlomi Fish <shlomif@shlomifish.org> 0.10.3-1
- New upstream version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Shlomi Fish <shlomif@shlomifish.org> 0.10.2-1
- New upstream version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 19 2022 Shlomi Fish <shlomif@shlomifish.org> 0.10.1-1
- New upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 07 2021 Shlomi Fish <shlomif@shlomifish.org> 0.10.0-1
- New upstream version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 2020 Shlomi Fish <shlomif@shlomifish.org> 0.6.0-1
- New upstream version

* Fri Jul 31 2020 Shlomi Fish <shlomif@shlomifish.org> 0.4.1-1
- New upstream version&use cmake macros.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 28 2020 Shlomi Fish <shlomif@shlomifish.org> - 0.4.0-1
- New upstream version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Shlomi Fish <shlomif@shlomifish.org> - 0.1.4-1
- Initial package.

