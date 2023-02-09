%global commit0 8e14a663281d2c0898e2da5d07144c844c6b680a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20220526

Name: axc
Version: 0.3.7
Release: 1.%{date}git%{shortcommit0}%{?dist}

License: GPL-3.0-or-later
Summary: Client library for libsignal-protocol-c
URL: https://github.com/gkdr/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libsignal-protocol-c)
BuildRequires: pkgconfig(sqlite3)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: ninja-build

%description
Client library for libsignal-protocol-c, implementing the needed database
and crypto interfaces using SQLite and gcrypt. Initially, the
libsignal-protocol-c project was named libaxolotl, hence the name axc.

Additionally it provides utility functions for common use cases like
encrypting and decrypting, ultimately making direct use of
libsignal-protocol-c unnecessary.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DAXC_INSTALL:BOOL=ON \
    -DAXC_WITH_PTHREADS:BOOL=ON \
    -DAXC_WITH_TESTS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Mon Feb 06 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.7-1.20220526git8e14a66
- Initial SPEC release.
