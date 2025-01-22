Name: libomemo
Version: 0.8.1
Release: 6%{?dist}

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
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 06 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.8.1-1
- Initial SPEC release.
