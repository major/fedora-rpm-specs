Name: libomemo
Version: 0.8.1
Release: 1%{?dist}

License: MIT
Summary: OMEMO implementation in plain C
URL: https://github.com/gkdr/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(mxml)
BuildRequires: pkgconfig(sqlite3)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: ninja-build

%description
Implements OMEMO (XEP-0384) in plain C.

Input and output are XML strings, so it does not force you to use a certain
XML lib. While the actual protocol functions do not depend on any kind of
storage, it comes with a basic implementation in SQLite.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DOMEMO_INSTALL:BOOL=ON \
    -DOMEMO_WITH_TESTS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Feb 06 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.1-1
- Initial SPEC release.
