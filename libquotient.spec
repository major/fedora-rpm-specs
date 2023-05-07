%global appname Quotient
%global libname lib%{appname}

Name: libquotient
Version: 0.7.1
Release: 2%{?dist}

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild
