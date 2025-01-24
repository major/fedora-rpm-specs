# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# all packages requiring libindi are now disabled on i686
ExcludeArch:    %{ix86}

# Define boolean to quickly set option and dependencies for
# building QT5 client
%global build_qt5_client 1

# Define boolean to quickly set option and dependencies for
# building with websocket support
# RHEL 10 doesn't have websocketcpp
%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with websocket
%else
%bcond_without websocket
%endif

# Define boolean to quickly set option and dependencies for
# unit tests
%global build_tests 1

Name:       libindi
Version:    2.1.1
Release:    %autorelease
Summary:    Instrument Neutral Distributed Interface

# See COPYRIGHT file for a description of the licenses and files covered
# 'LicenseRef-NASA-FV-License-Agreement' (CFITSIO) headers found in:
# - /libs/fpack/fpack.h
# - /libs/fpack/fpackutil.c
License:    GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later and BSD-3-Clause AND ISC AND MIT AND CFITSIO

URL:        http://www.indilib.org
Source0:    https://github.com/indilib/indi/archive/v%{version}/indi-%{version}.tar.gz

# Fix build with GCC15 / C++23
# https://github.com/indilib/indi/pull/2165
Patch:      fix_gcc15-c++23.patch

BuildRequires: cmake
BuildRequires: libev-devel
BuildRequires: libogg-devel
BuildRequires: libnova-devel
BuildRequires: libtheora-devel
BuildRequires: libXISF-devel
BuildRequires: systemd-rpm-macros

%if 0%{?fedora}
%global system_httplib ON
BuildRequires: cpp-httplib-static
%global system_jsonlib ON
BuildRequires: json-static
%else
%global system_httplib OFF
%global system_jsonlib OFF
%endif

BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(zlib)

%if 0%{?build_qt5_client}
BuildRequires: pkgconfig(Qt5Network)
%global qt5_client ON
%else
%global qt5_client OFF
%endif

%if %{with websocket}
BuildRequires: boost-devel
BuildRequires: websocketpp-devel
%global websocket ON
%else
%global websocket OFF
%endif

%if 0%{?build_tests}
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
%global tests ON
%else
%global tests OFF
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Provides: bundled(fpack) = 1.7.0
Provides: bundled(hidapi)
%if !0%{?fedora}
Provides: bundled(httplib) = 0.12.4
Provides: bundled(json) = 3.10.5
%endif

# These drivers have been migrated here from 3rdparty
Obsoletes:  indi-3rdparty-astrolink4 <= 2.1.0
Provides:   indi-3rdparty-astrolink4 = %{version}

Obsoletes:  indi-3rdparty-astromechfoc <= 2.1.0
Provides:   indi-3rdparty-astromechfoc = %{version}

Obsoletes:  indi-3rdparty-dreamfocuser <= 2.1.0
Provides:   indi-3rdparty-dreamfocuser = %{version}

Obsoletes:  indi-3rdparty-spectracyber <= 2.1.0
Provides:   indi-3rdparty-spectracyber = %{version}

%description
INDI is a distributed control protocol designed to operate
astronomical instrumentation. INDI is small, flexible, easy to parse,
and scalable. It supports common DCS functions such as remote control,
data acquisition, monitoring, and a lot more.


%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-static%{?_isa} = %{version}-%{release}

%description devel
These are the header files needed to develop a %{name} application


%package libs
Summary: INDI shared libraries

%description libs
These are the shared libraries of INDI.


%if 0%{?build_qt5_client}
%package qt
Summary: INDI Qt5 client libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description qt
These are the Qt5 client libraries of INDI.
%endif


%package static
Summary: Static libraries, includes, etc. used to develop an application with %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description static
Static library needed to develop a %{name} application

%prep
%autosetup -p1 -n indi-%{version}

# For Fedora we want to put udev rules in %%{_udevrulesdir}
sed -i 's|/lib/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt
chmod -x drivers/telescope/pmc8driver.h
chmod -x drivers/telescope/pmc8driver.cpp

%if 0%{?fedora}
# Remove bundled httplib-headers and license file
rm -rf libs/httplib
# Remove bundled json library
rm -rf libs/nlohmann
%endif

%build
%cmake \
    -DINDI_BUILD_QT5_CLIENT="%{qt5_client}" \
    -DINDI_BUILD_UNITTESTS="%{tests}" \
    -DINDI_BUILD_WEBSOCKET="%{websocket}" \
    -DINDI_SYSTEM_HTTPLIB="%{system_httplib}" \
    -DINDI_SYSTEM_JSONLIB="%{system_jsonlib}"

%cmake_build

%install
%cmake_install


%check
%if 0%{?build_tests}
%ctest
%endif


%files
%license COPYING.BSD COPYING.GPL COPYING.LGPL COPYRIGHT LICENSE
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/indi_*
%{_bindir}/indiserver
%{_bindir}/shelyak_usis
%{_datadir}/indi
%{_udevrulesdir}/80-dbk21-camera.rules
%{_udevrulesdir}/99-indi_auxiliary.rules

%files libs
%license COPYING.BSD COPYING.GPL COPYING.LGPL COPYRIGHT LICENSE
%if 0%{?build_qt5_client}
%exclude %{_libdir}/libindiclientqt.so.*
%endif
%{_libdir}/%{name}*.so.2
%{_libdir}/%{name}*.so.2.*
%{_libdir}/indi/MathPlugins

%if 0%{?build_qt5_client}
%files qt
%{_libdir}/libindiclientqt.so.2
%{_libdir}/libindiclientqt.so.2.*
%endif

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%{_libdir}/%{name}*.a


%changelog
%autochangelog
