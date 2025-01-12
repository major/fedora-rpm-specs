%bcond_without compat

%global compat_soname libminizip.so.1

# Compatible with the following minizip-compat version.
%global minizip_ver 1.2.13
# Obsoletes minizip versions less than.
%global minizip_obsoletes 1.3
# Old minizip-ng version before it was renamed to minizip-ng-compat
%global minizip_ng_ver 3.0.7
# Obsolete version of old minizip-ng
%global minizip_ng_obsoletes 3.0.7-5

Name:           minizip-ng
Version:        4.0.8
Release:        %autorelease
Summary:        Minizip-ng contrib in zlib-ng with the latest bug fixes and advanced features

License:        Zlib
URL:            https://github.com/nmoinvaz/%{name}
Source0:        https://github.com/nmoinvaz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libbsd-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libzstd-devel
BuildRequires: xz-devel
BuildRequires: openssl-devel-engine

%description
Minizip-ng zlib-ng contribution that includes:
* AES encryption
* I/O buffering
* PKWARE disk splitting
It also has the latest bug fixes that having been found all over the internet.


%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   zlib-devel

%description devel
Development files for %{name} library.

%if %{with compat}

%package       compat
Summary:       Minizip implementation provided by %{name}
Provides:      minizip = %{minizip_ver}
Provides:      minizip-compat%{?_isa} = %{minizip_ver}
Obsoletes:     minizip-compat < %{minizip_obsoletes}
# We need to Provide and Obsolete the old minizip-ng package before it was rename to minizip-ng-compat
Provides:      minizip-ng = %{minizip_ng_ver}
Obsoletes:     minizip-ng < %{minizip_ng_obsoletes}

# This part is mandatory for the renaming process
# It can be removed in Fedora 42
Provides: minizip <= %{version}-%{release}
Obsoletes: minizip < 3.0.3

%description   compat
minizip-ng is a minizip replacement that provides optimizations for "next generation"
systems.
The %{name}-compat package contains the library that is API and binary
compatible with minizip.

%package       compat-devel
Summary:       Development files for %{name}-compat
Requires:      %{name}-compat%{?_isa} = %{version}-%{release}
Provides:      minizip-compat-devel = %{minizip_ver}
Provides:      minizip-compat-devel%{?_isa} = %{minizip_ver}
Obsoletes:     minizip-compat-devel < %{minizip_obsoletes}
# We need to Provide and Obsolete the old minizip-ng package before it was rename to minizip-ng-compat
Provides:      minizip-ng-devel = %{minizip_ng_ver}
Obsoletes:     minizip-ng-devel < %{minizip_ng_obsoletes}

# This part is mandatory for the renaming process
# It can be removed in Fedora 42
Provides: minizip-devel <= %{version}-%{release}
Obsoletes: minizip-devel < 3.0.3

%description   compat-devel
The %{name}-compat-devel package contains libraries and header files for
developing application that use minizip.

%endif


%prep
%autosetup -p 1 -n %{name}-%{version}


%build

cat <<_EOF_
###########################################################################
#
# Build the default minizip-ng library
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}
%cmake \
  -DMZ_BUILD_TESTS:BOOL=ON \
  -DSKIP_INSTALL_BINARIES:BOOL=ON \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DMZ_FORCE_FETCH_LIBS:BOOL=OFF \
  -DMZ_COMPAT:BOOL=OFF

%cmake_build

%if %{with compat}
cat <<_EOF_
###########################################################################
#
# Build the compat mode library
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}-compat
%cmake \
  -DMZ_BUILD_TESTS:BOOL=ON \
  -DSKIP_INSTALL_BINARIES:BOOL=ON \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DMZ_FORCE_FETCH_LIBS:BOOL=OFF \
  -DMZ_COMPAT:BOOL=ON

%cmake_build
%endif

%install
%global __cmake_builddir %{_vpath_builddir}
%cmake_install

%if %{with compat}
%global __cmake_builddir %{_vpath_builddir}-compat
%cmake_install
%endif


%files
%license LICENSE
%doc README.md
%{_libdir}/libminizip-ng.so.4
%{_libdir}/libminizip-ng.so.4{,.*}


%files devel
%{_libdir}/libminizip-ng.so
%{_libdir}/pkgconfig/minizip-ng.pc
%{_libdir}/cmake/minizip-ng/
%{_includedir}/minizip-ng/mz*.h


# Compat files
%if %{with compat}

%files compat
%{_libdir}/%{compat_soname}
%{_libdir}/libminizip.so.4{,.*}

%files compat-devel
%{_libdir}/libminizip.so
%{_libdir}/pkgconfig/minizip.pc
%{_libdir}/cmake/minizip/
%{_includedir}/minizip/mz*.h
%{_includedir}/minizip/unzip.h
%{_includedir}/minizip/zip.h
%{_includedir}/minizip/ioapi.h

%endif


%changelog
%autochangelog
