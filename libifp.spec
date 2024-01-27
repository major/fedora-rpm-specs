# Relax due to incompatible pointer issues
%global build_type_safety_c 2

Name:           libifp
Version:        1.0.0.2
Release:        %autorelease
Summary:        General-purpose library-driver for iRiver's iFP portable audio players

License:        GPL-2.0-only
URL:            http://ifp-driver.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/ifp-driver/%{name}/%{version}-stable/%{name}-%{version}.tar.gz
Source:         libifp.hotplug
Source:         10-libifp.rules
# autoconf-2.69 breaks configure.in (likely configure.in is the broken part)
# Upstream is dead, so fix it here:
Patch:          libifp-1.0.0.2-fix-broken-configure.in.diff
Patch:          libifp-1.0.0.2-fix-broken-configure-again.diff

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd

BuildRequires:  libusb-compat-0.1-devel

%description
libifp is a general-purpose library-driver for iRiver's iFP (flash-based)
portable audio players. The source code is pure C and is fairly portable.

Also included is a console app that uses the library.

%package        devel
Summary:        Headers and libraries for developing with libifp
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries for developing apps that use
libifp.

%prep
%autosetup

%build
autoreconf -fiv
%configure --with-libusb --disable-static
%make_build

%install
%make_install

install -Dpm 0755 %{SOURCE1} %{buildroot}/sbin/libifp-hotplug
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/10-libifp.rules

%files
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/ifpline
%{_libdir}/libifp.so.4*
/sbin/libifp-hotplug
%{_udevrulesdir}/10-libifp.rules

%files devel
%{_includedir}/ifp.h
%{_libdir}/libifp.so
%{_mandir}/man3/ifp.h.3*

%changelog
%autochangelog
