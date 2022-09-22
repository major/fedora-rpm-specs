# Define boolean to quickly set option and dependencies for
# building QT5 client
%global build_qt5_client 1

# Define boolean to quickly set option and dependencies for
# unit tests
# s390x test fail https://github.com/indilib/indi/issues/1359
%ifarch s390x
%global build_tests 0
%else
%global build_tests 1
%endif

Name:       libindi
Version:    1.9.7
Release:    %autorelease
Summary:    Instrument Neutral Distributed Interface

License:    LGPLv2+ and GPLv2+
# See COPYRIGHT file for a description of the licenses and files covered

URL:        http://www.indilib.org
Source0:    https://github.com/indilib/indi/archive/v%{version}/indi-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: libev-devel
BuildRequires: libogg-devel
BuildRequires: libnova-devel
BuildRequires: libtheora-devel
BuildRequires: systemd

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

%if 0%{?build_tests}
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gmock)
%global tests ON
%else
%global tests OFF
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

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

%build
%cmake \
    -DINDI_BUILD_QT5_CLIENT="%{qt5_client}" \
    -DINDI_BUILD_UNITTESTS="%{tests}"

%cmake_build

%install
%cmake_install


%check
%if 0%{?build_tests}
%ctest --test-dir test
%endif


%files
%license COPYING.BSD COPYING.GPL COPYING.LGPL COPYRIGHT LICENSE
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/indi
%{_udevrulesdir}/*.rules

%files libs
%license COPYING.BSD COPYING.GPL COPYING.LGPL COPYRIGHT LICENSE
%{_libdir}/*.so.*
%{_libdir}/indi/MathPlugins

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files static
%{_libdir}/*.a

%changelog
%autochangelog
