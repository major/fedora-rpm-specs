%global forgeurl https://gitlab.com/inkscape/lib2geom
Version:        1.3
%forgemeta

Name:           lib2geom
Release:        %autorelease
Summary:        Easy to use 2D geometry library in C++

License:        LGPL-2.1-only AND MPL-1.1
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  boost-devel
BuildRequires:  gsl-devel
BuildRequires:  double-conversion-devel
BuildRequires:  gtest-devel
BuildRequires:  ragel

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gsl)

%description
2Geom is a C++ 2D geometry library geared towards robust processing of
computational geometry data associated with vector graphics.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -D2GEOM_BUILD_SHARED=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \

%cmake_build

%install
%cmake_install

%check
# skip elliptical-arc-test test on aarch64, ppc64le and s390x
# https://koji.fedoraproject.org/koji/taskinfo?taskID=103958899
# https://gitlab.com/inkscape/lib2geom/-/issues/67
%ifarch x86_64
%ctest
%else
%ctest -E elliptical-arc-test
%endif

%files
%license COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc README.md
%{_libdir}/lib2geom.so.1*

%files devel
%dir %{_includedir}/2geom-*
%{_includedir}/2geom-*/2geom/
%{_libdir}/cmake/2Geom/
%{_libdir}/lib2geom.so
%{_libdir}/pkgconfig/2geom.pc

%changelog
%autochangelog
