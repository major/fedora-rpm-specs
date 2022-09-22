%global _hardened_build 1
%bcond_without build_lib

Name:       ddcutil
Version:    0.9.9
Release:    %autorelease
Summary:    Query and update monitor settings
License:    GPLv2+
URL:        http://www.ddcutil.com
Source0:    http://www.ddcutil.com/tarballs/%{name}-%{version}.tar.gz

# Excluding arch s390/s390x due to i2c-tools does so
ExcludeArch:    s390 s390x

BuildRequires:      automake
BuildRequires:      gcc
BuildRequires:      make
BuildRequires:      pkgconfig(glib-2.0)   >= 2.32
BuildRequires:      pkgconfig(libusb-1.0) >= 1.0.15
BuildRequires:      pkgconfig(systemd)
BuildRequires:      pkgconfig(libudev)
BuildRequires:      pkgconfig(xrandr)
BuildRequires:      pkgconfig(libdrm) >= 2.4.16

Requires:   hwdata
Requires:   i2c-tools

# file that may be used at runtime
Recommends: /usr/bin/lsusb
Recommends: /usr/bin/modprobe
Recommends: pkg-config
Recommends: /usr/bin/lscpu
Recommends: /usr/bin/lsb_release
Recommends: xrandr

%description
Query and change monitor settings

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.  In general, anything that can be controlled using a monitor's
on-screen display can be controlled by this program.  Examples include 
changing a monitor's input source and adjusting its brightness.

# libddcutil can be installed separately
%if %{with build_lib}
%package -n libddcutil
Summary:        Shared library to query and update monitor settings

%description -n libddcutil
Shared library version of ddcutil, exposing a C API.

%package -n libddcutil-devel
Summary:        Development files for libddcutil
# FindDDCUtils.cmake has BSD license header
License:        GPLv2+ and BSD
Requires:       libddcutil%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}

%description -n libddcutil-devel
Development files for libddcutil
%endif

%prep
%setup -q
chmod -x ChangeLog NEWS.md

%build
%configure \
%if %{with build_lib}
    --enable-lib=yes
%else
    --enable-lib=no
%endif
%make_build

%install
%make_install

%files
%doc NEWS.md README.md AUTHORS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*


%if %{with build_lib}
%files -n libddcutil
%doc NEWS.md README.md AUTHORS ChangeLog
%license COPYING
%{_libdir}/lib%{name}.so.3*

%files -n libddcutil-devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}*.h
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%endif

%changelog
%autochangelog
