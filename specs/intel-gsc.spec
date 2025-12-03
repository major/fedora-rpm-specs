%global short_name igsc

Name:    intel-gsc
Version: 0.9.5
Release: %autorelease
Summary: Intel Graphics System Controller Firmware Update Library (IGSC FUL)

License: Apache-2.0
URL:     https://github.com/intel/igsc
Source0: %{url}/archive/V%{version}/%{short_name}-%{version}.tar.gz
Patch0:  dont_hardcode_libdir.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  systemd-devel
BuildRequires:  intel-metee-devel >= 5.0.0

# Upstream only supports x86_64
ExclusiveArch:  x86_64

%description
The Intel Graphics System Firmware Update Library (IGSC FUL) is
a pure C low level library that exposes a required API
to perform a firmware update of a particular Intel discrete
graphics device. The library utilized a cross platform library metee_ in
order to access the GSC (mei) device. GSC device is an extension of the
Intel discrete graphics device (dGFX).

The library can update GSC firmware itself, and as well as OPROM VBT
and the code (VBIOS, GOP).

The library provides retrieval of identity and version information from
both graphic device and supplied firmware or OPROM image as well as
function for firmware update of those images to the device.

Summary:        Intel Graphics System Controller Firmware Update Library (IGSC FUL)
Requires:       intel-metee >= 5.0.0

%package        devel
Summary:        Development headers for igsc
Requires:       intel-gsc = %{version}-%{release}
Requires:       intel-metee-devel >= 5.0.0

%description    devel
The Intel Graphics System Firmware Update Library (IGSC FUL) is
a pure C low level library that exposes a required API
to perform a firmware update of a particular Intel discrete
graphics device. The library utilized a cross platform library metee_ in
order to access the GSC (mei) device. GSC device is an extension of the
Intel discrete graphics device (dGFX).

The library can update GSC firmware itself, and as well as OPROM VBT
and the code (VBIOS, GOP).

The library provides retrieval of identity and version information from
both graphic device and supplied firmware or OPROM image as well as
function for firmware update of those images to the device.

%prep
%autosetup -p1 -n %{short_name}-%{version}

%build
%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DENABLE_DOCS=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_bindir}/igsc
%{_libdir}/libigsc.so.%{version}
%{_libdir}/libigsc.so.0

%files devel
%{_libdir}/libigsc.so
%{_libdir}/cmake/igsc/
%{_includedir}/igsc_lib.h
%{_docdir}/%{short_name}
%{_mandir}/man3/*

%changelog
%autochangelog
