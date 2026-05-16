%global commit 74b6fe45751bd60be749bc80766f38745d29ed72
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260209


Name:     stepcode
Version:  0.8.2^%{commitdate}git%{shortcommit}
Release:  %autorelease
Summary:  A generator of C++ and Python to read and write STEP files
License:  BSD-3-Clause
URL:      https://stepcode.github.io/
Source:   https://github.com/stepcode/stepcode/archive/%{commit}/stepcode-%{shortcommit}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc

ExclusiveArch: x86_64
# self-tests fail on all but x86_64 and s390x.  s390x times out.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}
Provides: stepcode-static = %{version}-%{release}

%description
STEPcode (formerly NIST's STEP Class Library) is used with IFC, STEP, and
other standards that utilize the technologies of ISO10303 (STEP). It generates
C++ and Python from EXPRESS (10303-11) schemes. The code is capable of reading
and writing STEP Part 21 exchange files. It also utilizes Parts 22 and 23
(SDAI and its C++ binding).
SC reads ISO10303-11 EXPRESS schemes and generates C++ source code that can
read and write Part 21 files conforming to that schema. In addition to C++, SC
includes experimental support for Python.


%description devel
Development files for STEPCode

%prep
%autosetup -n stepcode-%{commit}


%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DBUILD_STATIC_LIBS=OFF \
    -DSC_ENABLE_TESTING=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON

%cmake_build

%install
%cmake_install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%check
%ctest

%files
%doc README.md
%license COPYING
%{_bindir}/check-express
%{_bindir}/exppp
%{_bindir}/print_attrs
%{_bindir}/print_schemas
%{_bindir}/schema_scanner
%{_mandir}/man1/fedex.1*
%{_libdir}/libexppp.so.0
%{_libdir}/libexppp.so.0.9.1
%{_libdir}/libexpress.so.0
%{_libdir}/libexpress.so.0.9.1
%{_libdir}/libstepcore.so.0
%{_libdir}/libstepcore.so.0.9.1
%{_libdir}/libstepdai.so.0
%{_libdir}/libstepdai.so.0.9.1
%{_libdir}/libstepeditor.so.0
%{_libdir}/libstepeditor.so.0.9.1
%{_libdir}/libsteplazyfile.so.0
%{_libdir}/libsteplazyfile.so.0.9.1
%{_libdir}/libsteputils.so.0
%{_libdir}/libsteputils.so.0.9.1
%{_libdir}/libsdai_*.so.0
%{_libdir}/libsdai_*.so.0.9.1

%files devel
%doc README.md
%license COPYING
%{_bindir}/exp2cxx
%{_bindir}/exp2python
%{_mandir}/man1/exp2cxx.1*
%{_includedir}/schemas/
%{_includedir}/stepcode/
%{_libdir}/libexppp.so
%{_libdir}/libexpress.so
%{_libdir}/libstepcore.so
%{_libdir}/libstepdai.so
%{_libdir}/libstepeditor.so
%{_libdir}/libsteplazyfile.so
%{_libdir}/libsteputils.so
%{_libdir}/libsdai_*.so

%changelog
%autochangelog
