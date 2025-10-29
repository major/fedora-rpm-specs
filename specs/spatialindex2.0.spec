Name:      spatialindex2.0
Version:   2.0.0
Release:   1%{?dist}
%global so_version 7
Summary:   Spatial index 2.0 compatibility library

License:   MIT
URL:       https://libspatialindex.org
Source:    https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2

# Support testing with a system/external copy of GTest
# https://github.com/libspatialindex/libspatialindex/pull/270
Patch:          https://github.com/libspatialindex/libspatialindex/pull/270.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(GTest)

%description
Spatialindex 2.0 compatibility library.


%package devel
Summary: Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Conflicts: spatialindex-devel

%description devel
Development files for %{name}.


%prep
%autosetup -n spatialindex-src-%{version} -p1
# Remove bundled gtest:
rm -rv test/gtest/gtest-*


%conf
# Since https://src.fedoraproject.org/rpms/cmake/pull-request/45 in Fedora 43,
# the expansion of %%cmake no longer overrides INCLUDE_INSTALL_DIR and
# LIB_INSTALL_DIR, which don’t mean exactly the same thing here as they do in
# whatever historical convention %%cmake was trying to support. See discussion
# in https://github.com/libspatialindex/libspatialindex/issues/271. However, we
# retain the workaround of undefining them in case this version of the spec
# file is branched to EPEL10.
#
# GTest >=1.13 requires C++14 (-DCMAKE_CXX_STANDARD=14).
%cmake \
    -DBUILD_TESTING:BOOL=ON \
    -DSYSTEM_GTEST:BOOL=ON \
    -UINCLUDE_INSTALL_DIR -ULIB_INSTALL_DIR \
    -DCMAKE_CXX_STANDARD=14


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license COPYING
%doc AUTHORS ChangeLog CITATION.cff

%{_libdir}/libspatialindex{,_c}.so.%{so_version}{,.*}


%files devel
%{_includedir}/spatialindex/
%{_libdir}/libspatialindex{,_c}.so
%{_libdir}/cmake/libspatialindex/
%{_libdir}/pkgconfig/libspatialindex.pc


%changelog
* Sun Oct 26 2025 Sandro Mani <manisandro@gmail.com> - 2.0-1
- 2.0 compat package
