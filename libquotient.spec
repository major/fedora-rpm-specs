%global appname Quotient
%global libname lib%{appname}

Name: libquotient
Version: 0.7.1
Release: 1%{?dist}

License: LGPL-2.1-or-later
URL: https://github.com/quotient-im/%{libname}
Summary: Qt5 library to write cross-platform clients for Matrix
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(QtOlm)
BuildRequires: pkgconfig(openssl)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
The Quotient project aims to produce a Qt5-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: cmake(Olm)
Requires: cmake(Qt5Sql)
Requires: cmake(QtOlm)
Requires: pkgconfig(openssl)

%description devel
%{summary}.

%prep
%autosetup -n %{libname}-%{version}
rm -rf 3rdparty

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DQuotient_ENABLE_E2EE:BOOL=ON \
    -DQuotient_INSTALL_TESTS:BOOL=OFF \
    -DQuotient_INSTALL_EXAMPLE:BOOL=OFF
%cmake_build

%check
%ctest --exclude-regex 'testolmaccount|testkeyverification'

%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/ndk-modules

%files
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{libname}.so.0*

%files devel
%{_includedir}/%{appname}/
%{_libdir}/cmake/%{appname}/
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/%{libname}.so

%changelog
* Tue Jan 10 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.1-1
- Updated to version 0.7.1.

* Tue Dec 20 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-1
- Updated to version 0.7.0.
- Enabled E2EE support.
- Switched to SPDX license tag.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 30 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.11-3
- Rebuilt to mitigate GCC 12 regressions.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.11-1
- Updated to version 0.6.11.

* Mon Oct 04 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.10-1
- Updated to version 0.6.10.

* Mon Sep 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.9-1
- Updated to version 0.6.9.

* Wed Aug 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.8-1
- Updated to version 0.6.8.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.7-1
- Updated to version 0.6.7.

* Thu Mar 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.6-1
- Updated to version 0.6.6.

* Mon Feb 22 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.5-1
- Updated to version 0.6.5.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.4-1
- Updated to version 0.6.4.

* Sun Dec 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.3-2
- Disabled E2EE support due to lots of crashes.

* Fri Dec 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.3-1
- Updated to version 0.6.3.

* Sat Oct 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-1
- Updated to version 0.6.2.

* Sat Sep 05 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Wed Jul 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Sat Mar 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.4.20200207git9bcf0cb
- Updated to latest Git snapshot.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20200121gite3a5b3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.2.20200121gite3a5b3a
- Updated to version 0.6.0-git.
