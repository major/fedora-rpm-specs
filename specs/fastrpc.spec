Name:		fastrpc
Version:	1.0.7
Release:	%autorelease
Summary:	Qualcomm FastRPC and library

License:	BSD-3-Clause
URL:		https://github.com/qualcomm/fastrpc
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/qualcomm/fastrpc/pull/372
Patch0:		372.patch

ExclusiveArch:	%{arm64}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	pkgconfig(yaml-0.1)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	systemd-rpm-macros

%description
FastRPC is Qualcomm's userspace library that facilitates efficient remote
procedure calls between the CPU and DSP for high-performance computing.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package	services
Summary:	Daemons for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Suggests:	hexagon-dsp-binaries

%description	services
This package contains daemons and systemd files for %{name}.

%prep
%autosetup -p1

# disable the test application
# https://github.com/qualcomm/fastrpc/issues/235
sed -e 's/SUBDIRS = inc src test files/SUBDIRS = inc src files/' -i Makefile.am

%conf
autoreconf -fiv
%configure --with-config-base-dir=/usr/share/hexagon-dsp

%build
%make_build

%install
%make_install

%post services
%systemd_post adsprpcd.service adsprpcd_audiopd.service
%systemd_post cdsp1rpcd.service cdsprpcd.service
%systemd_post gdsp0rpcd.service gdsp1rpcd.service
%systemd_post sdsprpcd.service

%preun services
%systemd_preun adsprpcd.service adsprpcd_audiopd.service
%systemd_preun cdsp1rpcd.service cdsprpcd.service
%systemd_preun gdsp0rpcd.service gdsp1rpcd.service
%systemd_preun sdsprpcd.service

%postun services
%systemd_postun_with_restart adsprpcd.service adsprpcd_audiopd.service
%systemd_postun_with_restart cdsp1rpcd.service cdsprpcd.service
%systemd_postun_with_restart gdsp0rpcd.service gdsp1rpcd.service
%systemd_postun sdsprpcd.service

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libadsprpc.so.*
%{_libdir}/libadsp_default_listener.so.*
%{_libdir}/libcdsp_default_listener.so.*
%{_libdir}/libcdsprpc.so.*
%{_libdir}/libsdsp_default_listener.so.*
%{_libdir}/libsdsprpc.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libadsp_default_listener.so
%{_libdir}/libadsprpc.so
%{_libdir}/libcdsp_default_listener.so
%{_libdir}/libcdsprpc.so
%{_libdir}/libsdsp_default_listener.so
%{_libdir}/libsdsprpc.so
%{_mandir}/man3/fastrpc.3*

%files services
%{_sbindir}/adsprpcd
%{_sbindir}/cdsprpcd
%{_sbindir}/gdsprpcd
%{_sbindir}/sdsprpcd
%{_unitdir}/adsprpcd.service
%{_unitdir}/adsprpcd_audiopd.service
%{_unitdir}/cdsprpcd.service
%{_unitdir}/cdsp1rpcd.service
%{_unitdir}/gdsp0rpcd.service
%{_unitdir}/gdsp1rpcd.service
%{_unitdir}/sdsprpcd.service
%{_mandir}/man8/adsprpcd.8*
%{_mandir}/man8/cdsprpcd.8*
%{_mandir}/man8/dsprpcd.8*
%{_mandir}/man8/gdsprpcd.8*
%{_mandir}/man8/sdsprpcd.8*
%{_udevrulesdir}/59-fastrpc-remoteproc.rules
%{_udevrulesdir}/60-fastrpc.rules
%{_sysusersdir}/fastrpc.conf

%changelog
%autochangelog
