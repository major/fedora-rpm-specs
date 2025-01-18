%bcond qt5 1
%bcond qt6 1

%global appname FutureSQL
%global qt5_build_dir release-qt5
%global qt6_build_dir release-qt6
%global _description %{expand:
FutureSQL was in part inspired by Diesel, and provides a higher level of
abstraction than QtSql. Its features include non-blocking database access by
default, relatively boilerplate-free queries, automatic database migrations
and simple mapping to objects.  In order to make FutureSQL's use of templates
less confusing, FutureSQL uses C++20 concepts, and requires a C++20 compiler.}

Name:    futuresql
Version: 0.1.1
Release: 5%{?dist}
License: (LGPL-2.1-only OR LGPL-3.0-only) AND BSD-2-Clause
Summary: Non-blocking database framework for Qt
URL:     https://invent.kde.org/libraries/futuresql/
Source0: https://download.kde.org/stable/futuresql/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: ninja-build
%if %{with qt5}
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(QCoro5Core)
%endif
%if %{with qt6}
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(QCoro6Core)
%endif


%description %_description

%if %{with qt5}
%package qt5
Summary: Non-blocking database framework for Qt 5
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name} < %{?epoch:%{epoch}:}%{version}-%{release}

%package qt5-devel
Summary: Development files for %{appname} (Qt 5 version)
Requires: %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Provides: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}

%description qt5 %_description
%description qt5-devel %_description
%endif

%if %{with qt6}
%package qt6
Summary: Non-blocking database framework for Qt 6

%package qt6-devel
Summary: Development files for %{appname} (Qt 6 version)
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}

%description qt6 %_description
%description qt6-devel %_description
%endif

%prep
%autosetup -p1

%build
%if %{with qt5}
mkdir %{qt5_build_dir} && pushd %{qt5_build_dir}
%cmake -G Ninja \
    -S .. \
    -DBUILD_WITH_QT6:BOOL=OFF \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DBUILD_TESTING:BOOL=ON
%cmake_build
popd
%endif

%if %{with qt6}
mkdir %{qt6_build_dir} && pushd %{qt6_build_dir}
%cmake -G Ninja \
    -S .. \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON
%cmake_build
popd
%endif

%install
%if %{with qt5}
pushd %{qt5_build_dir}
%cmake_install
popd
%endif

%if %{with qt6}
pushd %{qt6_build_dir}
%cmake_install
popd
%endif

%check
%if %{with qt5}
pushd %{qt5_build_dir}
%ctest --timeout 3600
popd
%endif

%if %{with qt6}
pushd %{qt6_build_dir}
%ctest --timeout 3600
popd
%endif

%if %{with qt5}
%files qt5
%doc README.md
%license LICENSES/*
%{_libdir}/lib%{name}5.so.0*

%files qt5-devel
%{_includedir}/%{appname}5/
%{_libdir}/cmake/%{appname}5/
%{_libdir}/lib%{name}5.so
%endif

%if %{with qt6}
%files qt6
%doc README.md
%license LICENSES/*
%{_libdir}/lib%{name}6.so.0*

%files qt6-devel
%{_includedir}/%{appname}6/
%{_libdir}/cmake/%{appname}6/
%{_libdir}/lib%{name}6.so
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 09 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.1-1
- Initial release
