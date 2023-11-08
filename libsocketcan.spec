Name:           libsocketcan
Version:        0.0.12
Release:        3%{?dist}
Summary:        Library for SocketCAN

License:        LGPL-2.1-or-later
URL:            https://public.pengutronix.de/software/libsocketcan/
Source0:        %{url}/%name-%version.tar.bz2

BuildRequires:  gcc
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig

%description
This library allows you to control some basic functions in socketcan
from userspace.


%package devel
Summary:        Development files for the SocketCAN library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This library allows you to control some basic functions in socketcan
from userspace.

This package contains the libsocketcan development files.

%prep
%autosetup

%build
./autogen.sh
%configure --disable-static --docdir="%_docdir/%name"
%make_build

%install
%make_install
rm -rf "%buildroot/%_libdir"/*.la "%buildroot/%_docdir/%name"


%files
%doc README
%_libdir/libsocketcan.so.2*
%license LICENSE

%files devel
%_includedir/can_netlink.h
%_includedir/libsocketcan.h
%_libdir/libsocketcan.so
%_libdir/pkgconfig/libsocketcan.pc

%changelog
* Sun Nov 05 2023 Vasiliy Glazov <vascom2@gmail.com> - 0.0.12-3
- Update spec

* Thu Nov 02 2023 Vasiliy Glazov <vascom2@gmail.com> - 0.0.12-2
- Added BR gcc
- Removed patch

* Mon Oct 30 2023 Vasiliy Glazov <vascom2@gmail.com> - 0.0.12-1
- Initial packaging for Fedora
