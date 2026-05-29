#global commit 2e95c9001bf1ad0177c54923029ed8f4c53b70e0
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?rhel}
# Qt5 only up to 9, and Qt6 in 9+
%if %{rhel} >= 10
%bcond_with	qt5
%else
%bcond_without	qt5
%endif
%if %{rhel} >= 9
%bcond_without	qt6
%else
%bcond_with	qt6
%endif
%bcond_with     mingw
%else
# Fedora - build everything
%bcond_without  qt5
%bcond_without  qt6
%bcond_with  mingw
%endif

%bcond_without test


Name:           quazip
Version:        1.7.0
Release:        %autorelease
Summary:        Qt/C++ wrapper for the minizip library

# Following files are zlib licensed:
#  - quazip/unzip.c
#  - quazip/unzip.h
#  - quazip/zip.c
#  - quazip/zip.h
# Rest is LGPLv2 with a static linking exception, see COPYING
License:        (LGPL-2.1-or-later WITH Qwt-exception-1.0) AND Zlib
URL:            https://github.com/stachenov/quazip
%if 0%{?commit:1}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
%endif
# Fix qt6 build
Patch1:         quazip_build.patch
# Fix use in qt5 applications (Qt5 does not have QStringConverter)
Patch0:         quazip_qt5.patch

BuildRequires:  cmake
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  zlib-devel
%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libzip

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libzip
%endif


%description
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package (AKA Minizip)
using Qt library.


%if %{with qt5}
%package qt5
Summary: Qt5 wrapper for the minizip library
BuildRequires:  qt5-qtbase-devel

%description qt5
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package (AKA Minizip)
using Qt library.


%package qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       bzip2-devel%{?_isa}
Requires:       qt5-qtbase-devel%{?_isa}
Requires:       zlib-devel%{?_isa}

%description qt5-devel
The %{name}-qt5-devel package contains libraries, header files and documentation
for developing applications that use %{name}-qt5.


%if %{with mingw}
%package -n mingw32-%{name}-qt5
Summary:       MinGW Windows Qt5 %{name} library
BuildRequires: mingw32-qt5-qtbase

%description -n mingw32-%{name}-qt5
MinGW Windows Qt5 %{name} library.


%package -n mingw64-%{name}-qt5
Summary:       MinGW Windows Qt5 %{name} library
BuildRequires: mingw64-qt5-qtbase

%description -n mingw64-%{name}-qt5
MinGW Windows Qt5 %{name} library.
%endif
%endif


%if %{with qt6}
%package qt6
Summary: Qt6 wrapper for the minizip library
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel

%description qt6
QuaZip is the C++ wrapper for Gilles Vollant's ZIP/UNZIP package (AKA Minizip)
using Qt library.


%package qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       bzip2-devel%{?_isa}
Requires:       qt6-qtbase-devel%{?_isa}
Requires:       qt6-qt5compat-devel%{?_isa}
Requires:       zlib-devel%{?_isa}

%description qt6-devel
The %{name}-qt6-devel package contains libraries, header files and documentation
for developing applications that use %{name}-qt6.


%if %{with mingw}
%package -n mingw32-%{name}-qt6
Summary:       MinGW Windows Qt6 %{name} library
BuildRequires: mingw32-qt6-qtbase
BuildRequires: mingw32-qt6-qt5compat

%description -n mingw32-%{name}-qt6
MinGW Windows Qt6 %{name} library.


%package -n mingw64-%{name}-qt6
Summary:       MinGW Windows Qt6 %{name} library
BuildRequires: mingw64-qt6-qtbase
BuildRequires: mingw64-qt6-qt5compat

%description -n mingw64-%{name}-qt6
MinGW Windows Qt6 %{name} library.
%endif
%endif

%if %{with mingw}
%{?mingw_debug_package}
%endif


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-%{version}
%endif


%build
%if %{with mingw}
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%endif

%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake -DQUAZIP_QT_MAJOR_VERSION=5 -DQUAZIP_ENABLE_TESTS=ON
%cmake_build

%if %{with mingw}
mkdir build_qt5
pushd build_qt5
(
%mingw_cmake -DQUAZIP_QT_MAJOR_VERSION=5 -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make_build
)
popd
%endif
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake -DQUAZIP_QT_MAJOR_VERSION=6 -DQUAZIP_ENABLE_TESTS=ON
%cmake_build

%if %{with mingw}
mkdir build_qt6
pushd build_qt6
(
%mingw_cmake -DQUAZIP_QT_MAJOR_VERSION=6 -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make_build
)
popd
%endif
%endif

doxygen Doxyfile
for file in doc/html/*; do touch -r Doxyfile $file; done


%install
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake_install

%if %{with mingw}
pushd build_qt5
%mingw_make_install
popd
%endif
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake_install

%if %{with mingw}
pushd build_qt6
%mingw_make_install
popd
%endif
%endif

%if %{with mingw}
%mingw_debug_install_post
%endif



%if %{with test}
# Qt4 uses the locale rather than libicu to determine file name encoding.
# Thus we need to force a UTF-8 locale, otherwise the tests will fail
# under Qt4.
# https://github.com/stachenov/quazip/issues/127
export LC_ALL=C.UTF-8

# In some emulated environments (such as the s390x mock chroot emulated
# on x86_64) the regexp JIT is broken, so turn it off to avoid incorrect
# test failures.
export QT_ENABLE_REGEXP_JIT=0

%check
%if %{with qt5}
%global _vpath_builddir build-qt5
%ctest
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%ctest
%endif
%endif


%if %{with qt5}
%files qt5
%doc NEWS.txt README.md
%license COPYING
%{_libdir}/libquazip1-qt5.so.1.7
%{_libdir}/libquazip1-qt5.so.1.7.0

%files qt5-devel
%doc doc/html
%{_includedir}/QuaZip-Qt5-%{version}/
%{_libdir}/libquazip1-qt5.so
%{_libdir}/cmake/QuaZip-Qt5-%{version}/
%{_libdir}/pkgconfig/quazip1-qt5.pc

%if %{with mingw}
%files -n mingw32-%{name}-qt5
%license COPYING
%{mingw32_bindir}/libquazip1-qt5.dll
%{mingw32_includedir}/QuaZip-Qt5-%{version}/
%{mingw32_libdir}/libquazip1-qt5.dll.a
%{mingw32_libdir}/pkgconfig/quazip1-qt5.pc
%{mingw32_libdir}/cmake/QuaZip-Qt5-%{version}/

%files -n mingw64-%{name}-qt5
%license COPYING
%{mingw64_bindir}/libquazip1-qt5.dll
%{mingw64_includedir}/QuaZip-Qt5-%{version}/
%{mingw64_libdir}/libquazip1-qt5.dll.a
%{mingw64_libdir}/pkgconfig/quazip1-qt5.pc
%{mingw64_libdir}/cmake/QuaZip-Qt5-%{version}/
%endif
%endif

%if %{with qt6}
%files qt6
%doc NEWS.txt README.md
%license COPYING
%{_libdir}/libquazip1-qt6.so.1.7
%{_libdir}/libquazip1-qt6.so.1.7.0

%files qt6-devel
%doc doc/html
%{_includedir}/QuaZip-Qt6-%{version}/
%{_libdir}/libquazip1-qt6.so
%{_libdir}/cmake/QuaZip-Qt6-%{version}/
%{_libdir}/pkgconfig/quazip1-qt6.pc

%if %{with mingw}
%files -n mingw32-%{name}-qt6
%license COPYING
%{mingw32_bindir}/libquazip1-qt6.dll
%{mingw32_includedir}/QuaZip-Qt6-%{version}/
%{mingw32_libdir}/libquazip1-qt6.dll.a
%{mingw32_libdir}/pkgconfig/quazip1-qt6.pc
%{mingw32_libdir}/cmake/QuaZip-Qt6-%{version}/

%files -n mingw64-%{name}-qt6
%license COPYING
%{mingw64_bindir}/libquazip1-qt6.dll
%{mingw64_includedir}/QuaZip-Qt6-%{version}/
%{mingw64_libdir}/libquazip1-qt6.dll.a
%{mingw64_libdir}/pkgconfig/quazip1-qt6.pc
%{mingw64_libdir}/cmake/QuaZip-Qt6-%{version}/
%endif
%endif


%changelog
%autochangelog
